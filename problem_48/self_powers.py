def self_powers(last_power):
    return sum(map(lambda x: pow(x, x), range(1, last_power + 1)))