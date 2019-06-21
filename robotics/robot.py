import random
import constants as c

class ROBOT:
		def __init__(self, sim, wts):	
				self.send_objects(sim)
				self.send_joints(sim)
				self.send_sensors(sim)
				self.send_neurons(sim)
				self.send_synapses(sim, wts)
				del self.O
				del self.J
				del self.S
				del self.SN
				del self.MN

				#sim.send_synapse(source_neuron_id = SN1 , target_neuron_id = MN2 , weight = wt )
				#sim.send_synapse(source_neuron_id = SN0 , target_neuron_id = MN2 , weight = -1.0 )

		def send_objects(self, sim):
			#self.whiteObject = sim.send_cylinder(x=0, y=0, z=0.6, length=1.0, radius=0.1)
			#self.redObject = sim.send_cylinder(x=0.0, y=0.5, z=1.1, r=1, g=0, b=0, r1=0,r2=1,r3=0)
			#1st robot
			self.O0 = sim.send_box(x=-2, y=0, z=.05, length=3*c.L, width=3*c.L, height=c.L/2, r=.5, g=.5, b=.5)
			self.O10 = sim.send_box(x=-2, y=0, z=.15, r1=-1, r2=0, r3=1, length=c.L/2, width=c.L, height=3*c.L, r=.5, g=.5, b=.5, collision_group='default')
			self.O11 = sim.send_box(x=2, y=0, z=.15, r1=1, r2=0, r3=1, length=c.L/2, width=c.L, height=3*c.L, r=.5, g=.5, b=.5)
			#self.O11 = sim.send_box(x=-2, y=.5, z=.15, r1=-1, r2=0, r3=1, length=c.L/2, width=c.L, height=3*c.L, r=.5, g=.5, b=.5, collision_group='default')
			self.O12 = sim.send_box(x=-2.15, y=0, z=.275, length=2.5*c.L, width=3*c.L, height=c.L/3, r=.5, g=.5, b=.5, collision_group='r')
			self.O13 = sim.send_box(x=2.15, y=0, z=.275, length=2.5*c.L, width=3*c.L, height=c.L/3, r=.5, g=.5, b=.5, collision_group='r')
			#self.O13 = sim.send_box(x=-2.05, y=.5, z=.275, length=2.5*c.L, width=2.5*c.L, height=c.L/3, r=.5, g=.5, b=.5, collision_group='r')
			self.O14 = sim.send_box(x=-2.15, y=0, z=.32, length=2.5*c.L, width=c.L/2, height=c.L, r=.5, g=.5, b=.5, collision_group='r')
			self.O15 = sim.send_box(x=2.15, y=0, z=.32, length=2.5*c.L, width=c.L/2, height=c.L, r=.5, g=.5, b=.5, collision_group='r')
			#self.O15 = sim.send_box(x=-2.15, y=.5, z=.32, length=2.5*c.L, width=c.L/2, height=c.L, r=.5, g=.5, b=.5, collision_group='r')
			self.O1 = sim.send_cylinder(x=-2.1, y=.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O2 = sim.send_cylinder(x=-1.9, y=.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O3 = sim.send_cylinder(x=-2.1, y=-.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O4 = sim.send_cylinder(x=-1.9, y=-.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			#2nd Robot
			self.O5 = sim.send_box(x=2, y=0, z=.05, length=3*c.L, width=3*c.L, height=c.L/2, r=.5, g=.5, b=.5)
			self.O6 = sim.send_cylinder(x=2.1, y=.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O7 = sim.send_cylinder(x=1.9, y=.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O8 = sim.send_cylinder(x=2.1, y=-.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O9 = sim.send_cylinder(x=1.9, y=-.17, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			#self.O5 = sim.send_box(x=-2, y=.5, z=.05, length=3*c.L, width=3*c.L, height=c.L/2, r=.5, g=.5, b=.5)
			#self.O6 = sim.send_cylinder(x=-2.1, y=.67, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			#self.O7 = sim.send_cylinder(x=-1.9, y=.67, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			#self.O8 = sim.send_cylinder(x=-2.1, y=.33, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			#self.O9 = sim.send_cylinder(x=-1.9, y=.33, z=.05, r1=0, r2=1, r3=0, length= 0.05, radius= 0.05, mass=1.0, collision_group='r', capped=False)
			self.O16 = sim.send_box(x=0, y=2, z=.3, r1=0, r2=1, r3=0, length=3, width=.1, height=.1, r=.5, g=.5, b=.5, collision_group='r')
			self.O17 = sim.send_box(x=-.8, y=2, z=.4, r1=1, r2=0, r3=0, length=.1, width=.1, height=.1, r=.5, g=.5, b=.5, collision_group='r')
			self.O18 = sim.send_box(x=.8, y=2, z=.4, r1=1, r2=0, r3=0, length=.1, width=.1, height=.1, r=.5, g=.5, b=.5, collision_group='r')
			sim.send_box(x=-1.5, y=2, z=.18, length=2.5*c.L, width=2.5*c.L, height=.3, r=.5, g=.5, b=.5, collision_group='r')
			sim.send_box(x=1.5, y=2, z=.18, length=2.5*c.L, width=2.5*c.L, height=.3, r=.5, g=.5, b=.5, collision_group='r')
			sim.assign_collision('r', 'r')

			self.O = {}
			self.O[0] = self.O0
			self.O[1] = self.O1
			self.O[2] = self.O2
			self.O[3] = self.O3
			self.O[4] = self.O4
			#self.O[5] = self.O5
			#self.O[6] = self.O6
			#self.O[7] = self.O7
			#self.O[8] = self.O8
			#self.O[9] = self.O9
			self.O[10] = self.O10
			self.O[11] = self.O11
			self.O[12] = self.O12
			self.O[13] = self.O13
			self.O[14] = self.O14
			self.O[15] = self.O15
			
 		def send_joints(self, sim):
			#self.joint = sim.send_hinge_joint(first_body_id = self.whiteObject, second_body_id = self.redObject, x=0, y=0, 	z=1.1, n1 =-1, n2= 0, n3 = 0, lo=-3.14159/2, hi=3.14159/2)
			self.J0 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O1, x=-2.1, y=.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J1 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O2, x=-1.9, y=.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J2 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O3, x=-2.1, y=-.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J3 = sim.send_hinge_joint(first_body_id = self.O0, second_body_id = self.O4, x=-1.9, y=-.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J4 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O6, x=2.1, y=.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J5 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O7, x=1.9, y=.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J6 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O8, x=2.1, y=-.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J7 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O9, x=1.9, y=-.17, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			#self.J4 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O6, x=-2.1, y=.67, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			#self.J5 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O7, x=-1.9, y=.67, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			#self.J6 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O8, x=-2.1, y=.33, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			#self.J7 = sim.send_hinge_joint(first_body_id = self.O5, second_body_id = self.O9, x=-1.9, y=.33, z=.05, n1=0, n2=1, n3 =0, torque=100, position_control=False)
			self.J8 = sim.send_fixed_joint(first_body_id = self.O10, second_body_id = self.O0)
			self.J9 = sim.send_fixed_joint(first_body_id = self.O12, second_body_id = self.O10)
			self.J10 = sim.send_fixed_joint(first_body_id = self.O14, second_body_id = self.O12)
			self.J11 = sim.send_fixed_joint(first_body_id = self.O11, second_body_id = self.O5)
			self.J12 = sim.send_fixed_joint(first_body_id = self.O13, second_body_id = self.O11)
			self.J13 = sim.send_fixed_joint(first_body_id = self.O15, second_body_id = self.O13)
			self.J14 = sim.send_fixed_joint(first_body_id = self.O17, second_body_id = self.O16)
			self.J15 = sim.send_fixed_joint(first_body_id = self.O18, second_body_id = self.O17)
		
			self.J = {}
			self.J[0] = self.J0
			self.J[1] = self.J1
			self.J[2] = self.J2
			self.J[3] = self.J3
			self.J[4] = self.J4
			self.J[5] = self.J5
			self.J[6] = self.J6
			self.J[7] = self.J7



		def send_sensors(self, sim):
			self.T0 = sim.send_touch_sensor(body_id = self.O1)
			self.T1 = sim.send_touch_sensor(body_id = self.O2)
			self.T2 = sim.send_touch_sensor(body_id = self.O3)
			self.T3 = sim.send_touch_sensor(body_id = self.O4)
			self.T4 = sim.send_touch_sensor(body_id = self.O6)
			self.T5 = sim.send_touch_sensor(body_id = self.O7)
			self.T6 = sim.send_touch_sensor(body_id = self.O8)
			self.T7 = sim.send_touch_sensor(body_id = self.O9)
			self.L4 = sim.send_position_sensor(body_id = self.O17)
			self.L5 = sim.send_position_sensor(body_id = self.O18)
			self.L6 = sim.send_position_sensor(body_id = self.O0)
			self.L7 = sim.send_position_sensor(body_id = self.O5)
			self.L8 = sim.send_light_sensor(body_id = self.O16)
			self.S = {}
			self.S[0] = self.T0
			self.S[1] = self.T1
			self.S[2] = self.T2
			self.S[3] = self.T3
			self.S[4] = self.T4
			self.S[5] = self.T5
			self.S[6] = self.T6
			self.S[7] = self.T7
			self.S[8] = self.L4
			self.S[9] = self.L5
			self.S[10] = self.L6
			self.S[11] = self.L7
			self.S[12] = self.L8
			

			
		
		def send_neurons(self, sim):	
			self.SN = {}
			for s in self.S:
				self.SN[s] = sim.send_sensor_neuron(sensor_id = self.S[s])
			self.MN = {}
			for j in self.J:					
				self.MN[j] = sim.send_motor_neuron( joint_id = self.J[j], tau = 1.0 )

		def send_synapses(self, sim, wts):
			for j in self.SN:
				for i in self.MN:
					sim.send_synapse(source_neuron_id = self.SN[j] , target_neuron_id = self.MN[i] , weight = wts[j,i])	
					
