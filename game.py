from random import randint
from tictactoe.sprites import ToeTile

Coordinates = tuple[int, int]


class TicTacToe:
    def __init__(self):
        self.turn = None
        self.tiles: list[ToeTile] = [ToeTile((y, x, 300, 300)) for x in range(0, 900, 300)
                                     for y in range(0, 900, 300)]
        self.game_state = -1
        self.board = None
        self.reset()

    def reset(self):
        self.tiles = [ToeTile((y, x, 300, 300)) for x in range(0, 900, 300)
                      for y in range(0, 900, 300)]
        self.turn = randint(0, 1)
        self.game_state = -1

    def move(self, coord: Coordinates):
        for tile in self.tiles:
            if tile.rect.collidepoint(coord):
                if tile.tile_type != -1:
                    return
                tile.tile_type = self.turn
                self.turn = int(self.turn == 0)
                break

    def move_by_index(self, index: int):
        if self.tiles[index].tile_type != -1:
            return False
        self.tiles[index].tile_type = self.turn
        self.turn = int(self.turn == 0)
        return True

    def possible_turns(self):
        return [ind for ind in range(9) if self.tiles[ind].tile_type != -1]

    def is_game_over(self):
        tiles_sum = -1

        for zero_step in [1, 3, 4]:
            if (len(set([self.tiles[ind].tile_type for ind in range(0, zero_step * 2 + 1, zero_step)])) == 1
                    and self.tiles[0].tile_type != -1):
                tiles_sum = self.tiles[0].tile_type

        for one_step in [3, 6]:
            if (len(set([self.tiles[ind].tile_type for ind in range(one_step, one_step + 3)])) == 1
                    and self.tiles[one_step].tile_type != -1):
                tiles_sum = self.tiles[one_step].tile_type

        for two_step in range(2, 7, 2):
            if len(set([self.tiles[ind].tile_type for ind in range(2, 7, 2)])) == 1 and self.tiles[2].tile_type != -1:
                tiles_sum = self.tiles[2].tile_type

        for three_step in [1, 2]:
            if (len(set([self.tiles[ind].tile_type for ind in range(three_step, three_step + 7, 3)])) == 1
                    and self.tiles[three_step].tile_type != -1):
                tiles_sum = self.tiles[three_step].tile_type

        if tiles_sum == 0 or tiles_sum == 1:
            self.game_state = 1 if tiles_sum == 1 else 0
            print(f"Win {'X' if tiles_sum == 1 else 'O'}")
            self.reset()
        elif all([tile.tile_type != -1 for tile in self.tiles]):
            self.game_state = 2
            print(f"Draw")
            self.reset()
