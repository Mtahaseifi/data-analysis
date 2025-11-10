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
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    plusone REAL               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class702(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    plusone REAL               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class703(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    plusone REAL               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class704(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    plusone REAL               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class801(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    plusone REAL               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class802(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    plusone REAL               
)
''')

crs.execute('''
CREATE TABLE IF NOT EXISTS class901(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    art REAL,
    sport REAL,
    english REAL,
    technology REAL,
    socialstudies REAL,
    writing REAL,
    dictation REAL,
    literature REAL,
    math REAL,
    science REAL,
    arabic REAL,
    thinkinglifestyle REAL,
    religious REAL,
    quran REAL,
    defensive REAL,
    plusone REAL               
)
''')
conn.commit()

class ScoresProject:
    def __init__(self,root):
       self.root = root
       self.root.title(title)
       self.root.geometry(size)

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
            if art_score is None:
                return
            sport_score = simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window)
            if sport_score is None:
                return
            english_score = simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window)
            if english_score is None:
                return
            technology_score = simpledialog.askfloat('Input',' نمره ی کارو فناوری ',parent=window)
            if technology_score is None:
                return
            socialstudies_score = simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window)
            if socialstudies_score is None:
                return
            writing_score = simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window)
            if writing_score is None:
                return
            dictation_score = simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window)
            if dictation_score is None:
                return
            literature_score = simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window)
            if literature_score is None:
                return
            math_score = simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را پیدا کنید',parent=window)
            if math_score is None:
                return
            science_score = simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window)
            if science_score is None:
                return
            arabic_score = simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window)
            if arabic_score is None:
                return
            thinklifestyle_score = simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window)
            if thinklifestyle_score is None:
                return
            religious_score = simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window)
            if religious_score is None:
                return
            quran_score = simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window)
            if quran_score is None:
                return
            plusone_score = simpledialog.askfloat('Input','نمره ی مثبت یک را وارد کنید',parent=window)
            if plusone_score is None:
                return
            
            try:
                crs.execute('''INSERT INTO class701 
                            (name, surname, art, sport, english, technology, socialstudies, 
                             writing, dictation, literature, math, science, arabic, 
                             thinkinglifestyle, religious, quran, plusone) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                          (name1, surname, art_score, sport_score, english_score, technology_score, 
                           socialstudies_score, writing_score, dictation_score, literature_score, 
                           math_score, science_score, arabic_score, thinklifestyle_score, 
                           religious_score, quran_score, plusone_score))
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "دانش آموز با موفقیت اضافه شد")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در اضافه کردن دانش آموز: {str(e)}")

        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            item = tree.item(selected[0])
            cid = item['values'][0]

            name = simpledialog.askstring("Input", "نام جدید را وارد کنید : ", parent=window)
            if not name:
                return
            surname = simpledialog.askstring("Input", "نام خانوادگی جدید را وارد کنید",  parent=window)
            if not surname:
                return
            
            try:
                crs.execute("UPDATE class701 SET name=?, surname=? WHERE id=?", (name, surname, cid))
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "اطلاعات دانش آموز با موفقیت ویرایش شد")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در ویرایش دانش آموز: {str(e)}")

        def delete_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            
            if messagebox.askyesno("تایید", "آیا از حذف این دانش آموز مطمئن هستید؟"):
                item = tree.item(selected[0])
                student_id = item['values'][0]
                
                try:
                    crs.execute("DELETE FROM class701 WHERE id=?", (student_id,))
                    conn.commit()
                    load_data()
                    messagebox.showinfo("موفقیت", "دانش آموز با موفقیت حذف شد")
                except Exception as e:
                    messagebox.showerror("خطا", f"خطا در حذف دانش آموز: {str(e)}")

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ",command=add_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش نام و نام خانوادگی دانش اموز",command=update_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="حذف دانش اموز",command=delete_student).pack(side='left', padx=5)

    def open_702_window(self):
        window = tk.Toplevel(self.root)
        window.title("نمرات کلاس 702")
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
            crs.execute('SELECT * FROM class702')
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
            if art_score is None:
                return
            sport_score = simpledialog.askfloat('Input','نمره ی ورزش دانش اموز را وارد کنید',parent=window)
            if sport_score is None:
                return
            english_score = simpledialog.askfloat('Input','نمره ی زبان دانش اموز را وارد کنید',parent=window)
            if english_score is None:
                return
            technology_score = simpledialog.askfloat('Input',' نمره ی کارو فناوری ',parent=window)
            if technology_score is None:
                return
            socialstudies_score = simpledialog.askfloat('Input','نمره ی مطالعات اجتماعی دانش موز را وارد کنید',parent=window)
            if socialstudies_score is None:
                return
            writing_score = simpledialog.askfloat('Input','نمره ی نگارش دانش اموز را وارد کنید',parent=window)
            if writing_score is None:
                return
            dictation_score = simpledialog.askfloat('Input','نمره ی املا دانش اموز را وارد کنید',parent=window)
            if dictation_score is None:
                return
            literature_score = simpledialog.askfloat('Input','نمره ی ادبیات فارسی دانش اموز را وارد کنید',parent=window)
            if literature_score is None:
                return
            math_score = simpledialog.askfloat('Input','نمره ی ریاضی دانش اموز را پیدا کنید',parent=window)
            if math_score is None:
                return
            science_score = simpledialog.askfloat('Input','نمره ی علوم دانش اموز را وارد کنید',parent=window)
            if science_score is None:
                return
            arabic_score = simpledialog.askfloat('Input','نمره ی عربی دانش اموز را وارد کنید',parent=window)
            if arabic_score is None:
                return
            thinklifestyle_score = simpledialog.askfloat('Input','نمره ی تفکر و سبک زندگی دانش اموز را وارد کنید',parent=window)
            if thinklifestyle_score is None:
                return
            religious_score = simpledialog.askfloat('Input','نمره ی دینی دانش اموز را وارد کنید',parent=window)
            if religious_score is None:
                return
            quran_score = simpledialog.askfloat('Input','نمره ی قران دانش اموز را وارد کنید',parent=window)
            if quran_score is None:
                return
            plusone_score = simpledialog.askfloat('Input','نمره ی مثبت یک را وارد کنید',parent=window)
            if plusone_score is None:
                return
            
            try:
                crs.execute('''INSERT INTO class702 
                            (name, surname, art, sport, english, technology, socialstudies, 
                             writing, dictation, literature, math, science, arabic, 
                             thinkinglifestyle, religious, quran, plusone) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                          (name1, surname, art_score, sport_score, english_score, technology_score, 
                           socialstudies_score, writing_score, dictation_score, literature_score, 
                           math_score, science_score, arabic_score, thinklifestyle_score, 
                           religious_score, quran_score, plusone_score))
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "دانش آموز با موفقیت اضافه شد")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در اضافه کردن دانش آموز: {str(e)}")

        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            item = tree.item(selected[0])
            cid = item['values'][0]

            name = simpledialog.askstring("Input", "نام جدید را وارد کنید : ", parent=window)
            if not name:
                return
            surname = simpledialog.askstring("Input", "نام خانوادگی جدید را وارد کنید",  parent=window)
            if not surname:
                return
            
            try:
                crs.execute("UPDATE class702 SET name=?, surname=? WHERE id=?", (name, surname, cid))
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "اطلاعات دانش آموز با موفقیت ویرایش شد")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در ویرایش دانش آموز: {str(e)}")

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز ",command=add_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش نام و نام خانوادگی دانش اموز",command=update_student).pack(side='left', padx=5)

    # برای کلاس‌های دیگر هم به همین صورت ادامه دهید...
    def open_703_window(self):
        self.create_class_window("نمرات کلاس 703", "class703")

    def open_704_window(self):
        self.create_class_window("نمرات کلاس 704", "class704")

    def open_801_window(self):
        self.create_class_window("نمرات کلاس 801", "class801")

    def open_802_window(self):
        self.create_class_window("نمرات کلاس 802", "class802")

    def open_901_window(self):
        self.create_class_window("نمرات کلاس 901", "class901", has_defensive=True)

    def create_class_window(self, window_title, table_name, has_defensive=False):
        window = tk.Toplevel(self.root)
        window.title(window_title)
        window.geometry("1200x400")

        if has_defensive:
            columns = ("ID","Name",'Surname' ,"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', 'Defensive', 'plusone')
        else:
            columns = ("ID","Name",'Surname' ,"Art", "Sport", "English", 'Technology', 'Socialstudies', 'Writing', 'Dictation', 'Literature', 'Math', 'Science', 'Arabic', 'Thinkinglifestyle', 'Religious', 'Quran', 'plusone')
        
        tree = ttk.Treeview(window, columns=columns, show='headings')
        
        headings_config = {
            "ID": ("ایدی", 50),
            "Name": ("نام", 50),
            "Surname": ("نام خانوادگی", 70),
            "Art": ("هنر", 50),
            "Sport": ("ورزش", 50),
            "English": ("زبان", 50),
            "Technology": ("کار و فناوری", 70),
            "Socialstudies": ("مطالعات اجتماعی", 100),
            "Writing": ("نگارش", 50),
            "Dictation": ("املا", 50),
            "Literature": ("ادبیات فارسی", 70),
            "Math": ("ریاضی", 70),
            "Science": ("علوم", 50),
            "Arabic": ("عربی", 50),
            "Thinkinglifestyle": ("تفکر", 50),
            "Religious": ("پیام", 50),
            "Quran": ("قران", 50),
            "Defensive": ("امادگی دفاعی", 70),
            "plusone": ("مثبت یک", 70)
        }
        
        for col in columns:
            heading_text, width = headings_config[col]
            tree.heading(col, text=heading_text)
            tree.column(col, width=width)
        
        tree.pack(expand=True, fill='both')

        def load_data():
            for i in tree.get_children():
                tree.delete(i)
            crs.execute(f'SELECT * FROM {table_name}')
            for row in crs.fetchall():
                tree.insert('', 'end', values=row)

        load_data()

        def add_student():
            # دریافت اطلاعات پایه
            name1 = simpledialog.askstring('Input', 'نام دانش اموز را وارد کنید', parent=window)
            if not name1:
                return
            surname = simpledialog.askstring('Input', 'نام خانوادگی دانش اموز را وارد کنید', parent=window)
            if not surname:
                return

            # دریافت نمرات
            scores = {}
            subjects = [
                ("هنر", "art"),
                ("ورزش", "sport"),
                ("زبان انگلیسی", "english"),
                ("کار و فناوری", "technology"),
                ("مطالعات اجتماعی", "socialstudies"),
                ("نگارش", "writing"),
                ("املا", "dictation"),
                ("ادبیات فارسی", "literature"),
                ("ریاضی", "math"),
                ("علوم", "science"),
                ("عربی", "arabic"),
                ("تفکر و سبک زندگی", "thinkinglifestyle"),
                ("دینی", "religious"),
                ("قرآن", "quran")
            ]
            
            if has_defensive:
                subjects.append(("آمادگی دفاعی", "defensive"))
            
            subjects.append(("مثبت یک", "plusone"))

            for subject_name, field_name in subjects:
                score = simpledialog.askfloat('Input', f'نمره {subject_name} دانش اموز را وارد کنید', parent=window)
                if score is None:
                    return
                scores[field_name] = score

            # ساخت کوئری INSERT
            if has_defensive:
                crs.execute(f'''INSERT INTO {table_name} 
                            (name, surname, art, sport, english, technology, socialstudies, 
                             writing, dictation, literature, math, science, arabic, 
                             thinkinglifestyle, religious, quran, defensive, plusone) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                          (name1, surname, 
                           scores.get('art', 0), scores.get('sport', 0), scores.get('english', 0),
                           scores.get('technology', 0), scores.get('socialstudies', 0), scores.get('writing', 0),
                           scores.get('dictation', 0), scores.get('literature', 0), scores.get('math', 0),
                           scores.get('science', 0), scores.get('arabic', 0), scores.get('thinkinglifestyle', 0),
                           scores.get('religious', 0), scores.get('quran', 0), scores.get('defensive', 0),
                           scores.get('plusone', 0)))
            else:
                crs.execute(f'''INSERT INTO {table_name} 
                            (name, surname, art, sport, english, technology, socialstudies, 
                             writing, dictation, literature, math, science, arabic, 
                             thinkinglifestyle, religious, quran, plusone) 
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                          (name1, surname,
                           scores.get('art', 0), scores.get('sport', 0), scores.get('english', 0),
                           scores.get('technology', 0), scores.get('socialstudies', 0), scores.get('writing', 0),
                           scores.get('dictation', 0), scores.get('literature', 0), scores.get('math', 0),
                           scores.get('science', 0), scores.get('arabic', 0), scores.get('thinkinglifestyle', 0),
                           scores.get('religious', 0), scores.get('quran', 0), scores.get('plusone', 0)))
            
            conn.commit()
            load_data()
            messagebox.showinfo("موفقیت", "دانش آموز با موفقیت اضافه شد")

        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا','یک دانش اموز را انتخاب کنید')
                return
            item = tree.item(selected[0])
            cid = item['values'][0]

            name = simpledialog.askstring("Input", "نام جدید را وارد کنید : ", parent=window)
            if not name:
                return
            surname = simpledialog.askstring("Input", "نام خانوادگی جدید را وارد کنید", parent=window)
            if not surname:
                return
            
            try:
                crs.execute(f"UPDATE {table_name} SET name=?, surname=? WHERE id=?", (name, surname, cid))
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "اطلاعات دانش آموز با موفقیت ویرایش شد")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در ویرایش دانش آموز: {str(e)}")

        frame_buttons = tk.Frame(window)   
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="اضافه کردن دانش اموز", command=add_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش نام و نام خانوادگی", command=update_student).pack(side='left', padx=5)

title = 'مدیریت نمرات مدرسه نخبینو'
size = '450x400'

if __name__ == "__main__":
    root = tk.Tk()
    project = ScoresProject(root)
    root.mainloop()
    conn.close()