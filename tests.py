# dictionary of tests, one for each function in the project spec; in each case, list a number of function calls (as a str), and the correct output for each

# Version: 1.1
# Created 13/5/17




test_cases = {
    "phasedout_group_type":
    [
        ("""submission.phasedout_group_type(['2S', '2C', '2H'])""", 1), 
        ("""submission.phasedout_group_type(['AS', '2C', '3S', '4C'])""", None), 
        ("""submission.phasedout_group_type(['2C', '3S', '4C', '5S'])""", 5), 
    ],


    "phasedout_phase_type":
    [
        # two sets of three of same value (basic case)
        ("""submission.phasedout_phase_type([['9D', '9S', '9D'], ['0D', '0S', '0D']])""", 1), 
        # two sets of three of same value (case where value is the same)
        ("""submission.phasedout_phase_type([['9D', '9S', '9D'], ['9H', '9S', '9H']])""", 1), 
        # INVALID version of two sets of three of same value, as TOO MANY Wilds
        ("""submission.phasedout_phase_type([['9D', '9S', 'AD'], ['6D', 'AS', 'AD']])""", None), 
        # INVALID version of two sets of three, as one set is all Wilds
        ("""submission.phasedout_phase_type([['9D', '9S', 'AD'], ['AC', 'AS', 'AD']])""", None), 

        # one set of seven cards of same suit (basic case)
        ("""submission.phasedout_phase_type([['9D', '7D', '9D', '2D', '0D', '0D', 'KD']])""", 2), 
        # one set of seven cards of same suit (with Wilds)
        ("""submission.phasedout_phase_type([['9D', '7D', 'AH', '2D', '0D', 'AS', 'KD']])""", 2), 
        # INVALID set of seven cards of same suit (as ALL Wilds)
        ("""submission.phasedout_phase_type([['AD', 'AD', 'AH', 'AH', 'AS', 'AS', 'AC']])""", None), 
        # INVALID one set of cards of same suit, as wrong number
        ("""submission.phasedout_phase_type([['9D', '7D', 'AH', '2D', '0D', 'AS', 'KD', 'JD']])""", None), 

        # two sets of four of same value (basic case)
        ("""submission.phasedout_phase_type([['9D', '9S', '9D', '9C'], ['0D', '0S', '0D', '0H']])""", 3), 
        # two sets of four of same value (case where value is the same)
        ("""submission.phasedout_phase_type([['9D', '9S', '9D', '9C'], ['9H', '9S', '9H', '9C']])""", 3), 
        # INVALID version of two sets of four of same value, as TOO MANY Wilds
        ("""submission.phasedout_phase_type([['9D', '9S', 'AD', '9H'], ['6D', 'AS', 'AD', 'AH']])""", None), 
        # INVALID version of two sets of four, as one set is all Wilds
        ("""submission.phasedout_phase_type([['9D', '9S', 'AD', '9H'], ['AC', 'AS', 'AD', 'AH']])""", None), 

        # one run of eight cards (basic case)
        ("""submission.phasedout_phase_type([['2D', '3C', '4D', '5S', '6C', '7D', '8H', '9S']])""", 4), 
        # INVALID run of eight cards (out of order)
        ("""submission.phasedout_phase_type([['3C', '2D', '4D', '5S', '6C', '7D', '8H', '9S']])""", None), 
        # one run of eight cards (with Wilds)
        ("""submission.phasedout_phase_type([['3C', 'AD', '5S', '6C', '7D', '8H', 'AC', 'AS']])""", 4), 
        # one run of eight cards (with Wilds, incl at start)
        ("""submission.phasedout_phase_type([['AH', 'AC', 'AD', '5S', '6C', '7D', '8H', '9S']])""", 4), 
        # INVALID run of eight cards (first Wild assigned to invalid value)
        ("""submission.phasedout_phase_type([['AD', '2D', '3C', 'AD', '5S', '6C', '7D', '8H']])""", None), 

        # one run of four cards of same colour + one set of four of same value (basic case)
        ("""submission.phasedout_phase_type([['2D', '3H', '4D', '5D'], ['7C', '7D', '7H', '7C']])""", 5), 
        # one run of four cards of same colour + one set of four of same value (with Wilds)
        ("""submission.phasedout_phase_type([['AD', '3H', '4D', '5D'], ['7C', '7D', 'AH', '7C']])""", 5), 
        # INVALID run of four cards of same colour + one set of four of same value (order wrong)
        ("""submission.phasedout_phase_type([['7C', '7D', '7H', '7C'], ['2D', '3H', '4D', '5D']])""", None), 
        # IVALID run of four cards of same colour + one set of four of same value (Wild in run assigned to invalid value)
        ("""submission.phasedout_phase_type([['AC', 'AD', '3H', '4D'], ['7C', '7D', 'AH', '7C']])""", None), 
        # one run of four cards of same colour + one set of four of same value (with Wilds)
        ("""submission.phasedout_phase_type([['AD', '3D', '4D', '5D'], ['7C', '7D', 'AH', '7C']])""", 5), 
        # INVALID run of four cards of same colour + one set of four of same value (run out of order)
        ("""submission.phasedout_phase_type([['AD', '4D', '3D', '5D'], ['7C', '7D', 'AH', '7C']])""", None), 

        # INVALID phase (set of three and set of four)
        ("""submission.phasedout_phase_type([['9D', '9S', 'AD'], ['AC', 'AS', 'AD', 'AH']])""", None), 
    ],
    "phasedout_is_valid_play":
    [
        # play Phase 1
        ("""submission.phasedout_is_valid_play((3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [0, 0, 0, 0], ['AS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'], 'KC')""", True),
        # INVALID attempt to play Phase 1 (as already on Phase 2)
        ("""submission.phasedout_is_valid_play((3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [1, 0, 0, 0], ['AS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # INVALID attempt to play Phase 1 (as doesn't hold the necessary cards)
        ("""submission.phasedout_is_valid_play((3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [1, 0, 0, 0], ['KS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # play Phase 2
        ("""submission.phasedout_is_valid_play((3, [['2S', '2S', '9S', 'AS', '5S', '5S', 'JS']]), 0, [(None, []), (None, []), (None, []), (None, [])], [(0, [(1, 'XX')])], [1, 0, 0, 0], ['AS', '2S', '2S', '2C', '5S', '5S', '7S', '8S', '9S', '0S', 'JS'], 'KC')""", True),

        # place card on own phase (set of three)
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 0, 3))), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(1, 'XX'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
        # place card on own phase (set of three)
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 1, 0))), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
        # place card on own phase (set of same suit)
        ("""submission.phasedout_is_valid_play((4, ('JS', (1, 0, 0))), 1, [(None, []), (2, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']])])], [0, 2, 0, 0], ['5D', '0S', 'JS', 'KC'], 'KC')""", True),
        # INVALID attempt to place card on own phase (wrong suit)
        ("""submission.phasedout_is_valid_play((4, ('KC', (1, 0, 0))), 1, [(None, []), (2, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', 'AS', '5S', '5S', '7S', 'JS']])])], [0, 2, 0, 0], ['5D', '0S', 'JS', 'KC'], 'KC')""", False),
        # place card on own phase (set of four)
        ("""submission.phasedout_is_valid_play((4, ('5D', (1, 1, 0))), 1, [(None, []), (3, [['2S', '2S', '2C', '2H'], ['AS', '5S', '5S', '5H']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C', '2H'], ['AS', '5S', '5S', '5H']])])], [0, 3, 0, 0], ['5D', '0S', 'JS'], 'KC')""", True),
        # INVALID attempt to place card on own phase (index incorrect)
        ("""submission.phasedout_is_valid_play((4, ('AD', (1, 0, 4))), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # INVALID attempt to place card on own phase (group ID incorrect)
        ("""submission.phasedout_is_valid_play((4, ('2H', (1, 1, 3))), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['2H', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # INVALID attempt to place card on Player 0's phase (hasn't picked up card yet)
        ("""submission.phasedout_is_valid_play((4, ('2C', (0, 1, 3))), 1, [(1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, []), (None, [])], [(0, [(1, 'XX'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [1, 0, 0, 0], ['AD', '2C', '2H', '2H', '5H', '5D', '7S', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # INVALID attempt to place card on Player 0's phase (hasn't got own phase yet)
        ("""submission.phasedout_is_valid_play((4, ('2C', (0, 1, 3))), 1, [(1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, []), (None, [])], [(0, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])]), (1, [(1, '0S')])], [1, 0, 0, 0], ['AD', '2C', '2H', '2H', '5H', '5D', '7S', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # place card on own phase (run of 8)
        ("""submission.phasedout_is_valid_play((4, ('0S', (1, 0, 8))), 1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']])])], [0, 4, 0, 0], ['5D', '0S', 'JS'], 'KC')""", True),
        # INVALID attempt to place card on own phase (run of 8 -- doesn't hold card)
        ("""submission.phasedout_is_valid_play((4, ('0S', (1, 0, 8))), 1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']])])], [0, 4, 0, 0], ['5D', '9S', 'JS'], 'KC')""", False),
        # place card on own phase (run of 8 -- Wild)
        ("""submission.phasedout_is_valid_play((4, ('AS', (1, 0, 8))), 1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']])])], [0, 4, 0, 0], ['5D', 'AS', 'JS'], 'KC')""", True),
        
        # discard card
        ("""submission.phasedout_is_valid_play((5, 'JS'), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", True),
        # INVALID attempt to discard card (doesn't hold card)
        ("""submission.phasedout_is_valid_play((5, 'JC'), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']])])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", False),
        # INVALID attempt to discard card (has already discarded card)
        ("""submission.phasedout_is_valid_play((5, '9S'), 1, [(None, []), (1, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2S', '2S', '2C'], ['AS', '5S', '5S']]), (5, 'JC')])], [0, 1, 0, 0], ['AD', '8S', '9S', '0S', 'JS'], 'KC')""", False),
    ],

    "phasedout_score":
    [
        ("""submission.phasedout_score(['9D', '9S', '9D', '0D', '0S', '0D'])""", 57), 
        ("""submission.phasedout_score(['2D', '9S', 'AD', '0D'])""", 46), 
        ("""submission.phasedout_score([])""", 0), 
    ],

    "phasedout_play":
    [
        # can only discard final card
        ("""submission.phasedout_play(1, [(None, []), (4, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H', '0S', 'JS']]), (None, []), (None, [])], [(0, [(1, 'XX'), (5, 'JS')]), (1, [(2, 'JS'), (3, [['2C', '3H', '4D', 'AD', '6S', '7C', '8S', '9H']]), (4, ('0S', (1, 0, 8))), (4, ('JS', (1, 0, 9)))])], [0, 4, 0, 0], ['5D'], '7H')""", (5, '5D')),
    ]

}
