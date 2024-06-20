from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        ad_user = self.context['request'].user
        ad_quantity = Advertisement.objects.filter(status='OPEN', creator=ad_user)
        if self.context['request'].method == 'POST' and len(ad_quantity) >= 10:
            raise ValidationError('Вы не можете создавать более 10 объявлений')
        if self.context['request'].method == 'PATCH' and data.get('status') == 'OPEN' and len(ad_quantity) >= 10:
            raise ValidationError('Вы не можете создавать более 10 объявлений')
        if self.context['request'].method == 'PUT' and data.get('status') == 'OPEN' and len(ad_quantity) >= 10:
            raise ValidationError('Вы не можете создавать более 10 объявлений')
        return data
