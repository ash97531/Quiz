from tkinter import *
import sqlite3 as sql
from tkinter.font import Font
from tkinter import messagebox
import sys

con=sql.connect(".\\quizdata.db")
cur=con.cursor()

win=Tk()
def score1():
    scoreboard=Tk()
    junior=[3,4,1,2,1]
    rightans1, wrongans1, correct, incorrect, result = '', '', 0, 0, ''
    ansgot=[an1.get(), an2.get(), an3.get(), an4.get(), an5.get()]
    for i in range (5):
        if ansgot[i] == junior[i]:
            correct = correct + 1
            rightans1 = rightans1 + 'Ques ' + str(i+1) + ', '
        else:
            incorrect = incorrect + 1
            wrongans1 = wrongans1 + 'Ques ' + str(i+1) + ', '

    if ((correct/5)*100) > 50:
        result = 'pass'
    else:
        result = 'fail'

    cor=str(5-correct-incorrect)
    correct1=str(correct)
    incorrect1=str(incorrect)

    view11=Label(scoreboard, text='number of correct answers is -> '+correct1)
    view12=Label(scoreboard, text='number of incorrect answers is -> '+incorrect1)
    view13=Label(scoreboard, text='number of missed questions is -> '+cor)
    view14=Label(scoreboard, text='percentage corrected ->'+str((correct/5)*100) + '%')
    view15=Label(scoreboard, text='correct answer are -> '+rightans1)
    view16=Label(scoreboard, text='incorrect answer are -> '+wrongans1)
    view17=Label(scoreboard, text='result -> '+result)
    view11.pack()
    view12.pack()
    view13.pack()
    view14.pack()
    view15.pack()
    view16.pack()
    view17.pack()
    scoreboard.mainloop()
    con.close()

def score2():
    scoreboard1=Tk()
    senior=[4,1,2,1,1,3,3,4,2,3,2,1,4,2,4]
    correct, incorrect, rightans2, wrongans2, result=0, 0, '', '', ''
    ansgot=[ans1.get(),ans2.get(),ans3.get(),ans4.get(),ans5.get(),ans6.get(),ans7.get(),ans8.get(),ans9.get(),ans10.get(),ans11.get(),ans12.get(),ans13.get(),ans14.get(),ans15.get()]
    for i in range (15):
        if ansgot[i] == senior[i]:
            correct = correct + 1
            rightans2 = rightans2 + 'Ques ' + str(i+1) + ', '
        else:
            incorrect = incorrect + 1
            wrongans2 = wrongans2 + 'Ques ' + str(i+1) + ', '

    if ((correct/15)*100) > 50:
        result = 'pass'
    else:
        result = 'fail'

    cor=str(15-correct-incorrect)
    correct1=str(correct)
    incorrect1=str(incorrect)
    view21=Label(scoreboard1, text='number of correct answers is -> '+correct1)
    view22=Label(scoreboard1, text='number of incorrect answers is -> '+incorrect1)
    view23=Label(scoreboard1, text='number of missed questions is -> '+cor)
    view14=Label(scoreboard1, text='percentage corrected ->'+str((correct/15)*100) + '%')
    view15=Label(scoreboard1, text='correct answer are -> '+rightans2)
    view16=Label(scoreboard1, text='incorrect answer are -> '+wrongans2)
    view17=Label(scoreboard1, text='result -> '+result)
    view21.pack()
    view22.pack()
    view23.pack()
    view14.pack()
    view15.pack()
    view16.pack()
    view17.pack()
    scoreboard1.mainloop()
    con.close()

