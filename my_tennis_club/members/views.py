from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

# Create your views here.

# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def deatils(request, slug):
  mymember = Member.objects.get(slug=slug)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())


# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'fruits': ['Apple', 'Banana', 'Cherry'],   
#   }
#   return HttpResponse(template.render(context, request))

#--------------------------------------------------

# def testing(request):
#   template = loader.get_template('template.html')
#   context = {
#     'firstname': 'Linus',
#   }
#   return HttpResponse(template.render(context, request))

# -------------------------------------------------

# def testing(request):
#   mymembers = Member.objects.all().values()
#   template = loader.get_template('template.html')
#   context = {
#     'mymembers': mymembers,
#   }
#   return HttpResponse(template.render(context, request))

# --------------------------------------------------
# def testing(request):
#     return render(request, 'template.html', {'name': 'Alice'})

# -----------------------------------------------------
def testing(request):
  membersObjects = Member.objects.all()
  memberValues =  Member.objects.all().values()
  # Using Order_By View
  mydataOrderby = Member.objects.all().order_by('firstname').values()
  return render(request, 'template.html', {'members': membersObjects,'memberValues':memberValues,'mydataOrderby':mydataOrderby})