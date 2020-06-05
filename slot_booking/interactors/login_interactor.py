from slot_booking.interactors.storages.login_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import PresenterInterface
from slot_booking.common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService
from slot_booking.common.oauth2_storage import OAuth2SQLStorage

class UserLginInteractor:
    def __init__(self, storage: StorageInterface ,oauth2_storage: OAuth2SQLStorage, presenter: PresenterInterface):
        self.storage = storage
        self.presenter=presenter
        self.oauth2_storage = oauth2_storage
        
    def login(self, username:str, password: str):
        try:
            self.storage.validate_user_name(username=username)
        except:
            self.presenter.raise_exception_for_invalid_username()
            return 
        
        

        try:
            user_id = self.storage.validate_password(username=username, password=password)
        except:
            self.presenter.raise_exception_for_invalid_password()
            return 
        
        service = OAuthUserAuthTokensService(oauth2_storage=self.oauth2_storage)
        tokens_dto = service.create_user_auth_tokens(user_id)
        user_login_dto = self.storage.get_user_role(user_id)
        response = self.presenter.get_token_response_dto(tokens_dto=tokens_dto,
        user_login_dto=user_login_dto)
        return response
    