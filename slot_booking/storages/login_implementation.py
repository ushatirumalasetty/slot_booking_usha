from slot_booking.interactors.storages.login_interface import \
    StorageInterface
from slot_booking.models.user import User
from slot_booking.exceptions.exceptions import InvalidUserName, InvalidPassword
from slot_booking.interactors.storages.dtos import *


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
        if not user.check_passward(password):
            raise InvalidPassword
        return user.id

    def get_user_role(self,user_id):
        user_obj= User.objects.get(id=user_id)
        data=UserDetailsDto(
            user_id=user_obj.user_id,
            first_name=user_obj.first_name,
            last_name=user_obj.last_name,
            user_name=user_obj.user_name
            )
        return data
