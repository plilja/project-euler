coins = [1, 2, 5, 10, 20, 50, 100, 200]


def coin_sums(wanted_pence):
    return _coin_sums(wanted_pence, coins, {})


def _coin_sums(wanted_pence, available_coins, computation_cache):
    if wanted_pence == 0:
        return 1
    if not available_coins:
        return 0
    if (wanted_pence, len(available_coins)) in computation_cache:
        return computation_cache[(wanted_pence, len(available_coins))]

    res = 0
    first_coin = available_coins[0]
    for i in range(0, wanted_pence / first_coin + 1):
        res += _coin_sums(wanted_pence - first_coin * i, available_coins[1:], computation_cache)
    computation_cache[(wanted_pence, len(available_coins))] = res
    return res



