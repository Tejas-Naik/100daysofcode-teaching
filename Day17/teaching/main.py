class User:
    # def __init__(self):
    #     print("New User created successfully")
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print(f"New User {self.username} created successfully with the ID: {self.id}")

    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Tejas"


# user_2 = User()
# user_2.name = "Angela"
# user_2.id = "002"

user_1 = User("001", "Tejas")
user_2 = User("002", "Angela")
print(user_1.id)
print(user_1.username)

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)