from auth_service.interactors.presenters.presenter_interface import PresenterInterface
from auth_service.interactors.\
storages.login_interface import *


class PresenterImplementation(PresenterInterface):
    
    def raise_exception_for_invalid_username(self):
        raise NotFound(*INVALID_USER_NAME)

    
    def raise_exception_for_invalid_password(self):
        raise NotFound(*INVALID_PASSWORD)

    
    def get_token_response_dto(self, tokens_dto, user_login_dto):
        access_token = tokens_dto.access_token
        role=user_login_dto.role
        access_token_dict={}
        access_token_dict['access_token']=access_token
        access_token_dict['role']=role
        return access_token_dict

class NotFound(Exception):
    pass


INVALID_USER_NAME=(
    'Invalid user_name this user_name doesnt exists','INVALID_USER_NAME'
    )
    
INVALID_PASSWORD=(
    "Invalid password, gave wrong password", 'INVALID_PASSWORD'
    )