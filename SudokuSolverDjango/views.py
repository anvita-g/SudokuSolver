from django.shortcuts import render
from .sudoku_solver import SudokuSolver


def sudoku_board(request):
    board = [[0 for _ in range(9)] for _ in range(9)]
    solution = None

    if request.method == 'POST':
        # Parses the data from the form into a 2D list of integers
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                value = request.POST.get(f'cell_{i+1}_{j+1}')
                row.append(int(value) if value.isdigit() else 0)
            board.append(row)


        solver = SudokuSolver(board)
        solution = solver.solve()

        if 'clear' in request.POST:
            solver.clear()
        else:
            solution = solver.solve()
            context = {'board': board, 'solution': solution}
            return render(request, 'sudoku_board.html', context)

    context = {
        'board': board,
        'solution': solution,
    }

    return render(request, 'sudoku_board.html', context)

