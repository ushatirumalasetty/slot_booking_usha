from typing import List


class AuthService:

    @property
    def interface(self):
        from auth_service.interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_token(self, username:str, password:str):
        user_token = self.interface.get_login(username=username, password=password)
        return user_token
