from tkinter import *
from tkinter import ttk
import requests    #ต้องinstall request ก่อนถึงจะใช้ได้
url = 'https://notify-api.line.me/api/notify'
token = 'ZXxKJqNlf0Czdgh8ZwTZvstp46Qbq6chwzEQs534efe'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

#msg = 'hi title'
#r = requests.post(url, headers=headers, data = {'message':msg})
#print (r.text)



def calcu():

    laka = []
    list = []
    o = []
    t = []
    th = []
    f = []
    fi = []
    s = []
    se = []


    def elephantone():
        lion = int(laykanone.size())
        for i in range(lion):
            if laykanone.get(i) == 'บานพับเฟรมอลูมิเนียม':
                #print(i)
                laykantwo.delete(i)
                laykantwo.insert(i, len(o))
        #print(laykanone.get(1))
        #print(laykanone.get(2))
    def elephanttwo():
        tiger = int(laykanone.size())
        for i in range(tiger):
            if laykanone.get(i) == 'ขอบวงกบอลูมิเนียม':
                #print(i)
                laykantwo.delete(i)
                laykantwo.insert(i, len(t))

    def elephantthree():
        wolf = int(laykanone.size())
        for i in range(wolf):
            if laykanone.get(i) == 'มือจับเขาควาย':
                #print(i)
                laykantwo.delete(i)
                laykantwo.insert(i, len(th))

    def elephantfour():
        monkey = int(laykanone.size())
        for i in range(monkey):
            if laykanone.get(i) == 'ชุดประตูบานเลื่อน':
                j = i
                #print(j)
                laykantwo.delete(j)
                laykantwo.insert(j, len(f))

    def elephantfive():
        panda = int(laykanone.size())
        for i in range(panda):
            if laykanone.get(i) == 'ล้อมุ้งบานเลื่อน':
                j = i
                #print(j)
                laykantwo.delete(j)
                laykantwo.insert(j, len(fi))

    def elephantsix():
        bull = int(laykanone.size())
        for i in range(bull):
            if laykanone.get(i) == 'มือจับฝังอลูมิเนียม':
                j = i
                #print(j)
                laykantwo.delete(j)
                laykantwo.insert(j, len(s))

    def elephantseven():
        bear = int(laykanone.size())
        for i in range(bear):

            if laykanone.get(i) == 'ชุดมือจับมุ้งลวด':
                j = i
                print(j)
                laykantwo.delete(j)
                laykantwo.insert(j, len(se))



    def onebutton():
        o.append(1)
        title = 0
        laka.append(250)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('บานพับเฟรมอลูมิเนียม')
        #print(list)
        if len(o) == 1:
            laykanone.insert(END, 'บานพับเฟรมอลูมิเนียม')

            #laykantwo.insert(END, len(o))

    def twobutton():
        t.append(1)
        #print(len(t))
        title = 0
        laka.append(100)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('ขอบวงกบอลูมิเนียม')
        #print(list)
        if len(t) == 1:
            laykanone.insert(END, 'ขอบวงกบอลูมิเนียม')
            #laykantwo.insert(END, len(t))

    def threebutton():
        th.append(1)
        #print(len(t))
        title = 0
        laka.append(500)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('มือจับเขาควาย')
        #print(list)
        if len(th) == 1:
            laykanone.insert(END, 'มือจับเขาควาย')
            #laykantwo.insert(END, len(t))

    def fourbutton():
        f.append(1)
        title = 0
        laka.append(1500)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('ชุดประตูบานเลื่อน')
        #print(list)
        if len(f) == 1:
            laykanone.insert(END, 'ชุดประตูบานเลื่อน')

            #laykantwo.insert(END, len(o))

    def fivebutton():
        fi.append(1)
        #print(len(t))
        title = 0
        laka.append(160)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('ล้อมุ้งบานเลื่อน')
        #print(list)
        if len(fi) == 1:
            laykanone.insert(END, 'ล้อมุ้งบานเลื่อน')
            #laykantwo.insert(END, len(t))

    def sixbutton():
        s.append(1)
        #print(len(t))
        title = 0
        laka.append(380)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('มือจับฝังอลูมิเนียม')
        #print(list)
        if len(s) == 1:
            laykanone.insert(END, 'มือจับฝังอลูมิเนียม')
            #laykantwo.insert(END, len(t))

    def sevenbutton():
        se.append(1)
        #print(len(t))
        title = 0
        laka.append(50)
        #print(laka)
        for i in range(len(laka)):
            title = title + laka[i]
        #print(title)
        price.configure(text = title)
        list.append('ชุดมือจับมุ้งลวด')
        #print(list)
        if len(se) == 1:
            laykanone.insert(END, 'ชุดมือจับมุ้งลวด')
            #laykantwo.insert(END, len(t))

    def delete():
        dog = laykanone.curselection()
        print(dog)
        print(len(o))

        if laykanone.get(dog) == 'บานพับเฟรมอลูมิเนียม':
            print('come in')
            title = 0
            laka.remove(250)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(o) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                o.pop(1)
            else:
                print('else')
                o.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(o))

        elif laykanone.get(dog) == 'ขอบวงกบอลูมิเนียม':
            print('come in')
            title = 0
            laka.remove(100)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(t) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                t.pop(1)
            else:
                print('else')
                t.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(t))

        elif laykanone.get(dog) == 'มือจับเขาควาย':
            print('come in')
            title = 0
            laka.remove(500)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(th) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                th.pop(1)
            else:
                print('else')
                th.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(th))

        elif laykanone.get(dog) == 'ชุดประตูบานเลื่อน':
            print('come in')
            title = 0
            laka.remove(1500)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(f) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                f.pop(1)
            else:
                print('else')
                f.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(f))

        elif laykanone.get(dog) == 'ล้อมุ้งบานเลื่อน':
            print('come in')
            title = 0
            laka.remove(160)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(fi) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                fi.pop(1)
            else:
                print('else')
                fi.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(fi))

        elif laykanone.get(dog) == 'มือจับฝังอลูมิเนียม':
            print('come in')
            title = 0
            laka.remove(380)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(s) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                s.pop(1)
            else:
                print('else')
                s.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(s))

        elif laykanone.get(dog) == 'ชุดมือจับมุ้งลวด':
            print('come in')
            title = 0
            laka.remove(50)
            for i in range(len(laka)):
                title = title + laka[i]
            # print(title)
            price.configure(text=title)
            if len(se) == 1:
                print('if')

                laykanone.delete(dog)
                laykantwo.delete(dog)
                se.pop(1)
            else:
                print('else')
                se.pop(1)
                laykantwo.delete(dog)
                laykantwo.insert(dog,len(se))



    calcu = Tk()
    calcu.configure(bg='#FCF0C8')
    calcu.minsize(width=800, height=500)
    calcu.maxsize(width=800, height=500)
    calcu.title('คำนวนราคา')

    Label(master=calcu, text='คำนวนราคา             ', font=("Arial", 35), bg='#630A10', fg='white').place(x=0, y=0)
    Label(master=calcu, text='                                                                      ',
          font=("Arial", 35), bg='#630A10', fg='white').place(x=280, y=0)

    Label(master=calcu,text='ราคาทั้งหมด     ', font=("Arial", 35),bg='white').place(x=40,y=80)
    price = Label(master=calcu, text='0', font=("Arial", 35), bg='white')
    price.place(x=220, y=80)
    one = Button(master=calcu,text='บานพับเฟรมอลูมิเนียม', font=("Arial", 20),width = 12,bg='white', command = lambda:[onebutton(),elephantone()])
    one.place(x=20,y=150)
    two =Button(master=calcu, text='ขอบวงกบอลูมิเนียม', font=("Arial", 20),width = 12,bg='white', command = lambda:[twobutton(),elephanttwo()])
    two.place(x=230, y=150)
    three = Button(master=calcu, text='มือจับเขาควาย', font=("Arial", 20),width = 12,bg='white', command = lambda:[threebutton(),elephantthree()])
    three.place(x=20, y=220)
    four = Button(master=calcu, text='ชุดประตูบานเลื่อน', font=("Arial", 20),width = 12,bg='white', command = lambda:[fourbutton(),elephantfour()])
    four.place(x=230, y=220)
    five = Button(master=calcu, text='ล้อมุ้งบานเลื่อน', font=("Arial", 20),width = 12,bg='white', command = lambda:[fivebutton(),elephantfive()])
    five.place(x=20, y=290)
    six = Button(master=calcu, text='มือจับฝังอลูมิเนียม', font=("Arial", 20),width = 12,bg='white', command = lambda:[sixbutton(),elephantsix()])
    six.place(x=230, y=290)
    seven = Button(master=calcu, text='ชุดมือจับมุ้งลวด', font=("Arial", 20),width = 12,bg='white', command = lambda:[sevenbutton(),elephantseven()])
    seven.place(x=20, y=360)
    eight = Button(master=calcu, text='ลบรายการ', font=("Arial", 20), width=12,bg='white',command = delete)
    eight.place(x=230, y=360)

    Label(master=calcu,text='- รายการสินค้า -', font=("Arial", 20),bg='white',width = 16).place(x=500,y=80)
    laykanone = Listbox(master=calcu, bg='white', width=17, font=("Arial", 20))
    laykanone.place(x=500, y=118)
    laykantwo = Listbox(master=calcu, bg='white', width=5, font=("Arial", 20))
    laykantwo.place(x=685, y=118)


