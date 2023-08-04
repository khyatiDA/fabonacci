from tkinter import *
window = Tk()

window.title("FIBONACCI SUM")
window.geometry("600x600")

label_series  =Label(window , text = "Fibonacci Series :")
input1 = Entry(window)
label_spiral = Label(window)

def fabonacci():
    num = int(input1.get())
    sum2 = 0
    first_no = 0
    second_no = 0
    counter =1 
    while (counter<=num):
        sum2 = sum2 + sum
        counter += 1
        first_no + second_no
        second_no = sum 
        sum = first_no +second_no
        label_series["text"]+= str(sum2) + ""
        label_spiral["text"]= "Fabonacci Sum :" + str(sum2)

btn = Button(window , text = "Show Fabonacci Series" , command=fabonacci)  
btn.pack()   
input1.pack()  
label_series.pack()
label_spiral.pack()

window.mainloop()

