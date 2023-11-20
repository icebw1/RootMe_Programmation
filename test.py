# SECRET = "et merci la zone"
# essais = ["{self.__init__.__globals__}", "{self.__init__}", "{self.__init__.__globals__[SECRET]}", "{self.__init__.__globals__SECRET}"]

# class Sandbox:
   
#     def ask_age(self):
#         # self.age = input("How old are you ? ")
#         # self.width = input("How wide do you want the nice box to be ? ")
#         self.age = 0
#         self.width = 20
   
#     def ask_secret(self):
#         # if input("What is the secret ? ") == SECRET:
#         #     print("You found the secret ! I thought this was impossible.")
#         # else:
#         #     print("Wrong secret")
#         print("blc")
 
#     def run(self):
#         for i in range(len(essais)):
#             self.ask_age()
#             to_format = f""" Printing a {self.width}-character wide box: [Age: {{self.age:{self.width}}} ]"""
#             print(to_format.format(self=self))
#             self.ask_secret()


# for essai in essais:
#     Sandbox.age = essai
#     Sandbox().run()



SECRET = "et merci la zone"
 
class Sandbox:
   
    def ask_age(self):
        self.age = input("How old are you ? ")
        # self.age = "{self.__init__.__globals__.SECRET}"
        self.width = input("How wide do you want the nice box to be ? ")
   
    def ask_secret(self):
        if input("What is the secret ? ") == SECRET:
            print("You found the secret ! I thought this was impossible.")
        else:
            print("Wrong secret")
 
    def run(self):
        while True:
            self.ask_age()
            # example with : self.age = 123456 & self.width = 10 : 
#             to_format = f"""
# Printing a {self.width}-character wide box:
# [Age: {{self.age:{self.width}}} ]"""
            
            # to_format = f"""Printing a {self.width}-character wide box:[Age: {{self.age:{self.width}}} ]"""
            to_format = f"""Printing a {self.__class__.__module__.__dict__['SECRET']}-character wide box:[Age: {{self.age:{self.width}}} ]"""

            # to_format: '\nPrinting a 10-character wide box:\n[Age: {self.age:10} ]' 
            # the variable to_format change self.width w/ its value but not self.age
            print(to_format.format(self=self)) # > Printing a 10-character wide box:[Age: 123456     ]
            # Now self.age is replaced by its value and self.width converted in spaces
            self.ask_secret()
 
Sandbox().run()

# ["{self.__init__.__globals__}", "{self.__init__}", "{self.__init__.__globals__[SECRET]}", "{self.__init__.__globals__SECRET}"]

"""
__builtins__: {'__name__': 'builtins', '__doc__': 'Built-in functions, ....}
__call__: <method-wrapper '__call__' of function object at 0x0000015EAB603380>
__eq__: <method-wrapper '__eq__' of function object at 0x0000015EAB603380>

Globals (>) 
class variables (>) 
Sandbox: <class '__main__.Sandbox'> (>) 
function variables (>) 
ask_secret: <function Sandbox.ask_secret at 0x000002412C3D3380> (>) 
special variables (>)
__globals__: {'__name__': '__main__', '__doc__': None, ..., 'SECRET': 'et merci la zone'}

"""

# {self.__init__.__globals__[globals][SECRET]}
# self.__init__.__globals__['SECRET']
# {self.__class__.__module__.__dict__['SECRET']}