def primary2():
    global an5
    #bo2=Tk()
    bo2=Toplevel()
    an5=IntVar()
    d5=LabelFrame(bo2, text='Ques 5')
    f5=Label(d5, text='national youth day is celebrated ')
    h51=Radiobutton(d5, text='jan 12', value=1, variable=an5)
    h52=Radiobutton(d5, text='jan 15', value=2, variable=an5)
    h53=Radiobutton(d5, text='july 1', value=3, variable=an5)
    h54=Radiobutton(d5, text='26 nov', value=4, variable=an5)
    f5.pack()
    h51.pack()
    h52.pack()
    h53.pack()
    h54.pack()
    d5.pack()#1

    sub1=Button(bo2, text='submit', command=score1)
    sub1.pack()
    bo2.mainloop()

def primary():
    global an1, an2, an3, an4
    #bo=Tk()
    bo=Toplevel()
    an1=IntVar()
    d1=LabelFrame(bo, text='Ques 1')
    f1=Label(d1, text='which is the smallest ocean in the world')
    h11=Radiobutton(d1, text='atlantic ocean', value=1, variable=an1)
    h12=Radiobutton(d1, text='pacific ocean', value=2, variable=an1)
    h13=Radiobutton(d1, text='arctic ocean', value=3, variable=an1)
    h14=Radiobutton(d1, text='indian ocean', value=4, variable=an1)
    f1.pack()
    h11.pack()
    h12.pack()
    h13.pack()
    h14.pack()
    d1.pack()#3

    an2=IntVar()
    d2=LabelFrame(bo, text='Ques 2')
    f2=Label(d2, text='which is the highest peak in india')
    h21=Radiobutton(d2, text='kanchan jangha', value=1, variable=an2)
    h22=Radiobutton(d2, text='mount everset', value=2, variable=an2)
    h23=Radiobutton(d2, text='nanda devi', value=3, variable=an2)
    h24=Radiobutton(d2, text='K-2', value=4, variable=an2)
    f2.pack()
    h21.pack()
    h22.pack()
    h23.pack()
    h24.pack()
    d2.pack()#4

    an3=IntVar()
    d3=LabelFrame(bo, text='Ques 3')
    f3=Label(d3, text='what is national symbol of india')
    h31=Radiobutton(d3, text='ashok column, sarnath varansi', value=1, variable=an3)
    h32=Radiobutton(d3, text='lotus', value=2, variable=an3)
    h33=Radiobutton(d3, text='tiger', value=3, variable=an3)
    h34=Radiobutton(d3, text='none of these', value=4, variable=an3)
    f3.pack()
    h31.pack()
    h32.pack()
    h33.pack()
    h34.pack()
    d3.pack()#1

    an4=IntVar()
    d4=LabelFrame(bo, text='Ques 4')
    f4=Label(d4, text='who built red fort in delhi')
    h41=Radiobutton(d4, text='akbar', value=1, variable=an4)
    h42=Radiobutton(d4, text='shah jahan', value=2, variable=an4)
    h43=Radiobutton(d4, text='mohammad bin tuglak', value=3, variable=an4)
    h44=Radiobutton(d4, text='jahangir', value=4, variable=an4)
    f4.pack()
    h41.pack()
    h42.pack()
    h43.pack()
    h44.pack()
    d4.pack()#2

    next1=Button(bo, text='next', command=primary2)
    next1.pack(side=RIGHT)
    bo.mainloop()

