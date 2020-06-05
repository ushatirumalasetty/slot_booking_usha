from abc import ABC
from abc import abstractmethod
from slot_booking.constants.enums import *

class StorageInterface(ABC):

    @abstractmethod
    def add_washing_machine_wise_day_wise_slots(self,
                                                day:Days,
                                                washing_machine_id:str,
                                                start_time,
                                                end_time):
        pass
    
    @abstractmethod
    def validate_washing_machine_id(self, washing_machine_id: str):
        pass

    @abstractmethod
    def validate_day(self, day: Days):
        pass
    
    @abstractmethod
    def check_if_start_time_less_than_end_time(self, start_time, end_time):
        pass
