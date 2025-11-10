import sqlite3 as sq
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog
import csv

conn = sq.connect('Nokhbino.sqlite')
crs = conn.cursor()

# ایجاد جداول با ساختار صحیح
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
    def __init__(self, root):
        self.root = root
        self.root.title(title)
        self.root.geometry(size)
        
        # ایجاد فریم برای دکمه‌ها
        main_frame = tk.Frame(root)
        main_frame.pack(pady=20)
        
        btn701 = tk.Button(main_frame, text='701', width=20, height=2, command=self.open_701_window)
        btn701.grid(row=0, column=0, padx=10, pady=10)
        
        btn702 = tk.Button(main_frame, text='702', width=20, height=2, command=self.open_702_window)
        btn702.grid(row=0, column=1, padx=10, pady=10)
        
        btn703 = tk.Button(main_frame, text='703', width=20, height=2, command=self.open_703_window)
        btn703.grid(row=1, column=0, padx=10, pady=10)
        
        btn704 = tk.Button(main_frame, text='704', width=20, height=2, command=self.open_704_window)
        btn704.grid(row=1, column=1, padx=10, pady=10)
        
        btn801 = tk.Button(main_frame, text='801', width=20, height=2, command=self.open_801_window)
        btn801.grid(row=2, column=0, padx=10, pady=10)
        
        btn802 = tk.Button(main_frame, text='802', width=20, height=2, command=self.open_802_window)
        btn802.grid(row=2, column=1, padx=10, pady=10)
        
        btn901 = tk.Button(main_frame, text='901', width=20, height=2, command=self.open_901_window)
        btn901.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def create_class_window(self, window_title, table_name, has_defensive=False):
        window = tk.Toplevel(self.root)
        window.title(window_title)
        window.geometry("1300x500")
        
        # ایجاد Treeview
        if has_defensive:
            columns = ("ID", "Name", "Surname", "Art", "Sport", "English", "Technology", 
                      "Socialstudies", "Writing", "Dictation", "Literature", "Math", 
                      "Science", "Arabic", "Thinkinglifestyle", "Religious", "Quran", 
                      "Defensive", "Plusone")
        else:
            columns = ("ID", "Name", "Surname", "Art", "Sport", "English", "Technology", 
                      "Socialstudies", "Writing", "Dictation", "Literature", "Math", 
                      "Science", "Arabic", "Thinkinglifestyle", "Religious", "Quran", "Plusone")
        
        tree = ttk.Treeview(window, columns=columns, show='headings')
        
        # تعریف هدینگ‌ها
        headings = {
            "ID": "ایدی",
            "Name": "نام",
            "Surname": "نام خانوادگی",
            "Art": "هنر",
            "Sport": "ورزش",
            "English": "زبان",
            "Technology": "کار و فناوری",
            "Socialstudies": "مطالعات اجتماعی",
            "Writing": "نگارش",
            "Dictation": "املا",
            "Literature": "ادبیات فارسی",
            "Math": "ریاضی",
            "Science": "علوم",
            "Arabic": "عربی",
            "Thinkinglifestyle": "تفکر",
            "Religious": "پیام",
            "Quran": "قران",
            "Defensive": "امادگی دفاعی",
            "Plusone": "مثبت یک"
        }
        
        # تنظیم هدینگ‌ها و عرض ستون‌ها
        for col in columns:
            tree.heading(col, text=headings[col])
            tree.column(col, width=70)
        
        tree.column('ID', width=50)
        tree.column('Name', width=80)
        tree.column('Surname', width=100)
        tree.column('Socialstudies', width=100)
        tree.column('Technology', width=90)
        
        tree.pack(expand=True, fill='both', padx=10, pady=10)
        
        def load_data():
            for i in tree.get_children():
                tree.delete(i)
            crs.execute(f'SELECT * FROM {table_name}')
            for row in crs.fetchall():
                tree.insert('', 'end', values=row)
        
        def add_student():
            try:
                name = simpledialog.askstring('Input', 'نام دانش آموز را وارد کنید', parent=window)
                if not name:
                    return
                
                surname = simpledialog.askstring('Input', 'نام خانوادگی دانش آموز را وارد کنید', parent=window)
                if not surname:
                    return
                
                # دریافت نمرات
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
                
                scores = {}
                for subject_name, subject_code in subjects:
                    score = simpledialog.askfloat('Input', f'نمره {subject_name} را وارد کنید', parent=window, minvalue=0, maxvalue=20)
                    if score is None:
                        return
                    scores[subject_code] = score
                
                # درج در دیتابیس
                if has_defensive:
                    crs.execute(f'''INSERT INTO {table_name} 
                                (name, surname, art, sport, english, technology, socialstudies, 
                                 writing, dictation, literature, math, science, arabic, 
                                 thinkinglifestyle, religious, quran, defensive, plusone) 
                                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
                              (name, surname, scores['art'], scores['sport'], scores['english'],
                               scores['technology'], scores['socialstudies'], scores['writing'],
                               scores['dictation'], scores['literature'], scores['math'],
                               scores['science'], scores['arabic'], scores['thinkinglifestyle'],
                               scores['religious'], scores['quran'], scores['defensive'],
                               scores['plusone']))
                else:
                    crs.execute(f'''INSERT INTO {table_name} 
                                (name, surname, art, sport, english, technology, socialstudies, 
                                 writing, dictation, literature, math, science, arabic, 
                                 thinkinglifestyle, religious, quran, plusone) 
                                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
                              (name, surname, scores['art'], scores['sport'], scores['english'],
                               scores['technology'], scores['socialstudies'], scores['writing'],
                               scores['dictation'], scores['literature'], scores['math'],
                               scores['science'], scores['arabic'], scores['thinkinglifestyle'],
                               scores['religious'], scores['quran'], scores['plusone']))
                
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "دانش آموز با موفقیت اضافه شد")
                
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در اضافه کردن دانش آموز: {str(e)}")
        
        def update_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا', 'یک دانش آموز را انتخاب کنید')
                return
            
            item = tree.item(selected[0])
            student_id = item['values'][0]
            
            name = simpledialog.askstring("ویرایش", "نام جدید را وارد کنید:", parent=window)
            if not name:
                return
            
            surname = simpledialog.askstring("ویرایش", "نام خانوادگی جدید را وارد کنید:", parent=window)
            if not surname:
                return
            
            try:
                crs.execute(f"UPDATE {table_name} SET name=?, surname=? WHERE id=?", (name, surname, student_id))
                conn.commit()
                load_data()
                messagebox.showinfo("موفقیت", "اطلاعات دانش آموز با موفقیت ویرایش شد")
            except Exception as e:
                messagebox.showerror("خطا", f"خطا در ویرایش دانش آموز: {str(e)}")
        
        def delete_student():
            selected = tree.selection()
            if not selected:
                messagebox.showwarning('خطا', 'یک دانش آموز را انتخاب کنید')
                return
            
            if messagebox.askyesno("تایید", "آیا از حذف این دانش آموز مطمئن هستید؟"):
                item = tree.item(selected[0])
                student_id = item['values'][0]
                
                try:
                    crs.execute(f"DELETE FROM {table_name} WHERE id=?", (student_id,))
                    conn.commit()
                    load_data()
                    messagebox.showinfo("موفقیت", "دانش آموز با موفقیت حذف شد")
                except Exception as e:
                    messagebox.showerror("خطا", f"خطا در حذف دانش آموز: {str(e)}")
        
        def export_to_csv():
            filename = filedialog.asksaveasfilename(
                defaultextension=".csv",
                filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
                title="ذخیره به عنوان CSV"
            )
            if filename:
                try:
                    crs.execute(f'SELECT * FROM {table_name}')
                    rows = crs.fetchall()
                    
                    with open(filename, 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file)
                        # نوشتن هدر
                        writer.writerow([headings[col] for col in columns])
                        # نوشتن داده‌ها
                        writer.writerows(rows)
                    
                    messagebox.showinfo("موفقیت", f"داده‌ها با موفقیت در {filename} ذخیره شد")
                except Exception as e:
                    messagebox.showerror("خطا", f"خطا در ذخیره فایل: {str(e)}")
        
        # فریم برای دکمه‌ها
        frame_buttons = tk.Frame(window)
        frame_buttons.pack(pady=10)
        
        tk.Button(frame_buttons, text="اضافه کردن دانش آموز", command=add_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="ویرایش نام و نام خانوادگی", command=update_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="حذف دانش آموز", command=delete_student).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="خروجی CSV", command=export_to_csv).pack(side='left', padx=5)
        tk.Button(frame_buttons, text="بارگذاری مجدد", command=load_data).pack(side='left', padx=5)
        
        # بارگذاری اولیه داده‌ها
        load_data()
        
        return window

    def open_701_window(self):
        self.create_class_window("نمرات کلاس 701", "class701")

    def open_702_window(self):
        self.create_class_window("نمرات کلاس 702", "class702")

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

title = 'مدیریت نمرات مدرسه نخبینو'
size = '500x400'

if __name__ == "__main__":
    root = tk.Tk()
    project = ScoresProject(root)
    root.mainloop()
    conn.close()