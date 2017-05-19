import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        self.assertEqual((0, 0), string_to_location("A1"))
        self.assertEqual((2, 3), string_to_location("C4"))
        
    def test_location_to_string(self):
        self.assertEqual("A1", location_to_string((0, 0)))
        self.assertEqual("C4", location_to_string((2, 3)))
        
    def test_at(self):
        self.assertEqual('R', at((1, 2)))
        self.assertEqual('-', at((0, 0)))

    def test_all_locations(self):
        self.assertEqual([(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),(1, 0) , (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2) ,(4, 3) ,(4, 4)], all_locations())

    def test_adjacent_location(self):
        self.assertEqual((0, 0), adjacent_location((0, 1), "left"))
        self.assertEqual((2, 3), adjacent_location((1, 3), "down"))

    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((1, 3), "left"))
        self.assertFalse(is_legal_move_by_musketeer((1, 3), "up"))
        self.assertFalse(is_legal_move_by_musketeer((1, 3), "right"))
        
    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((1, 2), "left"))
        self.assertFalse(is_legal_move_by_enemy((1, 2), "right"))
        self.assertFalse(is_legal_move_by_enemy((3, 1), "up"))
        self.assertFalse(is_legal_move_by_enemy((4, 3), "down"))

    def test_is_legal_move(self):
        self.assertTrue(is_legal_move((1, 3), "left"))
        self.assertFalse(is_legal_move((1, 3), "up"))
        self.assertFalse(is_legal_move((1, 3), "right"))
        
        self.assertTrue(is_legal_move((1, 2), "left"))
        self.assertFalse(is_legal_move((1, 2), "right"))
        self.assertFalse(is_legal_move((3, 1), "up"))
        self.assertFalse(is_legal_move((4, 3), "down"))

    def test_can_move_piece_at(self):
        self.assertTrue(can_move_piece_at((1, 2)))
        self.assertFalse(can_move_piece_at((0, 3)))
        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(has_some_legal_move_somewhere('M'))
        self.assertFalse(has_some_legal_move_somewhere('R'))

    def test_possible_moves_from(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, R],
                    [_, _, _, R, R] ])
        self.assertEqual([], possible_moves_from((0, 3)))
        self.assertTrue(['left', 'down'], possible_moves_from((1, 3)))
        self.assertTrue(['left', 'up', 'right'], possible_moves_from((4, 3)))
        self.assertFalse([], possible_moves_from((4, 4)))

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(can_move_piece_at((2, 2)))
        self.assertFalse(can_move_piece_at((0, 4)))
        self.assertTrue(can_move_piece_at((1, 4)))
        self.assertFalse(can_move_piece_at((1, 3)))

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((0, 0)))
        self.assertFalse(is_legal_location((0, 5)))

    def test_is_within_board(self):
        self.assertTrue(is_within_board((0, 0), 'right'))
        self.assertFalse(is_within_board((4, 4), 'right'))
        self.assertFalse(is_within_board((0, 0), 'left'))

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual([((0, 3), 'left'), ((0, 3), 'right'), ((1, 4), 'up')], all_possible_moves_for('M'))
        self.assertEqual([((0, 2), 'left'), ((0, 2), 'down')], all_possible_moves_for('R'))
       
    def test_make_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        make_move((0, 3), 'left')
        self.assertEqual(at((0, 3)), '-')
  
    def test_choose_computer_move(self):
        self.assertEqual(((1, 3), 'left'), choose_computer_move('M'))
        self.assertEqual(((1, 2), 'left'), choose_computer_move('R'))
        
    def test_is_enemy_win(self):
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())

unittest.main()
