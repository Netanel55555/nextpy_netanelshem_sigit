from file1 import GreetingCard

class BirthdayCard(GreetingCard):
    def __init__(self):
        super().__init__()
        self._sender_age = 0

    def greeting_msg(self):
        print(f"Dear {self._recipient},\nHappy birthday!\nSincerely, {self._sender}\nAge: {self._sender_age}")
