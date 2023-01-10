class Context:
    def __init__(self):
        self.context = 'EchoBot mimics user input. It is infinitely repetitive.'
    def view(self):
        print(self.context.title())
    def set(self, new_context):
        self.context = new_context.title()
        return self.context
    def get(self):
        return self.context