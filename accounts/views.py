from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm  # 회원가입 모델 폼

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect(settings.LOGIN_URL)  # 로그인 창으로
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form
#     })

# 회원가입 클래스 기반 뷰 다른 방법
signup = CreateView.as_view(model=User, form_class=UserCreationForm,
                            success_url=settings.LOGIN_URL,
                            template_name='accounts/signup.html')


@login_required  # 로그인 된 사람만 응답하게. 로그인X시 로그인 창 뜸
def profile(request):
    return render(request, 'accounts/profile.html')
