# Experimental!
&fras "2.input"
⊜(□⊜⋕⊸≠@ )⊸≠@\n # Read every line into a box with the row of numbers

DropOneSafe ← (
  # creates all variants of the row where one value is dropped
  # including a variant that keeps the original
  ⊙¤⬚1⊂[1]¬⋯˜ⁿ2⇡⧻.
  ≡(□▽)
  ≡⍜°□(◫2)    # window by 2
  ≡(⍜°□≡(/-)) # calc differences
  # check which safe
  ≡(+/××⊃(<0)(≥¯3):/××⊃(>0)(≤3).°□)
  >0/+ # any safe?
)
≡(DropOneSafe °□)
/+
