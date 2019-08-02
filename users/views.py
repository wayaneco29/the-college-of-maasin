from django.shortcuts import render, get_object_or_404
from post.models import Posts
from users.models import *
# Create your views here.
def index(request):
    posts = Posts.objects.all()
    return render(request, 'users/index.html', {'posts': posts})

def view(request, id):
    posts = Posts.objects.get(pk=id)
    if request.method == "GET":
        context = {
            'posts': posts
        }
        return render(request, 'users/view.html', context)

def view_more(request):
    posts = Posts.objects.all()
    return render(request, 'users/list.html', {'posts': posts})
    
def founder(request):
    return render(request, 'users/founder.html')

def song(request):
    return render(request, 'users/song.html')

def academics(request):
    return render(request, 'users/academics.html')
def codeofconduct(request):
    return render(request, 'users/codeofconduct.html')

def admission(request):
    return render(request, 'users/admission.html')

def scholarship(request):
    return render(request, 'users/scholarship.html')

def bsit_homepage(request):
    return render(request, 'users/courses/bsit-homepage.html')

def bsn_homepage(request):
    context = {
        'first_year_first_semester':        first_year_first_semester_bsn.objects.all(),
        'first_year_second_semester':       first_year_second_semester_bsn.objects.all(),
        'first_year_summer':                first_year_summer_bsn.objects.all(),
        'second_year_first_semester':       second_year_first_semester_bsn.objects.all(),
        'second_year_second_semester':      second_year_second_semester_bsn.objects.all(),
        'second_year_summer':               second_year_summer_bsn.objects.all(),
        'third_year_first_semester':        third_year_first_semester_bsn.objects.all(),
        'third_year_second_semester':       third_year_second_semester_bsn.objects.all(),
        'fourth_year_first_semester':       fourth_year_first_semester_bsn.objects.all(),
        'fourth_year_second_semester':      fourth_year_second_semester_bsn.objects.all(),
    }
    return render(request, 'users/courses/bsn-homepage.html',context)

def bsa_homepage(request):
    return render(request, 'users/courses/bsa-homepage.html')

def laed_homepage(request):
    context = {
        'first_year_first_semester':        first_year_first_semester_math.objects.all(),
        'first_year_second_semester':       first_year_second_semester_math.objects.all(),
        'second_year_first_semester':       second_year_first_semester_math.objects.all(),
        'second_year_second_semester':      second_year_second_semester_math.objects.all(),
        'third_year_first_semester':        third_year_first_semester_math.objects.all(),
        'third_year_second_semester':       third_year_second_semester_math.objects.all(),
        'fourth_year_first_semester':       fourth_year_first_semester_math.objects.all(),
        'fourth_year_second_semester':      fourth_year_second_semester_math.objects.all(),
    }
    return render(request, 'users/courses/laed-homepage.html', context)

def fpst_homepage(request):
    return render(request, 'users/courses/fpst-homepage.html')

def bsa_homepage(request):
    context = {
        'first_year_first_semester':        first_year_first_semester_bsa.objects.all(),
        'first_year_second_semester':       first_year_second_semester_bsa.objects.all(),
        'first_year_summer':                first_year_summer_bsa.objects.all(),
        'second_year_first_semester':       second_year_first_semester_bsa.objects.all(),
        'second_year_second_semester':      second_year_second_semester_bsa.objects.all(),
        'second_year_summer':               second_year_summer_bsa.objects.all(),
        'third_year_first_semester':        third_year_first_semester_bsa.objects.all(),
        'third_year_second_semester':       third_year_second_semester_bsa.objects.all(),
        'third_year_summer':                third_year_summer_bsa.objects.all(),
        'fourth_year_first_semester':       fourth_year_first_semester_bsa.objects.all(),
        'fourth_year_second_semester':      fourth_year_second_semester_bsa.objects.all(),
    }
    return render(request, 'users/courses/bsa-homepage.html', context)

def bsba_homepage(request):
    context = {
        'first_year_first_semester':        first_year_first_semester_bsba.objects.all(),
        'first_year_second_semester':       first_year_second_semester_bsba.objects.all(),
        'second_year_first_semester':       second_year_first_semester_bsba.objects.all(),
        'second_year_second_semester':      second_year_second_semester_bsba.objects.all(),
        'third_year_first_semester':        third_year_first_semester_bsba.objects.all(),
        'third_year_second_semester':       third_year_second_semester_bsba.objects.all(),
        'fourth_year_first_semester':       fourth_year_first_semester_bsba.objects.all(),
        'fourth_year_second_semester':      fourth_year_second_semester_bsba.objects.all(),
    }
    return render(request, 'users/courses/bsba-homepage.html', context)
