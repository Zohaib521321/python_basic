import asyncio
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def intro(self):
            print(f"My name is {self.name} and age is {self.age}")



person=Person(name="Zohaib",
              age=30
              )
person.intro()



class Animal:
     def __init__(self,name):
          self.name=name
     def speak(self):
          print(f"{self.name} can speak")      

class Dog(Animal):
     def speak(self):
          print(f"{self.name} bark")

class Cat(Animal):
     def speak(self):
          print(f"{self.name} meon")


dog=Dog(name="Dog")
cat=Cat(name="Cat")

dog.speak()
cat.speak()



class StaticProgramm:
     #staticMethod
     name="Zohaib"
     @staticmethod
     def greet():
          print(f"Hello my name is {StaticProgramm.name}")



StaticProgramm.greet()          


class AsyncExample:
     @staticmethod
     async def printAfterDelay():
          await asyncio.sleep(3)
          print("Print after 3 second")

asyncio.run(AsyncExample.printAfterDelay())
