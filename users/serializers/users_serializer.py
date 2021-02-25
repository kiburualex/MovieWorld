import os
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from users.models import User


class ListSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name='users:update')
    delete_url = serializers.HyperlinkedIdentityField(view_name='users:delete')

    class Meta:
        ref_name = "Users List"
        model = User
        fields = ('id',
                  'name',
                  'email',
                  'created_at',
                  'updated_at',
                  'update_url',
                  'delete_url'
                 )


class CreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()  

    class Meta:
        ref_name = "Create User"
        model = User
        fields = ('id',
                  'name',
                  'email',
                  'token',
                  'password'
                 )

      
    def get_token(self, object):
        # create the user token as part of response
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER        
        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)        
        return token
    
    def validate_name(self, value):
        """validate name not to empty."""
        if not value:
            raise serializers.ValidationError("Name cannot be null")
        return value

    def validate_email(self, value):
        """validate description not to empty."""
        if not value:
            raise serializers.ValidationError("Email cannot be null")
        return value

    def create(self, validated_data):
        instance = User()
        if validated_data.get('name'):
            instance.name = validated_data.get('name')
        if validated_data.get('email'):
            instance.email = validated_data.get('email')
        
        instance.set_password(validated_data['password'])
        instance.save()

        return instance


class UpdateSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name='users:update')
    delete_url = serializers.HyperlinkedIdentityField(view_name='users:delete')

    class Meta:
        ref_name = "Update User"
        model = User
        fields = ('id',
                  'name',
                  'email',
                  'password',
                  'created_at',
                  'updated_at',
                  'update_url',
                  'delete_url'
                 )

    def update(self, instance, validated_data):
        try:
            if validated_data.get('name'):
                instance.name = validated_data.get('name')
            if validated_data.get('email'):
                if User.objects.exclude(pk=instance.pk).filter(email=validated_data.get('email')):
                    raise serializers.ValidationError('User with this email already exists.')
                instance.email = validated_data.get('email')
            if validated_data.get('password'):
                if validated_data['password'] != instance.password:
                    instance.set_password(validated_data['password'])
            instance.save()          
        except Exception as e:
            print(f'Error on updating user {e}')

        return instance


class GetFullUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'is_superuser', 
            'is_active', 
            'name', 
            'email'
            )
