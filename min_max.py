import chess
import math
import random
import  sys

def minimax_root(depth, board,is_maximizing):
    possible_moves = board.legal_moves
    best_move = -9999  # the best possible scenario
    second_best = -9999
    third_best = -9999
    best_move_final = None

    for x in possible_moves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        value = max(best_move, minimax(depth - 1, board, not is_maximizing))
        board.pop()
        if value > best_move:
            print("Best score: " ,str(best_move))
            print("Best move: ",str(best_move_final))
            print("Second best: ", str(second_best))
            third_best = second_best
            second_best = best_move
            best_move = value
            best_move_final = move
    return best_move_final

def minimax(depth, board, is_maximizing):
    if depth == 0:
        return -evaluation(board)
    possible_moves = board.legal_moves
    if is_maximizing:
        best_move = -9999
        for x in possible_moves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            best_move = max(best_move,minimax(depth - 1, board, not is_maximizing))
            board.pop()
        return best_move
    else:
        best_move = 9999
        for x in possible_moves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            best_move = min(best_move, minimax(depth - 1, board, not is_maximizing))
            board.pop()
        return best_move

def evaluation(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color)
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (get_piece_value(str(board.piece_at(i))) if x else -get_piece_value(str(board.piece_at(i))))
    return evaluation

def get_piece_value(piece):
    if piece == None:
        return 0
    value = 0
    if piece == "P" or piece == "p":
        value = 10
    if piece == "N" or piece == "n":
        value = 30
    if piece == "B" or piece == "b":
        value = 30
    if piece == "R" or piece == "r":
        value = 50
    if piece == "Q" or piece == "q":
        value = 90
    if piece == 'K' or piece == 'k':
        value = 900
    return value

if __name__ == "__main__":
    board = chess.Board()
    print(board)
    i = 0
    while i < 100:
        if i % 2 == 0:
            move = input("Enter your move: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else:
            print("AI's turn")
            move = minimax_root(4, board, True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        i += 1

