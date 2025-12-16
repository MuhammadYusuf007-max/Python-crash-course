class User:
    def __init__(self, first_name, last_name, information):
        self.f_name = first_name
        self.l_name = last_name
        self.info = information
        self.login_attemps = 0
        
    def describe_user(self):
        print(f"This user is {self.info}")
        
    def greet_user(self):
        print(f"I congrutulate {self.f_name} {self.l_name} to becoming our user")
    
    def increment_login_attemps(self):
        self.login_attemps += 1
    
    def reset_login_attemps(self):
        self.login_attemps = 0
        
        
user1 = User("Yusuf", "Mukhammadov", "very intelligent")
user1.describe_user()
user1.greet_user()

user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()
user1.increment_login_attemps()

print(user1.login_attemps)

user1.reset_login_attemps()
print(user1.login_attemps)