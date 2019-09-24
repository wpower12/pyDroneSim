import numpy as np

class Drone:
	def __init__(self, *args, **kwargs):
	    self.position = np.array([0.0,0.0,0.0])
	    self.v        = np.array([0.1,0.1,0.1])

	def update(dt):
		self.position += self.v