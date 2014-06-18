from collections import Counter

CARD_VALUES = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}


def cards_no_suit(hand):
    return map(lambda x: CARD_VALUES[x[0]], hand)


def suits(hand):
    return map(lambda x: x[1], hand)


def value_count(hand, count):
    _card_count = card_count(hand)
    return tuple(group for group, group_count in _card_count.most_common() if group_count == count)


def card_count(hand):
    return Counter(cards_no_suit(hand))


def high_card(hand):
    return sorted(value_count(hand, 1), reverse=True)


def pair(hand):
    return value_count(hand, 2)


def two_pairs(hand):
    count_pairs = value_count(hand, 2)
    if len(count_pairs) == 2:
        return count_pairs
    else:
        return None


def three_of_a_kind(hand):
    return value_count(hand, 3)


def straight(hand):
    def is_straight(sorted_card_values):
        return map(lambda x: x - sorted_card_values[0], sorted_card_values) == range(0, 5)

    def top_card(straight_cards):
        return straight_cards[-1]

    def _straight(card_values):
        sorted_card_values = sorted(card_values)
        if is_straight(sorted_card_values):
            return top_card(sorted_card_values)
        else:
            return None

    _cards_no_suit = cards_no_suit(hand)
    _cards_no_suit_with_ace_as_zero = [card if card != CARD_VALUES['A'] else 0 for card in _cards_no_suit]
    return _straight(_cards_no_suit), _straight(_cards_no_suit_with_ace_as_zero)


def flush(hand):
    return len(set(suits(hand))) == 1


def full_house(hand):
    if three_of_a_kind(hand) and pair(hand):
        return three_of_a_kind(hand), pair(hand)
    else:
        return None


def four_of_a_kind(hand):
    return value_count(hand, 4)


def straight_flush(hand):
    if straight(hand) and flush(hand):
        return straight(hand), flush(hand)
    else:
        return None


def rank_hand(hand):
    return straight_flush(hand), \
           four_of_a_kind(hand), \
           full_house(hand), \
           flush(hand), \
           straight(hand), \
           three_of_a_kind(hand), \
           two_pairs(hand), \
           pair(hand), \
           high_card(hand)


def who_wins(player_hand_dict):
    players = player_hand_dict.keys()
    winner = [players[0]]
    winning_hand_rank = rank_hand(player_hand_dict[winner[0]])
    for player in players[1:]:
        hand_rank = rank_hand(player_hand_dict[player])
        if winning_hand_rank < hand_rank:
            winner = [player]
            winning_hand_rank = hand_rank
        elif winning_hand_rank == hand_rank:
            winner += [player]
    return winner
