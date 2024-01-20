import inspect
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from CABack.models import CAProfile
from app.models import User
from app.resp import r500, r200
from app.views import send_error_mail


@api_view(['POST'])
def signup(request):
    data = request.data
    try:
        dt_fullname = data['fullname'].strip()
        dt_email = data['email']
        dt_password = data['password']
        dt_phone = data['phone']
        dt_college = data['college']
        dt_year = data['year']
    except KeyError as e:
        return r500(f'Error: {e}')
    try:
        CAProfile.objects.get(email=dt_email)
<<<<<<< HEAD
        return r500("Email already registered")
    
    try:
        user= User.objects.create(username=dt_email,password=dt_password)
        user.save()
    except Exception as e:
        # send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong (s1):'+(str)(e))

    
    try:
=======
    except CAProfile.DoesNotExist:
        return r500("Email already registered")
    
    try:
        user= User.objects.create(username=dt_email,password=dt_password)
        user.save()
    except Exception as e:
        send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong :'+(str)(e))
    try:
>>>>>>> parent of a7d3729 (signup error fix)
        ca_profile= CAProfile.objects.create(fullname=dt_fullname,email=dt_email,phone=dt_phone,college=dt_college,year=dt_year)

        ca_profile.generate_ca_code()

        ca_profile.save()
    
    except IntegrityError as e:
<<<<<<< HEAD
        # send_error_mail(inspect.stack()[0][3], request.data, str(e) + "\nintegrity")
        return r500('something went wrong (s3):'+(str)(e))
=======
        send_error_mail(inspect.stack()[0][3], request.data, str(e) + "\nintegrity")
        return r500('something went wrong :'+(str)(e))
>>>>>>> parent of a7d3729 (signup error fix)
    except Exception as e:
        send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong :'+(str)(e))

