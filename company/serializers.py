from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_field
from rest_framework import serializers

from common.serializers import MediaURLSerializer
from company.models import Banner, AboutUs, AboutUsGallery, SocialMedia, ContactWithUs, Contacts


class BannerListSerializer(serializers.ModelSerializer):
    bg_image = MediaURLSerializer()

    class Meta:
        model = Banner
        fields = ("id", "title", "subtitle", "bg_image")


class AboutUsGallerySerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = AboutUsGallery
        fields = ('image',)


class AboutUsHomeSerializer(serializers.ModelSerializer):
    galleries = serializers.SerializerMethodField()

    class Meta:
        model = AboutUs
        fields = ('desc', 'galleries')

    @extend_schema_field(OpenApiTypes.BINARY)
    def get_galleries(self, obj):
        return AboutUsGallerySerializer(obj.galleries.order_by('?')[:6], many=True, context=self.context).data


class AboutUsSerializer(serializers.ModelSerializer):
    galleries = serializers.SerializerMethodField()
    video = MediaURLSerializer()
    class Meta:
        model = AboutUs
        fields = ("id", "desc", "video", "galleries")

    @extend_schema_field(OpenApiTypes.BINARY)
    def get_galleries(self, obj):
        return AboutUsGallerySerializer(obj.galleries.all(), many=True, context=self.context).data

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ("link", "icon")


class ContactWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactWithUs
        fields = ("full_name", "phone_number", "subject", "message")

class ContactsListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ("id", "address", "phone_number1", "phone_number2", "work_time")
