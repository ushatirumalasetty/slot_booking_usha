from typing import List

from auth_service.storages.login_implementation import *
from auth_service.presenters.presenter_implementation import *
from auth_service.interactors.login_interactor import *
from auth_service.common.oauth2_storage import OAuth2SQLStorage

# TDOD: 

class ServiceInterface:

    @staticmethod
    def get_login(username: str, password: str): # TODO: maintain proper neccessary service
        
        storage = StorageImplementation()
        
        presenter = PresenterImplementation() 
        
        oauth2_storage = OAuth2SQLStorage()
        
        interactor = UserLginInteractor(storage=storage,
                                        oauth2_storage=oauth2_storage,
                                        presenter=presenter)
        
        tokens_dto,user_login_dto = interactor.login_wrapper(username=username, password=password)
        
        return tokens_dto,user_login_dto
