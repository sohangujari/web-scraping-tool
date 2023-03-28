import requests
from bs4 import BeautifulSoup
import pandas as pd
from tkinter import *

win=Tk()

win.title("Web Scraping Tool")
win.geometry('700x420')
head = Label(win, text="Web Scraping Tool",font=("Arial Bold", 18))
space = Label(win, text=" ",font=("Arial Bold", 18))

url_var=StringVar()
selected = IntVar()
tag1_var=StringVar()
tag2_var=StringVar()
class1_var=StringVar()
class2_var=StringVar()
name1_var=StringVar()
name2_var=StringVar()
table_var=StringVar()

def submit():
    url=url_var.get()
    select=selected.get()
    tag1=tag1_var.get()
    tag2=tag2_var.get()
    class1=class1_var.get()
    class2=class2_var.get()
    name1=name1_var.get()
    name2=name2_var.get()
    table=table_var.get()

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    a=soup.find_all(tag1, class_=class1)
    b=soup.find_all(tag2, class_=class2)

    d1=[]
    d2=[]
    for x,y in zip(a,b):
        d1.append(x.getText())
        d2.append(y.getText())

    df = pd.DataFrame({name1:d1,name2:d2})
    if select==0:
        df.to_csv(table+'.csv', index=False,header=True, encoding='utf-8')
        # print(df)
    else:
        df.to_csv(table+'.csv', mode='a', index=False, header=False, encoding='utf-8')

url_var.set("")
selected.set("")
tag1_var.set("")
tag2_var.set("")
class1_var.set("")
class2_var.set("")
name1_var.set("")
name2_var.set("")
table_var.set("")

#Url
url_label = Label(win, text = 'URL', font=('Arial',10))
url_entry = Entry(win, textvariable=url_var, width=40, font=('Arial',10))

#File
file_label = Label(win, text="File")
new_radio = Radiobutton(win,text='New',variable=selected,value=0)
add_radio = Radiobutton(win,text='Add',variable=selected,value=1)

#Table
table_label = Label(win, text="Table Name")
table_entry = Entry(win, textvariable=table_var, font=('Arial',10))

#Tag
tag_label = Label(win, text = 'Tag', font=('Arial',10))
tag1_entry = Entry(win, textvariable=tag1_var, font=('Arial',10))
tag2_entry = Entry(win, textvariable=tag2_var, font=('Arial',10))

#Class
class_label = Label(win, text = 'Class', font=('Arial',10))
class1_entry = Entry(win, textvariable=class1_var, font=('Arial',10))
class2_entry = Entry(win, textvariable=class2_var, font=('Arial',10))

#Name
name_label = Label(win, text = 'Name', font=('Arial',10))
name1_entry = Entry(win, textvariable=name1_var, font=('Arial',10))
name2_entry = Entry(win, textvariable=name2_var, font=('Arial',10))

#Button
button=Button(win,text = 'Submit',command=submit)

#Grid
head.grid(column=2,row=0,pady=10)
space.grid(column=0,row=0,padx=28,pady=48)

url_label.grid(column=1,row=1,pady=4)
url_entry.grid(column=2,row=1)

file_label.grid(column=1,row=2,pady=2)
new_radio.grid(column=2,row=2,pady=2)
add_radio.grid(column=3,row=2,pady=2)

table_label.grid(column=1,row=3,pady=2)
table_entry.grid(column=2,row=3,pady=2)

tag_label.grid(column=1,row=4,pady=4)
tag1_entry.grid(column=1,row=5,pady=4)
tag2_entry.grid(column=1,row=6,pady=4)

class_label.grid(column=2,row=4,pady=4)
class1_entry.grid(column=2,row=5,pady=4)
class2_entry.grid(column=2,row=6,pady=4)

name_label.grid(column=3,row=4,pady=4)
name1_entry.grid(column=3,row=5,pady=4)
name2_entry.grid(column=3,row=6,pady=4)

button.grid(column=2,row=7,pady=10)

win.mainloop()