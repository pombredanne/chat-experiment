from swampdragon.serializers.model_serializer import ModelSerializer


class MessageSerializer(ModelSerializer):
    class Meta:
        model = 'chatroom.Message'
        publish_fields = ('user', 'text', 'posted', 'room')


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = 'chatroom.Profile'
        publish_fields = ('pk', 'is_online', 'display_name')
