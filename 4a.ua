&fras "4.input"
⊜□⊸≠@\n
∵°□

DiagLeft ← (
  ⊸(⇡⧻)
  ≡↻
  ⍉
  ↘¯3
)

DiagRight ← (
  ⊸(¯⇡⧻)
  ≡↻
  ⍉
  ↘3
)

DFind ← (
  ≡(⌕"XMAS")
  ≡⊢
  /+
)
.
⊃⇌∘
∩(⇡-3⊸⧻
  ⊙¤
  ⊞(□↘)
  /+≡(DFind DiagLeft °□⊢)
)
+
:
.
⊃⇌∘
∩(⇡-3⊸⧻
  ⊙¤
  ⊞(□↘)
  /+≡(DFind DiagRight °□⊢)
)
:+
⊙+
# Find XMAS in all the directions
# Left to right, in all rows
/+/+≡(⌕"XMAS").
:
# Right to left, in all rows
/+/+≡(⌕"XMAS"⇌).
⊙+: # add to the total sum
⍉   # Columns are now rows and vice versa, so we can search vertically
/+/+≡(⌕"XMAS").
⊙+: # add to the total sum
/+/+≡(⌕"XMAS"⇌)
⊙+: # add to the total sum
+
