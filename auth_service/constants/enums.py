from enum import Enum
from ib_common.constants import BaseEnumClass

class UserRole(BaseEnumClass, Enum):
    ADMIN="ADMIN"
    USER="USER"

