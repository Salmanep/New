from django.shortcuts import render
from django .http import HttpResponse
from . models import Doctors, Hospital, Sikk
def home(request):
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
            return render(request, 'Searched.html', {'data':s,'cause':cause,'des':des,'dep':dep})
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
            return render(request, 'Details.html',{'data':data})
    except:
        return render(request, 'not.html')
def dfinded(request):
    dep = request.POST['department']
    dis = request.POST['district']
    data = Doctors.objects.filter(district=dis, department=dep)
    return render(request, 'Dfinded.html', {'data':data})
def hfinded(request):
    dis = request.POST['district']
    data = Hospital.objects.filter(district=dis)
    return render(request, 'Hfinded.html', {'data':data})
def notfind(request):
    return render(request, 'not.html')




