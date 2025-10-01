from random import randint, choice

def check_winners(scores, student_score):
    scores = sorted(scores)
    if student_score in scores[-3:]: print('Вы в тройке победителей!')
    else: print('Вы не попали в тройку победителей')
    #print(scores)

scores = [randint(0,100) for _ in range(10)]
student_score = choice(scores)

print(f'Список баллов: {scores} \nБаллы Стаса: {student_score}')
check_winners(scores, student_score)
