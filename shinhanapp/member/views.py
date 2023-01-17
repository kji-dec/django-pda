from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import Member

# Create your views here.

# def main(request):
#     # member = Member.objects.get(pk=1) # primary key(auto-generated (same as id=1)
#     # members = Member.objects.all()
#     # members = Member.objects.filter(age__gte=35)
#     # members = Member.objects.filter(name="shinhan")
#     # members = Member.objects.filter(name__contains="te")
#     # members = Member.objects.get(name__contains="te").first # only one data. if more than one data, it returns error
#     members = Member.objects.filter(name__contains="te").order_by('-age')

#     return render(request, 'index.html', {'members': members})


def login(request):
    if request.method == 'POST':
        user_id = request.POST.get("user_id")
        password = request.POST.get("password")

        if Member.objects.filter(user_id=user_id).exists():
            member = Member.objects.get(user_id=user_id)
            if check_password(password, member.password):
                request.session['user_pk'] = member.id
                request.session['user_id'] = member.user_id
                return redirect('/')
        print(user_id, password)
        # login fail
    
    return render(request, 'login.html')

def logout(request):
    if 'user_pk' in request.session:
        del(request.session['user_pk'])
    if 'user_id' in request.session:
        del(request.session['user_id'])

    return redirect('/')

def register(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        
        if not Member.objects.filter(user_id=user_id).exists():
            member = Member(
                user_id=user_id,
                password=make_password(request.POST.get('password')),
                name=request.POST.get('name'),
                age=request.POST.get('age'),
            )
            member.save()
            return redirect('/member/login/')

    return render(request, 'register.html')