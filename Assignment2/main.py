import Assignment

# Main method to run sudoku file easy, medium, hard or veryhard
def run_Sudoku():
    task = int(input("Skriv inn 1 for å kjøre easy, 2 for å kjøre medium, 3 for å kjøre hard, 4 for å kjøre veryhard, trykk 5 for å avslutte "))
    while (task == 1 or task == 2 or task == 3 or task ==4 ):
        if(task == 1):
            sudoku_csp = Assignment.create_sudoku_csp('Assignment2/easy.txt')
            solution = sudoku_csp.backtracking_search()
            if solution:
                Assignment.print_sudoku_solution(solution)
                sudoku_csp.print_backtrack_stats()
            else:
                print("Ingen løsning funnet!")
        elif(task == 2):
            sudoku_csp = Assignment.create_sudoku_csp('Assignment2/medium.txt')
            solution = sudoku_csp.backtracking_search()
            if solution:
                Assignment.print_sudoku_solution(solution)
                sudoku_csp.print_backtrack_stats()
            else:
                print("Ingen løsning funnet!")
        elif(task == 3):
            sudoku_csp = Assignment.create_sudoku_csp('Assignment2/hard.txt')
            solution = sudoku_csp.backtracking_search()
            if solution:
                Assignment.print_sudoku_solution(solution)
                sudoku_csp.print_backtrack_stats()
            else:
                print("Ingen løsning funnet!")
        elif(task == 4):
            sudoku_csp = Assignment.create_sudoku_csp('Assignment2/veryhard.txt')
            solution = sudoku_csp.backtracking_search()
            if solution:
                Assignment.print_sudoku_solution(solution)
                sudoku_csp.print_backtrack_stats()
            else:
                print("Ingen løsning funnet!")
        else:
            break
        task = int(input("Skriv inn 1 for å kjøre easy, 2 for å kjøre medium, 3 for å kjøre hard, 4 for å kjøre veryhard, trykk 5 for å avslutte "))


run_Sudoku()
