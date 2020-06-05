from typing import List
from slot_booking.constants.exception_messages import *
from slot_booking.interactors.presenters.presenter_interface import \
    PresenterInterface
from slot_booking.interactors.\
storages.get_washing_machine_wise_storage_interface import *
from slot_booking.interactors.storages.dtos import *
from .coversions_to_dict import *
from slot_booking.exceptions.exceptions import *


class PresenterImplementation(PresenterInterface):

    def raise_exception_for_invalid_washing_machine_id(self):
        raise NotFound(*INVALID_WASHING_MACHINE_ID)
    
    def raise_exception_for_invalid_user_id(self):
        raise NotFound(*INVALID_USER)

    def raise_exception_for_invalid_day(self):
        raise NotFound(*INVALID_DAY)

    def raise_exception_for_day_doesnt_belong_to_washing_machine(self):
        raise NotFound(*INVALID_DAY_FOR_WASHING_MACHINE)

    def raise_exception_for_invalid_access(self):
        raise Forbidden(*INVALID_ACCESS)
        
    def raise_exception_start_time_is_not_less_than_end_time(self):
        raise NotFound(*INVALID_START_TIME_GREATER_THAN_END_TIME)

    def get_response_washing_machine_wise_day_wise_slots(self,
        slots_dto_list:ListWashingMachineWiseSlotDto):

        washing_machine_wise_day_slots_list = convert_dto_to_dict(slots_dto_list)
        return washing_machine_wise_day_slots_list

    def get_reponse_for_previous_slots_list(self,
        previous_slots_list:PreviousOrUpcommingSlotsDtoList):
        user_previous_slots_list = convert_previous_slot_dto_to_dict(previous_slots_list)
        return user_previous_slots_list

    def get_reponse_for_upcomming_slots_list(self,
        upcomming_slots_list:PreviousOrUpcommingSlotsDtoList):
        user_upcomming_slots_list=convert_previous_slot_dto_to_dict(upcomming_slots_list)
        return user_upcomming_slots_list

    def get_response_for_washing_machines_details(self,
        washing_machines_details_dtos_list:List[WashingMachineDto]):
        washing_machines_details_list = convert_washing_machines_details_dtos_list_to_dict(
            washing_machines_details_dtos_list)
        return washing_machines_details_list
        
        
        
    def raise_exception_for_invalid_username(self):
        raise NotFound(*INVALID_USER_NAME)

    
    def raise_exception_for_invalid_password(self):
        raise NotFound(*INVALID_PASSWORD)

    
    def raise_exception_for_password_didnt_match(self):
        pass

    
    def get_token_response_dto(self, tokens_dto, user_login_dto):
        access_token = tokens_dto.access_token
        role=user_login_dto.role
        access_token_dict={}
        access_token_dict['access_token']=access_token
        access_token_dict['role']=role
        return access_token_dict
        

    
    def get_response_of_list_of_datewise_slots_till_range(self,
        avilable_slots:DatewiseSlotStatusListDto):
        list_of_datewise_slots_till_range = convert_datewise_slots_till_range_dtos_list_to_dict(
            avilable_slots)
        return list_of_datewise_slots_till_range
    
    
    def raise_washing_machine_already_exist(self):
        pass
    
    
    def raise_exception_for_invalid_washing_machine_status(self):
        pass
    
    def get_response_for_get_requests_details_of_an_user(self,
            requests_details_list: List[RequestCompleteDetailsDto]):
        list_details_of_an_responses_os_an_user=convert_responses_of_an_dto_to_dict(requests_details_list)
        return list_details_of_an_responses_os_an_user
   
    