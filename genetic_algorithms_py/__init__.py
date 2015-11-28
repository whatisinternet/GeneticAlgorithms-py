import mutation
import seeding
import reproduction
import crossover
def __init__(black_box, iterations, bit_size):
    seeding_pool = seeding.pool(8, bit_size)
    final_pool = _aux(seeding_pool, black_box, 0, iterations)
    print seeding_pool
    print final_pool
    return final_pool

def _aux(seed, black_box, depth, max_iterations):
    print '\n', depth, 'Seed       ', seed
    if depth == max_iterations:
        return seed
    else:
        pool = reproduction.reproduce(black_box, seed)
        print ' reproduction ',  pool
        crossed_over = crossover.crossover(pool)
        print ' crossover    ',  crossed_over
        mutated = mutation.mutate_pool(crossed_over)
        print ' mutated      ',  mutated
        return _aux(mutated, black_box, depth + 1, max_iterations)
