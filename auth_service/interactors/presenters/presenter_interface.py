from typing import List
from abc import ABC, abstractmethod

class PresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_token_response_dto(self, tokens_dto, user_login_dto):
        pass
    