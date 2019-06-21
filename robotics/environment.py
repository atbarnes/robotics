import constants as c
class ENVIRONMENT:
	def __init__(self, ID):
		self.ID = ID
		self.l = c.L
		self.w = c.L 
		self.h = c.L
		self.x = 0
		self.y = 0
		self.z = 0
		if(self.ID == 0):
			self.Place_Light_Source_To_The_Front()
		if(self.ID == 1):
			self.Place_Light_Source_To_The_Right()
		if(self.ID == 2):
			self.Place_Light_Source_To_The_Back()
		if(self.ID == 3):
			self.Place_Light_Source_To_The_Left()

		print("Size: L: ", self.l, "W: ", self.w, "H: ", self.h, " Position: X: ", self.x," Y: ", self.y, " Z: ", self.z)

	def Place_Light_Source_To_The_Front(self):
		self.x = 0
		self.y = 40 * c.L
		self.z = 0
	def Place_Light_Source_To_The_Right(self):
		self.x = 30 * c.L
		self.y = 0
		self.z = 0
	def Place_Light_Source_To_The_Back(self):
		self.x = 0
		self.y = 30 * -c.L
		self.z = 0
	def Place_Light_Source_To_The_Left(self):
		self.x = 30 * -c.L
		self.y = 0
		self.z = 0
			

	def Send_To(self, sim):
		self.lightSource = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h)
		sim.send_light_source( body_id = self.lightSource )
		