def promotion():
    promotion = Tk()
    promotion.configure(bg='#FCF0C8')
    promotion.minsize(width=800, height=500)
    promotion.maxsize(width=800, height=500)
    promotion.title('โปรโมชั่น')

    Label(master=promotion, text='โปรโมชั่น             ', font=("Arial", 35), bg='#630A10', fg='white').place(x=0, y=0)
    Label(master=promotion, text='                                                                      ',font=("Arial", 35), bg='#630A10', fg='white').place(x=280, y=0)

    Label(master=promotion,text='- โปรโมชั่น!!! ซื้อครบ500บาท ส่งฟรี(กรณีสั่งออนไลน์)', font=("Arial", 20),bg='#FCF0C8').place(x=40, y=70)


def addstackone():
    stack1.append(1)
    text = len(stack1)
    one_label.config(text = text)

def popstackone():
    if (len(stack1) == 1):
        one_label.config(text=len(stack8))
        stack1.clear()
        msg = 'บานพับเฟรมอลูมิเนียมหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)

        return
    stack1.pop(1)
    text = len(stack1)
    one_label.config(text = text)
    if (len(stack1) <= 3):
        msg = 'บานพับเฟรมอลูมิเนียมใกล้หมดเหลือ' + str(len(stack1))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)



def addstacktwo():
    stack2.append(1)
    text = len(stack2)
    two_label.config(text = text)

