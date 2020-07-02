from slot_booking.adapters.service_adapter import get_service_adapter, ServiceAdapter

class LoginInteractor:
    def login(self, username, password):
        try:    
            service_adapter = get_service_adapter()
            
            access_token = service_adapter.auth_service.\
            get_user_token( username=username, password=password)
        
        except InvalidUserName:
            self.
            