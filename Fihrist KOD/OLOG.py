from tkinter import *
import os
from shutil import copyfile
import sqlite3
from tkinter import ttk
#import tkinter as tk
from tkinter import filedialog

Profile = {1:""}

def register2():
    global register2_screen
    register2_screen = Toplevel(main2_screen)
    register2_screen.title("Kayıt Ekranı")
    register2_screen.geometry("600x600")

    global username2
    global password2
    global username2_entry
    global password2_entry
    username2 = StringVar()
    password2 = StringVar()

    Label(register2_screen, text="Lütfen Kullanıcı Adı ve Şifre Belirleyiniz").pack()
    Label(register2_screen, text="").pack()
    username2_lable = Label(register2_screen, text="Kullanıcı Adı * ")
    username2_lable.pack()
    username2_entry = Entry(register2_screen, textvariable=username2)
    username2_entry.pack()
    password2_lable = Label(register2_screen, text="Şifre * ")
    password2_lable.pack()
    password2_entry = Entry(register2_screen, textvariable=password2, show='*')
    password2_entry.pack()
    Label(register2_screen, text="").pack()
    Button(register2_screen, text="Kayıt Ol", width=10, height=1, bg="yellow", command=register2_user).pack()




def login2():
    global login2_screen
    login2_screen = Toplevel(main2_screen)
    login2_screen.title("Giriş Ekranı")
    login2_screen.geometry("600x600")
    Label(login2_screen, text="Lütfen bilgilerinizi giriniz.").pack()
    Label(login2_screen, text="").pack()

    global username2_verify
    global password2_verify

    username2_verify = StringVar()
    password2_verify = StringVar()

    global username2_login_entry
    global password2_login_entry

    Label(login2_screen, text="Kullanıcı Adı * ").pack()
    username2_login_entry = Entry(login2_screen, textvariable=username2_verify)
    username2_login_entry.pack()
    Label(login2_screen, text="").pack()
    Label(login2_screen, text="Şifre * ").pack()
    password2_login_entry = Entry(login2_screen, textvariable=password2_verify, show='*')
    password2_login_entry.pack()
    Label(login2_screen, text="").pack()
    Button(login2_screen, text="Giriş Yap",bg="turquoise", width=10, height=1, command=login2_verify).pack()




def register2_user():
    username2_info = username2.get()
    password2_info = password2.get()

    file2 = open(username2_info, "w")
    file2.write(username2_info + "\n")
    file2.write(password2_info)
    file2.close()

    username2_entry.delete(0, END)
    password2_entry.delete(0, END)

    Label(register2_screen, text="Kayıt Başarılı", fg="green", font=("calibri", 11)).pack()




def login2_verify():
    username2 = username2_verify.get()
    password2 = password2_verify.get()
    username2_login_entry.delete(0, END)
    password2_login_entry.delete(0, END)

    list2_of_files = os.listdir()
    if username2 in list2_of_files:
        file2 = open(username2, "r")
        verify = file2.read().splitlines()
        if password2 in verify:
            login2_sucess()

        else:
            password2_not_recognised()

    else:
        user2_not_found()




def login2_sucess():
    global login2_success_screen
    login2_success_screen = Toplevel(login2_screen)
    login2_success_screen.title("Giriş Başarılı")
    login2_success_screen.geometry("300x300")
    Label(login2_success_screen, text="Giriş Başarılı").pack()
    Button(login2_success_screen, text="Tamam", bg="turquoise", command=O_screen).pack()




def password2_not_recognised():
    global password2_not_recog_screen
    password2_not_recog_screen = Toplevel(login2_screen)
    password2_not_recog_screen.title("Hata")
    password2_not_recog_screen.geometry("300x300")
    Label(password2_not_recog_screen, text="Şifre Hatalı ").pack()
    Button(password2_not_recog_screen, text="Tamam",bg="red" , command=delete2_password_not_recognised).pack()



def user2_not_found():
    global user2_not_found_screen
    user2_not_found_screen = Toplevel(login2_screen)
    user2_not_found_screen.title("Hata")
    user2_not_found_screen.geometry("300x300")
    Label(user2_not_found_screen, text="Kullanıcı Bulunamadı").pack()
    Button(user2_not_found_screen, text="Tamam",bg="red",command=delete2_user_not_found_screen).pack()




def delete2_login_success():
    login2_success_screen.destroy()


def delete2_password_not_recognised():
    password2_not_recog_screen.destroy()


def delete2_user_not_found_screen():
    user2_not_found_screen.destroy()




