import inspect
from django.db import IntegrityError
from rest_framework.decorators import api_view
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
        r500(f'Error: {e}')
    try:
        CAProfile.objects.get(email=dt_email)
    except CAProfile.DoesNotExists():
        return r500("Email already registered")
    
    try:
        user= User.objects.create(username=dt_email,password=dt_password)
        user.save()
    except Exception as e:
        send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong :'+(str)(e))
    try:
        ca_profile= CAProfile.objects.create(fullname=dt_fullname,email=dt_email,phone=dt_phone,college=dt_college,year=dt_year)

        ca_profile.generate_ca_code()

        ca_profile.save()
    
    except IntegrityError as e:
        send_error_mail(inspect.stack()[0][3], request.data, e+"\nintegrity")
        return r500('something went wrong :'+(str)(e))
    except Exception as e:
        send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong :'+(str)(e))

