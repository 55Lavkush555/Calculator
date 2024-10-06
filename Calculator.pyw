import tkinter as tk

class Calculator:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('Calculator')

		self.create_widget()

		self.root.bind('<Return>', self.equal)

		self.root.mainloop()

	def create_widget(self):
		global contest
		contest = tk.StringVar()
		self.entry = tk.Entry(self.root, width=30, font="Arial 20", textvariable=contest).pack()
		
		self.fram1 = tk.Frame(self.root)
		self.b9 = tk.Button(self.fram1, text='9', width=10, font='Arial 18', command=b9).pack(side='left')
		self.b8 = tk.Button(self.fram1, text='8', width=10, font='Arial 18', command=b8).pack(side='left')
		self.b7 = tk.Button(self.fram1, text='7', width=10, font='Arial 18', command=b7).pack(side='left')
		self.fram1.pack()

		self.fram2 = tk.Frame(self.root)
		self.b6 = tk.Button(self.fram2, text='6', width=10, font='Arial 18', command=b6).pack(side='left')
		self.b5 = tk.Button(self.fram2, text='5', width=10, font='Arial 18', command=b5).pack(side='left')
		self.b4 = tk.Button(self.fram2, text='4', width=10, font='Arial 18', command=b4).pack(side='left')
		self.fram2.pack()

		self.fram3 = tk.Frame(self.root)
		self.b3 = tk.Button(self.fram3, text='3', width=10, font='Arial 18', command=b3).pack(side='left')
		self.b2 = tk.Button(self.fram3, text='2', width=10, font='Arial 18', command=b2).pack(side='left')
		self.b1 = tk.Button(self.fram3, text='1', width=10, font='Arial 18', command=b1).pack(side='left')
		self.fram3.pack()

		self.fram3 = tk.Frame(self.root)
		self.b3 = tk.Button(self.fram3, text='%', width=10, font='Arial 18', command=remander).pack(side='left')
		self.b2 = tk.Button(self.fram3, text='0', width=10, font='Arial 18', command=b0).pack(side='left')
		self.b1 = tk.Button(self.fram3, text='+', width=10, font='Arial 18', command=plus).pack(side='left')
		self.fram3.pack()

		self.fram3 = tk.Frame(self.root)
		self.b3 = tk.Button(self.fram3, text='/', width=10, font='Arial 18', command=divide).pack(side='left')
		self.b2 = tk.Button(self.fram3, text='-', width=10, font='Arial 18', command=mines).pack(side='left')
		self.b1 = tk.Button(self.fram3, text='*', width=10, font='Arial 18', command=multi).pack(side='left')
		self.fram3.pack()

		self.fram3 = tk.Frame(self.root)
		self.b3 = tk.Button(self.fram3, text='=', width=10, font='Arial 18', command=eq).pack(side='left')
		self.b2 = tk.Button(self.fram3, text='bac', width=10, font='Arial 18', command=bac).pack(side='left')
		self.b1 = tk.Button(self.fram3, text='C', width=10, font='Arial 18', command=C).pack(side='left')
		self.fram3.pack()

	def equal(self, l):
		global a
		try:
			a = eval(contest.get())
			a = str(a)
			contest.set(a)
		except:
			a = ''
			contest.set('Wrong input!')


a = ''

def b1():
	global a
	a = a + '1'
	contest.set(a)
		
def b2():
	global a
	a = a + '2'
	contest.set(a)
		
def b3():
	global a
	a = a + '3'
	contest.set(a)
		
def b4():
	global a
	a = a + '4'
	contest.set(a)
		
def b5():
	global a
	a = a + '5'
	contest.set(a)
		
def b6():
	global a
	a = a + '6'
	contest.set(a)
		
def b7():
	global a
	a = a + '7'
	contest.set(a)
		
def b8():
	global a
	a = a + '8'
	contest.set(a)
		
def b9():
	global a
	a = a + '9'
	contest.set(a)

def remander():
	global a
	a = a + '%'
	contest.set(a)

def b0():
	global a
	a = a + '0'
	contest.set(a)
		
def divide():
	global a
	a = a + '/'
	contest.set(a)
		
def multi():
	global a
	a = a + '*'
	contest.set(a)
		
def mines():
	global a
	a = a + '-'
	contest.set(a)
		
def plus():
	global a
	a = a + '+'
	contest.set(a)
		
def bac():
	global a
	b = len(a)
	c = b-1

	a = a[0:c]
	contest.set(a)
		
def eq():
	global a
	try:
		a = eval(contest.get())
		a = str(a)
		contest.set(a)
	except:
		a = ''
		contest.set('Wrong input!')
		
def C():
	global a
	a = ''
	contest.set(a)
		

if __name__ == '__main__':
	Window = Calculator()
	