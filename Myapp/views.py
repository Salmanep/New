from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Doctors, Hospital, Sikk, User


def index(request):
    return render(request, 'index.html')


def fDisease(request):
    return render(request, 'FindDisease.html')


def aDisease(request):
    return render(request, 'AboutDisease.html')


def fDoctor(request):
    return render(request, 'FindDoctor.html')


def fHospital(request):
    return render(request, 'FindHospital.html')


def searched(request):
    try:
        sym1 = request.POST['s1']
        sym2 = request.POST['s2']
        sym3 = request.POST['s3']
        sym4 = request.POST['s4']
        m = Sikk.objects.get(disease='Allergies')
        if m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(disease='Cold and Flu')
        if m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(disease='Conjunctivitis or pink eye')
        if m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(disease='Diarrhea')
        if m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(disease='Headaches')
        if m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym2 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym1 and m.symptom2 == sym4 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym1 and m.symptom3 == sym4 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym4 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym4:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym3 and m.symptom2 == sym4 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym2 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym1 and m.symptom3 == sym3 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym3 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym2 and m.symptom3 == sym1 and m.symptom4 == sym3:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym1 and m.symptom4 == sym2:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        elif m.symptom1 == sym4 and m.symptom2 == sym3 and m.symptom3 == sym2 and m.symptom4 == sym1:
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        else:
            return render(request, 'not.html')

    except:
        return render(request, 'not.html')


def details(request):
    try:
        name = request.POST['disease']
        if Sikk.objects.get(disease=name):
            data = Sikk.objects.filter(disease=name)
            return render(request, 'Details.html', {'data': data})
    except:
        return render(request, 'not.html')


def dfinded(request):
    try:
        dep = request.POST['department']
        dis = request.POST['district']
        data = Doctors.objects.filter(district=dis, department=dep)
        return render(request, 'Dfinded.html', {'data': data})
    except:
        return render(request, 'not.html')


def hfinded(request):
    try:
        dis = request.POST['district']
        data = Hospital.objects.filter(district=dis)
        return render(request, 'Hfinded.html', {'data': data})
    except:
        return render(request, 'not.html')


def notfind(request):
    return render(request, 'not.html')


@login_required()
def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def regd(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    username = request.POST['uname']
    password = request.POST['password']
    if User.objects.filter(Username=username):
        return render(request, 'sorry.html')
    else:
        data = User(First_name=fname, Last_name=lname, Email=email, Username=username, Password=password)
        data.save()
        return render(request, 'regd.html')


def sorry(request):
    return render(request, 'sorry.html')


def login(request):
    return render(request, 'Login.html')
def admin_login(request):
    return render(request, 'admin_login.html')
def logged_admin(request):
    user = request.POST['admin_user']
    pas = request.POST['admin_pass']
    if user == 'admin' and pas == 'admin':
        return render(request, 'Admin.html')
    else:
        return render(request,'not.html')

def show_disease(request):
    data = Sikk.objects.all()
    return render(request, 'Show_disease.html', {'data': data})

def Insert_disease(request):
    return render(request, 'Insert_disease.html')


def diseaseInserted(request):
    disease = request.POST['disease']
    description = request.POST['description']
    cause = request.POST['cause']
    department = request.POST['department']
    symptom1 = request.POST['symptom1']
    symptom2 = request.POST['symptom2']
    symptom3 = request.POST['symptom3']
    symptom4 = request.POST['symptom4']
    if Sikk.objects.filter(disease=disease):
        return render(request, 'Already.html')
    else:
        data = Sikk(disease=disease, description=description, cause=cause, department=department, symptom1=symptom1,
                    symptom2=symptom2, symptom3=symptom3, symptom4=symptom4)
        data.save()

        return render(request, 'Disease_inserted.html')


def already(request):
    return render(request, 'Already.html')


def Admin(request):
    return render(request, 'Admin.html')


def Show_doctors(request):
    data = Doctors.objects.all()
    return render(request, 'Show_doctors.html', {'data': data})


def Insert_doctor(request):
    return render(request, 'Insert_doctor.html')


def Doctor_inserted(request):
    name = request.POST['doctor']
    photo = request.FILES['photo']
    district = request.POST['district']
    department = request.POST['department']
    details = request.POST['details']
    if Doctors.objects.filter(doctor=name):
        return render(request, 'Already.html')
    else:
        data = Doctors(doctor=name, photo=photo, district=district, department=department, details=details)
        data.save()

        return render(request, 'Doctor_inserted.html')


def Show_hospitals(request):
    data = Hospital.objects.all()
    return render(request, 'Show_hospitals.html', {'data': data})


def Insert_hospital(request):
    return render(request, 'Insert_hospital.html')


def Hospital_inserted(request):
    name = request.POST['hospital']
    photo = request.FILES['photo']
    district = request.POST['district']
    address = request.POST['address']
    phone = request.POST['phone']
    emergency = request.POST['emergency']
    details = request.POST['details']
    if Hospital.objects.filter(hospital=name):
        return render(request, 'Already.html')
    else:
        data = Hospital(hospital=name, photo=photo, district=district, address=address, details=details, phone=phone,
                        emergency=emergency)
        data.save()
        return render(request, 'Hospital_inserted.html')


def show_users(request):
    data = User.objects.all()
    return render(request, 'show_users.html', {'data': data})
