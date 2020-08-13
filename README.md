# Rock-Paper-Scissors
If you’ve ever wanted to create games, this project will get you started! 
In this project you will code a Rock-Paper-Scissors-Lizard-Spock game, a more advanced version of Rock-Paper-Scissors, which can be played against the computer.

### Work on project. Stage 1/5: Unfair computer
Your program should:

1. Take an input from the user
2. Find an option that wins over the user's option
3. Output a line: Sorry,``` but computer chose <option>```

### Work on project. Stage 2/5: Equalizing chances
Your program should:

1. Read user's input specifying the option that user has chosen
2. Choose a random option
3. Compare the options and determine the winner
4. Output a line depending on the result of the game:
   - Lose -> ```Sorry, but computer chose <option>```
   - Draw -> ```There is a draw (<option>)```
   - Win -> ```Well done. Computer chose <option> and failed```
   
### Work on project. Stage 3/5: Endless game
Your program should:

1. Take an input from the user
2. If the input is ```!exit```, output ```Bye!``` and stop the game
3. If the input is the name of the option, then:
4. Pick a random option
5. Output a line with the result of the game in the following format (```<option>``` is the name of the option chosen by the program):
   - Lose -> ```Sorry, but computer chose <option>```
   - Draw -> ```There is a draw (<option>)```
   - Win -> ```Well done. Computer chose <option> and failed```
6. If the input corresponds to anything else, output ```Invalid input```
7. Do it all over again

### Work on project. Stage 4/5: Scoring the game
Your program should:

1. Output a line ```Enter your name:``` . Note that the user should enter his/her name on the same line (not the one following the output!)
2. Read input specifying the user's name and output a new line **```Hello, <name>```**
3. Read a file named ```rating.txt``` and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
4. Play the game by the rules defined on the previous stages:
5. Read user's input
6. If the input is ```!exit```, output ```Bye!``` and stop the game
7. If the input is the name of the option, then:
8. Pick a random option
9. Output a line with the result of the game in the following format (```<option>``` is the name of the option chosen by the program):
   - Lose -> ```Sorry, but computer chose <option>```
   - Draw -> ```There is a draw (<option>)```
   - Win -> ```Well done. Computer chose <option> and failed```
10. For each draw, add 50 point to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
11. If the input corresponds to anything else, output ```Invalid input```
12. Play the game again

### Work on project. Stage 5/5: More options
Your program should:

1. Output a line ```Enter your name:``` . Note that the user should enter his/her name on the same line (not the one following the output!)
2. Read input specifying the user's name and output a new line **```Hello, <name>```**
3. Read a file named ```rating.txt``` and check if there's a record for the user with the same name; if yes, use the score specified in the rating.txt for this user as a starting point for calculating the score in the current game. If no, start counting user's score from 0.
4. Read input specifying the list of options that will be used for playing the game (options are separated by comma). If the input is an empty line, play with default options.
5. Output a line ```Okay, let's start```
6. Play the game by the rules defined on the previous stages:
7. Read user's input
8 .If the input is ```!exit```, output ```Bye!``` and stop the game
9. If the input is the name of the option, then:
10. Pick a random option
11. Output a line with the result of the game in the following format (```<option>``` is the name of the option chosen by the program):
   - Lose -> ```Sorry, but computer chose <option>```
   - Draw -> ```There is a draw (<option>)```
   - Win -> ```Well done. Computer chose <option> and failed```
12. For each draw, add 50 points to the score. For each user's win, add 100 to his/her score. In case the user loses, don't change the score.
13. If the input corresponds to anything else, output ```Invalid input```
14. Play the game again (with the same options that were defined before the start of the game)
