# Battleship Terminal Game

## About Battleship
Battleship is a strategy type guessing game for two players. It is played on ruled grids on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns calling "shots" at the other player's ships, and the objective of the game is to destroy the opposing player's fleet. See [wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)) for more information. 

## Running the app
```
cd terminal-game-battleship  //path to the project folder
python3 Game.py
```
## How do you play
Playing this terminal game is very simple. Your terminal will be the second player and will secrelly place ships on the sea map. 
your job is to guess where they are strategically according the feedback after each attack. 
  1. You will be asked to set a dimention of your sea map, from 5 to 50 inclusive.
     Mind that this will affect the number of ships and number of attacks. The larger your sea map, you longer you will probably play.
     <p align='left'><img src="/images/start.png" alt="Sceenshot of sea map at game start" width="240" display='block'/></p>
     
  3. The number of ships and their location will be automatically set up for you.
     - Ships have various length, which is no less than 2 units and not more than half of the sea map length.
     - Ships could be placed vertically or horizontally.
     - No ship will overlap on each other.
  4. Terminal will let you know the number of ships and maximum number of attacks you could have.
     - Number of ships and number of attacks depend on the size of the sea map you set up in step one.
     - No more than 30% of the sea map will be covered by ships.
     - Number of attacks will not exceed 1/3 of the sea map units. (For example, with a sea map of size 5 x 5, you will have 8 chances to attack)
  5. You will enter into the terminal where you want to attack.
     - Horizontal axis is marked with alphabet, and vertical with number. 
     - Format of an attack location is '<alphabet><number>'. Samples: C1, A5, H8.
     ![Screenshot of sea map after several attacks](/images/attacks.png)
    
  6. After Each attack sea map will update in your terminal.
     - X: you hit a fleet! But carefully read the text, you might have hit a fleet which was already taken down. 
     - O: you missed.
  7. Hit all the fleets within the maximum number of attacks to win.
  8. At the end of the game, the sea map with all fleets marked will be revealed.
     ![Screenshot of sea map at the end of the game](/images/over.png)
     

