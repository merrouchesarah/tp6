class Tri:
    def __init__(self, strategy):
        self._strategy = strategy
    def tri_interface(self):
        self._strategy.algorithm_tri()

class StrategyTri():
    def algorithm_tri(self):
        pass

class TriParSelection(StrategyTri):

    def algorithm_tri(self):
        print("***Tri par Selection***")

class TriParInsertion(StrategyTri):

    def algorithm_tri(self):
        print("***Tri par Insertion***")

class TriParFusion(StrategyTri):

    def algorithm_tri(self):
        print("***Tri par Fusion***")

class TriParDenombrement(StrategyTri):

    def algorithm_tri(self):
        print("***Tri par Denombrement***")

class TriRapide(StrategyTri):

    def algorithm_tri(self):
        print("***Tri Rapide***")

def main():
    concrete_strategy = TriParInsertion()
    tri = Tri(concrete_strategy)
    tri.tri_interface()

if __name__ == "__main__":
    main()