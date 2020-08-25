import random
def main():
    score = float(input("Enter score: "))
    print(grade_calculate(score))
    score = int(random.randint(1, 100))
    print("Random score is {}".format(score))
    print(grade_calculate(score))

def grade_calculate(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()