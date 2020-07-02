import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from auth_service.interactors.login_interactor import \
    UserLginInteractor
from auth_service.presenters.presenter_implementation import PresenterImplementation
from auth_service.storages.login_implementation import StorageImplementation
from auth_service.common.oauth2_storage import OAuth2SQLStorage


def api_wrapper(*args, **kwargs):
    print("\n$$$$$$$$$$$$$$$$\n")
    user=kwargs['user']
    print("2:\ns")
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    print("3:\n")
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    print("*************")
    interactor = UserLginInteractor(storage=storage,presenter=presenter, oauth2_storage=oauth_storage)
    access_token = interactor.login(username=username, password=password)
    response_data = json.dumps(access_token)
    print("*************")
    print(response_data)
    return HttpResponse(response_data, status=200)
