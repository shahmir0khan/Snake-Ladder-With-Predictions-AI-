# Snakes and Ladders With Prediction Challenge

## Overview

This project presents a modified version of the classic **Snakes and Ladders** game with an innovative twist: the introduction of an **AI-powered prediction system**. In this version, both the player and the AI predict the next dice roll. Correct predictions grant bonus options that influence the game, such as skipping turns, doubling moves, or earning points. The AI uses a **frequency-based statistical prediction model** to forecast the next dice outcome, adding strategic depth to the traditional game of chance.

## Features

- **Prediction Challenge**: Both the player and AI predict the next dice roll.
- **Bonus Rewards**: Correct predictions unlock bonuses like:
  - Doubling the move
  - Skipping the opponent’s turn
  - Gaining bonus points
- **AI Strategy**: The AI uses **frequency analysis** to predict dice rolls based on past outcomes.
- **Neutralizing Snakes**: The AI can use earned points to neutralize the effect of snakes.
- **Interactive Visuals**: The game features a GUI built with **Pygame**, providing real-time feedback on predictions and actions.

## Objective

To develop an AI-powered game where both players (human and AI) must make predictions based on historical dice rolls, which introduces strategic decision-making into the game of Snakes and Ladders, previously based solely on chance.

## Game Rules

1. **Prediction Phase**: Each turn starts with a prediction phase where the player and AI predict the next dice roll.
2. **Bonus Activation**: If the prediction is correct, the player or AI receives a bonus:
   - Double move
   - Skip the opponent’s turn
   - Gain 10 points
3. **Snake Neutralization**: The AI can use 20 points to neutralize a snake’s effect.
4. **Turn-Based Play**: The player and AI alternate turns:
   - Roll the dice
   - Move accordingly
   - Handle snake/ladder effects
   - Evaluate prediction accuracy and trigger bonuses
5. **Winning Condition**: The first player to reach the top-left corner (coordinate (162, 6)) wins.

## AI Approach

- **Prediction Model**: The AI predicts the next dice roll using **frequency-based prediction**. It maintains a history of past dice rolls and predicts the next roll based on the most frequent past outcome.
- **Heuristic Decision-Making**: After a correct prediction, the AI selects a bonus based on the current game state (e.g., proximity to opponent, position relative to snakes/ladders).

## Technologies Used

- **Python**: The primary programming language used to implement the game logic.
- **Pygame**: For creating the graphical user interface (GUI) and handling user interactions.
- **collections (Counter)**: For analyzing the frequency of past dice rolls and predicting future outcomes.


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/snakes-and-ladders-with-prediction.git

