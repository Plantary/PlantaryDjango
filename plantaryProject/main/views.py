from django.contrib.auth.models import User
from django.shortcuts import render
from ourdiary.models import Ourdiary, Photo
from account.models import Profile
# Create your views here.
def home(request):
    return render(request, 'home.html')
    #모델.쿼리셋(objects).메소드

def new(request):
    return render(request, 'new.html')

def ourdiary_list(request):
    ourdiary = Ourdiary.objects.all()
    ourdiarys = ourdiary.order_by('-id')
    mydiary = ourdiary.filter(author_id = request.user).order_by('-id')
    profile = Profile.objects.all()
    current_user = request.user
    return render(request,'home.html',{'ourdiarys':ourdiarys,'current_user':current_user, 'mydiary':mydiary, 'profile': Profile})
