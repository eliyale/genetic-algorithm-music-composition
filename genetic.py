import random
import argparse
from LZ77 import LZ77Compressor

#class to genetrate a string that resembles targetString using a genetic algorithm
#with Nomralized Compression Distance as the Fitness function
#Individuals are represented as chromosomes where their genes are a string and the fitness of that 
#individual is the NCD calcualted for the string as shown below
#
#initalization parameters:
	#target_string = string that the algorithm will attempt to replicate
	#gene_set = string comprised of all the possible sharacters in the alphabet for target_strings
	#generation size = int for number of individuals in a generation
	#n_reporduce = int for the number fo individuals in a generation that will reporduce, (determined by highest fitness)
	#mutaion_rate = float for the rate at which individual mutations in the gene strings are introduced into the offspring
	#corssover_rate = float for the percentage of parent1 chromosome that is taken in the child,
	#	a value of 1, means all of parent 1 is taken, a value of 0.5 means the chromosome is crossed over halfway
	#	!!!!might not implement this, sounds comlicated
class Generator():
	def __init__(self, target_string, gene_set, generation_size = 30, n_reproduce = 2, mutation_rate = 0.8, crossover_rate = 0.5, iterations = 30):
		self.target_string = target_string
		self.gene_set = gene_set
		self.generation_size = generation_size
		self.n_reproduce = n_reproduce
		self.mutation_rate = mutation_rate
		self.crossover_rate = crossover_rate
		self.iterations = iterations

		#the generation is initalized to an empty array
		#self.generation = []

	#begin genetic algorithm
	def run(self):

		#first create generation_size random chromosomes and populate in the generation array
		self.generation = [chromosome(genes = self._random_gene()) for x in range(self.generation_size)]

		for i in range(self.iterations):
			#sort this generation by individual fitness
			self.generation.sort(key = lambda x: x.fitness, reverse=True)

			#restrict the generation to the n_reproduce strongest individuals as parents
			parents = self.generation[:self.n_reproduce]

			#crossover the parents to create children at the given crossover rate
			children = [chromosome(genes = self._crossover(parents)) for x in range(self.generation_size - len(parents))]

			#mutate the children according to the mutation rate
			children = self._mutate(children)

			self.generation = parents + children

			verbose_print("Generation:", i)
			for x in self.generation:
				verbose_print("\tgenes:",x.genes, " fitness:", x.fitness)



	def _random_gene(self):
		return random.choices(self.gene_set, k = len(self.target_string))

	#returns a new gene from random parents selected fron gene_pool
	def _crossover(self, gene_pool):
		parent1 = random.choice(gene_pool)
		parent2 = random.choice(gene_pool)

		crossover_point = int(round(self.crossover_rate * len(self.target_string)))

		#concatenate parent genes at crossover point
		new_gene = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]

		return new_gene

	def _mutate(self, gene_pool):
		for child in gene_pool:
			if random.randint(0,99) < (self.mutation_rate * 100):
				child.genes[random.randint(0,len(child.genes)-1)] = random.choice(self.gene_set)
				#if there is a mutation we need to recalculate fitness
				child.set_fitness(child.compute_fitness())

		return gene_pool





class chromosome():
	def __init__(self, genes, fitness = 0):
		self.genes = genes
		self.fitness = self.compute_fitness()

	def compute_fitness(self):
		#compute using NCD

		compressor = LZ77Compressor()
		compressed_data = compressor.compress(self.genes)

		verbose_print(len(compressed_data))


	def set_fitness(self, new_fitness):
		self.fitness = new_fitness


if __name__ == '__main__':

	alphabet = 'abcd'
	target = 'abcdabcdabcdabcd'

	parser = argparse.ArgumentParser(description='generate music with a genetic algorithm')
	#parser.add_argument('dataset', metavar='dataset', nargs=1, type=str)
	parser.add_argument('--verbose', dest='x', action='store_const', const=True, default=False)

	args = parser.parse_args()
	verbose = args.x

	global verbose_print
	verbose_print = print if verbose else lambda *a, **k: None

	generator = Generator(target, alphabet)
	generator.run()







