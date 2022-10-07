from tabnanny import verbose
from genetic.individual import Individual
import random

class GeneticAlgorithm(): 
    
    def __init__(self, individual: Individual):
        self.population = []
        self.history = []
        self.best_history = []         
        self.individual = individual
        self.best_individual = None
    
    def truncated_selection(self):
        cutting = round(len(self.population) * self.truncated_selection_ratio)
        pool = self.population[:cutting]
        individual1 = random.choice(pool)
        pool.remove(individual1)
        individual2 = random.choice(pool)
        pool.remove(individual2)
        while individual1 == individual2:
            if len(pool) > 0:
                individual2 = random.choice(pool)
                pool.remove(individual2)
            else:
                individual2 = None
                break
        if individual2 == None:
            return None
        return [individual1, individual2]
                        
    def run(self, population_size: int = 50, iters: int = 100, mutation_chance: float = 0.15, keep_best_ratio: float=0.3, truncated_selection_ratio: float=0.45, silent: bool = False, early_stopping: bool=True, early_stopping_tol: int = 10):
        if not silent:
            print('Creating initial population...')
        self.population = [type(self.individual)(self.individual.data, mutation_chance) for _ in range(population_size)]
        for x in self.population:
            x.calculate_fitness()        
        self.truncated_selection_ratio = truncated_selection_ratio
        last_best = 0
        tol = 0
        if not silent:
            print('Done')
        self.population.sort(reverse=True)
        
        self.best_individual = self.population[0]           
        if not silent:
            print('Starting algorithm')

        stop = False
        for i in range(iters):   
            new_population = []
            for j in range(round(len(self.population) / 2)):               
                parents = self.truncated_selection()
                if parents == None:
                    stop = True
                    if not verbose:
                        print('No parents found. Stopping algorithm')
                    break
                new_population.extend(parents[0].crossover(parents[1]))                         
            
            if stop:
                break

            for x in new_population:
                x.calculate_fitness()

            new_population += self.population[round(len(self.population) * keep_best_ratio):]            
            new_population.sort(reverse=True)

            new_population = new_population[:population_size]

            if(new_population[0] > self.best_individual):
                self.best_individual = new_population[0]
                self.best_history.append(new_population[0].fitness)
            else:                
                self.best_history.append(self.best_individual.fitness)
            self.history.append(new_population[0].fitness)
            if not silent:
                print('Iteration [', i+1, ' | ', iters, '] Best fitness:', self.best_individual.fitness, '| Best individual in current generation:', new_population[0].fitness)
            self.population = new_population 
            if self.best_individual.fitness != last_best:
                last_best = self.best_individual.fitness
                tol = 0
            elif self.best_individual.fitness == last_best:
                if early_stopping == True:
                    tol += 1
                    if tol >= early_stopping_tol:
                        if not silent:
                            print('Early stopping: iteration limit with no improvement reached')
                        break
        return self.best_individual                          