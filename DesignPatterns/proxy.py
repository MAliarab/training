import time
from abc import ABC, abstractmethod
from datetime import datetime


class UserDataAbstract(ABC):

    def __init__(self, user_id):
        self.user_id = user_id

    @abstractmethod
    def get_data(self):
        pass


class UserData(UserDataAbstract):

    def __init__(self, user_id):
        super().__init__(user_id)

    def get_data(self):
        time.sleep(2)
        return f"Sensitive data of user {self.user_id}"


class UserDataProxy(UserDataAbstract):

    _cache = {}

    def __init__(self, user_data: UserDataAbstract, requester_role: str):
        self.user_data = user_data
        self.requester_role = requester_role

    def get_data(self):
        # logging
        print(f"Fetching data request at: {datetime.now()}")

        # access control
        if self.requester_role != "admin":
            return "Access denied !!!"

        # caching
        if not self.user_data.user_id in UserDataProxy._cache:
            UserDataProxy._cache[self.user_data.user_id] = self.user_data.get_data()

        return UserDataProxy._cache[self.user_data.user_id]


def client(user_data: UserDataAbstract, role: str):
    proxy = UserDataProxy(user_data, role)
    print(proxy.get_data())
    print("-" * 20)


# slow fetch data (no cache at first time)
client(UserData(11), "admin")

# access forbidden
client(UserData(11), "guest")

# fast fetch data (cache)
client(UserData(11), "admin")
