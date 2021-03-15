import tkinter
from tkinter import Place, ttk
from tkinter import font
from typing import Sized
import time
root = tkinter.Tk()

granted = False

def grant():
	global granted
	granted = True

def login(name,password):
	succes = False
	file = open('users.txt', 'r')
	for i in file:
		a,b = i.split(',')
	
		b = b.strip()
	
		if(a==name and b==password):
			succes = True
			break
	file.close()
	if(succes):
		label2 = ttk.Label(text='Welcome Serban programming club', font=100)
		label2.pack()
		label2.place(relx = 0.5, rely = 0.1, anchor = 'center')
		label3 = ttk.Label(text=f'Username: {name}')
		label3.pack()
		label3.place(relx = 0.5, rely = 0.2, anchor = 'center')
	else:
		label4 = ttk.Label(text='Wrong username or password', font=100)
		label4.pack()
		label4.place(relx = 0.5, rely = 0.1, anchor = 'center')
		begin()
		
		
def register(name,password):
		file = open('users.txt', 'a')
		file.write('\n'+ name + ',' + password)
		file.close()
		grant()
		
	

def begin():
	def register_user():
		label.destroy()
		register_button.destroy()
		login_button.destroy()
		name_var=tkinter.StringVar()
		passw_var=tkinter.StringVar()
		
		def submit():
			name=name_var.get()
			password=passw_var.get()
			name_var.set("")
			passw_var.set("")
			register(name,password)
			name_label.destroy()
			name_entry.destroy()
			passw_label.destroy()
			passw_entry.destroy()
			sub_btn.destroy()
			begin()
			
		name_label = tkinter.Label(root ,text = 'Username', font=('calibre',10, 'bold'))
		name_entry = tkinter.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
		passw_label = tkinter.Label(root, text = 'Password', font = ('calibre',10,'bold'))
		passw_entry=tkinter.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
		sub_btn=tkinter.Button(root,text = 'Submit', command = submit)
		name_label.grid(row=0,column=0)
		name_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
		name_entry.grid(row=0,column=1)
		name_entry.place(relx = 0.56, rely = 0.5, anchor = 'center')
		passw_label.grid(row=1,column=0)
		passw_label.place(relx = 0.5, rely = 0.55, anchor = 'center')
		passw_entry.grid(row=1,column=1)
		passw_entry.place(relx = 0.56, rely = 0.55, anchor = 'center')
		sub_btn.grid(row=2,column=1)
		sub_btn.place(relx = 0.56, rely = 0.6, anchor = 'center')
		
	def login_user():
		label.destroy()
		register_button.destroy()
		login_button.destroy()
		name_var=tkinter.StringVar()
		passw_var=tkinter.StringVar()
		
		def submit():
			name=name_var.get()
			password=passw_var.get()
			name_var.set("")
			passw_var.set("")
			name_label.destroy()
			name_entry.destroy()
			passw_label.destroy()
			passw_entry.destroy()
			sub_btn.destroy()
			login(name,password)
			
		name_label = tkinter.Label(root ,text = 'Username', font=('calibre',10, 'bold'))
		name_entry = tkinter.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
		passw_label = tkinter.Label(root, text = 'Password', font = ('calibre',10,'bold'))
		passw_entry=tkinter.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
		sub_btn=tkinter.Button(root,text = 'Submit', command = submit)
		name_label.grid(row=0,column=0)
		name_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
		name_entry.grid(row=0,column=1)
		name_entry.place(relx = 0.56, rely = 0.5, anchor = 'center')
		passw_label.grid(row=1,column=0)
		passw_label.place(relx = 0.5, rely = 0.55, anchor = 'center')
		passw_entry.grid(row=1,column=1)
		passw_entry.place(relx = 0.56, rely = 0.55, anchor = 'center')
		sub_btn.grid(row=2,column=1)
		sub_btn.place(relx = 0.56, rely = 0.6, anchor = 'center')

	global option
	label = ttk.Label(text='welcome to Serban programming!!!', font='50')
	label.pack()
	label.place(relx = 0.5, 
                rely = 0.5,
                anchor = 'center')
	register_button = ttk.Button(text='Register' ,command=register_user)
	register_button.pack()
	register_button.place(relx = 0.5, 
                   rely = 0.6,
                   anchor = 'center')
	login_button = ttk.Button(text='Login',command=login_user)
	login_button.pack()
	login_button.place(relx = 0.5, 
                   rely = 0.7,
                   anchor = 'center')

	
	


	 
		
begin()

#access(option)
root.mainloop()
