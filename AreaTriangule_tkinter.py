# Traiangule Area Calculator

# Funtions
def getData():
    
    # Function to get ata from tkinter labels

    base = int(entryBase.get())
    altura = int(entryAltura.get())

    return base, altura

def areaTriangulo():

    # Function to calculate triangule area
    
    base, altura = getData()
    area = (base * altura) / 2
    labelOutput['text'] = f'({base} x {altura}) / 2 = {area}'


# GUI
import tkinter as tk

# Contructor
root = tk.Tk()
root.title('Aplicación')
root.geometry('400x180')

# Frame
frm = tk.Frame(root)
frm.grid()

# Labels, entries and button
labelTitulo = tk.Label(frm, text='Calculadora Área de Triángulo', font="Arial 15 bold", height=2)
labelTitulo.grid(row=0, column=1, columnspan=2)

labelSpaceLeft = tk.Label(frm, text = '          ')
labelSpaceLeft.grid(row=1, column=0)

labelBase = tk.Label(frm, text='Ingrese base', height=2)
labelBase.grid(row=1, column=1)

labelAltura = tk.Label(frm, text='Ingrese altura', height=2)
labelAltura.grid(row=2, column=1)

entryBase = tk.Entry(frm)
entryBase.grid(row=1, column=2)

entryAltura = tk.Entry(frm)
entryAltura.grid(row=2, column=2)

buttonCalculate = tk.Button(frm, text='Calcular', command=areaTriangulo)
buttonCalculate.grid(row=3, column=1)

labelOutput = tk.Label(frm, height=2)
labelOutput.grid(row=3, column=2)

labelSpaceRight = tk.Label(frm, text = '          ')
labelSpaceRight.grid(row=1, column=3)

root.mainloop()