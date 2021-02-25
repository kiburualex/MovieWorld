from users.serializers.users_serializer import GetFullUserSerializer

def custom_jwt_response_handler(token, user=None, request=None):
    return {
        'token' : token,
        'user' : GetFullUserSerializer(user, context={'request' : request}).data
    }