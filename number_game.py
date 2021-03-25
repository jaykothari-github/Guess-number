from tkinter import *
from random import randrange
from tkinter.messagebox import showinfo,showerror

rw = Tk()
rw.title('Guess the Number!!')
rw.geometry('600x400+300+100')
rw.resizable(width=False, height=False)

fm = Frame(rw,bg='black',height=400, width=600)
fm.pack()

cc = str(randrange(1,100))
print(cc)
var = StringVar()
var.set('XX')
ans = StringVar()
hint = StringVar()
hint.set('Number is between 1 to 100.')
hist = StringVar()
gh = ''
count = 0
count_l = IntVar()


def check():
    uc = en.get()
    
    if uc.isnumeric() == True:
        if cc == uc:
            var.set(cc)
            showinfo("Winner","🎉🎉Congratulations!! You've guess the right number!!🎉🎉")
            ans.set("🙌🙌Right one!!🙌🙌")
            hint.set('🎉🎉Congratulations!! player...🎉🎉')
            
        else:
            ans.set("Oooppps!! Sorry!! Wrong one!! \n Please try again...")
            if abs(int(cc) - int(uc)) <= 5:
                hint.set("You've almost guess it !!")
            
            elif abs(int(cc) - int(uc)) <= 10:
                hint.set("You are quite near !!")
            
            elif abs(int(cc) - int(uc)) <= 20 and int(cc) < int(uc):
                hint.set("Guess is little bit high !!")

            elif abs(int(cc) - int(uc)) <= 20 and int(cc) > int(uc):
                hint.set("Guess is little bit low !!")

            elif abs(int(cc) - int(uc)) <= 50 and int(cc) < int(uc):
                hint.set("Too High !!")

            elif abs(int(cc) - int(uc)) <= 50 and int(cc) > int(uc):
                hint.set("Too Low !!")

            else:
                hint.set('Still so Far away')

    else:
        showerror("Guess the Number","Please enter only number!!")

    global gh 
    global count

    count+=1
    gh = gh+' '+','+ uc
    hist.set(gh)
    count_l.set(count)


l1 = Label(fm,text='Welcome to the Game!!',bg='black',fg='lightgreen' ,font=('arial',20,'bold'))
l1.place(x = 150, y= 10)

line = Label(fm,text='>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<',bg='black',fg='white')
line.place(x = 50, y= 50)

l2 = Label(fm,text='Computer have guess the number',bg='black',fg='#4287f5' ,font=('arial',12))
l2.place(x = 10, y= 100)

l3 = Label(fm,textvariable=var ,bg='black',fg='white' ,font=('arial',12,'bold'))
l3.place(x = 100, y= 150)


l4 = Label(fm,text="Guess Computer's number",bg='black',fg='#4287f5' ,font=('arial',12))
l4.place(x = 350, y= 100)

en = Entry(fm,bg='#101010',fg='white',width=5, font=('arial',20,'bold'))
en.place(x = 400, y= 150)

btn = Button(fm,text='Check it!!', bg='black',fg='white',height=1,command=check)
btn.place(x=490, y=155)

l5 = Label(fm,text="Hint!! :",bg='black',fg='white' ,font=('arial',12))
l5.place(x = 150, y= 270)

l6 = Label(fm,textvariable=hint,bg='black',fg='white' ,font=('arial',12))
l6.place(x = 210, y= 270)

l7 = Label(fm,textvariable=ans , bg='black', fg='red').place(x=350, y=200)

l8 = Label(fm,textvariable=hist , bg='black', fg='lightblue').place(x=120, y=350)
l8 = Label(fm,text='Guess History > ' , bg='black', fg='lightblue').place(x=30, y=350)

l8 = Label(fm,textvariable= count_l, bg='black', fg='lightblue').place(x=250, y=220)
l8 = Label(fm,text='No. of Guesses :' , bg='black', fg='lightblue').place(x=150, y=220)

rw.mainloop()
