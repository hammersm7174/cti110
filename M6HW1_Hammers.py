# CTI-110
# M6HW1 - Test Grades and Average
# Mark Hammers
# 09 Nov 2017
#

  
#Average Function
def calc_average(score1, score2, score3, score4, score5):
    avg = (score1 + score2 + score3 + score4 + score5) / 5
    print("Your average test score is: ", str(avg))

#Grade Function
def determine_grade(score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif score < 101:
        return "A"

#Test Score Function
def test_scores():
    score1 = float(input("Please enter test score 1: "))
    score2 = float(input("Please enter test score 2: "))
    score3 = float(input("Please enter test score 3: "))
    score4 = float(input("Please enter test score 4: "))
    score5 = float(input("Please enter test score 5: "))

    return score1, score2, score3, score4, score5

#Table Function
def print_table(score1, score2, score3, score4, score5):
    print("Score\tLetter Grade")
    print(str(score1) + "\t\t" + determine_grade(score1),\
          str(score2) + "\t\t" + determine_grade(score2),\
          str(score3) + "\t\t" + determine_grade(score3),\
          str(score4) + "\t\t" + determine_grade(score4),\
          str(score5) + "\t\t" + determine_grade(score5), sep = "\n")

#Main function
def main():
    score1, score2, score3, score4, score5 = test_scores()
    print()
    print_table(score1, score2, score3, score4, score5)
    print()
    calc_average(score1, score2, score3, score4, score5)

main()
