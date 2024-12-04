&fras "3.input"

⊜□ ¬⊸⌕"don't()"   # Split on "don't()"
≡◇(□⊜□ ¬⊸⌕"do()") # Split again on "do()" (nested boxed arrays)
/◇⊂               # Unnest
∵(¬⊢⌕"on't()"°□). # Check which strings don't start with on't()
▽                 # Keep those arrays
/◇⊂               # Join the strings into one big string
# Apply the 3a solution:
regex "mul\\((\\d+),(\\d+)\\)"
≡↘1 # drop the first element of every row, the full capture
≡⋕  # parse the regex'd numbers
≡/× # do the mults
/+  # sum the results
