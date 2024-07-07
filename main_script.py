import os
import numpy as np
from creature import Creature
from cw_envt import make_arena, make_mountain, MountainEnvironment
from fitness import evolve_population

def main():
    make_arena()
    make_mountain()
    environment = MountainEnvironment(peak=(0, 10), base=(0, 0))
    population_size = 100
    num_generations = 50
    population = [Creature(start_position=[0, 0]) for _ in range(population_size)]
    
    positions_over_time = []
    fitness_over_time = []

    for generation in range(num_generations):
        population = evolve_population(population, environment)
        best_creature = max(population, key=lambda x: x.fitness)
        print(f"Generation {generation + 1}: Best fitness = {best_creature.fitness}")
        positions_over_time.append([creature.position for creature in population])
        fitness_over_time.append([creature.fitness for creature in population])

    best_creature = max(population, key=lambda x: x.fitness)
    print(f"Best creature position: {best_creature.position}")
    print(f"Best creature fitness: {best_creature.fitness}")

    # Ensure the directory exists
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the best creature's URDF file
    best_creature_filepath = os.path.join(output_dir, 'best_creature.urdf')
    with open(best_creature_filepath, 'w') as f:
        f.write(best_creature.to_xml())

    print(f"The best creature's URDF file is saved at: {best_creature_filepath}")

    # Save positions and fitness data
    np.save(os.path.join(output_dir, 'positions_over_time.npy'), positions_over_time)
    np.save(os.path.join(output_dir, 'fitness_over_time.npy'), fitness_over_time)

if __name__ == "__main__":
    main()
