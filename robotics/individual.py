import random
import pyrosim
import math
import numpy
from robot import ROBOT
import constants as c
class INDIVIDUAL:
	def __init__(self, i):
		self.genome = 2 * numpy.random.random_sample((13, 8)) - 1
		self.fitness = 0
		self.distanceCar1 = 0
		self.distanceCar2 = 0
		self.progress1 = 0
		self.progress2 = 0
		self.ID = i

	def Start_Evaluation(self, env, pp, pb):
		self.sim = pyrosim.Simulator(play_blind = pb, play_paused = pp, eval_time = c.evalTime)
		self.robot = ROBOT(self.sim, self.genome)
		env.Send_To(self.sim)
		self.sim.start()

	def Compute_Fitness(self):
		self.sim.wait_to_finish()
		t = 0
		#object positions
		x1 = self.sim.get_sensor_data( sensor_id = self.robot.L4, svi=0)
		y1 = self.sim.get_sensor_data( sensor_id = self.robot.L4, svi=1)
		x2 = self.sim.get_sensor_data( sensor_id = self.robot.L5, svi=0)
		y2 = self.sim.get_sensor_data( sensor_id = self.robot.L5, svi=1)
		#car positions
		x3 = self.sim.get_sensor_data( sensor_id = self.robot.L6, svi=0)
		y3 = self.sim.get_sensor_data( sensor_id = self.robot.L6, svi=1)
		x4 = self.sim.get_sensor_data( sensor_id = self.robot.L7, svi=0)
		y4 = self.sim.get_sensor_data( sensor_id = self.robot.L7, svi=1)
		light = self.sim.get_sensor_data( sensor_id = self.robot.L8)
		#first time step
		xval = x1[0]
		yval = y1[0]
		x2val = x2[0]
		y2val = y2[0]
		x3val = x3[0]
		y3val = y3[0]
		x4val = x4[0]
		y4val = y4[0]
		#last time step
		xval2 = x1[-1]
		yval2 = y1[-1]
		x2val2 = x2[-1]
		y2val2 = y2[-1]
		x3val2 = x3[-1]
		y3val2 = y3[-1]
		x4val2 = x4[-1]
		y4val2 = y4[-1]
		#calculate distance
		distance1 = math.sqrt( (x3val - xval)**2 + (y3val - yval)**2 )
		distance2 = math.sqrt( (x4val - x2val)**2 + (y4val - y2val)**2 )
		distance3 = math.sqrt( (x3val2 - xval2)**2 + (y3val2 - yval2)**2 )
		distance4 = math.sqrt( (x4val2 - x2val2)**2 + (y4val2 - y2val2)**2 )
		#find if car made progress from last time step
		self.distanceCar1 = distance1 - distance3
		self.distanceCar2 = distance2 - distance4
		#Difference in progress between both cars
		offset = abs(self.distanceCar1 - self.distanceCar2)
		#If difference is below one, just make it one
		if (offset < 1):
			offset = 1
		if (self.distanceCar1 < 0 and self.distanceCar2 < 0):
			self.fitness = 0
		#if one car isn't making progress, make offset high
		#if (self.distanceCar1 < 0 or self.distanceCar2 < 0):
			#offset = 10
		else:
			self.fitness = ((self.distanceCar1 * self.distanceCar2)/offset) * light[-1] 
		output = ('fitness:{: 3.3f}, d:{: 3.3f}, light:{: 3.1f}, offset:{: 3.1f}').format(self.fitness, self.distanceCar1, light[-1], offset)
		output2 = ('fitness:{: 3.3f},d:{: 3.3f}, light:{: 3.1f}, offset:{: 3.1f}').format(self.fitness, self.distanceCar2, light[-1], offset)
		print output + "\n"
		print output2 + "\n"	
		#for t in range(c.evalTime):
			#object positions
			#x1 = self.sim.get_sensor_data( sensor_id = self.robot.L4, svi=0)
			#y1 = self.sim.get_sensor_data( sensor_id = self.robot.L4, svi=1)
			#x2 = self.sim.get_sensor_data( sensor_id = self.robot.L5, svi=0)
			#y2 = self.sim.get_sensor_data( sensor_id = self.robot.L5, svi=1)
			#car positions
			#x3 = self.sim.get_sensor_data( sensor_id = self.robot.L6, svi=0)
			#y3 = self.sim.get_sensor_data( sensor_id = self.robot.L6, svi=1)
			#x4 = self.sim.get_sensor_data( sensor_id = self.robot.L7, svi=0)
			#y4 = self.sim.get_sensor_data( sensor_id = self.robot.L7, svi=1)
			#light = self.sim.get_sensor_data( sensor_id = self.robot.L8)
			#this time step
			#xval = x1[t]
			#yval = y1[t]
			#x2val = x2[t]
			#y2val = y2[t]
			#x3val = x3[t]
			#y3val = y3[t]
			#x4val = x4[t]
			#y4val = y4[t]
			#next time step
			#if(t != c.evalTime - 1):
				#xval2 = x1[t+1]
				#yval2 = y1[t+1]
				#x2val2 = x2[t+1]
				#y2val2 = y2[t+1]
				#x3val2 = x3[t+1]
				#y3val2 = y3[t+1]
				#x4val2 = x4[t+1]
				#y4val2 = y4[t+1]
			#calculate distance for each time step
				#distance1 = math.sqrt( (x3val - xval)**2 + (y3val - yval)**2 )
				#distance2 = math.sqrt( (x4val - x2val)**2 + (y4val - y2val)**2 )
				#distance3 = math.sqrt( (x3val2 - xval2)**2 + (y3val2 - yval2)**2 )
				#distance4 = math.sqrt( (x4val2 - x2val2)**2 + (y4val2 - y2val2)**2 )
			#find if car made progress from last time step
				#self.distanceCar1 += (distance1 - distance3)
				#self.distanceCar2 += (distance2 - distance4)
				#if(distance1 - distance3 > 0):
					#self.progress1 += 1
		
				#if(distance2 - distance4 > 0):
					#self.progress2 += 1
				
				#output = ('Distance 1: {:3d}:: d:{: 3.3f}, progress:{: 3.1f}, light:{: 3.1f}').format(t, self.distanceCar1, self.progress1, light[-1])
				#output2 = ('Distance 2: {:3d}:: d:{: 3.3f}, progress:{: 3.1f}, light:{: 3.1f}').format(t, self.distanceCar2, self.progress2, light[-1])
				
    				#output = ('Object 1: {:3d}:: x:{: 3.1f}, y:{: 3.1f},').format(t, xval, yval)
				#output2 = ('Object 2:{:3d}:: x:{: 3.1f}, y:{: 3.1f},').format(t, x2val, y2val)
				#output3 = ('Car 1:{:3d}:: x:{: 3.1f}, y:{: 3.1f},').format(t, x3val, y3val)
				#output4 = ('Car 2:{:3d}:: x:{: 3.1f}, y:{: 3.1f},').format(t, x4val, y4val)
				#print output + "\n"
				#print output2 + "\n"
				#print output3 + "\n"
				#print output4 + "\n"
			#self.fitness = (self.distanceCar1 + self.distanceCar2) * light[-1] * 1/
			
		del self.sim
		del self.robot
	
	def Mutate(self):
		geneToMutate = random.randint(0, 9)
		geneToMutate2 = random.randint(0, 7)
		self.genome[geneToMutate][geneToMutate2] = abs(random.gauss(self.genome[geneToMutate][geneToMutate2], math.fabs(self.genome[geneToMutate][geneToMutate2])))
		if(self.genome[geneToMutate][geneToMutate2] > 1):
			self.genome[geneToMutate][geneToMutate2] = 1
		if(self.genome[geneToMutate][geneToMutate2] < -1):
			self.genome[geneToMutate][geneToMutate2] = -1
			
	def Print(self):
		print(" ["),
		print(self.ID),
		print(self.fitness),
		print("] "),
		print()
