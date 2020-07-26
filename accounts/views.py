from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm  # 회원가입 모델 폼
from django.contrib.auth import login as auth_login
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             #등록 후 바로 로그인 처리
#             auth_login(request,user)
#             return redirect('profile')
#             # return redirect(settings.LOGIN_URL)  # 로그인 창으로
#     else:
#         form = UserCreationForm()
#     return render(request, 'accounts/signup.html', {
#         'form': form
#     })

# 클래스 기반 뷰 호 회원가입 후 로그인
class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    def get_success_url(self):
        return resolve_url('profile')
    def form_valid(self, form):
        user = form.save()
        auth_login(self.request,user)
        return redirect(self.get_success_url()) #redirect('profile')
signup = SignupView.as_view()
# 회원가입 클래스 기반 뷰 다른 방법
# signup = CreateView.as_view(model=User, form_class=UserCreationForm,
#                             success_url=settings.LOGIN_URL,
#                             template_name='accounts/signup.html')


@login_required  # 로그인 된 사람만 응답하게. 로그인X시 로그인 창 뜸
def profile(request):
    return render(request, 'accounts/profile.html')
