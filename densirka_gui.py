import tkinter as tk
import random
import time
from threading import Timer 

window = tk.Tk()
sequence = ''
'''Карты с номиналом очков могут иметь нули, которые отбирают жизни'''
cards = {1: [1, 1, 1, 1, 0, 0], 2: [2, 2, 2, 2, 0, 0],
         3: [3, 3, 3, 0, 0, 0], 4: [4, 4, 4, 0, 0, 0],
         5: [5, 5, 0, 0, 0, 0], 6: [6, 6, 0, 0, 0, 0]}
score = 0
lifes = 3
text=''
running = 1
temporary1 = dict()
temporary2 = dict()
temporary3 = dict()
temporary4 = dict()
temporary5 = dict()
temporary6 = dict()

'''Генерация последовательности, с которой будут браться числа на кнопки'''
while len(sequence) != 6:
    sequence += str(random.randrange(1, 7))
if sequence != list(sequence):
    sequence = str(sequence)
sequence = list(sequence)

'''Кубик d6'''
dice = random.randrange(1,7)

def kill():
    window.destroy()

def scoreorlife():
    global lifes, score, deleted_card, c, dice, sequence, temporary
    if deleted_card == 0:
        lifes -= 1
        text = '\nО нет, мышеловка! Жизней теперь: ' + str(lifes)
        text_log.insert(tk.END, text)
        text_log.see(tk.END)
        label_lifes = tk.Label(master=label_frame, text=lifes)
        label_lifes.grid(row=1, column=4)
        if lifes == 0:
            text = '\nУвы и ах. Вы проиграли. Ваш итоговый счёт:' + str(score)
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
            timer = Timer(5, kill)
            timer.start()
    else:
        score = score + deleted_card
        text = '\nОчков сейчас: ' + str(score)
        text_log.insert(tk.END, text)
        text_log.see(tk.END)
        label_score = tk.Label(master=label_frame, text=score)
        label_score.grid(row=1, column=1)

'''Основная функция кнопок'''
def delete1():
    global lifes, score, deleted_card, c, dice, sequence, temporary1
    #''''Проверка правильности нажатия игроком кнопки. Если в последовательности
    #есть цифры на которые игрок не кликает - вывод повтора попытки'''
    if str(button1['text']) != str(dice) and str(dice) in sequence:
        text = '\nОшибка ввода: Выберите карту совпадающую с кубиком'
        text_log.insert(tk.END, text)
        text_log.see(tk.END)

    #'''Условный вывод+удаление полученной карты по ключу из словаря cards
    #и перегенерация цифры на нажатой кнопке с операциями с жизнями/очками.
    #Также перегенерация кубика'''
    elif str(button1['text']) == str(dice):
        if int(button1['text']) not in temporary1:
            c = cards[int(button1['text'])]
            deleted_card = random.choice(c)
            scoreorlife()
        else:
            deleted_card = temporary1[int(button1['text'])]
            scoreorlife()
            temporary1.clear
        dice = random.randrange(1, 7)
        label_dice['text'] = dice
        sequence.remove(str(button1['text']))
        sequence.append(str(random.randrange(1, 7)))
        button1['text'] = sequence[5]

    # '''Вывод карты без операций с жизнями/очками с перегенерацией лишь кубика'''
    elif button1['text'] != str(dice):
        if temporary1.get(int(button1['text'])) != None:
            count0 = int(temporary1.get(int(button1['text'])))
        else:
            count0 = random.choice(cards[int(button1['text'])])
        if count0 == 0:
            text = '\nПодмастриваем - мышеловка'
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        else:
            text = '\nКарта скрывает под собой: ' + str(count0)
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        dice = random.randrange(1,7)
        label_dice['text']=dice
        x = int(button1['text'])
        temporary1[int(button1['text'])] = count0

def delete2():
    global lifes, score, deleted_card, c, dice, sequence, temporary2
    #''''Проверка правильности нажатия игроком кнопки. Если в последовательности
    #есть цифры на которые игрок не кликает - вывод повтора попытки'''
    if str(button2['text']) != str(dice) and str(dice) in sequence:
        text = '\nОшибка ввода: Выберите карту совпадающую с кубиком'
        text_log.insert(tk.END, text)
        text_log.see(tk.END)

    #'''Условный вывод+удаление полученной карты по ключу из словаря cards
    #и перегенерация цифры на нажатой кнопке с операциями с жизнями/очками.
    #Также перегенерация кубика'''
    elif str(button2['text']) == str(dice):
        if int(button2['text']) not in temporary2:
            c = cards[int(button2['text'])]
            deleted_card = random.choice(c)
            scoreorlife()
        else:
            deleted_card = temporary2[int(button2['text'])]
            scoreorlife()
            temporary2.clear
        dice = random.randrange(1, 7)
        label_dice['text'] = dice
        sequence.remove(str(button2['text']))
        sequence.append(str(random.randrange(1, 7)))
        button2['text'] = sequence[5]

    # '''Вывод карты без операций с жизнями/очками с перегенерацией лишь кубика'''
    elif button2['text'] != str(dice):
        if temporary2.get(int(button2['text'])) != None:
            count0 = int(temporary2.get(int(button2['text'])))
        else:
            count0 = random.choice(cards[int(button2['text'])])
        if count0 == 0:
            text = '\nПодмастриваем - мышеловка'
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        else:
            text = '\nКарта скрывает под собой: ' + str(count0)
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        dice = random.randrange(1,7)
        label_dice['text']=dice
        x = int(button2['text'])
        temporary2[int(button2['text'])] = count0

