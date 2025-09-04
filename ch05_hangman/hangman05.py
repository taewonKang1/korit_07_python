import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
'''
이상의 코드라인을 확인하면 내부의 element가 복수의 라인으로 이루어진 str인 list라고 할 수 있습니다.
'''
logo = '''
  o         o           o           o          o        o__ __o       o          o           o           o          o  
 <|>       <|>         <|>         <|\        <|>      /v     v\     <|\        /|>         <|>         <|\        <|> 
 < >       < >         / \         / \\o      / \     />       <\    / \\o    o// \         / \         / \\o      / \ 
  |         |        o/   \o       \o/ v\     \o/   o/               \o/ v\  /v \o/       o/   \o       \o/ v\     \o/ 
  o__/_ _\__o       <|__ __|>       |   <\     |   <|       _\__o__   |   <\/>   |       <|__ __|>       |   <\     |  
  |         |       /       \      / \    \o  / \   \\          |    / \        / \      /       \      / \    \o  / \ 
 <o>       <o>    o/         \o    \o/     v\ \o/     \         /    \o/        \o/    o/         \o    \o/     v\ \o/ 
  |         |    /v           v\    |       <\ |       o       o      |          |    /v           v\    |       <\ |  
 / \       / \  />             <\  / \        < \      <\__ __/>     / \        / \  />             <\  / \        < \ 
                                                                                                                       
                                                                                                                       
                                                                                                                                                                                                                       
'''
# https://patorjk.com/software/taag/
print(logo)
lives = 6       # stages의 index number 역할을 하게 될 겁니다.
word_list = [ 'apple', 'banana', 'camel' ]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)

end_of_game = False
while not end_of_game:
    print(stages[lives])
    guess = input('알파벳을 입력하세요 >>> ').lower()

    for i in range(len(chosen_word)):
        if chosen_word[i] == guess: # 선택된 단어의 알파벳이 일치할 때
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f'당신의 기회는 {lives} 번 남았습니다.')
        if lives == 0:
            print('모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print('정답입니다 !! 💌')
        end_of_game = True # 이 시점에 end_of_game이 True가 되었으므로 다음 반복문이 실행되지 않음 -> 105번 코드라인이 실행된다는 것을 의미합니다.
        # break              # 바로 반복문 정지 -> 105 번 코드라인이 실행 x
        print(f'정답은 {chosen_word}입니다.')

    print(' '.join(display))
