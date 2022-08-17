from collections import Counter
import tkinter as tk


def getData():

    # Function to get ata from tkinter labels
    text = entryText.get()
    return text

def topThree():
    
    # Get Top 3 with Counter class
    global Counter
    text = getData()

    split_it = text.split()
    Counter = Counter(split_it)
    most_occur = Counter.most_common(3)
    labelOutput['text'] = most_occur


# Contructor
root = tk.Tk()
root.title('Get Top Three')
root.geometry('400x200')

# Frame
frm = tk.Frame(root)
frm.grid()

# Labels, entries and button
labelSpaceLeft = tk.Label(frm, text = '    ')
labelSpaceLeft.grid(row=1, column=0)

labelTitulo = tk.Label(frm, text='Word Counter', font="Arial 15 bold", height=2)
labelTitulo.grid(row=0, column=1, columnspan=3)

labelText = tk.Label(frm, text='Paste Text', height=2)
labelText.grid(row=1, column=1)

entryText = tk.Entry(frm, width=35)
entryText.grid(row=2, column=1)

buttonCalculate = tk.Button(frm, text='Get Top Three', command=topThree)
buttonCalculate.grid(row=3, column=1)

buttonClose= tk.Button(frm, text='Finish', command=quit)
buttonClose.grid(row=4, column=1)

labelOutput = tk.Label(frm, height=2)
labelOutput.grid(row=5, column=1)

labelSpaceRight = tk.Label(frm, text = '    ')
labelSpaceRight.grid(row=1, column=2)

root.mainloop()
