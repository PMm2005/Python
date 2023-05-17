class user:
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print("First name: ",self.first_name)
        print("Last Name: ",self.last_name)
        print("Email: ", self.email)
        print("Age: ",self.age)
        print("reward member: ",self.is_rewards_member)
        print("gold card points: ",self.gold_card_points)
        return self
    
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self
    
ahmed = user("ahmed","amri","ml12@gmail.com",19)
amine = user("amine", "amri","ljlkj@gmail.com",22)

ahmed.display_info().enroll().spend_points(50).display_info()
amine.enroll().spend_points(80).display_info()