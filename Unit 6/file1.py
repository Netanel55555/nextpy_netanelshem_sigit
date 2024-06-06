class GreetingCard:
    def __init__(self):
        self._recipient = "Dana Ev"
        self._sender = "Eyal Ch"

    def greeting_msg(self):
        print(f"Dear {self._recipient},\nSincerely, {self._sender}")
