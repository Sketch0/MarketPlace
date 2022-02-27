from tkinter import *
import pywhatkit
from PIL import Image , ImageTk
import wikipedia
import pyttsx3
engine = pyttsx3.init()
engine_voice = engine.getProperty('voices')
engine.setProperty('voice',engine_voice[1].id)
engine.say("Welcome to Darsha's Technologies")
engine.runAndWait()
root = Tk()
root.title("Darshan's Technologies")
root.config(bg="grey")

r = Image.open("C:\\Users\\BEDAPRAKASH\\Downloads\\D.Tech_Logo.png")
f = r.resize((500,500))
p = ImageTk.PhotoImage(f)
l = Label(image=p,bg="grey")
l.place(x=200,y=300)

open_img = Image.open("C:\\Users\\BEDAPRAKASH\\Downloads\\D.Tech_Logo.png")
resize_open_img = open_img.resize((170,170))
photo = ImageTk.PhotoImage(resize_open_img)

l1 = Label(image=photo,bg="grey")
l1.place(x=0,y=0)

root.geometry("1000x1000")
root.maxsize(1000,1000)
head_label = Label(text="Darshan's Technologies",font=("Stencil",35),bg="grey")
head_label.place(x=180,y=50)

string_usr = StringVar()
string_usr_entry = Entry(textvariable=string_usr,width=50,bg="grey",font=("Times 15 italic bold"))
string_usr_entry.place(x=300,y=960)

main_label = Label(text="",font=("Stencil"),bg="grey")
main_label.place(x=0,y=200)

#wikipedia section
def wiki():
    result = wikipedia.summary("\n" + f"{string_usr.get()}",1)
    main_label.config(text=result)

def yt():
    pywhatkit.playonyt(f"{string_usr.get()}")

def search():
    pywhatkit.search(f"{string_usr.get()}")

search_btn = Button(text="Search",font=("Stencil",8),bd=5,command=search,bg="indigo",height="2",width="10")
search_btn.place(x=65,y=950)
wiki_btn = Button(text="Info",font=("Stencil",8),bd=5,command=wiki,bg="brown",height="2",width="10")
wiki_btn.place(x=710,y=950)
yt_btn = Button(text="Search_on_yt",font=("Stencil",8),bd=5,command=yt,bg="yellow",height="2",width="15")
yt_btn.place(x=160,y=950)
end_btn = Button(text="end",font=("Stencil",8),bd=5,command=root.destroy,bg="red",height="2",width="10")
end_btn.place(x=910,y=950)

class calc_sec:
    def calc():

        #Calculator section
        #Clac_title
        calc_title = Label(text="D.Tech_Calc",font=("Stencil",18),bg="grey")
        calc_title.place(x=750,y=455)

        expression = ""


        # Function to update expression
        # in the text entry box
        def press(num):
        	# point out the global expression variable
        	global expression

        	# concatenation of string
        	expression = expression + str(num)

        	# update the expression by using set method
        	equation.set(expression)

        def clear():
        	global expression
        	expression = ""
        	equation.set("")

        def equalpress():
        	try:

        		global expression
        		total = str(eval(expression))
        		equation.set(total)
        		expression = ""
        	except:

        		equation.set(" error ")
        		expression = ""
        equation = StringVar()
        expression_field = Entry(textvariable=equation,width=20,bg="grey",font=("Stencil",10))
        expression_field.place(x=750,y=500)
        button1 = Button(text=' 1 ', fg='white', bg='black',
        				command=lambda: press(1), height=1, width=7)
        button1.place(x=750,y=530)

        button2 = Button(text=' 2 ', fg='white', bg='black',
        				command=lambda: press(2), height=1, width=7)
        button2.place(x=820,y=530)

        button3 = Button(text=' 3 ', fg='white', bg='black',
        				command=lambda: press(3), height=1, width=7)
        button3.place(x=890,y=530)

        button4 = Button(text=' 4 ', fg='white', bg='black',
        				command=lambda: press(4), height=1, width=7)
        button4.place(x=750,y=567)

        button5 = Button(text=' 5 ', fg='white', bg='black',
        				command=lambda: press(5), height=1, width=7)
        button5.place(x=820,y=567)

        button6 = Button(text=' 6 ', fg='white', bg='black',
        				command=lambda: press(6), height=1, width=7)
        button6.place(x=890,y=567)

        button7 = Button(text=' 7 ', fg='white', bg='black',
        				command=lambda: press(7), height=1, width=7)
        button7.place(x=750,y=604)

        button8 = Button(text=' 8 ', fg='white', bg='black',
        				command=lambda: press(8), height=1, width=7)
        button8.place(x=820,y=604)

        button9 = Button(text=' 9 ', fg='white', bg='black',
        				command=lambda: press(9), height=1, width=7)
        button9.place(x=890,y=604)

        button0 = Button(text=' 0 ', fg='white', bg='black',
        				command=lambda: press(0), height=1, width=7)
        button0.place(x=750,y=641)

        plus = Button(text=' + ', fg='white', bg='black',
        			command=lambda: press("+"), height=1, width=7)
        plus.place(x=820,y=641)

        minus = Button(text=' - ', fg='white', bg='black',
        			command=lambda: press("-"), height=1, width=7)
        minus.place(x=890,y=641)

        multiply = Button(text=' * ', fg='white', bg='black',
        				command=lambda: press("*"), height=1, width=7)
        multiply.place(x=750,y=678)

        divide = Button(text=' / ', fg='white', bg='black',
        				command=lambda: press("/"), height=1, width=7)
        divide.place(x=820,y=678)

        equal = Button(text=' = / on', fg='white', bg='green',
        			command=equalpress, height=1, width=7)
        equal.place(x=890,y=678)

        clear = Button(text='Clear', fg='black', bg='red',
        			command=clear, height=1, width=7)
        clear.place(x=750,y=715)

        Decimal= Button(text='.', fg='white', bg='black',
        				command=lambda: press('.'), height=1, width=7)
        Decimal.place(x=890,y=715)
def call():
    obj = calc_sec
    obj.calc()


calc = Button(text="calc",font=("Stencil",8),bd=5,height="2",width="10",bg="black",command=call)
calc.place(x=800,y=950)

root.mainloop()
