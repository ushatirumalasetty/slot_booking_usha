from unittest.mock import create_autospec

from auth_service.interactors.login_interactor import *
from auth_service.interactors.presenters.presenter_interface import \
    PresenterInterface
from auth_service.interactors.storages.login_interface import StorageInterface
from auth_service.common.oauth2_storage import OAuth2SQLStorage
import pytest

class TestGetAvilableSlotsInteractor:

    def test_invalid_username(self):
        
        username = "usha"
        password = "ammu"
        
        storage = create_autospec(StorageInterface)
        
        oauth = create_autospec(OAuth2SQLStorage)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = UserLginInteractor(storage= storage,oauth2_storage= oauth,
                                        presenter=presenter)
        
        storage.validate_user_name.side_effect = InvalidUserName
        
        presenter.raise_exception_for_invalid_username.side_effect = NotFound
        
        with pytest.raises(NotFound):
            interactor.login_wrapper(username=username, password=password)
        
        storage.validate_user_name.assert_called_once_with(username=username)
        
        presenter.raise_exception_for_invalid_username.assert_called_once_with()


    def test_invalid_password(self):
        
        username = "usha"
        password = "ammu"
        
        storage = create_autospec(StorageInterface)
        
        oauth = create_autospec(OAuth2SQLStorage)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = UserLginInteractor(storage= storage,oauth2_storage= oauth,
                                        presenter=presenter)
        
        storage.validate_password.side_effect = InvalidPassword
        
        presenter.raise_exception_for_invalid_password.side_effect = NotFound
        
        with pytest.raises(NotFound):
            interactor.login_wrapper(username=username, password=password)
        
        storage.validate_password.assert_called_once_with(username = username, password = password)
        
        presenter.raise_exception_for_invalid_password.assert_called_once_with()
    
  '''  
    def test_login_valid_details(self):
        
        username = "usha"
        password = "ammu"
        
        storage = create_autospec(StorageInterface)
        
        oauth = create_autospec(OAuth2SQLStorage)
        
        presenter = create_autospec(PresenterInterface)
        
        interactor = UserLginInteractor(storage= storage,oauth2_storage= oauth,
                                        presenter=presenter)
        
        
        '''