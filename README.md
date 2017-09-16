# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation is the applying of local constraints to reduce a search
space. In the case of Sudoku, assuming we only look for twins with two possible
values for their box, we can't start off with applying `naked_twins`; we have to reduce
the possibilities of the board first. After we've applied the `eliminate` and
`only_choice` constraints, we've sufficiently reduced the amount of possibilities
per box to apply `naked_twins`.

 constraint that
 identifies any two boxes that both share the same two possible digits and are peers
of one another. This

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *Student should provide answer here*
