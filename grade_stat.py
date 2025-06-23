import numpy as np

def generate_grades(num = 50):
    return(np.sort(np.random.randint(0,101,size =num)))

def analyze_grades(grades):
    mean = np.mean(grades)
    min = np.min(grades)
    max = np.max(grades)
    aPlusGrade = grades > 90
    bPlusGrade = (grades > 80) & (grades < 90)
    cPlusGrade = (grades > 70) & (grades < 80)
    dPlusGrade = (grades > 60) & (grades < 70)
    failGrade = grades < 50
    failCount = len(grades[failGrade])
    passCount = len(grades[aPlusGrade])+len(grades[bPlusGrade])+len(grades[cPlusGrade])+len(grades[dPlusGrade])
    print(f'Mean : {mean}')
    print(f'Minimum : {min}')
    print(f'Maximum : {max}')
    print('--------')
    print(f'A plus grades : {grades[aPlusGrade]}')
    print(f'B plus grades : {grades[bPlusGrade]}')
    print(f'C plus grades : {grades[cPlusGrade]}')
    print(f'D plus grades : {grades[dPlusGrade]}')
    print(f'F grades : {grades[failGrade]}')
    print('--------')
    print(f'Overall pass grades : {passCount}')
    print(f'Overall fall grades : {failCount}')

def main():
    grades = generate_grades(50)
    analyze_grades(grades)

if __name__ == '__main__':
    main()