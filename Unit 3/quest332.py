class UnderAge(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        years_left = 18 - self.age
        return f"Your age is {self.age} In {years_left} years you'll be 18"


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + name)
    except UnderAge as e:
        print(e)


send_invitation('Nati', 20)
send_invitation('Ben', 17)\

