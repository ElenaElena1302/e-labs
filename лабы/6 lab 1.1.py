from operator import indexOf
from struct import unpack
class UserAccount:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    def set_password(self,new_password):
        self.password = new_password

    def check_password(self,password):
        return self.password == password
user = UserAccount("Elana", "elana.iliesku@gmail.com", "snaiper")
user.set_password("S")
print(user.check_password("snaiper"))
print(user.check_password("S"))