def delete3():
    global lifes, score, deleted_card, c, dice, sequence, temporary3
    #''''Проверка правильности нажатия игроком кнопки. Если в последовательности
    #есть цифры на которые игрок не кликает - вывод повтора попытки'''
    if str(button3['text']) != str(dice) and str(dice) in sequence:
        text = '\nОшибка ввода: Выберите карту совпадающую с кубиком'
        text_log.insert(tk.END, text)
        text_log.see(tk.END)

    #'''Условный вывод+удаление полученной карты по ключу из словаря cards
    #и перегенерация цифры на нажатой кнопке с операциями с жизнями/очками.
    #Также перегенерация кубика'''
    elif str(button3['text']) == str(dice):
        if int(button3['text']) not in temporary3:
            c = cards[int(button3['text'])]
            deleted_card = random.choice(c)
            scoreorlife()
        else:
            deleted_card = temporary3[int(button3['text'])]
            scoreorlife()
            temporary3.clear
        dice = random.randrange(1, 7)
        label_dice['text'] = dice
        sequence.remove(str(button3['text']))
        sequence.append(str(random.randrange(1, 7)))
        button3['text'] = sequence[5]

    # '''Вывод карты без операций с жизнями/очками с перегенерацией лишь кубика'''
    elif button3['text'] != str(dice):
        if temporary3.get(int(button3['text'])) != None:
            count0 = int(temporary3.get(int(button3['text'])))
        else:
            count0 = random.choice(cards[int(button3['text'])])
        if count0 == 0:
            text = '\nПодмастриваем - мышеловка'
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        else:
            text = '\nКарта скрывает под собой: ' + str(count0)
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        dice = random.randrange(1,7)
        label_dice['text']=dice
        x = int(button3['text'])
        temporary3[int(button3['text'])] = count0

def delete4():
    global lifes, score, deleted_card, c, dice, sequence, temporary4
    #''''Проверка правильности нажатия игроком кнопки. Если в последовательности
    #есть цифры на которые игрок не кликает - вывод повтора попытки'''
    if str(button4['text']) != str(dice) and str(dice) in sequence:
        text = '\nОшибка ввода: Выберите карту совпадающую с кубиком'
        text_log.insert(tk.END, text)
        text_log.see(tk.END)

    #'''Условный вывод+удаление полученной карты по ключу из словаря cards
    #и перегенерация цифры на нажатой кнопке с операциями с жизнями/очками.
    #Также перегенерация кубика'''
    elif str(button4['text']) == str(dice):
        if int(button4['text']) not in temporary4:
            c = cards[int(button1['text'])]
            deleted_card = random.choice(c)
            scoreorlife()
        else:
            deleted_card = temporary4[int(button4['text'])]
            scoreorlife()
            temporary4.clear
        dice = random.randrange(1, 7)
        label_dice['text'] = dice
        sequence.remove(str(button4['text']))
        sequence.append(str(random.randrange(1, 7)))
        button4['text'] = sequence[5]

    # '''Вывод карты без операций с жизнями/очками с перегенерацией лишь кубика'''
    elif button4['text'] != str(dice):
        if temporary4.get(int(button4['text'])) != None:
            count0 = int(temporary4.get(int(button4['text'])))
        else:
            count0 = random.choice(cards[int(button4['text'])])
        if count0 == 0:
            text = '\nПодмастриваем - мышеловка'
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        else:
            text = '\nКарта скрывает под собой: ' + str(count0)
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        dice = random.randrange(1,7)
        label_dice['text']=dice
        x = int(button4['text'])
        temporary4[int(button4['text'])] = count0

def delete5():
    global lifes, score, deleted_card, c, dice, sequence, temporary5
    #''''Проверка правильности нажатия игроком кнопки. Если в последовательности
    #есть цифры на которые игрок не кликает - вывод повтора попытки'''
    if str(button5['text']) != str(dice) and str(dice) in sequence:
        text = '\nОшибка ввода: Выберите карту совпадающую с кубиком'
        text_log.insert(tk.END, text)
        text_log.see(tk.END)

    #'''Условный вывод+удаление полученной карты по ключу из словаря cards
    #и перегенерация цифры на нажатой кнопке с операциями с жизнями/очками.
    #Также перегенерация кубика'''
    elif str(button5['text']) == str(dice):
        if int(button5['text']) not in temporary5:
            c = cards[int(button5['text'])]
            deleted_card = random.choice(c)
            scoreorlife()
        else:
            deleted_card = temporary5[int(button5['text'])]
            scoreorlife()
            temporary5.clear
        dice = random.randrange(1, 7)
        label_dice['text'] = dice
        sequence.remove(str(button5['text']))
        sequence.append(str(random.randrange(1, 7)))
        button5['text'] = sequence[5]

    # '''Вывод карты без операций с жизнями/очками с перегенерацией лишь кубика'''
    elif button5['text'] != str(dice):
        if temporary5.get(int(button5['text'])) != None:
            count0 = int(temporary5.get(int(button5['text'])))
        else:
            count0 = random.choice(cards[int(button5['text'])])
        if count0 == 0:
            text = '\nПодмастриваем - мышеловка'
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        else:
            text = '\nКарта скрывает под собой: ' + str(count0)
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        dice = random.randrange(1,7)
        label_dice['text']=dice
        x = int(button5['text'])
        temporary5[int(button5['text'])] = count0

