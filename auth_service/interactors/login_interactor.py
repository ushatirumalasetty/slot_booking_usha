from auth_service.interactors.storages.login_interface import StorageInterface

from auth_service.interactors.presenters.presenter_interface import PresenterInterface

from auth_service.common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService

from auth_service.common.oauth2_storage import OAuth2SQLStorage


class UserLginInteractor:


    def __init__(self, storage: StorageInterface ,oauth2_storage: OAuth2SQLStorage, presenter: PresenterInterface): # TODO: Clean code
        self.storage = storage
        self.presenter=presenter # TODO: no need of presenter
        self.oauth2_storage = oauth2_storage
    # TODO: no need or two lines
   
    def login_wrapper(self, username:str, password: str):# TODO: clean code maintain space betwee :
        
        try:
            self.login(username=username, password=password) # TODO: return value
        
        except InvalidUserName:
            self.presenter.raise_exception_for_invalid_username()
        
        except InvalidPassword:
            self.presenter.raise_exception_for_invalid_password()        

    
    def login_response(self, username:str, password: str):
        
        tokens_dto,user_login_dto = self.login_wrapper(username=username, password=password)
        
        response = self.presenter.get_token_response_dto(tokens_dto=tokens_dto,
                                                 user_login_dto=user_login_dto)

        return response

    
    def login(self, username:str, password: str):
        
        self.storage.validate_user_name(username=username)
        
        user_id = self.storage.validate_password(username=username, password=password)
        # TODO: try to maintain service_adapter if possible for service
        service = OAuthUserAuthTokensService(oauth2_storage=self.oauth2_storage)

        tokens_dto = service.create_user_auth_tokens(user_id=user_id)

        user_login_dto = self.storage.get_user_role(user_id)

        return tokens_dto,user_login_dto

# TODO: maintain exceptions in exceptions files
class InvalidUserName(Exception):
    pass


class InvalidPassword(Exception):
    pass


class NotFound(Exception):
    pass
