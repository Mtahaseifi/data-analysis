import sqlite3 as sq
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import csv

conn = sq.connect('Nokhbino.sqlite')
crs = conn.cursor()

crs.execute('''
CREATE TABLE IF NOT EXISTS class701(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,        
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
            
)
''')
conn.commit()

crs.execute('''
CREATE TABLE IF NOT EXISTS class702(
    id INTEGER PRIMARY KEY,
    name TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
            
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class703(
    id INTEGER PRIMARY KEY,
    name TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
    
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class704(
    id INTEGER PRIMARY KEY,
    name TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
    
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class801(
    id INTEGER PRIMARY KEY,
    name TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
    
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class802(
    id INTEGER PRIMARY KEY,
    name TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    plusone TEXT               
            
    
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class901(
    id INTEGER PRIMARY KEY,
    name TEXT,
    art INTEGER,
    sport INTEGER,
    english INTEGER,
    technology INTEGER,
    socialstudies INTEGER,
    writing INTIGER,
    dictation INTEGER,
    literature INTEGER,
    math INTEGER,
    science INTEGER,
    arabic INTEGER,
    thinkinglifestyle INTEGER,
    religious INTEGER,
    quran INTEGER,
    defensive INTEGER,
    plusone TEXT               
            
)
''')
conn.commit()