def secondary3():
    global ans9, ans10, ans11, ans12
    body3=Toplevel()
    ans9=IntVar()
    q9=LabelFrame(body3, text='Ques 9')
    l9=Label(q9, text='which instrument is used to check internal organs of body?')
    r91=Radiobutton(q9, text='cardiogram', value=1, variable=ans9)
    r92=Radiobutton(q9, text='endoscope', value=2, variable=ans9)
    r93=Radiobutton(q9, text='sterioscope', value=3, variable=ans9)
    r94=Radiobutton(q9, text='microscope', value=4, variable=ans9)
    l9.pack()
    r91.pack()
    r92.pack()
    r93.pack()
    r94.pack()
    q9.pack()#2

    ans10=IntVar()
    q10=LabelFrame(body3, text='Ques 10')
    l10=Label(q10, text='the grassland of north america is called')
    r101=Radiobutton(q10, text='steppes', value=1, variable=ans10)
    r102=Radiobutton(q10, text='temperate', value=2, variable=ans10)
    r103=Radiobutton(q10, text='prairies', value=3, variable=ans10)
    r104=Radiobutton(q10, text='none of these', value=4, variable=ans10)
    l10.pack()
    r101.pack()
    r102.pack()
    r103.pack()
    r104.pack()
    q10.pack()#3

    ans11=IntVar()
    q11=LabelFrame(body3, text='Ques 11')
    l11=Label(q11, text='what is the dry ice out of the following')
    r111=Radiobutton(q11, text='calcium hydroxide', value=1, variable=ans11)
    r112=Radiobutton(q11, text='solid carbon dioxide', value=2, variable=ans11)
    r113=Radiobutton(q11, text='sodium hydroxide', value=3, variable=ans11)
    r114=Radiobutton(q11, text='none of these', value=4, variable=ans11)
    l11.pack()
    r111.pack()
    r112.pack()
    r113.pack()
    r114.pack()
    q11.pack()#2

    ans12=IntVar()
    q12=LabelFrame(body3, text='Ques 12')
    l12=Label(q12, text='which indian state is the largest producer of bamboo?')
    r121=Radiobutton(q12, text='assam', value=1, variable=ans12)
    r122=Radiobutton(q12, text='west bengal', value=2, variable=ans12)
    r123=Radiobutton(q12, text='goa', value=3, variable=ans12)
    r124=Radiobutton(q12, text='gujrat', value=4, variable=ans12)
    l12.pack()
    r121.pack()
    r122.pack()
    r123.pack()
    r124.pack()
    q12.pack()#1

    next4=Button(body3, text='next', command=secondary4)
    next4.pack(side=RIGHT)
    prev4=Button(body3, text='previous page', command=secondary2)
    prev4.pack(side=LEFT)
    
    body3.mainloop()

def secondary2():
    global ans5, ans6, ans7, ans8
    body2=Toplevel()
    ans5=IntVar()
    q5=LabelFrame(body2, text='Ques 5')
    l5=Label(q5, text='who gave the famous slogan "simon commission go back"')
    r51=Radiobutton(q5, text='lala lajpat rai', value=1, variable=ans5)
    r52=Radiobutton(q5, text='mahatma gandhi', value=2, variable=ans5)
    r53=Radiobutton(q5, text='dardar balabh bhai patel', value=3, variable=ans5)
    r54=Radiobutton(q5, text='bhagat singh', value=4, variable=ans5)
    l5.pack()
    r51.pack()
    r52.pack()
    r53.pack()
    r54.pack()
    q5.pack()#1

    ans6=IntVar()
    q6=LabelFrame(body2, text='Ques 6')
    l6=Label(q6, text='which of the following steps moon does not appear at all?')
    r61=Radiobutton(q6, text='cresent moon', value=1, variable=ans6)
    r62=Radiobutton(q6, text='full moon', value=2, variable=ans6)
    r63=Radiobutton(q6, text='new moon', value=3, variable=ans6)
    r64=Radiobutton(q6, text='gibbous moon', value=4, variable=ans6)
    l6.pack()
    r61.pack()
    r62.pack()
    r63.pack()
    r64.pack()
    q6.pack()#3

    ans7=IntVar()
    q7=LabelFrame(body2, text='Ques 7')
    l7=Label(q7, text='who created the "four minar"')
    r71=Radiobutton(q7, text='akbar', value=1, variable=ans7)
    r72=Radiobutton(q7, text='babar', value=2, variable=ans7)
    r73=Radiobutton(q7, text='oli qutbshah', value=3, variable=ans7)
    r74=Radiobutton(q7, text='jahangir', value=4, variable=ans7)
    l7.pack()
    r71.pack()
    r72.pack()
    r73.pack()
    r74.pack()
    q7.pack()#3

    ans8=IntVar()
    q8=LabelFrame(body2, text='Ques 8')
    l8=Label(q8, text='biggest planet in our solar system')
    r81=Radiobutton(q8, text='neptune', value=1, variable=ans8)
    r82=Radiobutton(q8, text='mars', value=2, variable=ans8)
    r83=Radiobutton(q8, text='earth', value=3, variable=ans8)
    r84=Radiobutton(q8, text='jupiter', value=4, variable=ans8)
    l8.pack()
    r81.pack()
    r82.pack()
    r83.pack()
    r84.pack()
    q8.pack()#4

    next3=Button(body2, text='next', command=secondary3)
    next3.pack(side=RIGHT)
    prev3=Button(body2, text='previous page', command=secondary)
    prev3.pack(side=LEFT)
    body2.mainloop()

