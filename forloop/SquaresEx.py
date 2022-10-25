class SquaresEx:

    numberArray = [4, 2, 6, 7, 3, 5, 8, 10, 6, 1, 9, 2]
    square = 0
    squares = []
    for number in numberArray:
        square = number ** 2
        squares.append(square)
    print(squares)
