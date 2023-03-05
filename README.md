# SudokuSolver

## Introduction

Sudoku is a popular logic-based game involving a 9x9 grid divided into 3x3 sub-grids. The goal of the game is to fill in the empty squares with numbers from 1 to 9, such that each row, column, and sub-grid contains all the numbers from 1 to 9 exactly once.

This game can get challenging- that's where a Sudoku solver comes in! The solver can solve the puzzle no matter the difficulty. 

The purpose of this sudoku solver is to help others solve the puzzle and to help those who want to learn more about the techniques used to solve Sudoku.

## Functionality

Upon launching Sudoku grid appears where inputs may be typed directly into the boxes.<br>
Solve button will use the algorithm to solve the puzzle and Clear button will reset the the grid.<br><br>
<img src = "https://user-images.githubusercontent.com/75912590/222982067-f9834010-97ae-4b2e-a7ce-f3ce29e6ad3d.png" width ="300" /> <img src = "https://user-images.githubusercontent.com/75912590/222982157-0247b193-0a93-4fd1-94b0-0385bf60d9f0.png" width ="300" /> <img src = "https://user-images.githubusercontent.com/75912590/222984290-0854bce1-7b65-40e5-8d44-2215858d79eb.png" width ="300" />

## Features
* The algorithm uses a backtracking approach to solve the puzzle. It iterates through each cell in the grid, and tries out values for each empty cell until it finds a valid solution
* The _solve method is a recursive function that calls itself to solve each cell in the grid. This allows the algorithm to try out different combinations of values until it finds a valid solution.
* Time complexity and space/storage ensures the alorithm is fast and efficient.
