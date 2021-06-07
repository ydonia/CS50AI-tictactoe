# CS50AI-tictactoe
Here is an tictactoe bot I made for the AI course I'm taking at CS50. Try to beat it!

for the AI to be able to pick the best possible square, I had to use the minimax algorithm. This is a recursive algorithm, that basically checks every possible move and all the possible outcomes of the game after picking that move. It assigns a value to each move depending on whether that move is good or bad for the computer, and makes its decision based on that. Moves that favor the X player, for example, are given 1 point. Moves that benefit the O player are -1, and a tie is 0.