def secondary4():
    global ans13, ans14, ans15
    body4=Toplevel()
    ans13=IntVar()
    q13=LabelFrame(body4, text='Ques 13')
    l13=Label(q13, text='ECG is used to detect any disease related to?')
    r131=Radiobutton(q13, text='brain', value=1, variable=ans13)
    r132=Radiobutton(q13, text='lung', value=2, variable=ans13)
    r133=Radiobutton(q13, text='kidney', value=3, variable=ans13)
    r134=Radiobutton(q13, text='heart', value=4, variable=ans13)
    l13.pack()
    r131.pack()
    r132.pack()
    r133.pack()
    r134.pack()
    q13.pack()#4

    ans14=IntVar()
    q14=LabelFrame(body4, text='Ques 14')
    l14=Label(q14, text='whose plants make meals in the presence of green plants')
    r141=Radiobutton(q14, text='root', value=1, variable=ans14)
    r142=Radiobutton(q14, text='leaf', value=2, variable=ans14)
    r143=Radiobutton(q14, text='flower', value=3, variable=ans14)
    r144=Radiobutton(q14, text='stem', value=4, variable=ans14)
    l14.pack()
    r141.pack()
    r142.pack()
    r143.pack()
    r144.pack()
    q14.pack()#2

    ans15=IntVar()
    q15=LabelFrame(body4, text='Ques 15')
    l15=Label(q15, text='world earth day is celebrated on which day?')
    r151=Radiobutton(q15, text='april 21', value=1, variable=ans15)
    r152=Radiobutton(q15, text='july 11', value=2, variable=ans15)
    r153=Radiobutton(q15, text='june 5', value=3, variable=ans15)
    r154=Radiobutton(q15, text='april 22', value=4, variable=ans15)
    l15.pack()
    r151.pack()
    r152.pack()
    r153.pack()
    r154.pack()
    q15.pack()#4

    sub2=Button(body4, text='submit', command=score2)
    sub2.pack()
    body4.mainloop()

