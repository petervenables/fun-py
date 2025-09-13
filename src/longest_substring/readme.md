# Algorithm


- if the string is 0 or 1 in length, return the length of the string
- set the pointer start to 0 and end at 1 and index at end
- for each character in the string beyond the first:
- while the indexed char is in the substring bounded by string[start:end]:
  - ensure start does not equal end or go out of bounds
  - compare the length of this substring to the longest and set if larger
  - increment start + 1
- if the indexed char is not in the substring bounded by string[start:end]:
  - increment the end + 1
  - increment index and continue

