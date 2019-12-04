from django.contrib.auth.decorators import login_required


# 登录装饰器Mixin类
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)
