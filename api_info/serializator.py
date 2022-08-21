from rest_framework import serializers
from csinf.models import SkinInfo, Notice


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinInfo
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
