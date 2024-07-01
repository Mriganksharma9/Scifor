# -*- coding: utf-8 -*-
"""if else statement.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QJPm5mHtRggn_Iiu9-fTmVadot5ch-c9

CONDITIONAL MAKING STATEMENTS
IT HELPS US TO MAKE DECISION BASED ON CERTAIN CONDITIONS

TYPES OF CONDITIONAL STATEMENTS

1. IF-ELSE
2. NESTED - IF - STATEMENT
3. MATCH CASE STATEMENT

1. **if else**
"""

i = 5

if (i>15):
  print("20 is less than 15")
else :
  print("stop")

"""2. Nested If

"""

if value <10 :
  print("value is less than 10")

if value>20:
  print("value ias greater than 20")

"""3. Switch Case"""

def number(a):
  match a :
    case 0 :
      return "zero"
    case 1:
      return "one"
    case 2:
      return "two"
    case default :
      return "defaultstatement"

head = number(5)
print(head)