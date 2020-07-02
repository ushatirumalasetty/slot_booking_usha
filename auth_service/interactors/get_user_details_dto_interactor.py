from typing import List
from dataclasses import dataclass
from auth_service.constants.enums import *

@dataclass
class UserDetailsDto:
    user_name : str
    first_name : str
    last_name : str
    role: UserRole
    user_id: int
    
class InvalidUserId(Exception):
    pass
# TODO: maintain two line after class
class GetUserDetails:
    def __init__(self, storage, presenter):
        self.storage = storage
        self.presenter = presenter
        
    def get_user_details_wrapper(self, user_ids:List[int]):
        try:
            self.get_user_details(user_ids=user_ids)
        except InvalidUserId as err:
            self.presenter.raise_exception_for_invalid_user_id(err)
        
        
    def get_user_details(self, user_ids:List[int]):
        
        user_details_dto_list=[]

        for user_id in user_ids:
            self.storage.validate_user_id(user_id)
            
        user_objs = self.storage.get_user_objects(user_ids)

        for user_obj in user_objs:
            user_details_dto = UserDetailsDto(user_name = user_obj.user_name, # TODO: clean code 
                                          first_name = user_obj.first_name,
                                          last_name = user_obj.last_name,
                                          role = user_obj.role,
                                          user_id = user_obj.user_id)
                              
            user_details_dto_list.append(user_details_dto)
        
        return self.presenter.get_response_for_user_detals(user_details_dto_list) 
                                        
