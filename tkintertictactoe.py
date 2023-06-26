import tkinter as tk
from tkinter import messagebox
window = tk.Tk()

window.geometry("530x600")
window.maxsize(530, 530)
window.minsize(530, 600)
count = 2
winner = "Draw"


def game():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global count
    count = 2
    # ROW 1 ↓

    button1 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button1))
    button1.grid(row=0, column=0)

    button2 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button2))
    button2.grid(row=0, column=1)

    button3 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button3))
    button3.grid(row=0, column=2)

    # ROW 2 ↓

    button4 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button4))
    button4.grid(row=1, column=0)

    button5 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button5))
    button5.grid(row=1, column=1)

    button6 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button6))
    button6.grid(row=1, column=2)

    # ROW 3 ↓

    button7 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button7))
    button7.grid(row=2, column=0)

    button8 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button8))
    button8.grid(row=2, column=1, columnspan=1)

    button9 = tk.Button(window, text='', font="Calibri 64", bg="white", width=4, height=1, bd=0,
                        command=lambda: buttons(button9))
    button9.grid(row=2, column=2)


game()


def buttons(num):

    global count
    if count % 2 == 0:
        num['text'] = 'X'
        num['bg'] = '#27FFB7'
        count += 1
    else:
        num['text'] = 'O'
        num['bg'] = '#FF4183'
        count += 1
    num['state'] = 'disabled'
    winconditions()


def disablebuttons():
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')
    button4.config(state='disabled')
    button5.config(state='disabled')
    button6.config(state='disabled')
    button7.config(state='disabled')
    button8.config(state='disabled')
    button9.config(state='disabled')


def winconditions():
    win = ['X', 'O']
    global winner
    winner = "Draw"
    for i in win:
        if button1['text'] == button2['text'] == button3['text'] == i:
            winner = i
            print('anan')
        elif button4['text'] == button5['text'] == button6['text'] == i:
            winner = i
        elif button7['text'] == button8['text'] == button9['text'] == i:
            winner = i
        elif button1['text'] == button4['text'] == button7['text'] == i:
            winner = i
        elif button2['text'] == button5['text'] == button8['text'] == i:
            winner = i
        elif button3['text'] == button6['text'] == button9['text'] == i:
            winner = i
        elif button1['text'] == button5['text'] == button9['text'] == i:
            winner = i
        elif button3['text'] == button5['text'] == button7['text'] == i:
            winner = i

    if winner != "Draw":
        winmessage = ("The winner is " + winner)
        messagebox.showinfo(title='Winner', message=str(winmessage))
        disablebuttons()
        game()


resetbutton = tk.Button(window, text="RESET", width=7, height=1, font="Calibri 12",
                        fg="black", relief="raised", command=game)
resetbutton.place(x=230, y=550)

window.mainloop()
