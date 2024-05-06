class hero:
	def __init__(self,name):
		self.health_pool = [0,100,200,300,400,500]
		self.power_pool = [0,10,20,30,40,50]
		self.armor_pool = [0,1,2,3,4,5]
		self.__name = name
		self.__exp = 0
		self.__level = 0

	def show_info(self):
		print("\nName: {}\nLevel: {}\nHealth: {}\nPower: {}\nArmor: {}".format(
				self.__name,
				self.__level,
				self.__health,
				self.__power,
				self.__armor
			)
		)
		
    # property
	@property
	def health_pool(self):
		pass

	@property
	def power_pool(self):
		pass

	@property
	def armor_pool(self):
		pass

	@property
	def gain_exp(self):
		pass

	@property
	def level_up(self):
		pass
	
    # setter
	@health_pool.setter
	def health_pool(self,input):
		self.__health_pool = input

	@power_pool.setter
	def power_pool(self,input):
		self.__power_pool = input

	@armor_pool.setter
	def armor_pool(self,input):
		self.__armor_pool = input

	@gain_exp.setter
	def gain_exp(self,input):
		self.__exp += input
		if(self.__exp >= 100):
			self.level_up = self.__exp//100
			self.__exp %= 100

	@level_up.setter
	def level_up(self,input):
		self.__level += input
		self.__health = self.__health_pool[self.__level]
		self.__power = self.__power_pool[self.__level]
		self.__armor = self.__armor_pool[self.__level]


class hero_intelligent(hero):
	def __init__(self,name):
		super().__init__(name)
		self.health_pool = [0,50,100,150,200,250]
		self.power_pool = [0,20,40,60,80,100]
		self.armor_pool = [0,0.5,1,1.5,2,2.5]
		self.level_up = 1


class hero_strength(hero):
	def __init__(self,name):
		super().__init__(name)
		self.health_pool = [0,200,300,400,500,600]
		self.power_pool = [0,20,40,60,80,100]
		self.armor_pool = [0,2,4,6,8,10]
		self.level_up = 1