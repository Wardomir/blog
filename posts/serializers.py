from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=120)
    body = serializers.CharField()
    creator_id = serializers.IntegerField(read_only=True)
    likes = serializers.StringRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        validated_data['creator_id'] = user_id
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):

        user_id = self.context['request'].user.id
        post_user_id = instance.creator_id

        if user_id != post_user_id:
            raise serializers.ValidationError("You can't edit post of another user!")

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

    def delete(self, instance):
        user_id = self.context['request'].user.id
        post_user_id = instance.creator_id

        if user_id != post_user_id:
            raise serializers.ValidationError("You can't delete post of another user!")

        instance.delete()


class LikeSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    user_id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateField(read_only=True)
