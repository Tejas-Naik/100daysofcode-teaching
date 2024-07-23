class User:
    # Constructor function
    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
    
    # Methods
    def follow(self, user):
        self.following += 1
        user.followers += 1
        

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Tejas"

# print(user_1.id)
# print(user_1.username)

# user_2 = User()
# user_2.id = "002"
# user_2.name = "Jonas"

user_1 = User("001", "Tejas")
print(user_1.name)
print(user_1.id)
print(user_1.following)


user_2 = User("002", "Jonas")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)