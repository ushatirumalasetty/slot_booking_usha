from slot_booking.interactors.storages.\
get_washing_machine_wise_storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *

class GetWashingMachineWiseDaySlotsInteractor:
    def __init__(self, storage:StorageInterface):
        self.storage = storage
        
    def get_washing_machine_wise_day_wise_slots_wrapper(self, day:Days,
                                        washing_machine_id:washing_machine_id,
                                        presenter:PresenterInterface):
        try:
            washing_machine_wise_slots_dto_list = self.\
            get_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id)
        
                                        
        except InvalidWashingMachineId:
            presenter.raise_exception_for_invalid_washing_machine_id()
        except InvalidDay:
            presenter.raise_exception_for_invalid_day()
        except DayDoesntBelongToWashingMachine:
            presenter.raise_exception_for_day_doesnt_belong_to_washing_machine()
        return presenter.\
        get_response_washing_machine_wise_day_wise_slots(slots_dto_list=washing_machine_wise_slots_dto_list)   
        
        
        
        

    def get_washing_machine_wise_day_wise_slots(self, day:Days,
                                                     washing_machine_id:str):
        self.storage.\
            validate_washing_machine_id(washing_machine_id=washing_machine_id)
        self.storage.validate_day(day=day)
        self.storage.validate_if_day_belong_to_washing_machine(day=day,
                                     washing_machine_id=washing_machine_id)
        
        washing_machine_wise_slots_dto_list = self.storage.\
        get_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id)
        
        return washing_machine_wise_slots_dto_list