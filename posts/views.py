from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post, Like
from posts.serializers import PostSerializer, LikeSerializer


class PostView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data})

    def post(self, request):
        post = request.data
        serializer = PostSerializer(data=post,
                                    context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success": f"Post created successfully"})

    def put(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data
        serializer = PostSerializer(instance=saved_post,
                                    context={'request': request},
                                    data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({
            "success": "Post updated successfully"
        })

    def delete(self, request, pk):
        saved_post = get_object_or_404(Post.objects.all(), pk=pk)
        data = request.data
        serializer = PostSerializer(instance=saved_post,
                                    context={'request': request},
                                    data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.delete(saved_post)
        return Response({
            "success": "Post deleted!"
        })


class LikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        serializer = LikeSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            post = get_object_or_404(Post.objects.all(), pk=data['post_id'])
            user = request.user
            try:
                existing_like = Like.objects.get(user=user, post=post)
                existing_like.delete()
                return Response({
                    "success": "Post unliked!"
                })
            except Like.DoesNotExist:
                like = Like()
                like.save(user=user, post=post)
                return Response({
                    "success": "Post liked!"
                })


class LikeStatisticsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        likes = Like.objects.filter(created_at__range=(date_from, date_to))
        print(date_from)
        print(date_to)

        serializer = LikeSerializer(likes, many=True)
        return Response({"likes": serializer.data})

