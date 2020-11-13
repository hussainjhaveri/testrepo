from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views import View



class UrMom(View):
    def get(self,request):
        return render(request,'urmomsux.html')



class Profile(View):
    def get(self,request):
        user=self.request.user
        one=User.objects.get(pk=user.pk)
        context={'pop':one}
        return render(request, 'profile.html', context)


class Extra(View):
    def get(self,request):
        return render(request, 'fuqu.html')
