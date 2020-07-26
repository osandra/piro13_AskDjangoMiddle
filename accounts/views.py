from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required #로그인 된 사람만 응답하게. 로그인X시 로그인 창 뜸
def profile(request):
    return render(request, 'accounts/profile.html')
