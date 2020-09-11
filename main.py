# Author: Michael Lavallee mal6423@gmail.com
# Collaborator: 
# Collaborator:
# Collaborator:
# Section: 
# Breakout: 
import math
def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is: {getLetterGrade(grade)}.")
def getLetterGrade(grade):
  if grade >= 93:
    return "A"
  elif grade > 90 and grade < 93:
    return "A-"
  elif grade < 90 and grade >= 87:
    return "B+"
  elif grade < 87 and grade >= 83:
    return "B"
  elif grade < 83 and grade >= 80:
    return "B-"
  elif grade < 80 and grade >= 77:
    return "C+"
  elif grade < 77 and grade >= 70:
    return "C"
  elif grade < 70 and grade >= 60:
    return "D"
  elif grade < 60:
    return "F"
  else:
    return "Error"

if __name__ == "__main__":
  run()