description = "In this module, will demostrate how to use the 'hello' function to greet users in different languages."

class HelloWorld:
    def __init__(self, name, language='en'):
        self.__name = name # will be mangled to HelloWorld__name
        self.language = language
    def show(self):
        greetings = {
            'en': f"Hello, {self.__name}!",
            'es': f"¡Hola, {self.__name}!",
            'fr': f"Bonjour, {self.__name}!",
            'de': f"Hallo, {self.__name}!",
            'it': f"Ciao, {self.__name}!"
        }
        return greetings.get(self.language, greetings['en'])

language = input("Enter your preferred language (en, es, fr, de, it): ")
name = input("Enter your name: ")  
hello_world = HelloWorld(name, language)
print(hello_world.show())
