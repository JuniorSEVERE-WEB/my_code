class Animal:
  def parler(self):
    print("Je suis un animal et je fais un son")

class Chien(Animal):
  def parler(self):
    print("Woof! woof!")

class Chat(Animal):
  def parler(self):
    print("Miaw! Miaw!")

c = Animal()
chien = Chien()
chat = Chat()

c.parler()
chien.parler()
chat.parler()
