
class Facade:
    def __init__(self):
        self._servicecommerc = GServiceCommerciale()
        self._caisse = Caisse()
    def payement(self):
        self._servicecommerc.payer()
        self._caisse.payer()
        self._servicecommerc.payer()

class GServiceCommerciale:
    def payer(self):
        print("ici c'est le guichet service commerciale")

class Caisse:
    def payer(self):
        print("ici c'est la caisse")

def main():
    facade = Facade()
    facade.payement()

if __name__ == "__main__":
    main()