&fras "3.input"
regex "mul\\((\\d+),(\\d+)\\)"
≡↘1 # drop the first element of every row, the full capture
≡⋕  # parse the regex'd numbers
≡/× # do the mults
/+  # sum the results
