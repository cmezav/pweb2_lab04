from interpreter import draw
from chessPictures import *

rockN = rock.negative()
knightN = knight.negative()
bishopN = bishop.negative()
queenN = queen.negative()
kingN = king.negative()
peonN = pawn.negative()
squareN = square.negative()

#Figuras negras en cuadrados claros
rockNsquare = square.under(rockN)
knightNsquare = square.under(knightN)
bishopNsquare = square.under(bishopN)
peonNsquare = square.under(peonN)

#Figuras negras en cuadrados oscuros
rockNsquareN = squareN.under(rockN)
knightNsquareN = squareN.under(knightN)
bishopNsquareN = squareN.under(bishopN)
peonNsquareN = squareN.under(peonN)

#Figuras blancas en cuadrados claros
rockSquare = square.under(rock)
knightSquare = square.under(knight)
bishopSquare = square.under(bishop)
peonSquare = square.under(pawn)

#Figuras blancas en cuadrados oscuros
rockSquareN = squareN.under(rock)
knightSquareN = squareN.under(knight)
bishopSquareN = squareN.under(bishop)
peonSquareN = squareN.under(pawn)