import random
import hangman_arts
import hangman_word_list

print(hangman_arts.logo)
chosen_word = random.choice(hangman_word_list.word_list)
print(chosen_word)
lives = 6
display = []
for _ in range(len(chosen_word)):
    display.append('_')
print(display)

end_of_game = False
while not end_of_game:
    print(hangman_arts.stages[lives])
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
            print(hangman_arts.stages[lives])
            print(f'정답은 {chosen_word}입니다.')

    if '_' not in display:
        print('정답입니다 !! 💌')
        end_of_game = True # 이 시점에 end_of_game이 True가 되었으므로 다음 반복문이 실행되지 않음 -> 105번 코드라인이 실행된다는 것을 의미합니다.
        # break              # 바로 반복문 정지 -> 105 번 코드라인이 실행 x
        print(f'정답은 {chosen_word}입니다.')

    print(' '.join(display))