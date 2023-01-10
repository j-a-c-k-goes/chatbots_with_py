'''
    EchoBot echoes user input.
'''
from Greeting import Greeting
from Context import Context
greeting = Greeting('Hello there!')
greeting.view()
context = Context()
context.view()
using_the_bot = True
while using_the_bot:
    stuff_to_echo = str(input('enter something for the bot to echo ( quit to stop ): '))
    if stuff_to_echo.lower() == 'quit':
        using_the_bot = False
        break
    print('\nYou said:', stuff_to_echo.title(), '\n')