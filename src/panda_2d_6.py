import pandas as pd

# Change False to True for this block of code to see what it does

# DataFrame applymap()
if False:
    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [10, 20, 30],
        'c': [5, 10, 15]
    })


    def add_one(x):
        return x + 1


    print df.applymap(add_one)

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)


def convert_grade(grade):
    if grade < 60:
        return 'F'
    elif grade < 70:
        return 'D'
    elif grade < 80:
        return 'C'
    elif grade < 90:
        return 'B'
    else:
        return 'A'

def convert_grades(grades):
    return grades.applymap(convert_grade)

print(convert_grades(grades_df))