class ScoresProject:
    def __init__(self,root):
       self.root = root
       self.root.title(title)
       self.root.geometry(size)
    #    self.root.configure(bg='')

       btn701 = tk.Button(root,text='701',width=20,command=self.open_701_window)
       btn701.pack(pady=10)

       btn702 = tk.Button(root,text='702',width=20,command=self.open_702_window)
       btn702.pack(pady=10)

       btn703 = tk.Button(root,text='703',width=20,command=self.open_703_window)
       btn703.pack(pady=10)

       btn704 = tk.Button(root,text='704',width=20,command=self.open_704_window)
       btn704.pack(pady=10)

       btn801 = tk.Button(root,text='801',width=20,command=self.open_801_window)
       btn801.pack(pady=10)

       btn802 = tk.Button(root,text='802',width=20,command=self.open_802_window)
       btn802.pack(pady=10)

       btn901 = tk.Button(root,text='901',width=20,command=self.open_901_window)
       btn901.pack(pady=10)

    def open_701_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 701")
        window.geometry("1200x400") 

        tree = ttk.Treeview(window, columns=("ID","Name",'Surname' ,"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran',  'plusone'), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text='نام')
        tree.heading('Surname',text='نام خانوادگی')
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=50)
        tree.column('Surname',width=70)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
        tree.pack(expand=True,fill='both')

        def load_data():
            for i in tree.get_children():
                tree.delete(i)
            crs.execute('SELECT * FROM class701')
            for row in crs.fetchall():
                tree.insert('','end',values=row) 

        load_data()

        def add_student():
            name1 = simpledialog.askstring('Input','نام دانش اموز را وارد کنید',parent=window)
            if not name1:
                return
            surname = simpledialog.askstring('Input','نام خانوادگی دانش اموز را وارد کنید',parent=window)
            if not surname:
                return          
            art_score = simpledialog.askfloat('Input','نمره ی هنر دانش اموز را وارد کنید',parent=window)
            if not art_score:
                return
            sport_score = simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window)
            if not sport_score:
                return
            english_score = simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window)
            if not english_score:
                return
            technology_score = simpledialog.askfloat('Input',' نمره ی کارو فناوری ',parent=window)
            if not technology_score:
                return
            socialstudies_score = simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window)
            if not socialstudies_score:
                return
            writing_score = simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window)
            if not writing_score:
                return
            dictation_score = simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window)
            if not dictation_score:
                return
            leterature_score = simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window)
            if not leterature_score:
                return
            math_score = simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را پیدا کنید',parent=window)
            if not math_score:
                return
            science_score = simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window)
            if not science_score:
                return
            arabic_score = simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window)
            if not arabic_score:
                return
            thinklifestyle_score = simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window)
            if not thinklifestyle_score:
                return
            religious_score = simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window)
            if not religious_score:
                return
            quran_score = simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window)
            if not quran_score:
                return
            plusone_score = simpledialog.askfloat('Input','نمره ی مثبت یک را وارد کنید',parent=window)
            if not plusone_score:
                return
            crs.execute('INSERT INTO class701 (name,surname,art,sport,english,technology,socialstudies,writing,dictation,leterature,math,science,arabic,thinklifestyle,religious,quran,plusone) VALUES(?,?,?)',(name1,surname,art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,leterature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score))
            conn.commit()
            load_data()

        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            item = tree.item(selected[0])
            cid, name_old, surname_old = item['values']

            name = simpledialog.askstring("Input", "نام جدید را وارد کنید : ", parent=window)
            if not name:
                return
            surname = simpledialog.askstring("Input", "نام خانوادگی جدید را وارد کنید",  parent=window)
            if not surname:
                return
            crs.execute("UPDATE class701 SET name=?, surname=? WHERE id=?", (name, surname, cid))
            conn.commit()
            load_data()

        # def commit_scores():

            
        #     crs.execute('INSERT INTO class701 (art,sport,english,technology,socialstudies,writing,dictation,leterature,math,science,arabic,thinklifestyle,religious,quran,plusone) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(art_score,sport_score,english_score,technology_score,socialstudies_score,writing_score,dictation_score,leterature_score,math_score,science_score,arabic_score,thinklifestyle_score,religious_score,quran_score,plusone_score))
        #     conn.commit()
        #     load_data()

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ",command=add_student ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش نام و نام خانوادگی دانش اموز",command=update_student ).pack(side='left', padx=5)
        # tk.Button(frame_buttons,text='ثبت نمرات دانش اموز',command=commit_scores).pack(side='left',padx=5)

    def open_702_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 702")
        window.geometry("1200x400")  
        tree = ttk.Treeview(window, columns=( 'plusone',"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', "Name","ID" ), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text="نام و نام خانوادگی")
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=100)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
 
        tree.pack(expand=True,fill='both')

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ", ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش دانش اموز", ).pack(side='left', padx=5)

    def open_703_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 703")
        window.geometry("1200x400")  


        tree = ttk.Treeview(window, columns=( 'plusone',"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', "Name","ID" ), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text="نام و نام خانوادگی")
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=100)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
 
        tree.pack(expand=True,fill='both')

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)
        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ", ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش دانش اموز", ).pack(side='left', padx=5)

    def open_704_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 704")
        window.geometry("1200x400")  

        tree = ttk.Treeview(window, columns=( 'plusone',"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', "Name","ID" ), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text="نام و نام خانوادگی")
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=100)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
 
        tree.pack(expand=True,fill='both')

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)
        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ", ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش دانش اموز", ).pack(side='left', padx=5)

    def open_801_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 801")
        window.geometry("1200x400") 

        tree = ttk.Treeview(window, columns=( 'plusone',"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', "Name","ID" ), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text="نام و نام خانوادگی")
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=100)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
 
        tree.pack(expand=True,fill='both')

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)
        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ", ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش دانش اموز", ).pack(side='left', padx=5)

    def open_802_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 802")
        window.geometry("1200x400")  

        tree = ttk.Treeview(window, columns=( 'plusone',"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', "Name","ID" ), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text="نام و نام خانوادگی")
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=100)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('plusone',width=70)
 
        tree.pack(expand=True,fill='both')

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)
        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ", ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش دانش اموز", ).pack(side='left', padx=5)

    def open_901_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 901")
        window.geometry("1200x400")  

        tree = ttk.Treeview(window, columns=( 'plusone','Defensive',"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', "Name","ID" ), show='headings')
        tree.heading("ID", text="ایدی")
        tree.heading("Name", text="نام و نام خانوادگی")
        tree.heading("Art", text="هنر")
        tree.heading("Sport", text="ورزش")
        tree.heading("English", text="زبان")
        tree.heading("Technology", text="کار و فناوری")
        tree.heading("Socialstudies", text="مطالعات اجتماعی")
        tree.heading("Writing", text="نگارش")
        tree.heading("Dictation", text="املا")
        tree.heading("Literature", text="ادبیات فارسی")
        tree.heading("Math", text="ریاضی")
        tree.heading("Science", text="علوم")
        tree.heading("Arabic", text="عربی")
        tree.heading("Thinkinglifestyle", text='تفکر')
        tree.heading("Religious", text="پیام")
        tree.heading("Quran", text="قران")
        tree.heading('Defensive',text='امادگی دفاعی')
        tree.heading("plusone", text="مثبت یک")

        tree.column('ID',width=50)
        tree.column('Name',width=100)
        tree.column('Art',width=50)
        tree.column('Sport',width=50)
        tree.column('English',width=50)
        tree.column('Technology',width=70)
        tree.column('Socialstudies',width=100)
        tree.column('Writing',width=50)
        tree.column('Dictation',width=50)
        tree.column('Literature',width=70)
        tree.column('Math',width=70)
        tree.column('Science',width=50)
        tree.column('Arabic',width=50)
        tree.column('Thinkinglifestyle',width=50)
        tree.column('Religious',width=50)
        tree.column('Quran',width=50)
        tree.column('Defensive',width=75)
        tree.column('plusone',width=70)

        tree.pack(expand=True,fill='both')

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)
        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ", ).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش دانش اموز", ).pack(side='left', padx=5)     

title = 'مدیریت نمرات مدرسه نخبینو'
size = '450x400'

root = tk.Tk()
project = ScoresProject(root)
root.mainloop()