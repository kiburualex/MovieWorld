import os
from datetime import datetime
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from movies.models import Movie as Table


class ListSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name='movies:update')
    delete_url = serializers.HyperlinkedIdentityField(view_name='movies:delete')

    class Meta:
        ref_name = "Movies List"
        model = Table
        fields = ('id',
                  'title',
                  'description',
                  'created_at',
                  'updated_at',
                  'update_url',
                  'delete_url'
                 )


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        ref_name = "movies Create"
        model = Table
        fields = ('id',
                  'title',
                  'description'
                 )

    def validate_title(self, value):
        """validate name not to empty."""
        if not value:
            raise serializers.ValidationError("Name cannot be null")
        return value

    def validate_description(self, value):
        """validate description not to empty."""
        if not value:
            raise serializers.ValidationError("Description cannot be null")
        return value


class UpdateSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name='movies:update')
    delete_url = serializers.HyperlinkedIdentityField(view_name='movies:delete')
    
    class Meta:
        ref_name = "Movies Update"
        model = Table
        fields = ('id',
                  'title',
                  'description',
                  'created_at',
                  'updated_at',
                  'update_url',
                  'delete_url'
                 )

    def validate_title(self, value):
        """validate name not to empty."""
        if not value:
            raise serializers.ValidationError("Name cannot be null")
        return value

    def validate_description(self, value):
        """validate description not to empty."""
        if not value:
            raise serializers.ValidationError("Description cannot be null")
        return value