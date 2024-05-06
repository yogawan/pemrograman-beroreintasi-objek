import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window, text = "label1")
label2 = tkinter.Label(main_window, text = "label2")

button1 = tkinter.Button(main_window, text = "label1")
button2 = tkinter.Button(main_window, text = "label2")

# method postitioning
label1.pack()
label2.pack()
button1.pack()
button2.pack()

# menampilkan gui
main_window.mainloop()