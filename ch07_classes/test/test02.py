'''
학생의 이름과 학번, 그리고 과목별 성적을 관리하는 Student 클래스를 작성하시오.
이 클래스는 생성자를 통해 학생 정보와 성적 딕셔너리를 초기화하고, 성적을 추가하는 메서드와 평균 성적을 계산하여 반환하는 메서드를 포함해야 한다.
지시사항:
1. Student 클래스를 정의하고, 생성자(__init__)를 통해 name과 student_id를 초기화하시오. 성적을 저장할 빈 딕셔너리(grades)도 초기화하시오.
참고 -
self.name = name
self.student_id = student_id
self.grade = {}
2. add_grade라는 메서드를 정의하여 subject와 score를 매개변수로 받아 grades 딕셔너리에 추가하시오.
3. get_average_grade라는 메서드를 정의하여 grades 딕셔너리의 점수들을 기반으로 평균 성적을 계산하여 반환하시오.
4. Student 객체를 생성하고, 성적을 추가한 뒤, 평균 성적을 출력하시오.
실행 예:
학생 이름: 김일
평균 성적: 90.0점
'''

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grade = {}

    def set_name(self, name):
        self.name = name

    def set_student_id(self, student_id):
        self.student_id = student_id

    def get_name(self):
        return self.name

    def get_student_id(self):
        return self.student_id

    def add_grade(self, subject, score):
        self.grade[subject] = score

    def average_grade(self):
        return sum(self.grade.values()) / len(self.grade)

    def print_all_status(self):
        print(f'학생이름 : {self.name}')
        print(f'평균성적 : {self.average_grade()}')

student1 = Student('김일', '001')
student1.add_grade('국어', 89)
student1.add_grade('수학', 91)
student1.print_all_status()
