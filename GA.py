
import Chromosome
import random
import Mate

class GA:
    def __init__(self):

        #Test Commit

        # ***********************************
        # * Parameters for Algorithm
        # ***********************************

        #Number of Chromosomes in each iteration
        self.populationSize = 100

        #Number of iterations to perform
        self.numIterations = 25

        #Pairing Types Currently Available:
        # a. topDown
        # b. tournament
        self.pairingType = 'topDown'

        #Mating Types Currently Available:
        # a. cycle
        # b. replacement
        self.matingType = 'replacement'

        # ***********************************
        # * Initial Population
        # ***********************************
        self.population = []
        for i in range(self.populationSize):
            trip = ['b','c','d','e','f','g','h']
            random.shuffle(trip)
            trip = ['a'] + trip + ['a']
            chromosome = Chromosome.Chromosome(trip)
            self.population.append(chromosome)



    def sortPopulation(self):
        self.population.sort(key=lambda x: x.cost, reverse=False)

    def printPopulationGenes(self):
        for chrom in self.population:
            print chrom.getGene()
            print "cost = " + str(chrom.getCost())

    def getPopulation(self):
        return self.population


    def evolve(self):

        self.sortPopulation() #Sort population first so we can kill off the worst half

        for i in range(self.numIterations):

            print 'Run ' + str(i+1)

            # * Kill of worst half
            self.population = self.population[:(self.populationSize/2)]

            # * Pair Population
            pairedPop = Mate.Mate(self.population,self.pairingType)

            # * Mate Pairs
            offspring = pairedPop.matePairs(self.matingType)

            # * Append Offspring to Population
            self.population += offspring

            # * Mutate New Population
            # TODO: Build Mutation Algorithm

            # * Resort New Population
            self.sortPopulation()

            # * Print Best Chromosome in Population
            print 'Best Trip: ' + str(self.population[0].getGene())
            print 'Cost: ' + str(self.population[0].getCost())

            # Uncomment below to see all chromosome costs at each step
            #for chrom in self.population:
             #   print chrom.getCost()

            print ''












