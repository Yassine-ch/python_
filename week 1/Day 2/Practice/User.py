class User:
    #CONSTRUCTOR
    def __init__(self, first_name, last_name, email, age):
        #ATTRIBUT
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    #METHODS
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        #ENROLL_METHOD
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200

my_user = User("Yassine", "CHebbi", "yassine@gmail.com", 25)
my_user.display_info()
my_user.enroll()
my_user.display_info()

