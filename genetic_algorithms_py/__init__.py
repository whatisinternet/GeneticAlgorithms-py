import mutation
import seeding
import reproduction
import crossover
def __init__(black_box, iterations):
    seeding_pool = seeding.pool(8)
    final_pool = _aux(seeding_pool, black_box, 0, iterations)
    print seeding_pool
    print final_pool
    return final_pool

def _aux(seed, black_box, depth, max_iterations):
    if depth == max_iterations:
        return seed
    else:
        pool = reproduction.reproduce(black_box, seed)
        crossed_over = crossover.crossover(pool)
        mutated = mutation.mutate_pool(crossed_over)
        return _aux(mutated, black_box, depth + 1, max_iterations)
