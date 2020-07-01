from auth_service.interactors.storages.login_interface import \
    StorageInterface
    
from auth_service.models.user import User
from django.contrib.auth.hashers import check_password

class StorageImplementation(StorageInterface):
    def validate_user_name(self, username: str):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName

    def validate_password(self, username, password):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise InvalidUserName
        if not user.check_password(password):
            raise InvalidPassword
        return user.id

    def get_user_role(self,user_id):
        user_obj= User.objects.get(id=user_id)
        data=UserDto(
            user_id=user_id,
            first_name=user_obj.first_name,
            last_name=user_obj.last_name,
            user_name=user_obj.user_name,
            role=user_obj.role
            )
        return data
        
from dataclasses import dataclass

@dataclass
class UserDto:
    user_id: int
    first_name: str
    last_name : str
    user_name : str
    role : str
    
class InvalidUserName(Exception):
    pass

class InvalidPassword(Exception):
    pass

class NotFound(Exception):
    pass

