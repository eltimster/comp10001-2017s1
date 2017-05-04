test_cases = {
    "phasedout_is_valid_play":
    [
        # place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 0, 0))), 2, [(None, []), (1, [['2S', '2S', '2C', '2C'], ['AS', '5S', '5S']]), (1, [['3S', '3S', '3C'], ['AS', '4S', '4S']]), (None, [])], [(0, [(2, 'JS'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (4, ('2C', (1, 0, 4))), (5, 'KS')]), (2, [(2, 'KS'), (3, [['3S', '3S', '3C'], ['AS', '6S', '6S']])])], [0, 1, 1, 0], ['AD', '8S', '9S', '0S', 'JS'], '3C')""", True),
		# place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('5D', (1, 1, 0))), 2, [(None, []), (1, [['2S', '2S', '2C', 'AC'], ['AS', '5S', '5S']]), (1, [['3S', '3S', '3C'], ['AS', '4S', '4S']]), (None, [])], [(0, [(2, 'JS'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (4, ('AC', (1, 0, 4))), (5, 'KS')]), (2, [(2, 'KS'), (3, [['3S', '3S', '3C'], ['AS', '6S', '6S']])])], [0, 1, 1, 0], ['5D', '8S', '9S', '0S', 'JS'], '3C')""", True),
		# place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('5D', (1, 1, 0))), 2, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S', '5C']]), (1, [['3S', '3S', '3C'], ['AS', '4S', '4S']]), (None, [])], [(0, [(2, 'JS'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (4, ('5C', (1, 1, 4))), (5, 'KS')]), (2, [(2, 'KS'), (3, [['3S', '3S', '3C'], ['AS', '6S', '6S']])])], [0, 1, 1, 0], ['5D', '8S', '9S', '0S', 'JS'], '3C')""", True),
		# place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('2D', (1, 0, 0))), 2, [(None, []), (1, [['2S', '2S', '2C', 'AC'], ['AS', '5S', '5S']]), (1, [['3S', '3S', '3C'], ['AS', '4S', '4S']]), (None, [])], [(0, [(2, 'JS'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (4, ('AC', (1, 0, 4))), (5, 'KS')]), (2, [(2, 'KS'), (3, [['3S', '3S', '3C'], ['AS', '6S', '6S']])])], [0, 1, 1, 0], ['2D', '8S', '9S', '0S', 'JS'], '3C')""", True),
	]
}
