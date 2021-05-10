from django.shortcuts import render
from django .http import HttpResponse
from . models import Doctors, Cold, Hospitals, Sikk
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
        m = Sikk.objects.get(symptom1 = sym1, symptom2= sym2, symptom3 = sym3, symptom4 = sym4)
        if m.disease == 'Allergies':
            s=m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data':s,'cause':cause,'des':des,'dep':dep})
        m = Sikk.objects.get(symptom1 = sym1, symptom2= sym2, symptom3 = sym3, symptom4 = sym4)
        if m.disease == 'Cold and Flu':
            s=m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(symptom1=sym1, symptom2=sym2, symptom3=sym3, symptom4=sym4)
        if m.disease == 'Conjunctivitis or pink eye':
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(symptom1=sym1, symptom2=sym2, symptom3=sym3, symptom4=sym4)
        if m.disease == 'Diarrhea':
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
        m = Sikk.objects.get(symptom1=sym1, symptom2=sym2, symptom3=sym3, symptom4=sym4)
        if m.disease == 'Headaches':
            s = m.disease
            cause = m.cause
            des = m.description
            dep = m.department
            return render(request, 'Searched.html', {'data': s, 'cause': cause, 'des': des, 'dep': dep})
    except:
        return render(request, 'not.html')


def details(request):
    name = request.POST['disease']
    data = Sikk.objects.filter(disease=name)
    return render(request, 'Details.html', {'data':data})
def dfinded(request):
    return render(request, 'Dfinded.html')
def hfinded(request):
    return render(request, 'Hfinded.html')
def notfind(request):
    return render(request, 'not.html')




