from tkinter import *
from tkinter import messagebox

# глобальные переменные
matrix = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
buttons = [[None, None, None], [None, None, None], [None, None, None]]
value = 'X'

# возобновление к старту
def Clear():
    global matrix
    global buttons
    global value
    matrix = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''
    value = 'X'

# функция хода
def Move(i, j):
    global value
    if matrix[i][j] == '0':
        matrix[i][j] = value
        buttons[i][j]['text'] = value
        if value == 'X':
            value = 'O'
        else:
            value = 'X'

    if CheckWinX():
        messagebox.showinfo(title='Игра окончена', message='Крестики выиграли')
        Clear()
    elif CheckWinO():
        messagebox.showinfo(title='Игра окончена', message='Нолики выиграли')
        Clear()
    elif CheckNone():
        messagebox.showinfo(title='Игра окончена', message='Ничья')
        Clear()

        
# функция проверки на ничью
def CheckNone():
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == '0':
                return False
    return True

# функция проверки на победу крестиков
def CheckWinX():
    if matrix[1][1] == 'X' and ((matrix[0][0] == 'X' and matrix[2][2] == 'X') or 
                                (matrix[0][2] == 'X' and matrix[2][0] == 'X') or 
                                (matrix[0][1] == 'X' and matrix[2][1] == 'X') or 
                                (matrix[1][0] == 'X' and matrix[1][2] == 'X')):
        return True

    if matrix[0][0] == 'X' and ((matrix[0][1] == 'X' and matrix[0][2] == 'X') or (matrix[1][0] == 'X' and matrix[2][0] == 'X')):
        return True
    if matrix[2][2] == 'X' and ((matrix[2][0] == 'X' and matrix[2][1] == 'X') or (matrix[0][2] == 'X' and matrix[1][2] == 'X')):
        return True

# функция на проверку победы ноликов
def CheckWinO():
    if matrix[1][1] == 'O' and ((matrix[0][0] == 'O' and matrix[2][2] == 'O') or 
                                (matrix[0][2] == 'O' and matrix[2][0] == 'O') or 
                                (matrix[0][1] == 'O' and matrix[2][1] == 'O') or 
                                (matrix[1][0] == 'O' and matrix[1][2] == 'O')):
        return True

    if matrix[0][0] == 'O' and ((matrix[0][1] == 'O' and matrix[0][2] == 'O') or (matrix[1][0] == 'O' and matrix[2][0] == 'O')):
        return True
    if matrix[2][2] == 'O' and ((matrix[2][0] == 'O' and matrix[2][1] == 'O') or (matrix[0][2] == 'O' and matrix[1][2] == 'O')):
        return True


def Set00():
    Move(0, 0)

def Set01():
    Move(0, 1)

def Set02():
    Move(0, 2)

def Set10():
    Move(1, 0)

def Set11():
    Move(1, 1)

def Set12():
    Move(1, 2)

def Set20():
    Move(2, 0)

def Set21():
    Move(2, 1)

def Set22():
    Move(2, 2)


if __name__ == '__main__':
    root = Tk()
    root.title('Крестики-нолики')

    handlers = [[Set00, Set01, Set02],
                [Set10, Set11, Set12],
                [Set20, Set21, Set22]]
    for i in range(3):
        for j in range(3):
            btn = Button(text='', width=10, height=5, command=handlers[i][j])
            btn.grid(row=i, column=j, padx=0, pady=0, ipadx=0, ipady=0)
            buttons[i][j] = btn

    exitBtn = Button(text='exit', width=10, height=5, command=root.destroy)
    exitBtn.grid(row=3, column=1, padx=0, pady=0, ipadx=0, ipady=0)

    clearBtn = Button(text='clear', width=10, height=5, command=Clear)
    clearBtn.grid(row=3, column=0, padx=0, pady=0, ipadx=0, ipady=0)
    root.mainloop()



