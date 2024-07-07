# with open('creature.py', 'w') as f:
#     f.write('''

# import random
# import numpy as np
# import pybullet as p

# class Creature:
#     def __init__(self, start_position, shape='box', evolveable_part_indices=[0, 1]):
#         self.position = start_position if len(start_position) == 3 else start_position + [0]
#         self.shape = shape
#         self.fitness = 0
#         self.evolveable_part_indices = evolveable_part_indices
#         self.body = self.create_body()

#     def create_body(self):
#         shape_dict = {
#             'box': (p.GEOM_BOX, [0.5, 0.5, 0.5]),
#             'cylinder': (p.GEOM_CYLINDER, [0.5, 0.5, 1]),
#             'sphere': (p.GEOM_SPHERE, [0.5])
#         }
#         shape, dimensions = shape_dict[self.shape]
#         if shape == p.GEOM_BOX or shape == p.GEOM_CYLINDER:
#             collision_shape = p.createCollisionShape(shape, halfExtents=dimensions)
#             visual_shape = p.createVisualShape(shape, halfExtents=dimensions)
#         elif shape == p.GEOM_SPHERE:
#             collision_shape = p.createCollisionShape(shape, radius=dimensions[0])
#             visual_shape = p.createVisualShape(shape, radius=dimensions[0])
#         body = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=collision_shape, baseVisualShapeIndex=visual_shape, basePosition=self.position)
#         return body

#     def move(self):
#         force = [random.uniform(-100, 100), random.uniform(-100, 100), 0]  # Increase force magnitude
#         p.applyExternalForce(self.body, -1, force, self.position, p.WORLD_FRAME)
#         p.stepSimulation()  # Ensure simulation step
#         self.position = p.getBasePositionAndOrientation(self.body)[0]
#         print(f"Position after move: {self.position}")  # Debugging

#     def calculate_fitness(self, environment):
#         peak_3d = list(environment.peak) + [0]
#         distance_to_peak = np.linalg.norm(np.array(self.position) - np.array(peak_3d))
#         self.fitness = -distance_to_peak
#         print(f"Creature at {self.position} with fitness {self.fitness}")  # Debugging

#     def to_xml(self):
#         return f'<robot><link name="creature"><visual><geometry><{self.shape}/></geometry></visual></link></robot>'


# ''')



with open('creature.py', 'w') as f:
    f.write('''

import random
import numpy as np
import pybullet as p

class Creature:
    def __init__(self, start_position, shape='box', evolveable_part_indices=[0, 1]):
        self.position = start_position if len(start_position) == 3 else start_position + [0]
        self.shape = shape
        self.fitness = 0
        self.evolveable_part_indices = evolveable_part_indices
        self.body = self.create_body()

    def create_body(self):
        shape_dict = {
            'box': (p.GEOM_BOX, [0.5, 0.5, 0.5]),
            'cylinder': (p.GEOM_CYLINDER, [0.5, 0.5, 1]),
            'sphere': (p.GEOM_SPHERE, [0.5])
        }
        shape, dimensions = shape_dict[self.shape]
        if shape == p.GEOM_BOX or shape == p.GEOM_CYLINDER:
            collision_shape = p.createCollisionShape(shape, halfExtents=dimensions)
            visual_shape = p.createVisualShape(shape, halfExtents=dimensions)
        elif shape == p.GEOM_SPHERE:
            collision_shape = p.createCollisionShape(shape, radius=dimensions[0])
            visual_shape = p.createVisualShape(shape, radius=dimensions[0])
        body = p.createMultiBody(baseMass=1, baseCollisionShapeIndex=collision_shape, baseVisualShapeIndex=visual_shape, basePosition=self.position)
        return body

    def move(self):
        force = [random.uniform(-10, 10), random.uniform(-10, 10), 0]  # Reduced force magnitude
        p.applyExternalForce(self.body, -1, force, self.position, p.WORLD_FRAME)
        p.stepSimulation()
        self.position = p.getBasePositionAndOrientation(self.body)[0]
        print(f"Position after move: {self.position}")

    def calculate_fitness(self, environment):
        peak_3d = list(environment.peak) + [0]
        distance_to_peak = np.linalg.norm(np.array(self.position) - np.array(peak_3d))
        self.fitness = -distance_to_peak
        print(f"Creature at {self.position} with fitness: {self.fitness}")

    def to_xml(self):
        return f'<robot><link name="creature"><visual><geometry><{self.shape}/></geometry></visual></link></robot>'
    
''')