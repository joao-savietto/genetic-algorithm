from random import uniform    
from typing import Dict, List

class Individual(object):
    
    def __init__(self, data: Dict[object, object], mutation_chance: float = 0.15):
        self.chromossome = [] 
        self.fitness = 0
        self.data = data    
        self.mutation_chance = mutation_chance
        self.random_chromossome()

    def mutate(self):
        """Method to mutate the chromossome"""
        raise NotImplementedError('mutate() not implemented')

    def calculate_fitness(self):
        """Method to calculate the fitness of the individual"""
        raise NotImplementedError('calculate_fitness() not implemented')

    def random_chromossome(self) -> List[object]:
        """Method to generate a random chromossome"""
        raise NotImplementedError('random_chromossome() not implemented')

    def crossover(self, other):        
        """Method for crossover"""
        cutting = round(uniform(0, len(self.chromossome) + 1))

        son1_chromossome = other.chromossome[0 : cutting] + self.chromossome[cutting : len(self.chromossome) + 1]        
        son2_chromossome = self.chromossome[0 : cutting] + other.chromossome[cutting : len(self.chromossome) + 1]

        sub1 = type(self)(self.data, self.mutation_chance)
        sub1.chromossome = son1_chromossome
        sub1.mutate()
        sub2 = type(self)(self.data, self.mutation_chance)
        sub2.chromossome = son2_chromossome
        sub2.mutate()
        return [sub1, sub2]        
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            for i in range(len(self.chromossome)):
                if self.chromossome[i] != other.chromossome[i]:
                    return False
        else:
            return False
        return True
    
    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness != other.fitness
        return False
    
    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness < other.fitness
        return False    
    
    def __le__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness <= other.fitness
        return False     

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness > other.fitness
        return False       
    
    def __ge__(self, other):
        if isinstance(other, self.__class__):
            return self.fitness >= other.fitness
        return False                     