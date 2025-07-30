from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from account_module.models import CustomUser


class AuthorRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if request.user.is_author:
            return super().dispatch(request, *args, **kwargs)

        raise PermissionDenied("شما دسترسی لازم برای مشاهده این صفحه را ندارید.")