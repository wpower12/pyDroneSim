import numpy as np
import pyglet
import ratcave as rc
from drone import Drone
from pyglet.window import key

VEL = 0.5
EPSILON = 1

def make_3d_lattice(side_num, sep_len):
	# create a 3d lattice (cube) of drones
	# with side_num drones per edge, sepearted by a distance of sep_len
	# Means you will have side_num^3 many drones.
	ds = []
	for i in range(side_num):
		for j in range(side_num):
			for k in range(side_num):
				d = Drone()
				d.position = np.array([i*sep_len, j*sep_len, k*sep_len])
				ds.append(d)
	return ds

def get_center_point(ds):
	# Just the average of their positions?
	ds_pos = []
	for d in ds:
		ds_pos.append(d.position)
	return np.mean(ds_pos, axis=0)

ds  = make_3d_lattice(3, 0.5)
wps = [np.array([0.0,   0.0,  0.0]),
       np.array([100.0, 0.0,  0.0]),
       np.array([100.0, 0.0,  150.0]),
       np.array([0.0,   0.0,  0.0])]
curr_wp = 0 # What wp are we currently moving towards

def update(dt):
	global curr_wp
	# Determine velocity - Difference between curr_wp and center_point,
	# scaled by a 'max velocity'
	cp_pos = get_center_point(ds)
	new_d = (wps[curr_wp]-cp_pos)

	# If new_d is within EPSILON of current wp, move to next one
	if((new_d**2).sum()**0.5 <= EPSILON):
		curr_wp += 1
		new_d = (wps[curr_wp]-cp_pos)

	new_v = (new_d/(new_d**2).sum()**0.5)*VEL
	for d in ds:
		d.v = new_v
		d.position += d.v

	print(cp_pos, new_v)
	# if done with last WP, finish sim

pyglet.clock.schedule_interval(update, 0.5)
pyglet.app.run()