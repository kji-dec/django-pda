from django.shortcuts import render
# from .models import Member

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