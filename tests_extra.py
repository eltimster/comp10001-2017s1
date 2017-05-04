test_cases = {
    "phasedout_is_valid_play":
    [
        # place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 1, 0))), 1, [(None, []), (1, [['2S', '2S', '2C', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
		# place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 0, 0))), 1, [(None, []), (1, [['2S', '2S', '2C', 'AC'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
		# place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 1, 0))), 1, [(None, []), (1, [['2S', '2S', '2C', '2C'], ['AS', '5S', '5S', '5C']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
		# place card on phase where group has extra cards
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 0, 0))), 1, [(None, []), (1, [['2S', '2S', '2C', '2C'], ['AS', '5S', '5S', 'AC']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
	]
}
