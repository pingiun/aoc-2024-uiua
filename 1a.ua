# Experimental!
&fras "1.input"
# Preprocess the text input to turn it into an 2xm array of numbers
⊜(⊜⋕⊸≠@ )⊸≠@\n
⍉   # transpose the matrix, creating a mx2 array
°⊟  # Split the two arrays to the stack
⍆:⍆ # sort both arrays
⌵-  # difference
/+  # Sum
