import json

from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from slot_booking.interactors.get_washing_machine_wise_day_slots_interactor import \
    GetWashingMachineWiseDaySlotsInteractor
from slot_booking.presenters.presenter_implementation import PresenterImplementation
from slot_booking.storages.get_washing_machine_wise_day_slots_implementation import StorageImplementation


def api_wrapper(*args, **kwargs):
    request_data = kwargs['request_data']
    washing_machine_id = request_data['washing_machine_id']
    day = request_data['day']
    storage = StorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetWashingMachineWiseDaySlotsInteractor(storage=storage,presenter=presenter)
    print("**********REquest****")
    washing_machine_wise_slots_dict = interactor.get_washing_machine_wise_day_wise_slots(
        washing_machine_id=washing_machine_id,
        day=day)
    print("**********END******")
    response_data = json.dumps(washing_machine_wise_slots_dict)
    return HttpResponse(response_data, status=200)
