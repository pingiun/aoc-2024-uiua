&fras "2.input"
⊜(□⊜⋕⊸≠@ )⊸≠@\n # Read every line into a box with the row of numbers

∵⍜°□(◫2) # window every box by two
♭        # deshape?
∵⍜°□(⍉)  # transform to put the pairs in the correct dimension
∵⍜°□(/-) # find the differences of the pairs
# check which rows are safe, by comparing the differnces
∵(+/××⊃(<0)(≥¯3):/××⊃(>0)(≤3).°□)
/+ # sum up the rows that are safe
