# # Experimental!
# &fras "1.input"
# # Preprocess the text input to turn it into an mx2 array of numbers
# ⊜(⊜⋕⊸≠@ )⊸≠@\n
[3_4 4_3 2_5 1_3 3_9 3_3]
⍉  # transpose the matrix, creating a 2xm array
°⊟ # split the two arrays to the stack
⊞⌕⊙¤ # find the values from the first array in the second array
/⊂   # collapse extra dimension
≡/+  # row wise sum
