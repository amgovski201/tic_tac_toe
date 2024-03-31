from gameparts import Board

from gameparts.exceptions import FieldIndexError, CellOccupiedError


def save_result(result):
    file = open('results.txt.', 'a')
    file.write(result)
    file.close


def main():
    game = Board()
    current_player = 'X'
    running = True
    game.display()
    while running:
        print(f'Ход делают {current_player}')
        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 1 or row > game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 1 or column > game.field_size:
                    raise FieldIndexError
                if game.board[row-1][column-1] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print(
                    'Пожалуйста, введите значения для строки и столбца заново.'
                )
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break
        game.make_move(row-1, column-1, current_player)
        print('Ход сделан!')
        if game.check_win(current_player):
            print(f'Победили {current_player}!')
            save_result(current_player)
            save_result('\n')
            running = False
        elif game.is_board_full():
            print('Ничья!')
            save_result('Ничья!\n')
            running = False
        game.display()
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
