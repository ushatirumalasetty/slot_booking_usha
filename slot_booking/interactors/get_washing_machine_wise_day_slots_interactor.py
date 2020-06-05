from slot_booking.interactors.storages.\
get_washing_machine_wise_storage_interface import StorageInterface
from slot_booking.interactors.presenters.presenter_interface import\
PresenterInterface
from slot_booking.constants.enums import *
from slot_booking.exceptions.exceptions import *

class GetWashingMachineWiseDaySlotsInteractor:
    def __init__(self, storage:StorageInterface, presenter:PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_washing_machine_wise_day_wise_slots(self, day:Days,
                                                     washing_machine_id:str):
        try:
            self.storage.validate_washing_machine_id(washing_machine_id=washing_machine_id)
        except InvalidWashingMachineId:
            self.presenter.raise_exception_for_invalid_washing_machine_id()
            return

        try:
             self.storage.validate_day(day=day)
        except InvalidDay:
            self.presenter.raise_exception_for_invalid_day()
            return

        try:
            self.storage.validate_if_day_belong_to_washing_machine(day=day,
                                     washing_machine_id=washing_machine_id)
        except DayDoesntBelongToWashingMachine:
            self.presenter.\
            raise_exception_for_day_doesnt_belong_to_washing_machine()
            return

        washing_machine_wise_slots_dto_list = self.storage.\
        get_washing_machine_wise_day_wise_slots(day=day,
                                        washing_machine_id=washing_machine_id)
        return self.presenter.\
        get_response_washing_machine_wise_day_wise_slots(
            slots_dto_list=washing_machine_wise_slots_dto_list)