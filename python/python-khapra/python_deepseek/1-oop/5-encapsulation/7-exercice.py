class Thermostat:
    def __init__(self):
        self.__temperature = 20  # Température par défaut

    def augmenter(self):
        if self.__temperature < 30:
            self.__temperature += 1
            print("Température augmentée.")
        else:
            print("Température maximale atteinte (30°C).")

    def diminuer(self):
        if self.__temperature > 15:
            self.__temperature -= 1
            print("Température diminuée.")
        else:
            print("Température minimale atteinte (15°C).")

    def set_temperature(self, nouvelle_temp):
        if 15 <= nouvelle_temp <= 30:
            self.__temperature = nouvelle_temp
            print(f"Température réglée à {nouvelle_temp}°C.")
        else:
            print("Température invalide (doit être entre 15°C et 30°C).")

    def get_temperature(self):
        return self.__temperature

# Test
maison = Thermostat()
maison.augmenter()           # 20 → 21°C
maison.set_temperature(25)   # OK → 25°C
maison.set_temperature(10)   # Erreur : Température invalide
maison.diminuer()            # 25 → 24°C
print(maison.get_temperature())  # Affiche 24