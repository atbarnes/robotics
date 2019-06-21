from population import POPULATION
#import random
import copy
#import pickle
#from robot import ROBOT
#from individual import INDIVIDUAL
#import pyrosim
#import matplotlib.pyplot as plt
#parent = INDIVIDUAL()
#parent.Evaluate(True)
#print(parent.fitness)
#for i in range(0,1000): 
#	child = copy.deepcopy(parent)
#	child.Mutate()
#	child.Evaluate(True)
#	print("[g:", i+1, "] [pw: ", parent.genome, "] [p:", #parent.fitness , "] [c:" , child.fitness ,"]")
#	if (child.fitness > parent.fitness):
#		parent = child
#		child.Evaluate(True)
#		f = open('robot.p','w')
#		pickle.dump(parent , f )
#		f.close()
from environments import ENVIRONMENTS
import constants as c
import numpy as np
import matplotlib.pyplot as plt
envs = ENVIRONMENTS()
parents = POPULATION(c.popSize)
fitnesses = np.zeros(c.numGens, dtype='f')
parents.Initialize()
parents.Evaluate(envs, pp=False, pb=True)
highest = -100
for i in parents.p:
	if (parents.p[i].fitness > highest):
		highest = parents.p[i].fitness
fitnesses[0] = highest
highest = -100
for g in range(1,c.numGens):
	children = POPULATION(c.popSize)
	#FOR RANDOM SEARCH ONLY, COMMENT OUT OTHERWISE
	#for i in parents.p:
		#parents.p[i].fitness = 0
	children.Fill_From(parents)
	children.Evaluate(envs, pp=False, pb=True)
	for i in children.p:
		if (children.p[i].fitness > highest):
			highest = children.p[i].fitness
	fitnesses[g] = highest
	highest = -100
	print(g)
	children.Print()
	parents.ReplaceWith(children)
	if(g == c.numGens-1):
		for e in range(0, c.numEnvs):
			children.p[0].Start_Evaluation(envs.envs[e],pp=True, pb=False)
low = fitnesses[0]
hi = fitnesses[c.numGens-2]
print(fitnesses)
f = plt.figure()
panel = f.add_subplot(111)
panel.set_xlim(0, 100)
panel.set_ylim(0, 1.2)
#panel.set_xlim(0, c.numGens)
#panel.set_ylim(low, hi)
plt.plot(fitnesses)
plt.show()
	#children = copy.deepcopy(parents)
	#children.Mutate()
	#if(g == 199):
	#	children.Evaluate(envs, pp=False, pb=True)
	#children.Evaluate(True)
	#parents.ReplaceWith(children)
	#print(g),
	#parents.Print()



