from scenario.particleGroups import *

def scenario(world):
	hexagon(world, (-45.0, 0.0, 0.0), 49)
	world.add_tile((7.5, 1.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((7.0, 0.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((8.0, 2.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((7.5, -1.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((8.0, -2.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((9.0, 2.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((10.0, 2.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((9.0, -2.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((10.0, -2.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((10.5, -1.0, 0), color=(0.3, 0.3, 0.8, 1.0))
	world.add_tile((10.5, 1.0, 0), color=(0.3, 0.3, 0.8, 1.0))
