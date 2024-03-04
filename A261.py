import chess
import chess.engine


engine = chess.engine.SimpleEngine.popen_uci("stockfish-mv")
board = chess.Board()

while True:
  result = engine.play(board, chess.engine.Limit(time=0.05))
  print(board)
  board.push_san(input("Your move: "))

# requires stockfish installed as exe, put path in place of 'stockfish-mv'