def popstacktwo():
    if (len(stack2) == 1):
        stack2.clear()
        two_label.config(text=len(stack8))
        msg = 'ขอบวงกบอลูมิเนียมหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)
        return
    stack2.pop(1)
    text = len(stack2)
    two_label.config(text = text)
    if (len(stack2) <= 3):
        msg = 'ขอบวงกบอลูมิเนียมใกล้หมดเหลือ' + str(len(stack2))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)

def addstackthree():
    stack3.append(1)
    text = len(stack3)
    three_label.config(text = text)

def popstackthree():
    if (len(stack3) == 1):
        three_label.config(text=len(stack8))
        stack3.clear()
        msg = 'มือจับเขาควายหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)
        return
    stack3.pop(1)
    text = len(stack3)
    three_label.config(text = text)
    if (len(stack3) <= 3):
        msg = 'มือจับเขาควายใกล้หมดเหลือ' + str(len(stack3))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)

def addstackfour():
    stack4.append(1)
    text = len(stack4)
    four_label.config(text = text)

def popstackfour():
    if (len(stack4) == 1):
        four_label.config(text=len(stack8))
        stack4.clear()
        msg = 'ชุดประตูบานเลื่อนหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)
        return
    stack4.pop(1)
    text = len(stack4)
    four_label.config(text = text)
    if (len(stack4) <= 3):
        msg = 'ชุดประตูบานเลื่อนใกล้หมดเหลือ' + str(len(stack4))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)

def addstackfive():
    stack5.append(1)
    text = len(stack5)
    five_label.config(text = text)

def popstackfive():
    if (len(stack5) == 1):
        stack5.clear()
        five_label.config(text=len(stack8))
        msg = 'ล้อมุ้งบานเลื่อนหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)
        return
    stack5.pop(1)
    text = len(stack5)
    five_label.config(text = text)
    if (len(stack5) <= 3):
        msg = 'ล้อมุ้งบานเลื่อนใกล้หมดเหลือ' + str(len(stack5))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)

def addstacksix():
    stack6.append(1)
    text = len(stack6)
    six_label.config(text = text)

