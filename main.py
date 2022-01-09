from tkinter import *
import backend

def get_selected_data(event):
    global selected_data
    index= databox.curselection()[0]
    selected_data=databox.get(index)
    director_entry.delete(0,END)
    director_entry.insert(END,selected_data[1])
    title_entry.delete(0,END)
    title_entry.insert(END,selected_data[2])
    year_entry.delete(0, END)
    year_entry.insert(END,selected_data[3])
    revenue_entry.delete(0, END)
    revenue_entry.insert(END,selected_data[4])


def view():
    databox.delete(0,END)
    for line in backend.view():
        databox.insert(END,line)

def search():
    databox.delete(0, END)
    for line in backend.search(director_text.get(),title_text.get(),year_text.get(),revenue_text.get()):
        databox.insert(END,line)

def save():
    backend.save(director_text.get(),title_text.get(),year_text.get(),revenue_text.get())

def delete():
    backend.delete(selected_data[0])

def update():
    backend.update(selected_data[0],director_text.get(),title_text.get(),year_text.get(),revenue_text.get())

# Tkinter interface

tk = Tk()
tk.title("My favorite movies list")
tk.geometry("350x400")

# Labels

director_label = Label(tk,text="Director")
director_label.grid(row=0,column=0,pady=5)

title_label = Label(tk,text="Title")
title_label.grid(row=1,column=0,pady=5)

year_label = Label(tk,text="Year")
year_label.grid(row=2,column=0,pady=5)

revenue_label = Label(tk,text="Revenue")
revenue_label.grid(row=3,column=0,pady=5)

# Inputs

director_text = StringVar()
director_entry = Entry(tk,textvariable=director_text)
director_entry.grid(row=0,column=1)

title_text = StringVar()
title_entry = Entry(tk,textvariable=title_text)
title_entry.grid(row=1,column=1)

year_text = StringVar()
year_entry = Entry(tk,textvariable=year_text)
year_entry.grid(row=2,column=1)

revenue_text = StringVar()
revenue_entry = Entry(tk,textvariable=revenue_text)
revenue_entry.grid(row=3,column=1)

# Listbox

databox = Listbox(tk, height=10,width=40)
databox.grid(row=5,column=0,columnspan=2,pady=5,padx=5)

# Scrollbar

scrollbar = Scrollbar(tk)
scrollbar.grid(row=5,column=2)

databox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=databox.yview)

databox.bind('<<ListboxSelect>>',get_selected_data)

# Buttons

search_btn = Button(tk,text="Search",width=10,command=search)
search_btn.grid(row=0,column=2)

save_btn = Button(tk,text="Save",width=10,command=save)
save_btn.grid(row=1,column=2)

update_btn = Button(tk,text="Update",width=10,command=update)
update_btn.grid(row=2,column=2)

delete_btn = Button(tk,text="Delete",width=10,command=delete)
delete_btn.grid(row=3,column=2)

view_btn= Button(tk,text="View Data",width=10,command=view)
view_btn.grid(row=4,column=2)


tk.mainloop()
