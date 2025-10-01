class User: # PascalCase camelCase snake_case
    def __init__(self,user_id, username): 
        self.id = user_id 
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)

#contructor does initialize: to set (variables, coutners, switches, etc.) to their starting values
#__init__

#method is what the object does
#attribute is what the object has
