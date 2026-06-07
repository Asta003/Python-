from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        self.input_var = StringVar()
        self.input_var.set("")

        self.create_input_field()
        self.create_buttons()
        
    def create_input_field(self):
        input_frame = Frame(self.root)
        input_frame.pack(expand=True, fill=BOTH, padx=10, pady=10)
        
        entry = Entry(input_frame, 
                     textvariable=self.input_var,
                     font=('Arial', 18),
                     justify='right',
                     bd=10,
                     relief=SUNKEN)
        entry.pack(expand=True, fill=BOTH)
        
    def create_buttons(self):
        button_frame = Frame(self.root)
        button_frame.pack(expand=True, fill=BOTH, padx=10, pady=10)
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'CE'
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == '=':
                btn = Button(button_frame, text=button, font=('Arial', 14),
                           bg='blue', fg='white',
                           command=lambda x=button: self.button_click(x))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            elif button == 'C' or button == 'CE':
                btn = Button(button_frame, text=button, font=('Arial', 14),
                           bg='red', fg='white',
                           command=lambda x=button: self.button_click(x))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            else:
                btn = Button(button_frame, text=button, font=('Arial', 14),
                           bg='lightgray', command=lambda x=button: self.button_click(x))
                btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value == 'C':
            self.expression = ""
            self.input_var.set(self.expression)
        elif value == 'CE':
            self.expression = self.expression[:-1]
            self.input_var.set(self.expression)
        elif value == '=':
            try:
                result = eval(self.expression)
                self.input_var.set(result)
                self.expression = str(result)
            except Exception as e:
                self.input_var.set("Ошибка")
                self.expression = ""
        else:
            self.expression += str(value)
            self.input_var.set(self.expression)

def main():
    root = Tk()
    calculator = Calculator(root)
    def on_closing():
        print("Калькулятор закрыт")
        root.destroy()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
