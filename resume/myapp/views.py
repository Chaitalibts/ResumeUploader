from django.shortcuts import render
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages

# Create your views here.
from django.shortcuts import render
from .forms import ResumeForm
from .models import Resume
from django.views import View


class HomeView(View):
 def get(self, request):
  form = ResumeForm()
  candidates = Resume.objects.all()
  return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})

 def post(self, request):
  form = ResumeForm(request.POST, request.FILES)
  if form.is_valid():
   messages.success(request,'Your Application is Added!!!!')
   form.save()
   return HttpResponseRedirect('/')




class CandidateView(View):
 def get(self, request, pk):
  candidate = Resume.objects.get(pk=pk)
  return render(request, 'myapp/candidate.html', {'candidate':candidate})