from django.contrib.auth.hashers import check_password
from .models import Member


class MemberAuth:
    
    def authenticate(self, request, username=None, password=None, *args, **kwargs):
        # kwargs를 이용해도 되지만 default값으로 None을 두기 위해 username과 password를 따로 씀
        if not username or not password: # 아닌 상황에서 빠져나오는 게 depth가 덜 깊음
            if request.user.is_authenticated: #혹시나 이미 로그인했는데 다시 로그인을 시도한 경우
                return request.user
            return None

        try:
            member = Member.objects.get(username=username)
        except Member.DoesNotExist:
            return None
        
        if check_password(password, member.password):
            if member.status == '일반':
                return member
        
        return None
    
    def get_user(self, pk):
        try:
            member = Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            return None
        
        return member # if member.is_active and member.status == '일반' else None 
        # -> above if else is no more useful b/c check this at authenticate func.