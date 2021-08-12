
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed, APIException
from app03.models import UserToken
class MyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 认证逻辑, 如果认证通过, 返回两个值
        # 如果认证失败,  抛出AuthenticationFailed或APIException异常
        token = request.query_params.get('token')
        if token:
            user_token = UserToken.objects.filter(token=token).first()
            # 认证通过
            if user_token:
                return user_token.user, token
            else:
                raise AuthenticationFailed('认证失败')
        else:
            raise AuthenticationFailed('请求地址需要携带token')
