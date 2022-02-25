import random
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
from tkinter import scrolledtext
import datetime
import requests
import threading
import ftest
#import multiprocessing
import time
window = Tk()
window.wm_title('demo facebook requests sender')
welcome = ttk.Label(window, text="أهلا بك في برنامج اضافة الاصدقاء" ,font="blue 15")
col, r = 0, 0
welcome.grid(column=0, row=r)
r = r + 1
def demo():
    date = datetime.datetime(2022, 3, 1, 10, 18, 11)
    now = datetime.datetime.now()
    if now>date:
        welcome.configure(text="sorry your trial is over:(")
        window.mainloop()
demo()
accounts_frame = LabelFrame(window, text="الحسابات الشخصية" )
accounts_frame.grid(column=0, row=r)
usernamel = ttk.Label(accounts_frame, text="إسم المستخدم")
usernamel.grid(column=1, row=0)
username = Entry(accounts_frame,width=50)
username.grid(column=0, row=0)
passwordl = ttk.Label(accounts_frame, text='كلمة السر')
passwordl.grid(row=1, column=1)
password = Entry(accounts_frame,width=50)
password.grid(row=1, column=0)
error = Label(accounts_frame)
error.grid(column=0, row=3)
sender = ftest.RequestSenderBot(0)
acc=False
f=False
window.title='Demo'

def add_account():
    global sender,acc
    try:
        x = sender.login(username.get(), password.get())
    except:
        counter.configure(text='make sure you are connected to the internet')

    #x = sender.login(username.get(), password.get())
    print(x)
    if x == 0:
        error.configure(text='تم التسجيل بنجاح')
        timer_frame.grid(column=0, row=3)
        acc=True
    elif x == 1:
        error.configure(text='فشلت العملية تحقق من الاسم و كلمة المرور')
    else:
        error.configure(text="انت متصل بالفعل")
        acc=True
    if acc and f:
        start1['state'] = tkinter.NORMAL
    return sender


#add_account = ttk.Button(accounts_frame, text="أضف", command=add_account)add_account.grid(row=2, column=0)
freinds_frame = ttk.Labelframe(window, text=" الأصدقاء")
freinds_frame.grid(column=0, row=2)
#def add():
#    global sender
#    x = sender.add_friend(frname.get())
#    errors.configure(text=x)
#add_f = ttk.Button(freinds_frame, text="أضف", command=add)
trl1 = ttk.Label(freinds_frame, text="مسار الملف ")
trl1.grid(column=2, row=0)
var=StringVar()
tr12 = Entry(freinds_frame)
tr12.grid(column=1, row=0)
trl = ttk.Label(freinds_frame)
trl.grid(column=0, row=1)
file=''
ids=[]
stopped_id={'name':'','p':'','file':'','id':0}
def open_file():
    global ids,file
    tr12.delete(0, END)
    file=filedialog.askopenfilename()
    tr12.delete(0, END)
    tr12.insert(0,file)
def open1():
    global f,ids
    #global file
    file=tr12.get()
    if file=='':
        trl.configure(text="اختر الملف",background='blue')
        f=False
        return

    if file.endswith("txt"):
        try:
            w = open(file, 'r')
            x = w.read()
            ids = x.split()
            f=True
            stopped_id["file"]=file


        except:
            trl.configure(text="الملف خطأ "+file, background='blue')
            print("open")


    else:
        trl.configure(text="ملف غير مناسب ", background='blue')

force_stop=False
def truing():
    x=counter['text']
    if x=='stopped':
        counter.configure(text='operating')
    else:
        counter.configure(text='stopped')

def threaded():
    global stop
    if start1['text'] == 'start':
        print('should be stop')
        threaded=threading.Thread(target=add_from_file)
        threaded.start()

        stop=False

    else:
        stop=True
        start1['text']='start'
        counter.configure(text='stopped')
        print('changed by button to start')
stop=False

def add_from_file():
    explain.delete(0.0, END)
    counter.configure(text='')
    global sender,t,f,stop
    global ids,stopped_id,acc
    start=0
    n,p= username.get(), password.get()
    if sender.username=='' and n!='' and p!='':
        add_account()
        print('add friend')
    elif sender.username==n and sender.password==p:
        print("continue")

    print(acc)
    if not acc:
        trl.configure(text="ادخل الاسم و كلمة السر الصحيحين")
        return
    print('a')
    if stopped_id['file'] != tr12.get():
        open1()
        print(' opened file')
    elif stopped_id['name']==n:
        start=stopped_id['id']
    else:
        open1()
        print('same file but user changed')
    if not f:
        print('f')
        return

    time=datetime.datetime.now()

    #timer=time.time()+c
    r = 5
    if len(ids)==0:
        trl.configure(text="ملف غير مناسب ", background='blue')

    r=1
    c=100
    if start==len(ids)-1:
        counter.configure(text='this file has been added to this account')
        start=0
    for i in range(start,len(ids)):
        d = datetime.timedelta(seconds=c)
        closing_time = time + d

        if stop:

            return
        c = close_after()
        id=ids[i]

        x = sender.add_friend(id)
        explain.insert(1.0,str(x)+'\n')
        percent=r/len(ids)
        pr['value']=pr['value']+percent*100
        pr.update()
        r=r+1
        stopped_id['id']=i
        if datetime.datetime.now()>=closing_time:
            start1['text']='start'

            counter.configure(text="انتهى الوقت المحدد")
            print('timeout')
            start1['text']='start'
            return





#t2=multiprocessing.Process(target=add_from_file)

timer_frame = ttk.Labelframe(freinds_frame, text='حدد وقتا لتوقف البرنامج')
timer_frame.grid(column=0, row=5,columnspan=5)
Label(timer_frame, text='اوقف العمل ما بعد').grid(column=5, row=0)

# mins=Spinbox(timer_frame,default='--')
# mins.grid(column=1,row=0)


sec1 = Spinbox(timer_frame, from_=0, to_=10000)
sec1.grid(column=4, row=0)
Label(timer_frame, text="الى").grid(column=3, row=0)
sec2 = Spinbox(timer_frame, from_=10, to_=10000)
sec2.grid(column=2, row=0)
counter = Label(window)
counter.grid(column=0, row=7, columnspan=10)
pr=ttk.Progressbar(timer_frame,orient='horizontal',length=200,mode='determinate')
pr.grid(column=0,row=4,columnspan=4)
pr['maximum']=100




def close_after():

    x = sec1.get()
    y = sec2.get()
    if x != 0 or y != '':
        s = int(x)
        s1 = int(y)
        if s < s1:
            c = random.randrange(s, s1)
        elif s > s1:
            c = random.randrange(s1, s)
        elif s1 == s and s != 0:
            c = random.randrange(0, s1)
        else:
            counter.configure(text="يجب ان يكون هناك فرق بين الرقمين")
            c=s
        print(c)

       # sec1.after(c, sender.close())

    else:
        counter.configure(text="choose numbers for time")
        c=1000
    return c
    #while c > 0:

      #  counter.configure(text= c)
      #  time.sleep(1)
      #  print(c)
      #  c = c - 1

    #t2.terminate()
t=StringVar()
t.set("start")
start1= Button(timer_frame, text='start', command=threaded)#,state=tkinter.DISABLED

start1.grid(column=0, row=0)

add_from_file1 = ttk.Button(freinds_frame, text=
"اختر ملف"   , command=open_file)
add_from_file1.grid(column=0, row=0)
explain=scrolledtext.ScrolledText(freinds_frame,width=105,height=10)
explain.grid(column=0,row=7,columnspan=4)

window.mainloop()
