from rest_framework.decorators import api_view
from app.resp import r500, r200


@api_view(['POST'])
def signup(request):
    data = request.data
    try:
        username = data['username'].strip()
        email = data['email']
        password = data['password']
        phone = data['phone']
        college = data['college']
        year = data['year']
    except KeyError as e:
        r500(f'Error: {e}')
    
    # if 