from rest_framework import serializers
from custom_auth.models import CustomUser


class EmailLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'photo']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        photo = validated_data.get('photo')
        if photo:
            instance.photo = photo

        instance.save()
        return instance

    def validate_email(self, value):
        if self.instance is not None:
            query = CustomUser.objects.filter(email=value).exclude(pk=self.instance.pk)
        else:
            query = CustomUser.objects.filter(email=value)

        if query.exists():
            raise serializers.ValidationError("Этот email уже используется.")
        return value

    def validate_password(self, value):
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Пароль должен содержать хотя бы одну цифру.")
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен быть не менее 8 символов.")
        return value

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    reset_token = serializers.CharField()
    new_password = serializers.CharField()