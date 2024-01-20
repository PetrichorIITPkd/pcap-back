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
        return Response({
                'status': 404,
                "registered": False,
                'message': "Username Already Taken",
                "username": username
            })
    try:
        CAProfile.objects.get(email=dt_email)
        return r500("Email already registered")
    except CAProfile.DoesNotExist:
        pass
    except Exception as e:
        # send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong (s1):'+(str)(e))

    
    try:
        ca_profile= CAProfile(fullname=dt_fullname,email=dt_email,phone=dt_phone,college=dt_college,year=dt_year)
        ca_profile.generate_ca_code()
    except IntegrityError as e:
        # send_error_mail(inspect.stack()[0][3], request.data, str(e) + "\nintegrity")
        return r500('something went wrong (s3):'+(str)(e))
    except Exception as e:
        # send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong (s4):'+(str)(e))
    ca_profile.save()

    try:
        user= User(username=dt_email,password=dt_password)
        user.save()
        return r200("")
    except Exception as e:
        # send_error_mail(inspect.stack()[0][3], request.data, e)
        return r500('something went wrong (s2):'+(str)(e))
