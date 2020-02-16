/* @Atul Prakash
 * 1801038
 * CS231: Assignment 1:N-Queen using UCS
*/

from n_queens import NQueens


def main():
    print('******* N-Queens Problem *******')
    size = int(input('Number of Queens: '))
    print_solutions = 'true'
    n_queens = NQueens(size)
    ucs_solutions = n_queens.solve_ucs()
    if print_solutions:
        for i, solution in enumerate(ucs_solutions):
            print('UCS Solution %d:' % (i + 1))
            n_queens.print(solution)
    print('Total UCS solutions: %d' % len(ucs_solutions))

if __name__ == '__main__':
    main()
