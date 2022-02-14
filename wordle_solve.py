from tkinter import *

global t
global attempt
global word_list
global iternum
global label1
global label2
global label3
global label4
global label5

def get_values():
    global result_val
    global attempt
    global word_list
    global t
    global iternum
    global label1
    global label2
    global label3
    global label4
    global label5

    result_val = val1.get() + val2.get() + val3.get() + val4.get() + val5.get()
    if result_val == "GGGGG":
        exit_message = Label(root, text="The word has been found, program will be terminated.").grid(row=5, column=0)
        exit()
    print(result_val)

    for i in range(len(result_val)):
        if result_val[i] == "B":
            banned = attempt[i]
            word_list = [word for word in word_list if banned not in word]

        elif result_val[i] == "Y":
            word_list = [word for word in word_list if attempt[i] in word]

        elif result_val[i] == "G":
            word_list = [word for word in word_list if word[i] == attempt[i]]

    attempt = word_list[0]
    t += 1
    iternum = Label(root, text=f"attempt {t}").grid(row=0, column=0)
    label1 = Label(root, text=f"{attempt[0]}").grid(row=0, column=1)
    label2 = Label(root, text=f"{attempt[1]}").grid(row=0, column=2)
    label3 = Label(root, text=f"{attempt[2]}").grid(row=0, column=3)
    label4 = Label(root, text=f"{attempt[3]}").grid(row=0, column=4)
    label5 = Label(root, text=f"{attempt[4]}").grid(row=0, column=5)

f = open("sgb-words.txt", "r")
word_list = f.readlines()
f.close()
word_list = [word[:5] for word in word_list]

root = Tk()
t = 1
attempt = "crane"
iternum = Label(root, text=f"attempt {t}").grid(row=0, column=0)
label1 = Label(root, text=f"{attempt[0]}").grid(row=0, column=1)
label2 = Label(root, text=f"{attempt[1]}").grid(row=0, column=2)
label3 = Label(root, text=f"{attempt[2]}").grid(row=0, column=3)
label4 = Label(root, text=f"{attempt[3]}").grid(row=0, column=4)
label5 = Label(root, text=f"{attempt[4]}").grid(row=0, column=5)

option_B = Label(root, text="B").grid(row = 1, column = 0)
option_Y = Label(root, text="Y").grid(row = 2, column = 0)
option_G = Label(root, text="G").grid(row = 3, column = 0)

val1 = StringVar()
val1.set("B")
val2 = StringVar()
val2.set("B")
val3 = StringVar()
val3.set("B")
val4 = StringVar()
val4.set("B")
val5 = StringVar()
val5.set("B")

radio_1B = Radiobutton(root, text="", variable=val1, value="B").grid(row=1, column=1)
radio_1Y = Radiobutton(root, text="", variable=val1, value="Y").grid(row=2, column=1)
radio_1G = Radiobutton(root, text="", variable=val1, value="G").grid(row=3, column=1)

radio_2B = Radiobutton(root, text="", variable=val2, value="B").grid(row=1, column=2)
radio_2Y = Radiobutton(root, text="", variable=val2, value="Y").grid(row=2, column=2)
radio_2G = Radiobutton(root, text="", variable=val2, value="G").grid(row=3, column=2)

radio_3B = Radiobutton(root, text="", variable=val3, value="B").grid(row=1, column=3)
radio_3Y = Radiobutton(root, text="", variable=val3, value="Y").grid(row=2, column=3)
radio_3G = Radiobutton(root, text="", variable=val3, value="G").grid(row=3, column=3)

radio_4B = Radiobutton(root, text="", variable=val4, value="B").grid(row=1, column=4)
radio_4Y = Radiobutton(root, text="", variable=val4, value="Y").grid(row=2, column=4)
radio_4G = Radiobutton(root, text="", variable=val4, value="G").grid(row=3, column=4)

radio_5B = Radiobutton(root, text="", variable=val5, value="B").grid(row=1, column=5)
radio_5Y = Radiobutton(root, text="", variable=val5, value="Y").grid(row=2, column=5)
radio_5G = Radiobutton(root, text="", variable=val5, value="G").grid(row=3, column=5)

mybutton = Button(root, text="submit", padx=50, command=get_values).grid(row = 5, column = 0)

root.mainloop()