def delete6():
    global lifes, score, deleted_card, c, dice, sequence, temporary6
    #''''Проверка правильности нажатия игроком кнопки. Если в последовательности
    #есть цифры на которые игрок не кликает - вывод повтора попытки'''
    if str(button6['text']) != str(dice) and str(dice) in sequence:
        text = '\nОшибка ввода: Выберите карту совпадающую с кубиком'
        text_log.insert(tk.END, text)
        text_log.see(tk.END)

    #'''Условный вывод+удаление полученной карты по ключу из словаря cards
    #и перегенерация цифры на нажатой кнопке с операциями с жизнями/очками.
    #Также перегенерация кубика'''
    elif str(button6['text']) == str(dice):
        if int(button6['text']) not in temporary6:
            c = cards[int(button6['text'])]
            deleted_card = random.choice(c)
            scoreorlife()
        else:
            deleted_card = temporary6[int(button6['text'])]
            scoreorlife()
            temporary6.clear
        dice = random.randrange(1, 7)
        label_dice['text'] = dice
        sequence.remove(str(button6['text']))
        sequence.append(str(random.randrange(1, 7)))
        button6['text'] = sequence[5]

    # '''Вывод карты без операций с жизнями/очками с перегенерацией лишь кубика'''
    elif button6['text'] != str(dice):
        if temporary6.get(int(button6['text'])) != None:
            count0 = int(temporary6.get(int(button6['text'])))
        else:
            count0 = random.choice(cards[int(button6['text'])])
        if count0 == 0:
            text = '\nПодмастриваем - мышеловка'
            text_log.insert(tk.END, text)
            text_log.see(tk.END)
        else:
            text = '\nКарта скрывает под собой: ' + str(count0)
            text_log.insert(tk.END, text)
            
        dice = random.randrange(1,7)
        label_dice['text']=dice
        x = int(button6['text'])
        temporary6[int(button6['text'])] = count0

'''Инициализация фреймов, без них text_log закрывал собой всё остальное'''
other_frame = tk.Frame(master=window)
label_frame = tk.Frame(master=window)
log_frame = tk.Frame(master=window)
other_frame.pack()
label_frame.pack()
log_frame.pack()

'''Генерация кнопок/карт по последовательности'''
# for i in range(6):
#     button = tk.Button(master=other_frame, text=random.choice(sequence), width=5, height=2, command=delete)
#     button.grid(row=0, column=i, sticky='nsew')

button1 = tk.Button(master=other_frame, text=sequence[0], width=5, height=2, command=delete1)
button1.grid(row=0, column=0, sticky='nsew')
button2 = tk.Button(master=other_frame, text=sequence[1], width=5, height=2, command=delete2)
button2.grid(row=0, column=1, sticky='nsew')
button3 = tk.Button(master=other_frame, text=sequence[2], width=5, height=2, command=delete3)
button3.grid(row=0, column=2, sticky='nsew')
button4 = tk.Button(master=other_frame, text=sequence[3], width=5, height=2, command=delete4)
button4.grid(row=0, column=3, sticky='nsew')
button5 = tk.Button(master=other_frame, text=sequence[4], width=5, height=2, command=delete5)
button5.grid(row=0, column=4, sticky='nsew')
button6 = tk.Button(master=other_frame, text=sequence[5], width=5, height=2, command=delete6)
button6.grid(row=0, column=5, sticky='nsew')


'''Инициализация кубика'''
label_dice = tk.Label(master=other_frame, text=dice, relief= tk.GROOVE, width=5, height=2)
label_dice.grid(row=0, column=7, sticky='nsew')

'''Инициализация очков и жизней'''
label_namescore = tk.Label(master=label_frame, text='Очки:')
label_namescore.grid(row=1, column=0)
label_score = tk.Label(master=label_frame, text=score)
label_score.grid(row=1, column=1)
label_namelifes = tk.Label(master=label_frame, text='Жизней:')
label_namelifes.grid(row=1, column=3)
label_lifes = tk.Label(master=label_frame, text=lifes)
label_lifes.grid(row=1, column=4)

# scrlbar = tk.Scrollbar(log_frame, orient='vertical', command= )

'''Инициализация лога'''
text_log = tk.Text(master=log_frame, width=50, height=10)
text=''
text_log.insert(tk.END, text)
text_log.grid()

window.mainloop()