def popstacksix():
    if (len(stack6) == 1):
        six_label.config(text=len(stack8))
        stack6.clear()
        msg = 'มือจับฝังอลูมิเนียมหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)
        return
    stack6.pop(1)
    text = len(stack6)
    six_label.config(text = text)
    if (len(stack6) <= 3):
        msg = 'มือจับฝังอลูมิเนียมใกล้หมดเหลือ' + str(len(stack6))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)


def addstackseven():
    stack7.append(1)
    text = len(stack7)
    seven_label.config(text = text)

def popstackseven():
    if (len(stack7) == 1):
        seven_label.config(text=len(stack8))
        stack7.clear()
        msg = 'ชุดมือจับมุ้งลวดหมดเเล้ว'
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)
        return
    stack7.pop(1)
    text = len(stack7)
    seven_label.config(text = text)
    if (len(stack7) <= 3):
        msg = 'ชุดมือจับมุ้งลวดใกล้หมดเหลือ' + str(len(stack7))
        r = requests.post(url, headers=headers, data={'message': msg})
        print(r.text)

def konharsinkar():
    ooo = konhar_555.get()
    if ooo == 'บานพับเฟรมอลูมิเนียม':
        text = len(stack1)
        konhar_label.configure(text = text)
    elif ooo == 'ขอบวงกบอลูมิเนียม':
        text = len(stack2)
        konhar_label.configure(text=text)
    elif ooo == 'มือจับเขาควาย':
        text = len(stack3)
        konhar_label.configure(text=text)
    elif ooo == 'ชุดประตูบานเลื่อน':
        text = len(stack4)
        konhar_label.configure(text=text)
    elif ooo == 'ล้อมุ้งบานเลื่อน':
        text = len(stack5)
        konhar_label.configure(text=text)
    elif ooo == 'มือจับฝังอลูมิเนียม':
        text = len(stack6)
        konhar_label.configure(text=text)
    elif ooo == 'ชุดมือจับมุ้งลวด':
        text = len(stack7)
        konhar_label.configure(text=text)


stack1 = [1,1,1,1,1]
stack2 = [1,1,1,1,1]
stack3 = [1,1,1,1,1]
stack4 = [1,1,1,1,1]
stack5 = [1,1,1,1,1]
stack6 = [1,1,1,1,1]
stack7 = [1,1,1,1,1]
stack8 = []



window = Tk()  ##สร้างตัวแปรwindow
window.title('ระบบจัดการสินค้า')
window.minsize(width=800, height=500)
window.maxsize(width=800, height=500)



main_frame = Frame(window,bg='#FCF0C8')
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set,bg='#FCF0C8')
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

second_frame.configure(bg='#FCF0C8')
window.configure(bg='#FCF0C8') ##เปลี่ยนสีพื้นหลัง

##ส่วนของUI

Label(master=second_frame, text='   ', font=("Arial", 20),bg='#FCF0C8').grid(row=1,column=1,padx=20,pady=20)
Label(master=window, text='เพิ่ม-ลดรายการสินค้า', font=("Arial", 35), bg='#630A10', fg='white').place(x=0,y=0)
Label(master=window, text='                                                                      ', font=("Arial", 35), bg='#630A10', fg='white').place(x=280,y=0)

logo = PhotoImage(file='logo.png')
Label(master=window,image=logo).place(x=500,y=80)



konhar_555 = Entry(font=("Arial", 10))
konhar_555.place(x=475,y=28)


Button(master=window,text='ค้นหา', font=("Arial", 15),bg='white',command = konharsinkar).place(x=620,y=10)
konhar_label = Label(master=window,text='0', font=("Arial", 15),width = 5)
konhar_label.place(x=670,y=20)



photo = PhotoImage(file='1.png')
Label(master=second_frame,image=photo).grid(row=6,column=0,padx=5,pady=5)
Label(master=second_frame, text='บานพับเฟรมอลูมิเนียม', font=("Arial", 20),bg='#FCF0C8').grid(row=6,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=6,column=1,padx=5,pady=5,sticky=SW)
one_label = Label(master=second_frame, text=len(stack1), font=("Arial", 20),bg='#FCF0C8')
one_label.grid(row=6,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstackone).grid(row=6,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstackone).grid(row=6,column=2,padx=5,pady=5,sticky=SW)

