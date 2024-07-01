from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
import Library_Backend

class Library:
       
       def __init__(self, root):
              self.root = root
              self.root.title('Transport Management System')
              self.root.geometry('1350x750')
              self.root.config(bg = 'navajowhite')

       #===================================================Variables===================================================
              self.Mtype = StringVar()
              self.refno = StringVar()
              self.fname = StringVar()
              self.surname = StringVar()
              self.address = StringVar()
              self.post = StringVar()
              self.mobno = StringVar()
              self.ID = StringVar()
              self.title = StringVar()
              self.driver = StringVar()
              self.borrow = StringVar()
              self.due = StringVar()
              self.loan = StringVar()
              self.yop = StringVar()
              self.edsn = StringVar()
              


       #================================================Functions======================================================
              def BookRec(event):
                     try:
                            global selected_tuple
                            index = self.Listbox_2.curselection()[0]
                            selected_tuple = self.Listbox_2.get(index)

                            self.Entry_0.delete(0, END)
                            self.Entry_0.insert(END, selected_tuple[1])  
                            self.Entry_1.delete(0, END)
                            self.Entry_1.insert(END, selected_tuple[2])                           
                            self.Entry_2.delete(0, END)
                            self.Entry_2.insert(END, selected_tuple[3])
                            self.Entry_3.delete(0, END)
                            self.Entry_3.insert(END, selected_tuple[4])
                            self.Entry_4.delete(0, END)
                            self.Entry_4.insert(END, selected_tuple[5])
                            self.Entry_5.delete(0, END)
                            self.Entry_5.insert(END, selected_tuple[6])
                            self.Entry_6.delete(0, END)
                            self.Entry_6.insert(END, selected_tuple[7])
                            self.Entry_7.delete(0, END)
                            self.Entry_7.insert(END, selected_tuple[8])
                            self.Entry_8.delete(0, END)
                            self.Entry_8.insert(END, selected_tuple[9])
                            self.Entry_9.delete(0, END)
                            self.Entry_9.insert(END, selected_tuple[10])
                            self.Entry_10.delete(0, END)
                            self.Entry_10.insert(END, selected_tuple[11])
                            self.Entry_11.delete(0, END)
                            self.Entry_11.insert(END, selected_tuple[12])
                            self.Entry_12.delete(0, END)
                            self.Entry_12.insert(END, selected_tuple[13])
                             

                     except IndexError:
                            pass
              def Insert():
                     if(len(self.refno.get()) != 0):
                            Library_Backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                   , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                   , self.title.get(), self.driver.get(), self.borrow.get(), self.due.get()\
                                                   , self.loan.get())
                            self.Listbox_2.delete(0, END)
                            self.Listbox_2.insert(END , (self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                         , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                         , self.title.get(), self.driver.get(), self.borrow.get(), self.due.get()\
                                                         , self.loan.get()))
                            

              def Display():
                     self.Listbox_2.delete(0, END)
                     for row in Library_Backend.view():
                            self.Listbox_2.insert(END, row, str(' '))  
                                                       
              def Exit():
                     Exit = tkinter.messagebox.askyesno('Amrita Transport Management System','Confirm if you want to Exit')
                     if Exit > 0:
                            root.destroy()
                            return
                                                                    
              def Reset():
                     self.Mtype.set('')
                     self.refno.set('')
                     self.fname.set('')
                     self.surname.set('')
                     self.address.set('')
                     self.post.set('')
                     self.mobno.set('')
                     self.ID.set('')
                     self.title.set('')
                     self.driver.set('')
                     self.borrow.set('')
                     self.due.set('')
                     self.loan.set('')
                     self.Display.delete('1.0',END)
                     self.Listbox_2.delete(0, END)

              def Delete():
                     Library_Backend.delete(selected_tuple[0])
                     Reset()
                     Display()

              def Update():
                     Library_Backend.delete(selected_tuple[0])
                     Library_Backend.insert(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                  , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                  , self.title.get(), self.driver.get(), self.borrow.get(), self.due.get()\
                                                  , self.loan.get())
                     self.Listbox_2.delete(0, END)
                     self.Listbox_2.insert(END,(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                  , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                  , self.title.get(), self.driver.get(), self.borrow.get(), self.due.get()\
                                                  , self.loan.get()))

              def Search():
                     self.Listbox_2.delete(0, END)
                     for row in Library_Backend.search(self.Mtype.get(), self.refno.get(), self.fname.get(), self.surname.get()\
                                                  , self.address.get(), self.post.get(), self.mobno.get(), self.ID.get()\
                                                  , self.title.get(), self.driver.get(), self.borrow.get(), self.due.get()\
                                                  , self.loan.get()):
                            self.Listbox_2.insert(END, row, str(' '))

              def Details():
                     self.Display.delete('1.0',END)
                     self.Display.insert(END, 'Plate No: ' + self.ID.get() + '\n')
                     self.Display.insert(END, 'Bus No: ' + self.title.get() + '\n')
                     self.Display.insert(END, 'Driver:  ' +  self.driver.get() + '\n')
                     self.Display.insert(END, 'Edition: ' + self.edsn.get() + '\n')
                     self.Display.insert(END, 'Year Bought: \t' + self.yop.get() + '\n')
                     self.Display.insert(END, 'Last Inspection: ' + self.borrow.get() + '\n')
                     self.Display.insert(END, 'Inspection Due:' + self.due.get() + '\n')
                     self.Display.insert(END, 'Capacity: ' + self.loan.get() + '\n')
                             

       #=====================================================Frames=====================================================
              Main_Frame = Frame(self.root, bg = 'navajowhite')
              Main_Frame.grid()

              title_Frame_1 = Frame(Main_Frame, width = 1350, bg = 'navajowhite', relief = RIDGE, bd = 15, padx = 20)
              title_Frame_1.pack(side = TOP)

              self.lbltitle = Label(title_Frame_1, font = ('arial',40,'bold'), text = '\tAmrita Transport Management System\t', \
                                    bg = 'navajowhite', padx = 13)
              self.lbltitle.grid()

              Button_Frame = Frame(Main_Frame, width = 1350, height = 50, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Button_Frame.pack(side = BOTTOM)

              Detail_Frame = Frame(Main_Frame, width = 1350, height = 100, relief = RIDGE, bd = 10, bg = 'navajowhite')
              Detail_Frame.pack(side = BOTTOM)

              Data_Frame = Frame(Main_Frame, width = 1350, height = 400, relief = RIDGE, bd = 15, bg = 'navajowhite')
              Data_Frame.pack(side = BOTTOM)

              Frame_1 = LabelFrame(Data_Frame, width = 800, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                              text = "Student Info:", padx = 20, font = ('arial',15,'bold'))
              Frame_1.pack(side = LEFT, padx = 3)

              Frame_2 = LabelFrame(Data_Frame, width = 550, height = 400, relief = RIDGE, bd = 10, bg = 'navajowhite', \
                              text = "BUS Details:", padx = 20, font = ('arial',15,'bold'))
              Frame_2.pack(side = RIGHT)


       #================================================Labels========================================================
              self.Label_1 = Label(Frame_1, text = 'User type', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_1.grid(row = 0, column = 0, sticky = W)
              self.Label_2 = Label(Frame_1, text = 'Reference No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_2.grid(row = 1, column = 0, sticky = W)
              self.Label_3 = Label(Frame_1, text = 'First Name', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_3.grid(row = 2, column = 0, sticky = W)
              self.Label_4 = Label(Frame_1, text = 'Surname', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_4.grid(row = 3, column = 0, sticky = W)
              self.Label_5 = Label(Frame_1, text = 'Address', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_5.grid(row = 4, column = 0, sticky = W)
              self.Label_6 = Label(Frame_1, text = 'Post Code', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_6.grid(row = 5, column = 0, sticky = W)
              self.Label_7 = Label(Frame_1, text = 'Mobile No.', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_7.grid(row = 6, column = 0, sticky = W)
              self.Label_8 = Label(Frame_1, text = 'Plate NO', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_8.grid(row = 0, column = 2, sticky = W)
              self.Label_9 = Label(Frame_1, text = 'Bus No', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_9.grid(row = 1, column = 2, sticky = W)
              self.Label_10 = Label(Frame_1, text = 'Driver', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_10.grid(row = 2, column = 2, sticky = W)
              self.Label_11 = Label(Frame_1, text = 'Last Inspection', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_11.grid(row = 3, column = 2, sticky = W)
              self.Label_13 = Label(Frame_1, text = 'Inspection Due', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_13.grid(row = 4, column = 2, sticky = W)
              self.Label_13 = Label(Frame_1, text = 'Capacity', font = ('arial',13,'bold'), pady = 2, \
                                   bg = 'navajowhite' )
              self.Label_13.grid(row = 5, column = 2, sticky = W)
              


       #================================================Entries========================================================
              self.Entry_0 = ttk.Combobox(Frame_1, values = (' ','Student','Faculty','Staff Member'), \
                                          font = ('arial',13,'bold'), width = 23, textvariable = self.Mtype )
              self.Entry_0.grid(row = 0, column = 1)
              self.Entry_1 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.refno )
              self.Entry_1.grid(row = 1, column = 1, padx = 15)
              self.Entry_2 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.fname)
              self.Entry_2.grid(row = 2, column = 1, padx = 15)
              self.Entry_3 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.surname)
              self.Entry_3.grid(row = 3, column = 1, padx = 15)
              self.Entry_4 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.address)
              self.Entry_4.grid(row = 4, column = 1, padx = 15)
              self.Entry_5 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.post)
              self.Entry_5.grid(row = 5, column = 1, padx = 15)
              self.Entry_6 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.mobno)
              self.Entry_6.grid(row = 6, column = 1, padx = 15)
              self.Entry_7 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.ID)
              self.Entry_7.grid(row = 0, column = 4, padx = 15)
              self.Entry_8 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.title)
              self.Entry_8.grid(row = 1, column = 4, padx = 15)
              self.Entry_9 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.driver)
              self.Entry_9.grid(row = 2, column = 4, padx = 15)
              self.Entry_10 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.borrow)
              self.Entry_10.grid(row = 3, column = 4, padx = 15)
              self.Entry_11 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.due)
              self.Entry_11.grid(row = 4, column = 4, padx = 15)
              self.Entry_12 = Entry(Frame_1, font = ('arial',13,'bold'), width = 25, textvariable = self.loan)
              self.Entry_12.grid(row = 5, column = 4, padx = 15)                                        


       #=============================================Widgets=========================================================
              self.Display = Text(Frame_2, font = ('arial',13,'bold'), width = 28, height = 11)
              self.Display.grid(row = 0, column = 2)


              List_of_Books = [' Amrita-1',' Amrita-2',' Amrita-3',' Amrita-4',' Amrita-5',' Amrita-6']


       #===========================================Function for Books Details=========================================
              def SelectedBook(event):
                     value = str(self.Listbox_1.get(self.Listbox_1.curselection()))
                     v = value

                     if (v == ' Amrita-1'):
                            self.ID.set('TN 20 BM 4836')
                            self.title.set('A1')
                            self.driver.set('Ajay')
                            self.yop.set('2019')
                            self.edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 14)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('14')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Amrita-2'):
                            self.ID.set('TN 20 BM 2341')
                            self.title.set('A2')
                            self.driver.set('Saravanan')
                            self.yop.set('2019')
                            self.edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 10)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('10')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Amrita-3'):
                            self.ID.set('TN 20 BM 6721')
                            self.title.set('A3')
                            self.driver.set('Natraj')
                            self.yop.set('2023')
                            self.edsn.set('7th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('13')
                            self.due.set(d3)
                            Details()
                     elif (v == 'Amrita-4'):
                            self.ID.set('TN 20 BM 7490')
                            self.title.set('A3')
                            self.driver.set('John')
                            self.yop.set('2021')
                            self.edsn.set('3rd')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('13')
                            self.due.set(d3)
                            Details()
                     elif (v == ' Amrita-5'):
                            self.ID.set('TN 20 AW 4375')
                            self.title.set('A5')
                            self.driver.set('Dilli')
                            self.yop.set('2019')
                            self.edsn.set('5th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 15)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('15')
                            self.due.set(d3)
                            Details()
                     elif (v == 'Amrita-6'):
                            self.ID.set('TN 21 AS 5628')
                            self.title.set('A6')
                            self.driver.set('Antony Das')
                            self.yop.set('2004')
                            self.edsn.set('4th')                            

                            import datetime

                            d1 = datetime.date.today()
                            d2 = datetime.timedelta(days = 13)
                            d3 = (d1 + d2)
                            self.borrow.set(d1)
                            self.loan.set('13')
                            self.due.set(d3)
                            Details()
                     
                            
       #===========================================List Box and Scroll Bar==========================================                    
              sb_1 = Scrollbar(Frame_2)
              sb_1.grid(row =0, column = 1, sticky = 'ns')

              self.Listbox_1 = Listbox(Frame_2, font = ('arial',13,'bold'), width = 20, height = 10)
              self.Listbox_1.bind('<<ListboxSelect>>', SelectedBook)
              self.Listbox_1.grid(row = 0, column = 0)
              sb_1.config(command = self.Listbox_1.yview)

              
              sb_2 = Scrollbar(Detail_Frame)
              sb_2.grid(row = 1, column = 1, sticky = 'ns')

              self.Listbox_2 = Listbox(Detail_Frame, font = ('arial',13,'bold'), width = 144, height = 11)
              self.Listbox_2.bind('<<ListboxSelect>>', BookRec)
              self.Listbox_2.grid(row = 1, column = 0)
              sb_2.config(command = self.Listbox_2.yview)

              for items in List_of_Books:
                     self.Listbox_1.insert(END, items)


       #=============================================Buttons=========================================================
              Button_1 = Button(Button_Frame, text = 'SAVE', font = ('arial',15,'bold'), width = 10, command = Insert)
              Button_1.grid(row = 0, column = 0, padx = 8, pady = 5)
              Button_2 = Button(Button_Frame, text = 'DISPLAY', font = ('arial',15,'bold'), width = 10, command = Display)
              Button_2.grid(row = 0, column = 1, padx = 8)
              Button_3 = Button(Button_Frame, text = 'RESET', font = ('arial',15,'bold'), width = 10, command = Reset)
              Button_3.grid(row = 0, column = 2, padx = 8)
              Button_4 = Button(Button_Frame, text = 'UPDATE', font = ('arial',15,'bold'), width = 10, command = Update)
              Button_4.grid(row = 0, column = 3, padx = 8)
              Button_5 = Button(Button_Frame, text = 'SEARCH', font = ('arial',15,'bold'), width = 10, command = Search)
              Button_5.grid(row = 0, column = 4, padx = 8)
              Button_6 = Button(Button_Frame, text = 'DELETE', font = ('arial',15,'bold'), width = 10, command = Delete)
              Button_6.grid(row = 0, column = 5, padx = 8)
              Button_7 = Button(Button_Frame, text = 'EXIT', font = ('arial',15,'bold'), width = 10, command = Exit)
              Button_7.grid(row = 0, column = 6, padx = 8)

              

if __name__ == '__main__':
       root = Tk()
       applicaton = Library(root)
       root.mainloop()
