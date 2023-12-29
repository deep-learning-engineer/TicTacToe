from tictactoe.game import TicTacToe
from ai import Agent

import pygame as pg
import torch

if __name__ == "__main__":
    pg.init()

    surface = pg.display.set_mode((900, 900))
    board = TicTacToe()
    model = Agent()
    optimizer = torch.optim.Adam(params=model.parameters(), lr=3e-4)

    while True:
        surface.fill("white")

        for tile in board.tiles:
            tile.draw(surface)

        board.is_game_over()
        if not board.turn:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    board.move(pg.mouse.get_pos())

            pg.display.flip()

        else:
            input_model = torch.tensor([tile.tile_type for tile in board.tiles]).to(torch.float32)
            output = model.forward(input_model)
            predict = torch.argmax(output)

            is_move = board.move_by_index(predict)

            if is_move:
                model.errors += 1.5
            print(is_move)
            while not is_move:
                model.errors += 0.001

                output = model.forward(input_model)
                predict = torch.argmax(output)
                is_move = board.move_by_index(predict)

                print([tile.tile_type for tile in board.tiles])
                print(predict)
                game_state = board.game_state
                if game_state == board.turn:
                    model.errors -= 3
                elif game_state == 2:
                    model.errors -= 1
                elif game_state != -1:
                    model.errors += 6

                model.train(optimizer)

        game_state = board.game_state
        if game_state == board.turn:
            model.errors -= 3
        elif game_state == 2:
            model.errors -= 1
        elif game_state != -1:
            model.errors += 6

        model.train(optimizer)

        pg.display.flip()
