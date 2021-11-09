# Original challenge can be found here"
# https://www.hackerrank.com/challenges/nested-list/

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students += [[name, score]]
        
    def score(list):
        return list[1]
    
    students.sort(key=score)
    lowest_score = students[0][1]
    while students[0][1] == lowest_score:
        students.remove(students[0])
    new_low_score = students[0][1]
    name_list = [student[0] for student in students if student[1] == new_low_score]
    name_list.sort()
    for name in name_list:
        print(name)
