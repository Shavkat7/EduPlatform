import hashlib
import datetime
from abc import ABC, abstractmethod


# Abstract Base Class
class AbstractRole(ABC):
    _id_counter = 1

    def __init__(self, full_name, email, password):
        self._id = AbstractRole._id_counter
        AbstractRole._id_counter += 1

        self._full_name = full_name
        self._email = email
        self._password_hash = self._hash_password(password)
        self._created_at = datetime.datetime.now().isoformat()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    @abstractmethod
    def get_profile(self):
        pass

    @abstractmethod
    def update_profile(self, full_name=None, email=None, password=None):
        pass
