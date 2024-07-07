# Save the content to fitness.py
with open('fitness.py', 'w') as f:
    f.write('''

import random
import numpy as np
from creature import Creature

def selection(population):
    sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
    return sorted_population[:len(population) // 2]

def crossover(parent1, parent2):
    child_position = [
        (parent1.position[0] + parent2.position[0]) / 2,
        (parent1.position[1] + parent2.position[1]) / 2,
        (parent1.position[2] + parent2.position[2]) / 2]
    child_shape = random.choice([parent1.shape, parent2.shape])
    return Creature(child_position, shape=child_shape, evolveable_part_indices=parent1.evolveable_part_indices)

def mutate(creature, mutation_rate=0.1):
    if random.random() < mutation_rate:
        if 0 in creature.evolveable_part_indices:
            creature.position[0] += random.uniform(-1, 1)
        if 1 in creature.evolveable_part_indices:
            creature.position[1] += random.uniform(-1, 1)
        if 2 in creature.evolveable_part_indices:
            creature.position[2] += random.uniform(-1, 1)
        if random.random() < 0.1:  # Small chance to mutate shape
            creature.shape = random.choice(['box', 'cylinder', 'sphere'])
    return creature

def evolve_population(population, environment):
    for creature in population:
        creature.move()
        creature.calculate_fitness(environment)

    selected_population = selection(population)
    next_generation = []

    while len(next_generation) < len(population):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        child = crossover(parent1, parent2)
        next_generation.append(mutate(child))

    return next_generation

class MountainEnvironment:
    def __init__(self, peak, base):
        self.peak = peak
        self.base = base

''')            