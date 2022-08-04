from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView, DetailView, UpdateView
from django.views.generic.edit import ModelFormMixin, CreateView

from accounts.models import MyUser
from csinf.forms import FormOrderBy, NoticeForm
from csinf.models import SkinInfo, Notice


# @login_required
def skins(request):
    return render(request, 'csinf/index.html')


class ListSkins(LoginRequiredMixin, ListView, FormView):
    model = SkinInfo
    template_name = 'csinf/goods.html'
    context_object_name = 'skins'
    form_class = FormOrderBy
    paginate_by = 50

    def get_paginate_by(self, queryset):
        value = self.request.GET.get('count_value', 50)
        return value

    def get_queryset(self):
        mm = self.request.GET.get('min_max')
        name_order = self.request.GET.get('order_by')
        max_value = self.request.GET.get('max_value')
        min_value = self.request.GET.get('min_value')
        filter_value = self.request.GET.get('filter_num')
        if mm and name_order and max_value and min_value and filter_value:
            queryset = SkinInfo.objects.filter(**{f'{filter_value}__gte': min_value}).filter(
                **{f'{filter_value}__lte': max_value}).order_by(f'{mm.replace("+", "")}{name_order}')
        elif mm and name_order:
            queryset = SkinInfo.objects.order_by(f'{mm.replace("+", "")}{name_order}')
        elif max_value and min_value and filter_value:
            queryset = SkinInfo.objects.filter(**{f'{filter_value}__gte': min_value}).filter(
                **{f'{filter_value}__lte': max_value})
        else:
            queryset = SkinInfo.objects.all()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['min_max'] = f"&min_max={self.request.GET.get('min_max', '')}"
        context['order_by'] = f"&order_by={self.request.GET.get('order_by', '')}"
        context['max_value'] = f"&max_value={self.request.GET.get('max_value', '')}"
        context['min_value'] = f"&min_value={self.request.GET.get('min_value', '')}"
        context['filter_num'] = f"&filter_num={self.request.GET.get('filter_num', '')}"
        context['count_value'] = f"&count_value={self.request.GET.get('count_value', self.paginate_by)}"
        context['cou_val'] = self.request.GET.get('count_value', 50)
        current_user = MyUser.objects.get(pk=self.request.user.id)
        context['list_favorite_skins'] = list(map(lambda x: x.id, current_user.favorite_skins.all()))
        return context

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        list_skins = self.request.POST.getlist('favorite_skinid')
        list_skins_del = self.request.POST.getlist('delfav_skinid')
        if list_skins or list_skins_del:
            current_user = MyUser.objects.get(pk=self.request.user.id)
            list_skins_fav = list(map(lambda x: x.id, current_user.favorite_skins.all()))
            if list_skins:
                skins_add = SkinInfo.objects.filter(id__in=list_skins).exclude(id__in=list_skins_fav)
                current_user.favorite_skins.add(*skins_add)
            if list_skins_del:
                skins_del = SkinInfo.objects.filter(id__in=list_skins_del)
                current_user.favorite_skins.remove(*skins_del)
        return super().get(request, *args, **kwargs)


class SkinDetail(LoginRequiredMixin, DetailView):
    template_name = 'csinf/detail.html'
    context_object_name = 'skin_info'
    model = SkinInfo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = MyUser.objects.get(pk=self.request.user.id)
        try:
            context['fav_skin'] = current_user.favorite_skins.get(id=self.object.id)
        except Exception:
            context['fav_skin'] = None
        return context

    def post(self, request, *args, **kwargs):
        current_user = MyUser.objects.get(pk=self.request.user.id)
        if self.request.POST.get('fav_add'):
            skin_add_fav = SkinInfo.objects.get(pk=self.request.POST.get('fav_add'))
            current_user.favorite_skins.add(skin_add_fav)
        elif self.request.POST.get('fav_delete'):
            skin_delete_fav = SkinInfo.objects.get(pk=self.request.POST.get('fav_delete'))
            current_user.favorite_skins.remove(skin_delete_fav)
        return super().get(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     return super().get(request, *args, **kwargs)


class ProfileListSkins(LoginRequiredMixin, ListView):
    template_name = 'csinf/profilelist.html'
    model = SkinInfo
    context_object_name = 'fav_list_skins'

    def get_queryset(self):
        current_user = MyUser.objects.get(pk=self.request.user.id)
        queryset = current_user.favorite_skins.all()
        return queryset

    def post(self, request, *args, **kwargs):
        current_user = MyUser.objects.get(pk=self.request.user.id)
        current_user.favorite_skins.clear()
        return super().get(self, request, *args, **kwargs)


class ProfileTableSkins(LoginRequiredMixin, ListView):
    template_name = 'csinf/profiletable.html'
    model = SkinInfo
    context_object_name = 'fav_table_skins'

    def get_queryset(self):
        current_user = MyUser.objects.get(pk=self.request.user.id)
        queryset = current_user.favorite_skins.all()
        return queryset

    def post(self, request, *args, **kwargs):
        current_user = MyUser.objects.get(pk=self.request.user.id)
        list_fav = self.request.POST.getlist('del_from_fav')
        if list_fav:
            list_skin = current_user.favorite_skins.filter(id__in=list_fav)
            current_user.favorite_skins.remove(*list_skin)
        return super().get(request, *args, **kwargs)


class NoticeSkins(LoginRequiredMixin, ListView):
    template_name = 'csinf/notice.html'
    model = SkinInfo
    context_object_name = 'notice_skins'

    def get_queryset(self):
        current_user = MyUser.objects.get(pk=self.request.user.id)
        queryset = current_user.favorite_skins.all()
        return queryset


class NoticeSkinDetail(LoginRequiredMixin, CreateView, DetailView):
    template_name = 'csinf/notice_detail.html'
    model = SkinInfo
    context_object_name = 'notice_skin'
    form_class = NoticeForm

    def get_success_url(self):
        skin_id = self.kwargs['pk']
        return reverse_lazy('notice_detail', kwargs={'pk': skin_id})

    '''
    Дописать!!!!!!!!!
    '''