def main2_account_screen():
    global main2_screen
    main2_screen = Tk()
    main2_screen.geometry("600x600")
    main2_screen.title("Öğretmen Paneli Seçim Ekranı")
    Label(text="Öğretmen Ekranı Lütfen Seçim Yapınız", bg="yellow", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Giriş Yap",bg="turquoise", height="2", width="30", command=login2).pack()
    Label(text="").pack()
    Button(text="Kayıt Ol",bg="turquoise", height="2", width="30", command=register2).pack()

    main2_screen.mainloop()

def O_screen():
    global  oscreen
    login2_success_screen.destroy()
    login2_screen.destroy()
    oscreen = Tk()
    oscreen.geometry("600x600")
    oscreen.title("Öğretmen Seçim Paneli")

    Label(oscreen, text="Lütfen Seçim Yapınız.").pack()

    Button(oscreen , text="Öğrenci İşlemleri",bg="lightblue",height="5", width="50", command= Ogrenci_İs).pack()

    Button(oscreen , text="Ders İşlemleri", bg="lightblue" , height="5", width="50", command= ders_is2).pack()

    Button(oscreen , text="Sınıf İşlemleri",bg="lightblue", height="5", width="50",command= snfis2).pack()

    oscreen.mainloop()

def Ogrenci_İs():
    global ogrs2
    oscreen.destroy()
    ogrs2 = Tk()
    ogrs2.title("Öğrenci İşlemleri")
    ogrs2.geometry("900x650")

    uygulama = Frame(ogrs2)
    uygulama.grid()

    chek1 = Checkbutton(uygulama, text="Online Eğitime Katılıyor", onvalue=1, offvalue=0, height=5, width=20)
    chek1.grid(row=0, column=1, padx=550, pady=30)

    chek2 = Checkbutton(uygulama, text="Online Eğitime Katılmıyor", onvalue=1, offvalue=0, height=5, width=20)
    chek2.grid(row=1, column=1, padx=600)

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database1.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database1.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(ogrs2, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(ogrs2, text=" Ad Soyad : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(ogrs2, text="Telefon : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(ogrs2)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "E Mail: " + moreInfoSelect)

    # Add Title
    lblTitle = Label(ogrs2, text="")
    lblTitle.place(x=0, y=0, width=250)

    # Label & Entry name
    lblName = Label(ogrs2, text="Adınız Soyadınız:",fg="white",bg="gray")
    lblName.place(x=5, y=50, width=155)
    entryName = Entry(ogrs2)
    entryName.place(x=170, y=50, width=380)

    # Label & Entry Phone
    lblPhone = Label(ogrs2, text="Veli Telefon Numarası:",fg="white",bg="gray")
    lblPhone.place(x=5, y=80, width=155)
    entryPhone = Entry(ogrs2)
    entryPhone.place(x=170, y=80, width=380)

    # Label & Entry Photo
    lblPhoto = Label(ogrs2, text="Sınıfınız:",fg="white",bg="gray")
    lblPhoto.place(x=5, y=110, width=155)
    entryPhoto = Entry(ogrs2)
    entryPhoto.place(x=170, y=110, width=300)

    # More Info
    lblMore = Label(ogrs2, text="E mail:",fg="white",bg="gray")
    lblMore.place(x=5, y=140, width=155)
    entryMore = Entry(ogrs2)
    entryMore.place(x=170, y=140, width=380)

    # Command Button
    bAdd = Button(ogrs2, text="Kullanıcı Ekle",fg="black",bg="lightblue", command=add_customer)
    bAdd.place(x=5, y=170, width=155)

    bDelete = Button(ogrs2, text="Seçimi SİL", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(ogrs2, text="Geri Dön", fg="black",bg="lightblue", command=O_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(ogrs2, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(ogrs2, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(ogrs2, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="İsim Soyisim")
    tree.heading(3, text="Telefon")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database1.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    ogrs2.mainloop()

def ders_is2():
    global drs2
    oscreen.destroy()
    drs2= Tk()
    drs2.title("Ders İşlemleri")
    drs2.geometry("600x600")

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database2.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database2.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database2.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(drs2, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(drs2, text=" Ders Adı : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(drs2, text="Derslik Kapasitesi : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(drs2)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Öğretmen : " + moreInfoSelect)

    # Add Title
    lblTitle = Label(drs2, text="")
    lblTitle.place(x=0, y=0, width=250)


    # Command Button

    bDelete = Button(drs2, text="Seçimi SİL",  fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(drs2, text="Geri Dön", fg="black",bg="lightblue", command=O_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(drs2, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(drs2, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(drs2, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="Ders Adı")
    tree.heading(3, text="Derslik Kapasitesi")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database2.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    drs2.mainloop()

def snfis2():
    global snf2
    oscreen.destroy()
    snf2 = Tk()
    snf2.title("Sınıf İşlemleri")
    snf2.geometry("600x600")

    def add_customer():
        name = entryName.get()
        phone = entryPhone.get()
        more = entryMore.get()

        # Create connection
        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        # Insert data
        cur.execute('''INSERT INTO customers (`name` , `phone`, `moreinfo`) VALUES (?,?,?)''', (name, phone, more))
        # commit connection
        conn.commit()
        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers order by id desc")
        select = list(select)
        tree.insert('', END, values=select[0])
        # Photo profile
        filename = entryPhoto.get()
        ext = filename.split(".")
        id = select[0][0]

        conn.close()

    def delete_customer():
        idSelect = tree.item(tree.selection())['values'][0]
        conn = sqlite3.connect("database3.db")
        cur = conn.cursor()
        delete = cur.execute("delete from customers where id = {}".format(idSelect))
        conn.commit()
        conn.close()
        tree.delete(tree.selection())

    def sortByName():
        # clear the treeview
        for i in tree.get_children():
            tree.delete(i)
        # create connection
        conn = sqlite3.connect("database3.db")
        cur = conn.cursor()
        select = cur.execute("select*from customers order by `name` asc")
        conn.commit()
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def SearchByName(event):
        for i in tree.get_children():
            tree.delete(i)

        name = entrySearchByName.get()

        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `name` = (?) ", (name,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)

        conn.close()

    def SearchByPhone(event):
        for i in tree.get_children():
            tree.delete(i)

        phone = entrySearchByPhone.get()

        conn = sqlite3.connect('database3.db')
        cur = conn.cursor()
        select = cur.execute("SELECT*FROM customers where `phone` = (?) ", (phone,))
        conn.commit()
        select = list(select)
        for row in select:
            tree.insert('', END, values=row)
        conn.close()

    def treeActionSelect(event):
        # load image

        idSelect = tree.item(tree.selection())['values'][0]
        nameSelect = tree.item(tree.selection())['values'][1]
        phoneSelect = tree.item(tree.selection())['values'][2]
        moreInfoSelect = tree.item(tree.selection())['values'][3]

        lid = Label(snf2, text="ID : " + str(idSelect))
        lid.place(x=110, y=350, width=50)
        lname = Label(snf2, text=" Sınıf İsmi : " + nameSelect)
        lname.place(x=110, y=380, width=150)
        lphone = Label(snf2, text="Sınıf Kapasitesi : " + str(phoneSelect))
        lphone.place(x=110, y=410, width=150)
        Tmore = Text(snf2)
        Tmore.place(x=260, y=360, width=280, height=100)
        Tmore.insert(END, "Sınıf Düzeyi : " + moreInfoSelect)

    # Add Title
    lblTitle = Label(snf2, text="")
    lblTitle.place(x=0, y=0, width=250)



    # Command Button


    bDelete = Button(snf2, text="Seçimi SİL", fg="black",bg="lightblue", command=delete_customer)
    bDelete.place(x=5, y=205, width=155)

    bSort = Button(snf2, text="Geri Dön", fg="black",bg="lightblue", command=O_screen)
    bSort.place(x=5, y=275, width=155)

    bExit = Button(snf2, text="Programdan Çık", fg="black",bg="lightblue")
    bExit.place(x=5, y=310, width=155)

    # Load Image
    # Add Treeview
    tree = ttk.Treeview(snf2, columns=(1, 2, 3), height=5, show="headings")
    tree.place(x=170, y=170, width=400, height=175)
    tree.bind("<<TreeviewSelect>>", treeActionSelect)
    # Add scrollbar
    vsb = ttk.Scrollbar(snf2, orient="vertical", command=tree.yview)
    vsb.place(x=530, y=200, height=175)
    tree.configure(yscrollcommand=vsb.set)

    # Add headings
    tree.heading(1, text="ID")
    tree.heading(2, text="Sınıf İsmi")
    tree.heading(3, text="Sınıf Kapasitesi")
    # Define column width
    tree.column(1, width=50)
    tree.column(2, width=100)
    tree.column(3, width=100)
    # Display data in treeview object
    conn = sqlite3.connect('database3.db')
    cur = conn.cursor()
    select = cur.execute("select*from customers")
    for row in select:
        tree.insert('', END, values=row)
    snf2.mainloop()


main2_account_screen()
