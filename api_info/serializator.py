from django.contrib.auth import get_user_model
from rest_framework import serializers
from csinf.models import SkinInfo, Notice

User = get_user_model()


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinInfo
        fields = '__all__'


class SkinDetalizer(serializers.ModelSerializer):
    class Meta:
        model = SkinInfo
        fields = ('name', 'steam_price', 'market_price', 'buff_price', 'buff_link', 'market_link', 'steam_link')


class UserDetalizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active')


class DefaultSkin:
    def set_context(self, serializer_field):
        self.skin = serializer_field.parent.instance.skin_name

    def __call__(self):
        return self.skin


class NoticeSerializer(serializers.ModelSerializer):
    username_notice = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Notice
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['skin_name'] = SkinDetalizer(instance.skin_name).data
        response['buy_from'] = Notice.get_buy_from(instance).title()
        response['sell_to'] = Notice.get_sell_to(instance).title()
        return response


class NoticeSerializerAdmin(NoticeSerializer):
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['skin_name'] = SkinDetalizer(instance.skin_name).data
        response['username_notice'] = UserDetalizer(instance.username_notice).data
        response['buy_from'] = Notice.get_buy_from(instance).title()
        response['sell_to'] = Notice.get_sell_to(instance).title()
        return response


class NoticeDetailSerializer(NoticeSerializer):
    skin_name = serializers.HiddenField(default=DefaultSkin())
