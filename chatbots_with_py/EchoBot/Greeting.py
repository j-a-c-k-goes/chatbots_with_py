class Greeting:
    def __init__(self, greeting):
        self.greeting = greeting.title()
    def view(self):
        print( self.greeting )
    def set(self, new_greeting):
        self.greeting = new_greeting.title()
        return self.greeting
    def get(self):
        return self.greeting