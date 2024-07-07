# # Save the content to fitness.py
# with open('cw-envt.py', 'w') as f:
#     f.write('''


# import random
# import numpy as np
# import pybullet as p
# from creature import Creature

# class MountainEnvironment:
#     def __init__(self, peak, base):
#         self.peak = peak
#         self.base = base

# def selection(population):
#     sorted_population = sorted(population, key=lambda x: x.fitness, reverse=True)
#     return sorted_population[:len(population) // 2]

# def crossover(parent1, parent2):
#     child_position = [
#         (parent1.position[0] + parent2.position[0]) / 2,
#         (parent1.position[1] + parent2.position[1]) / 2,
#         (parent1.position[2] + parent2.position[2]) / 2]
#     child_shape = random.choice([parent1.shape, parent2.shape])
#     return Creature(child_position, shape=child_shape, evolveable_part_indices=parent1.evolveable_part_indices)

# def mutate(creature, mutation_rate=0.1):
#     if random.random() < mutation_rate:
#         if 0 in creature.evolveable_part_indices:
#             creature.position[0] += random.uniform(-1, 1)
#         if 1 in creature.evolveable_part_indices:
#             creature.position[1] += random.uniform(-1, 1)
#         if 2 in creature.evolveable_part_indices:
#             creature.position[2] += random.uniform(-1, 1)
#         if random.random() < 0.1:  # Small chance to mutate shape
#             creature.shape = random.choice(['box', 'cylinder', 'sphere'])
#     return creature

# def evolve_population(population, environment):
#     # Calculate fitness for all creatures
#     for creature in population:
#         creature.move()
#         creature.calculate_fitness(environment)
    
#     # Log the fitness values
#     for creature in population:
#         print(f"Pre-selection fitness: {creature.fitness}")

#     selected_population = selection(population)
    
#     # Log selected creatures' fitness values
#     for creature in selected_population:
#         print(f"Selected fitness: {creature.fitness}")

#     next_generation = []

#     while len(next_generation) < len(population):
#         parent1 = random.choice(selected_population)
#         parent2 = random.choice(selected_population)
#         child = crossover(parent1, parent2)
#         next_generation.append(mutate(child))

#     # Recalculate fitness for the next generation
#     for creature in next_generation:
#         creature.calculate_fitness(environment)
#         print(f"Next generation fitness: {creature.fitness}")

#     return next_generation

# def main():
#     p.connect(p.DIRECT)
#     population_size = 10
#     generations = 5
#     start_position = [0, 0, 0]
#     environment = MountainEnvironment(peak=[10, 10], base=[0, 0])

#     population = [Creature(start_position) for _ in range(population_size)]

#     results = []
#     for generation in range(generations):
#         print(f"Generation {generation}")
#         population = evolve_population(population, environment)
#         gen_results = []
#         for creature in population:
#             print(f"Creature Fitness: {creature.fitness}")
#             gen_results.append(creature.fitness)
#         results.append(gen_results)
#     p.disconnect()
#     return results

# if __name__ == "__main__":
#     main()



# ''')            



import random
import numpy as np
import pybullet as p
import json
from creature import Creature

class MountainEnvironment:
    def __init__(self, peak, base):
        self.peak = peak
        self.base = base

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
    # Calculate fitness for all creatures
    for creature in population:
        creature.move()
        creature.calculate_fitness(environment)
    
    # Log the fitness values
    for creature in population:
        print(f"Pre-selection fitness: {creature.fitness}")

    selected_population = selection(population)
    
    # Log selected creatures' fitness values
    for creature in selected_population:
        print(f"Selected fitness: {creature.fitness}")

    next_generation = []

    while len(next_generation) < len(population):
        parent1 = random.choice(selected_population)
        parent2 = random.choice(selected_population)
        child = crossover(parent1, parent2)
        next_generation.append(mutate(child))

    # Recalculate fitness for the next generation
    for creature in next_generation:
        creature.calculate_fitness(environment)
        print(f"Next generation fitness: {creature.fitness}")

    # Save best creatures to a file
    best_creatures = [{
        'position': creature.position,
        'shape': creature.shape,
        'fitness': creature.fitness
    } for creature in selected_population]

    with open('best_creatures.json', 'w') as f:
        json.dump(best_creatures, f, indent=4)

    return next_generation

def main():
    p.connect(p.DIRECT)
    population_size = 10
    generations = 5
    start_position = [0, 0, 0]
    environment = MountainEnvironment(peak=[10, 10], base=[0, 0])

    population = [Creature(start_position) for _ in range(population_size)]

    results = []
    for generation in range(generations):
        print(f"Generation {generation}")
        population = evolve_population(population, environment)
        gen_results = []
        for creature in population:
            print(f"Creature Fitness: {creature.fitness}")
            gen_results.append(creature.fitness)
        results.append(gen_results)
    p.disconnect()
    return results

if __name__ == "__main__":
    main()
# ''')
