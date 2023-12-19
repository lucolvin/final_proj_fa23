# final_proj_fa23

# Comp 120-01 Final Project: The Curse of the Jungle

**Authors:** Luke Colvin, Devin Kagak  
**Institution:** Olivet Nazarene University  
**Professor:** Daniel Kender

**Date:** December 11, 2023

## Functional Specifications

### Explore

The game, *The Curse of the Jungle*, is a choice-based adventure set in a jungle environment. Players can navigate north, east, south, and west. A numerical indicator follows the player, representing their distance into the never-ending jungle. The journey reveals glimpses of different biomes, but the increasing distance makes reaching them impossible.

### Randomized Mini-Game Encounters

As players explore, they encounter random mini-games. One involves an exaggerated jungle temple with three doors, including potentially lethal ones. Another mini-game presents a tablet and a creature challenging players to play hangman with jungle-themed words.

### Goal

Players aim to explore the jungle, discover mini-games, and travel as far as possible without perishing. The game keeps track of directional travels to trigger the discovery of different environments.

## Technical Specifications

### 1. Global Variables

The program initializes local variables such as `northCounter`, `southCounter`, `eastCounter`, `westCounter`, `travelCounter`, and `environment` to track game state and player progress.

### 2. Screen Clearing

The `clearScreen()` function clears the console screen, providing a clean interface for the player. It works across different operating systems (Linux, Mac, Windows).

### 3. Player Input

The `getplayerInput()` function retrieves player input, updates the `travelCounter`, and dynamically changes the game environment after a certain number of travels.

### 4. Direction Outputs

Directional outputs are stored in the `directionOutputs` module, imported from `jungle_lists.py`. These outputs offer descriptive messages for each direction.

### 5. Command Processing

The `getCommand(playerInput)` function processes player input, converts it to lowercase, triggers mini-games with a 1 in 10 chance, and updates directional counters.

### 6. Mini-Game

The `miniGame(environment)` function initiates mini-games based on the environment (jungle or savanna). It prompts the player to make decisions with potential consequences that influence the main game progression.

### 7. Main Loop

The `main()` function initiates the main game loop, providing initial instructions. The game continues until the player quits or reaches a travel limit. A game over message is displayed with ASCII art.

### 8. Testing and Error Handling

The program includes error handling for non-string and non-integer inputs. It offers visual cues for player choices and provides feedback messages for invalid input.


