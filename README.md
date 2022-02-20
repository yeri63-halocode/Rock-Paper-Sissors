# Rock Paper Sissors

Here's a favorite game, played with nothing more than two friends using simple hand gesters<sup>1</sup>, representing the objects of the game in the title. What is so fantastic about the game is its simplicity, and the lack materials needed to play. I've seen it played on road trips, summer camp, and on the playground. The challenge was always trying to predict what your opponent was going to use, to block or win that game.

The game has 1 of 3 possible outcomes, a win, draw, or loss. The win or loss is based on which item is selected<sup>2</sup>, as each item has the ability to beat, be beaten, or force a draw based on the following rules, rock crushes sissors, sissors cuts paper, and paper wraps rock, all producing a win for the player selecting the 1st item. A draw results when both players pick the same object.

Use the table below to see all the possible scenarios when playing against the Halocode computer.

| You     | Halocode | Result                | Winner   |
| :-:     | :-:      | :-:                   | :-:      |
| Rock    | Rock     | Draw                  |          |
| Rock    | Paper    | Paper wraps rock.     | Halocode |
| Rock    | Sissors  | Rock crushes sissors. | You      |
| Paper   | Rock     | Paper wraps rock.     | You      |
| Paper   | Paper    | Draw                  |          |
| Paper   | Sissors  | Sissors cuts paper.   | Halocode |
| Sissors | Rock     | Rock crushes sissors. | Halocode |
| Sissors | Paper    | Sissors cuts paper.   | You      |
| Sissors | Sissors  | Draw                  |          |

So the next time you have some time on your hands, but no one to play this game with, consider playing this against the Halocode computer. You may be pleasantly surprised by the outcome.

Notes:

1. The hand gesters used to represent the items in the game are a closed fist (rock), flat hand (paper), and peace sign pointed horizontally (sissors).
2. An easy way to see who would win is by recalling the game title, "Rock, Paper, Sissors", and the word order. The winner will always be the player who picked the word to the right of the word selected by the other player. Using this schema, Rock would be considered to be to the right of word Sissors.

### mBlock5 source code

![mBlock5-code](https://github.com/yeri63-halocode/Rock-Paper-Sissors/raw/main/RockPaperSissors.png)
