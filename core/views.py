
from django.http import HttpResponse
from django.shortcuts import render
from mailer.mailer import Mailer
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        data = {
        'holder': request.POST['body'],
        }
        subject = request.POST['subject']
        to=[request.POST['toemail']]
        fm = request.POST['fmemail']
        Mailer(
            subject= subject,
            data=data,
            fm=fm,
            to=to,
            template='welcome.html',
        ).send()
        messages.success(request, "Email sent." )
        return render(request, 'home.html')
    

    return render(request, 'home.html')


def bulk_mail(request):
    if request.method == 'POST':
        data = {
        'holder': request.POST['body'],
        }
        subject = request.POST['subject']
        
        resiver_mail = request.POST['toemails']
        to=[]
        tox = resiver_mail.split('\n')
        for item in tox:
            mail = (item.strip('\r'))
            to.append(mail)
        print(to)
        
        
        
        fm = request.POST['fmemail']
        Mailer(
            subject= subject,
            data=data,
            fm=fm,
            to=to,
            template='welcome.html',
        ).send()
        messages.success(request, "Email sent." )
        return render(request, 'home.html')
    

    return render(request, 'home.html')