from django.shortcuts import render
from django.http import HttpResponse
from UserCards import models as user_modules
from Documents import models as documents_models


def signup(request):
    return render(request, 'UserCards/signup.html', {})


def login(request):
    return render(request, 'UserCards/login.html', {})

def index(request):
    user = user_modules.UserCard.objects.filter(session_id=request.COOKIES['sessionid'])
    if user:
        copies = user[0].documentcopy_set.all()
        return render(request, 'UserCards/index.html', {'user': user[0], 'copies': copies})
    else:
        return HttpResponse("You are not currently logged in")


def make_user(request):
    '''
    Processing signup step
    '''
    username = request.POST.get("Name")
    surname = request.POST.get("Surname")
    email = request.POST.get("Email")
    password = request.POST.get("Password")
    phone = request.POST.get("Phone")
    address = request.POST.get("Address")
    user = user_modules.UserCard(name=username, status="student", email=email,
                                 password=password, phone_number=phone, surname=surname, address=address)
    user.session_id = request.COOKIES['sessionid']
    user.save()
    response = render(request, 'UserCards/index.html', {})
    return response

def identify_user(request):
    '''
    Processing login step
    '''
    user = user_modules.UserCard.objects.get(email=request.POST.get("Email"), password=request.POST.get("Password"))
    if user:
        user.session_id = request.COOKIES['sessionid']
        user.save()
        return render(request, 'Documents/index.html', {'documents': documents_models.Document.objects.all()})
    else:
        return render(request, 'UserCards/login.html', {'error': True})

