import json

from django.http import HttpResponse
from slot_booking.adapters.service_adapter import get_service_adapter, ServiceAdapter


def api_wrapper(*args, **kwargs):
    user=kwargs['user']
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    service_adapter = get_service_adapter()
    print("&"*1000)
    access_token = service_adapter.\
    auth_service.get_user_token( username=username, password=password)
    response_data = json.dumps(access_token)
    return HttpResponse(response_data, status=200)
