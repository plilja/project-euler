import unittest

from poker_hands import *


class PokerHandsTest(unittest.TestCase):

    def test_higher_card_beats_lower_card(self):
        self.assertEqual(who_wins({1: _split('5D 8C 9S JS AC'),
                                   2: _split('2C 5C 7D 8S QH')}), [1])

    def test_equal_highest_card(self):
        self.assertEqual(who_wins({1: _split('5D 8C 9S JS AC'),
                                   2: _split('2C 5C 7D 8S AH')}), [1])

    def test_equal_second_highest_card(self):
        self.assertEqual(who_wins({1: _split('5D 8C 9S JS AC'),
                                   2: _split('2C 5C TD JS AH')}), [2])

    def test_equal_third_highest_card(self):
        self.assertEqual(who_wins({1: _split('5D 8C TS JS AC'),
                                   2: _split('2C 5C TD JS AH')}), [1])

    def test_equal_fourth_highest_card(self):
        self.assertEqual(who_wins({1: _split('5D 8C TS JS AC'),
                                   2: _split('6C 8C TD JS AH')}), [2])

    def test_higher_pair_beats_lower_pair(self):
        self.assertEqual(who_wins({1: _split('5H 5C 6S 7S KD'),
                                   2: _split('2C 3S 8S 8D TD')}), [2])

    def test_equal_pair_highest_card_decides(self):
        self.assertEqual(who_wins({1: _split('5H 5C 6S 7S KD'),
                                   2: _split('5C 5S AS 8D TD')}), [2])

    def test_equal_pair_equal_highest_card_second_highest_card_decides(self):
        self.assertEqual(who_wins({1: _split('5H 5C AS 7S KD'),
                                   2: _split('5C 5S AS 8D TD')}), [1])

    def test_pair_beats_high_card(self):
        self.assertEqual(who_wins({1: _split('5H 5C 6S 7S KD'),
                                   2: _split('2C 5C 7D 8S QH')}), [1])

    def test_two_pairs_beats_one_pair(self):
        self.assertEqual(who_wins({1: _split('TH TC 6S 7S KD'),
                                   2: _split('2C 2D 8D 8S QH')}), [2])

    def test_highest_pair_in_two_pairs(self):
        self.assertEqual(who_wins({1: _split('TH TC 7S 7S KD'),
                                   2: _split('9C 9D 8D 8S QH')}), [1])

    def test_equal_highest_pair_in_two_pairs_second_pair_decides(self):
        self.assertEqual(who_wins({1: _split('TH TC 7S 7S KD'),
                                   2: _split('TC TD 8D 8S QH')}), [2])

    def test_equal_two_pairs_highest_card_decides(self):
        self.assertEqual(who_wins({1: _split('9H 9C 8S 8S KD'),
                                   2: _split('9C 9D 8D 8S QH')}), [1])

    def test_three_of_a_kind_beats_two_pair(self):
        self.assertEqual(who_wins({1: _split('9H 9C 9S 8S KD'),
                                   2: _split('AC AD KD KS QH')}), [1])

    def test_equal_three_of_kind_high_card_decides(self):
        self.assertEqual(who_wins({1: _split('9H 9C 9S 8S KD'),
                                   2: _split('9C 9D 9D KS QH')}), [2])

    def test_higher_three_of_a_kind_beats_lower(self):
        self.assertEqual(who_wins({1: _split('TH TC TS 8S KD'),
                                   2: _split('9C 9D 9D KS QH')}), [1])

    def test_straight_beats_three_of_a_kind(self):
        self.assertEqual(who_wins({1: _split('TC JS QS KD AH'),
                                   2: _split('9C 9D 9D KS QH')}), [1])

    def test_ace_can_act_as_one_in_a_straight(self):
        self.assertEqual(who_wins({1: _split('AH 2C 3S 4S 5D'),
                                   2: _split('9C 9D 9D KS QH')}), [1])
        self.assertEqual(who_wins({1: _split('AH 2C 3S 4S 5D'),
                                   2: _split('2C 3D 4D 5S 6H')}), [2])

    def test_flush_beats_straight(self):
        self.assertEqual(who_wins({1: _split('AD 6D 3D TD 5D'),
                                   2: _split('2C 3D 4D 5S 6H')}), [1])

    def test_higher_flush_beats_lower_flush(self):
        self.assertEqual(who_wins({1: _split('2S 3S 7S JS TS'),
                                   2: _split('AD 6D 3D TD 5D')}), [2])

    def test_full_house_beats_flush(self):
        self.assertEqual(who_wins({1: _split('TH TC TS 8S 8D'),
                                   2: _split('KC KD KD JS QH')}), [1])

    def test_full_house_with_higher_three_of_a_kind_beats_full_house_with_lower_three_of_a_kind(self):
        self.assertEqual(who_wins({1: _split('TH TC TS 8S 8D'),
                                   2: _split('KC KD KD 5S 5H')}), [2])

    def test_four_of_a_kind_beats_full_house(self):
        self.assertEqual(who_wins({1: _split('TH TC TS TS 8D'),
                                   2: _split('KC KD KD 5S 5H')}), [1])

    def test_higher_four_of_a_kind_beats_lower_four_of_a_kind(self):
        self.assertEqual(who_wins({1: _split('TH TC TS TS 8D'),
                                   2: _split('9C 9D 9D 9S AH')}), [1])

    def test_straight_flush_beats_four_of_a_kind(self):
        self.assertEqual(who_wins({1: _split('AH 2H 3H 4H 5H'),
                                   2: _split('9C 9D 9D 9S AH')}), [1])

    def test_higher_straight_flush_beats_lower_straight_flush(self):
        self.assertEqual(who_wins({1: _split('AH 2H 3H 4H 5H'),
                                   2: _split('2C 3C 4C 5C 6C')}), [2])

    def test_royal_straight_flush_beats_straight_flush(self):
        self.assertEqual(who_wins({1: _split('AH KH JH QH TH'),
                                   2: _split('KC QC TC 9C JC')}), [1])

    def test_when_equal_hands_both_are_winners(self):
        self.assertEqual(who_wins({1: _split('5D 8C 9S JS AC'),
                                   2: _split('5H 8S 9C JD AH')}), [1,2])

def _split(hand):
    return hand.split(' ')


if __name__ == '__main__':
    unittest.main()
