# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

## Question 1 (Naked Twins)
#### Q: How do we use constraint propagation to solve the naked twins problem?  
Constraint propagation is the applying of local constraints to reduce a search
space. In the case of Sudoku, assuming we only look for twins with two possible
values for their box, we can't start off with applying `naked_twins`; we have to reduce
the possibilities of the board first. After we've applied the `eliminate` and
`only_choice` constraints, we've sufficiently reduced the amount of possibilities
per box to apply `naked_twins`. This constraint we can apply when there are two boxes
that both contain the same two values as possibilities. This means that we can remove
these two values as possibilities for their peers, thus further reducing the number of
possible boards we have to search through to find a solution.


## Question 2 (Diagonal Sudoku)
#### Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
The diagonal-sudoku *problem* in this case is another "constraint" we can use
to arrive closer to an eventual solution. I put constraint in quotes as it's not
a being coded as a function like our other constraints, like `only_choice`,
`eliminate`, and `naked_twins`. It actually bolsters those constraint functions
by applying another set of boxes to be viewed as peers giving us the ability to
enforce those constraints over a larger set of the board.