def secondary():
    global ans1, ans2, ans3, ans4 
    body=Toplevel()
    ans1=IntVar()
    q1=LabelFrame(body, text='Ques 1')
    l1=Label(q1, text='for many PCs and workstations, a central computer that collect data and programs is called')
    r11=Radiobutton(q1, text='super computer', value=1, variable=ans1)
    r12=Radiobutton(q1, text='mini computer', value=2, variable=ans1)
    r13=Radiobutton(q1, text='laptop', value=3, variable=ans1)
    r14=Radiobutton(q1, text='server', value=4, variable=ans1)
    l1.pack()
    r11.pack()
    r12.pack()
    r13.pack()
    r14.pack()
    q1.pack()#4

    ans2=IntVar()
    q2=LabelFrame(body, text='Ques 2')
    l2=Label(q2, text='which of the following is always found instinctively in nature?')
    r21=Radiobutton(q2, text='gold', value=1, variable=ans2)
    r22=Radiobutton(q2, text='silver', value=2, variable=ans2)
    r23=Radiobutton(q2, text='sodium', value=3, variable=ans2)
    r24=Radiobutton(q2, text='copper', value=4, variable=ans2)
    l2.pack()
    r21.pack()
    r22.pack()
    r23.pack()
    r24.pack()
    q2.pack()#1

    ans3=IntVar()
    q3=LabelFrame(body, text='Ques 3')
    l3=Label(q3, text='who gave the slogan jai jawan jai kissan?')
    r31=Radiobutton(q3, text='swami vivekananda', value=1, variable=ans3)
    r32=Radiobutton(q3, text='lal bahadur shastri', value=2, variable=ans3)
    r33=Radiobutton(q3, text='atal bihari vajpayi', value=3, variable=ans3)
    r34=Radiobutton(q3, text='none of these', value=4, variable=ans3)
    l3.pack()
    r31.pack()
    r32.pack()
    r33.pack()
    r34.pack()
    q3.pack()#2

    ans4=IntVar()
    q4=LabelFrame(body, text='Ques 4')
    l4=Label(q4, text='which of the following present chemical change?')
    r41=Radiobutton(q4, text='heat of mercury oxide', value=1, variable=ans4)
    r42=Radiobutton(q4, text='iodine depression', value=2, variable=ans4)
    r43=Radiobutton(q4, text='evapouration of alcohol', value=3, variable=ans4)
    r44=Radiobutton(q4, text='heat of platinum wire', value=4, variable=ans4)
    l4.pack()
    r41.pack()
    r42.pack()
    r43.pack()
    r44.pack()
    q4.pack()#1

    next2=Button(body, text='next', command=secondary2)
    next2.pack(side=RIGHT)
    body.mainloop()

def clear():
    global entry1, entry2
    se = "select login_id from info where paswd like '"+entry2.get()+"'"
    cur.execute(se)
    a=cur.fetchone()
    if a:
        if entry1.get() == a[0]:
            profile()
        else:
            messagebox.showerror('error', 'wrong id or password!!!')
    else:
        messagebox.showerror('error', 'wrong id or password!!!')

def logout():
    win.quit

def delaccount():
    m="delete from info where login_id like '"+entry1.get()+"'"
    cur.execute(m)
    con.commit()
    submit()

def start():
    bod()

def change():
    g1=k1.get()
    g2=k4.get()
    g3=k2.get()
    g4=k3.get()
    g5=k7.get()
    g6=k8.get()
    g7=k5.get()
    g8=k6.get()

    if g7 == g8:
        st="update info set name='{}', login_id='{}', father_name='{}', mother_name='{}',\
        gender='{}', mob_no='{}', paswd='{}' where login_id='{}'\
        ".format(g1, g2, g3, g4, g5, g6, g7, entry1.get())
        cur.execute(st)
        con.commit()
        pro=Tk()
        sp="select * from info where login_id like '"+k4.get()+"';"
        cur.execute(sp)
        a = cur.fetchone()
        tmain=Label(pro, text='YOUR PROFILE').grid(row=0, column=1)
        t1=Label(pro, text='name').grid(row=4, column=1)
        t2=Label(pro, text='login id').grid(row=5, column=1)
        t3=Label(pro, text='father name').grid(row=6, column=1)
        t4=Label(pro, text='mother name').grid(row=7, column=1)
        t5=Label(pro, text='gender').grid(row=8, column=1)
        t6=Label(pro, text='mobile no.').grid(row=9, column=1)
        t7=Label(pro, text='password').grid(row=10, column=1)

        r1=Label(pro, text=a[0]).grid(row=4, column=2)
        r2=Label(pro, text=a[1]).grid(row=5, column=2)
        r3=Label(pro, text=a[2]).grid(row=6, column=2)
        r4=Label(pro, text=a[3]).grid(row=7, column=2)
        r5=Label(pro, text=a[4]).grid(row=8, column=2)
        r6=Label(pro, text=a[5]).grid(row=9, column=2)
        r7=Label(pro, text=a[6]).grid(row=10, column=2)

        but1=Button(pro, text='edit', command=edit).grid(row=11, column=1)
        but2=Button(pro, text='delete account', command=delaccount).place(x=85, y=168)
        but3=Button(pro, text='start test', command=start).place(x=200, y=168)
        but4=Button(pro, text='logout', command=logout).place(x=200, y=10)

        pro.mainloop()

    else:
        messagebox.showerror('error', 'you had missed somthing!!!')