photo2 = PhotoImage(file='2.png')
Label(master=second_frame,image=photo2).grid(row=7,column=0,padx=5,pady=5)
Label(master=second_frame, text='ขอบวงกบอลูมิเนียม', font=("Arial", 20),bg='#FCF0C8').grid(row=7,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=7,column=1,padx=5,pady=5,sticky=SW)
two_label = Label(master=second_frame, text=len(stack2), font=("Arial", 20),bg='#FCF0C8')
two_label.grid(row=7,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstacktwo).grid(row=7,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstacktwo).grid(row=7,column=2,padx=5,pady=5,sticky=SW)

photo3 = PhotoImage(file='3.png')
Label(master=second_frame,image=photo3).grid(row=8,column=0,padx=5,pady=5)
Label(master=second_frame, text='มือจับเขาควาย', font=("Arial", 20),bg='#FCF0C8').grid(row=8,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=8,column=1,padx=5,pady=5,sticky=SW)
three_label = Label(master=second_frame, text=len(stack3), font=("Arial", 20),bg='#FCF0C8')
three_label.grid(row=8,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstackthree).grid(row=8,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstackthree).grid(row=8,column=2,padx=5,pady=5,sticky=SW)

photo4 = PhotoImage(file='4.png')
Label(master=second_frame,image=photo4).grid(row=9,column=0,padx=5,pady=5)
Label(master=second_frame, text='ชุดประตูบานเลื่อน', font=("Arial", 20),bg='#FCF0C8').grid(row=9,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=9,column=1,padx=5,pady=5,sticky=SW)
four_label = Label(master=second_frame, text=len(stack4), font=("Arial", 20),bg='#FCF0C8')
four_label.grid(row=9,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstackfour).grid(row=9,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstackfour).grid(row=9,column=2,padx=5,pady=5,sticky=SW)

photo5 = PhotoImage(file='5.png')
Label(master=second_frame,image=photo5).grid(row=10,column=0,padx=5,pady=5)
Label(master=second_frame, text='ล้อมุ้งบานเลื่อน', font=("Arial", 20),bg='#FCF0C8').grid(row=10,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=10,column=1,padx=5,pady=5,sticky=SW)
five_label = Label(master=second_frame, text=len(stack5), font=("Arial", 20),bg='#FCF0C8')
five_label.grid(row=10,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstackfive).grid(row=10,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstackfive).grid(row=10,column=2,padx=5,pady=5,sticky=SW)

photo6 = PhotoImage(file='6.png')
Label(master=second_frame,image=photo6).grid(row=11,column=0,padx=5,pady=5)
Label(master=second_frame, text='มือจับฝังอลูมิเนียม', font=("Arial", 20),bg='#FCF0C8').grid(row=11,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=11,column=1,padx=5,pady=5,sticky=SW)
six_label = Label(master=second_frame, text=len(stack6), font=("Arial", 20),bg='#FCF0C8')
six_label.grid(row=11,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstacksix).grid(row=11,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstacksix).grid(row=11,column=2,padx=5,pady=5,sticky=SW)

photo7 = PhotoImage(file='7.png')
Label(master=second_frame,image=photo7).grid(row=12,column=0,padx=5,pady=5)
Label(master=second_frame, text='ชุดมือจับมุ้งลวด', font=("Arial", 20),bg='#FCF0C8').grid(row=12,column=1,padx=5,pady=5,sticky=N)
Label(master=second_frame, text='เหลือ', font=("Arial", 20),bg='#FCF0C8').grid(row=12,column=1,padx=5,pady=5,sticky=SW)
seven_label = Label(master=second_frame, text=len(stack7), font=("Arial", 20),bg='#FCF0C8')
seven_label.grid(row=12,column=1,padx=5,pady=5,sticky=S)
Button(master=second_frame, text='เพิ่ม', font=("Arial", 20),bg='white',command = addstackseven).grid(row=12,column=1,padx=5,pady=5,sticky=SE)
Button(master=second_frame, text='ลด', font=("Arial", 20),bg='white',command = popstackseven).grid(row=12,column=2,padx=5,pady=5,sticky=SW)

Button(master=window,text='       คำนวนราคา       ', font=("Arial", 20), command = calcu,bg='white').place(x=510,y=300)
Button(master=window,text='        โปรโมชั่น        ', font=("Arial", 20), command = promotion,bg='white').place(x=512,y=390)
window.mainloop()   ##ตัวที่ทำให้โปรแกรมที่เขียนมารัน


