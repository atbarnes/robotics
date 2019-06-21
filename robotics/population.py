import copy
import random
from individual import INDIVIDUAL
from environments import ENVIRONMENTS
import constants as c

class POPULATION:
	def __init__ (self, popSize):
		self.p = {}
		self.popSize = popSize

	def Initialize(self):
		for i in range(0, self.popSize):
			self.p[i] = INDIVIDUAL(i)

	def Fill_From(self, other):
		self.Copy_Best_From(other)
		self.Collect_Children_From(other)

	def Copy_Best_From(self, other):
		best = -1
		index = 0
		for i in other.p:
			if(other.p[i].fitness > best):
				best = other.p[i].fitness
				index = i

		c = copy.deepcopy(other.p[index])
		self.p[0] = c
	def Collect_Children_From(self, other):
		for i in range(1, len(other.p)):
			winner = other.Winner_Of_Tournament_Selection()
			self.p[i] = copy.deepcopy(winner)
			self.p[i].Mutate()
 
	def Winner_Of_Tournament_Selection(other):
		p1 = random.randint(0, len(other.p)-1)
		p2 = random.randint(0, len(other.p)-1)
		while p2 == p1:
			p2 = random.randint(0, len(other.p)-1)
		
		
		if(other.p[p1].fitness > other.p[p2].fitness):
			return other.p[p1]
		else:
			return other.p[p2]

		
	def Print(self):
		for i in self.p:
			if (i in self.p):
				self.p[i].Print()
		print()
	def Evaluate(self, envs, pb, pp):
	    for i in self.p:
		self.p[i].fitness = 0
		self.p[i].progress1 = 0
		self.p[i].progress2 = 0
		self.p[i].distanceCar1 = 0
		self.p[i].distanceCar2 = 0

	    for e in range(0, c.numEnvs):
		for i in self.p:
			self.p[i].Start_Evaluation(envs.envs[e],pp, pb)
		for i in self.p:
			self.p[i].Compute_Fitness()

	    for i in self.p:
		self.p[i].fitness = self.p[i].fitness / c.numEnvs

	def Mutate(self):
		for i in self.p:
			self.p[i].Mutate()
	
	def ReplaceWith(self, other):
		for i in self.p:
			if ( self.p[i].fitness < other.p[i].fitness ):
				self.p[i] = other.p[i]
