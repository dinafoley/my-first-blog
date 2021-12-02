from django.shortcuts import render
from .models import Country
from .models import Diseasetype
from .models import Disease
from .models import Discover
from .models import Users
from .models import Publicservant
from .models import Doctor
from .models import Specialize
from .models import Record

from django.db import connection

from .forms import C
from .forms import DT
from .forms import Dise
from .forms import Disc
from .forms import Doc
from .forms import S
from .forms import R
from .forms import U
from .forms import P


from django.shortcuts import redirect


def C_(request):

    if request.method == "POST":
        form = C(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/country_base')
    else:
        form = C()
    return render(request, 'work/post_edit.html', {'form': form})

def DT_(request):

    if request.method == "POST":
        form = DT(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/disease_base')
    else:
        form = DT()
    return render(request, 'work/post_edit.html', {'form': form})

def Doc_(request):

    if request.method == "POST":
        form = Doc(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/Doctor_base')
    else:
        form = Doc()
    return render(request, 'work/post_edit.html', {'form': form})

def Dise_(request):

    if request.method == "POST":
        form = Dise(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/disease2_base')
    else:
        form = Dise()
    return render(request, 'work/post_edit.html', {'form': form})

def Disc_(request):

    if request.method == "POST":
        form = Disc(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/discover_base')
    else:
        form = Disc()
    return render(request, 'work/post_edit.html', {'form': form})

def S_(request):

    if request.method == "POST":
        form = S(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/Specialize_base')
    else:
        form = S()
    return render(request, 'work/post_edit.html', {'form': form})

def R_(request):

    if request.method == "POST":
        form = R(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/Record_base')
    else:
        form = R()
    return render(request, 'work/post_edit.html', {'form': form})

def U_(request):

    if request.method == "POST":
        form = U(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/Users_base')
    else:
        form = U()
    return render(request, 'work/post_edit.html', {'form': form})

def P_(request):

    if request.method == "POST":
        form = P(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('/Publicservant_base')
    else:
        form = P()
    return render(request, 'work/post_edit.html', {'form': form})

# Create your views here.
#def post_list(request):
 #   return render(request, 'work/post_list.html', {})

def main(request):
    return render(request, 'work/main.html', { })

def country_base(request):
    posts = Country.objects.all()
    return render(request, 'work/country_base.html', {'posts': posts})

def disease_base(request):
    posts = Diseasetype.objects.all()
    return render(request, 'work/disease_base.html', {'posts': posts})

def disease2_base(request):
    posts = Disease.objects.all()
    return render(request, 'work/disease2_base.html', {'posts': posts})

def discover_base(request):
    posts = Discover.objects.all()
    return render(request, 'work/discover_base.html', {'posts': posts})

def Users_base(request):
    posts = Users.objects.all()
    return render(request, 'work/Users_base.html', {'posts': posts})

def Publicservant_base(request):
    posts = Publicservant.objects.all()
    return render(request, 'work/Publicservant_base.html', {'posts': posts})

def Doctor_base(request):
    posts = Doctor.objects.all()
    return render(request, 'work/Doctor_base.html', {'posts': posts})
def Specialize_base(request):
    posts = Specialize.objects.all()
    return render(request, 'work/Specialize_base.html', {'posts': posts})
def Record_base(request):
    posts = Record.objects.all()
    return render(request, 'work/Record_base.html', {'posts': posts})


def q1(request):
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT e.disease_code as a,
            e.description as b
            FROM disease e 
            INNER JOIN discover r 
            ON e.disease_code = r.disease_code
            WHERE pathogen = 'bacteria'
            AND r.first_enc_date<'1990-01-01'""")
        posts = cursor.fetchall()
    finally:
        cursor.close()

    return render(request, 'work/q1.html', {'posts': posts})

def q2(request):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
                        SELECT DISTINCT u.name, u.surname, d.degree
                        FROM doctor d
                        INNER JOIN users u
                        ON u.email = d.email
                        INNER JOIN specialize s 
                        ON u.email = s.email 
                        INNER JOIN diseasetype t 
                        ON s.id = t.id
                        WHERE t.description != 'infectious'
                        AND d.email = u.email
                        AND s.email = u.email
                        ;"""
        )
        posts = cursor.fetchall()
    finally:
        cursor.close()

    return render(request, 'work/q2.html', {'posts': posts})


def q3(request):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
                        SELECT DISTINCT u.name,
                        u.surname,
                        d.degree
                        FROM users u, doctor d
                        WHERE u.email = d.email 
                        AND u.email IN(
                        SELECT s.email 
                        FROM specialize s 
                        GROUP BY s.email
                        HAVING COUNT(*)>2)
                        ;"""
        )
        posts = cursor.fetchall()
    finally:
        cursor.close()

    return render(request, 'work/q3.html', {'posts': posts})


def q4(request):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
                        SELECT DISTINCT u.cname,
                        AVG(u.salary)
                        FROM users u
                        INNER JOIN specialize s 
                        ON u.email = s.email 
                        INNER JOIN diseasetype t 
                        ON s.id = t.id
                        WHERE t.description = 'virology'
                        GROUP BY u.cname
                        ;"""

        )
        posts = cursor.fetchall()
    finally:
        cursor.close()

    return render(request, 'work/q4.html', {'posts': posts})


def q5(request):
    cursor = connection.cursor()
    try:
        cursor.execute(
            """
                        SELECT DISTINCT p.department,
                        COUNT (p.email)
                        FROM publicservant p
                        INNER JOIN record r 
                        on r.email = p.email
                        WHERE r.disease_code = 'covid-19'
                        GROUP BY r.cname, p.department
                        HAVING COUNT(*)>1
                        ;"""
        )
        posts = cursor.fetchall()
    finally:
        cursor.close()

    return render(request, 'work/q5.html', {'posts': posts})