import datetime
from user_management.models import User


class UpdateLastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        assert hasattr(request, 'user')
        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id) \
                .update(last_activity=datetime.datetime.now())
        return self.get_response(request)
