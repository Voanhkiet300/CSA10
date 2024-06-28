from datetime import datetime

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def welcome(self):
        print(f'Welcome {self.username}')
    
    def check_password(self, password):
        if self.password == password:
            return True
        return False

class SubscribedUser(User):
    def __init__(self, username, password, expiration_date) -> None:
        super().__init__(username, password)
        self.expiration_date = expiration_date

    def is_expired(self):
        if datetime.now() > self.expiration_date:
            return True
        return False
    
    

user = User('mindx', '12345')
user.welcome()
print(user.check_password('1234'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 1, 1))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())