def edit():
    rot=Tk()
    global a1,a2,a3,a4,a5,a6,a7,a8,k1,k2,k3,k4,k5,k6,k7,k8
    n1=Label(rot, text='name').grid(row=0, column=0)
    n2=Label(rot, text='father name').grid(row=1, column=0)
    n3=Label(rot, text='mother name').grid(row=2, column=0)
    n4=Label(rot, text='login id').grid(row=3, column=0)
    n5=Label(rot, text='password').grid(row=4, column=0)
    n6=Label(rot, text='confirm your password').grid(row=5, column=0)
    n7=Label(rot, text='gender (M/F)').grid(row=6, column=0)
    n8=Label(rot, text='mobile number').grid(row=7, column=0)

    a1=StringVar()
    a2=StringVar()
    a3=StringVar()
    a4=StringVar()
    a5=StringVar()
    a6=StringVar()
    a7=StringVar()
    a8=StringVar()

    k1=Entry(rot, textvariable=z1)
    k2=Entry(rot, textvariable=z2)
    k3=Entry(rot, textvariable=a3)
    k4=Entry(rot, textvariable=a4)
    k5=Entry(rot, textvariable=a5)
    k6=Entry(rot, textvariable=a6)
    k7=Entry(rot, textvariable=a7)
    k8=Entry(rot, textvariable=a8)

    k1.grid(row=0, column=1)
    k2.grid(row=1, column=1)
    k3.grid(row=2, column=1)
    k4.grid(row=3, column=1)
    k5.grid(row=4, column=1)
    k6.grid(row=5, column=1)
    k7.grid(row=6, column=1)
    k8.grid(row=7, column=1)

    b1=Button(rot, text='CHANGE', command=change).grid(row=9, column=1)

    rot.mainloop()

def profile():
    pro=Tk()
    sp="select * from info where login_id like '"+entry1.get()+"';"
    cur.execute(sp)
    a = cur.fetchone()
    tmain=Label(pro, text='YOUR PROFILE').grid(row=0, column=1)
    t1=Label(pro, text='name').grid(row=4, column=1)
    t2=Label(pro, text='login id').grid(row=5, column=1)
    t3=Label(pro, text='father name').grid(row=6, column=1)
    t4=Label(pro, text='mother name').grid(row=7, column=1)
    t5=Label(pro, text='gender').grid(row=8, column=1)
    t6=Label(pro, text='mobile no.').grid(row=9, column=1)
    t7=Label(pro, text='password').grid(row=10, column=1)

    r1=Label(pro, text=a[0]).grid(row=4, column=2)
    r2=Label(pro, text=a[1]).grid(row=5, column=2)
    r3=Label(pro, text=a[2]).grid(row=6, column=2)
    r4=Label(pro, text=a[3]).grid(row=7, column=2)
    r5=Label(pro, text=a[4]).grid(row=8, column=2)
    r6=Label(pro, text=a[5]).grid(row=9, column=2)
    r7=Label(pro, text=a[6]).grid(row=10, column=2)

    but1=Button(pro, text='edit', command=edit).grid(row=11, column=1)
    but2=Button(pro, text='delete account', command=delaccount).place(x=85, y=168)
    but3=Button(pro, text='start test', command=start).place(x=200, y=168)
    but4=Button(pro, text='logout', command=logout).place(x=200, y=10)

    pro.mainloop()

def submit():
    global entry1, entry2
    submit=Toplevel()
    label1=Label(submit, text='login id')
    label2=Label(submit, text='password')
    entry1=Entry(submit, textvariable = e1)
    entry2=Entry(submit, textvariable = e2)

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    butto=Button(submit, text='login', command=clear).grid(row=3, column=1)
    submit.mainloop()

