from tkinter import *
import tkinter.messagebox
import os

def main():
    root = Tk()
    app = Window_1(root)

class Window_1:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Window")
        self.master.geometry('1350x750')
        self.master.config(bg='lightskyblue')
        self.Frame = Frame(self.master, bg='lightskyblue')
        self.Frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.Lbl_Title = Label(self.Frame, text='Login Menu', font=('arial', 55, 'bold'), bg='lightskyblue', fg='Black')
        self.Lbl_Title.grid(row=0, column=0, columnspan=3, pady=40)

        self.Login_Frame_1 = LabelFrame(self.Frame, width=1350, height=600, relief='ridge', bg='lightskyblue', bd=15,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_1.grid(row=1, column=0)
        self.Login_Frame_2 = LabelFrame(self.Frame, width=1000, height=600, relief='ridge', bg='lightskyblue', bd=15,
                                        font=('arial', 20, 'bold'))
        self.Login_Frame_2.grid(row=2, column=0)

        self.Label_Username = Label(self.Login_Frame_1, text='Username', font=('arial', 20, 'bold'), bg='lightskyblue', bd=20)
        self.Label_Username.grid(row=0, column=0)
        self.text_Username = Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), textvariable=self.Username)
        self.text_Username.grid(row=0, column=1, padx=50)

        self.Label_Password = Label(self.Login_Frame_1, text='Password', font=('arial', 20, 'bold'), bg='lightskyblue', bd=20)
        self.Label_Password.grid(row=1, column=0)
        self.text_Password = Entry(self.Login_Frame_1, font=('arial', 20, 'bold'), show='*', textvariable=self.Password)
        self.text_Password.grid(row=1, column=1)

        self.btnLogin = Button(self.Login_Frame_2, text='Login', width=10, font=('arial', 15, 'bold'), command=self.Login)
        self.btnLogin.grid(row=3, column=0, padx=8, pady=20)

        self.btnReset = Button(self.Login_Frame_2, text='Reset', width=10, font=('arial', 15, 'bold'), command=self.Reset)
        self.btnReset.grid(row=3, column=1, padx=8, pady=20)

        self.btnExit = Button(self.Login_Frame_2, text='Exit', width=10, font=('arial', 15, 'bold'), command=self.Exit)
        self.btnExit.grid(row=3, column=2, padx=8, pady=20)

    def Login(self):
        u = self.Username.get()
        p = self.Password.get()

        if u == 'Prashant' and p == '12345678':  # Corrected the condition for login
            self.__menu__()
        else:
            tkinter.messagebox.askyesno("Login", "Error : Wrong Password")
            self.Username.set("")
            self.Password.set()

    def Reset(self):
        self.Username.set("")
        self.Password.set()
        self.text_Username.focus()

    def Exit(self):
        self.Exit = tkinter.messagebox.askokcancel("Login System", "Confirm if you want to Exit")
        if self.Exit > 0:
            self.master.destroy()

    def __menu__(self):
        filename = 'Menu.py'
        os.system('python ' + filename)

if __name__ == '__main__':
    main()
