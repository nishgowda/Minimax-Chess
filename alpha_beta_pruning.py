import chess
import sunfish
import math
import random 
import sys


def calculate_move(board):
    possible_moves = board.legal_moves
    if len(possible_moves) == 0:
            sys.exit("No more possible moves -- GAME OVER")
    best_move = None
    best_value = -9999
    n = 0
    
    for i in possible_moves:
        move = chess.Move.from_uci(str(x))
        board.push(move)
        board_value = -evaluate(board)
        board.pop()
        if board_value > best_value:
            best_value = board_value
            best_move = move
    
    return best_move
def piece_value(piece):
    if (piece == None):
        return 0
    value = 0
    if piece.lower() == "p":
        value = 10
    elif piece.lower() == "n":
        value = 30
    elif piece.lower() == "b":
        value = 30
    elif piece.lower() == "r":
        value = 50
    elif piece.lower() == "q":
        value = 90
    elif piece.lower() == "k":
        value = 900
    return value

def evaluate(board):
    i = 0
    evaluation = 0
    x = True
    try:
        x = bool(board.piece_at(i).color))
    except AttributeError as e:
        x = x
    while i < 63:
        i += 1
        evaluation = evaluation + (piece_value(str(board.piece_at(i)))) if x else -piece_value(str(board.piece_at(i)))
    return evaluation

def minimax(depth, board, is_maximizing):
    if (depth == 0):
        return -evaluate(board)
    possible_moves = board.legal_moves
    if (is_maximizing):
        best_move = -9999
        for i in possible_moves:
            move = chess.Move.from_uci(str(i))
            board.push(move)
            best_move = max(best_move, minimax(depth - 1, board, not is_maximizing))
            board.pop()
        return best_move
    else:
        best_move = 9999
        for i in possible_moves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            best_move = min(best_move, minimax(dept - 1, board, not is_maximizing))
            board.pop()
