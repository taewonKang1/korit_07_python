'''
외부 패키지의 설치 # 1 :settings를 통한 방법
좌측 리스트에서 project: 프로젝트명 으로 되어있는 부분 클릭
-> python Interpreter
-> 오른쪽 상단에 있는 + (Install) 버튼을 클릭

외부 패키지의 설치 # 2 :터미널에서 설치
pip install prettytable
'''
from prettytable import PrettyTable

from ch10_prettytable.pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()

table.field_names = ['이름', '나이', '주소']
for pokemon in pokemon_data:
    table.add_row(pokemon)
print(table)