def bod():
    bod=Tk()
    but1=Button(bod, text=' KIDS ', command=primary)
    but2=Button(bod, text=' LEGENDS ', command=secondary)
    but3=Label(bod, text=' SELECT LEVELS ')
    but1.grid(row=1, column=1)
    but2.grid(row=1, column=2)
    but3.grid(row=0, column=1)

    bod.mainloop()

def log():
    '''mysql login'''
    submit()

def reg():
    g1=e1.get()
    g2=e4.get()
    g3=e2.get()
    g4=e3.get()
    g5=e7.get()
    g6=e8.get()
    g7=e5.get()
    g8=e6.get()
    if t.get()==0 and g7 == g8:
        try:
            st="insert into info(name, login_id, father_name, mother_name, gender, mob_no, paswd)\
            values('{}', '{}', '{}', '{}', '{}', '{}', '{}')\
            ".format(g1, g2, g3, g4, g5, g6, g7)
            cur.execute(st)
            con.commit()
            bod()
        except:            
            cur.execute(
                """create table info (
                    name varchar(50),
                    login_id varchar(50) UNIQUE,
                    father_name varchar(50),
                    mother_name varchar(50),
                    gender char(1),
                    mob_no int,
                    paswd varchar(50)
                )"""
            )
            con.commit()
            st="insert into info(name, login_id, father_name, mother_name, gender, mob_no, paswd)\
            values('{}', '{}', '{}', '{}', '{}', '{}', '{}')\
            ".format(g1, g2, g3, g4, g5, g6, g7)
            cur.execute(st)
            con.commit()
            bod()
    else:
        messagebox.showerror('error', 'you had missed somthing!!!')
        
def but():
    root=Tk()
    global z1,z2,z3,z4,z5,z6,z7,z8,t,e1,e2,e3,e4,e5,e6,e7,e8
    n1=Label(root, text='name')
    n2=Label(root, text='father name')
    n3=Label(root, text='mother name')
    n4=Label(root, text='login id')
    n5=Label(root, text='password')
    n6=Label(root, text='confirm your password')
    n7=Label(root, text='gender (M/f)')
    n8=Label(root, text='mobile number')

    z1=StringVar()
    z2=StringVar()
    z3=StringVar()
    z4=StringVar()
    z5=StringVar()
    z6=StringVar()
    z7=StringVar()
    z8=StringVar()
    
    e1=Entry(root, textvariable=z1)
    e2=Entry(root, textvariable=z2)
    e3=Entry(root, textvariable=z3)
    e4=Entry(root, textvariable=z4)
    e5=Entry(root, textvariable=z5)
    e6=Entry(root, textvariable=z6)
    e7=Entry(root, textvariable=z7)
    e8=Entry(root, textvariable=z8)

    n1.grid(row=0, column=0)
    n2.grid(row=1, column=0)
    n3.grid(row=2, column=0)
    n4.grid(row=3, column=0)
    n5.grid(row=4, column=0)
    n6.grid(row=5, column=0)
    n7.grid(row=6, column=0)
    n8.grid(row=7, column=0)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)
    e6.grid(row=5, column=1)
    e7.grid(row=6, column=1)
    e8.grid(row=7, column=1)
    
    t = IntVar()
    chk=Checkbutton(root, text='my all information is correct', variable=t)
    chk.grid(row=8, column=1)

    b1=Button(root, text='register', command=reg)
    b2=Button(root, text='login', command=log)
    b1.grid(row=9, column=1)
    b2.grid(row=9, column=2)
    root.mainloop()

my_font=Font(family='Jokerman', size=90, weight='bold')
thelabel=Label(win, text='welcome to quiz', font=my_font)
thelabel.place(x=200, y=150)

button=Button(win, text='start', width=30, height=8, bg='green', command=but)
button.place(x=550, y=400)

win.mainloop()
