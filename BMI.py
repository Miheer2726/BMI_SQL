import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from datetime import datetime
from datetime import date
import datetime
import time
import mysql.connector
#======================================================================================================================================================
def f1():
	cal_window.deiconify()
	root.withdraw()
#======================================================================================================================================================

def f2():	
	root.deiconify()
	label_count.config(text="Count = " + str(count_records()))
	cal_window.withdraw()
#======================================================================================================================================================

def f3():
	convert_window.deiconify()
	cal_window.withdraw()
#======================================================================================================================================================
	
def f4():
	cal_window.deiconify()
	convert_window.withdraw()
#======================================================================================================================================================

def f5():
	ht = str(cal_window_ent_height.get())
	wt = str(cal_window_ent_weight.get())
	count1 = 0
	count2 = 0
	
	for h1 in ht:
		if h1 == ".":
			count1 += 1
	for w1 in wt:
		if w1 == ".":
			count2 +=1

	if(cal_window_ent_name.get()== "" or cal_window_ent_age.get()== "" or cal_window_ent_phone.get()== "" or cal_window_ent_height.get()=="" or cal_window_ent_weight.get()==""):
		showerror("Failure","Please fillout details ")
	elif (cal_window_ent_age.get().isdigit()==False or int(cal_window_ent_age.get())<= 0):
		showerror("Failure","Enter correct Age")
		cal_window_ent_age.delete(0, END)
	elif (len(cal_window_ent_name.get()) < 2) or (((cal_window_ent_name.get()).isalpha())==False):
		showerror("Failure","Enter correct Name")
		cal_window_ent_name.delete(0, END)
	elif(cal_window_ent_phone.get().isdigit()==False or len(cal_window_ent_phone.get())!=10 ):
		showerror("Failure","Enter correct Phone no")
		cal_window_ent_phone.delete(0, END)
	elif ((cal_window_ent_height.get()).replace(".","").isdigit()==False):
		showerror("Failure","Enter correct Height")
		cal_window_ent_height.delete(0, END)
	elif ((cal_window_ent_weight.get()).replace(".","").isdigit()==False):
		showerror("Failure","Enter correct Weight")
		cal_window_ent_weight.delete(0, END)
	elif count1 > 1:
		showerror("Failure", "Enter valid height")
		cal_window_ent_height.delete(0, END)
	elif count2 > 1:
		showerror("Failure", "Enter valid weight")
		cal_window_ent_weight.delete(0, END)
	elif (float(cal_window_ent_height.get())<=0 ):
		showerror("Failure","Height cannot be Zero")
		cal_window_ent_height.delete(0, END)
	elif (float(cal_window_ent_weight.get())<=0):
		showerror("Failure","Weight cannot be Zero")
		cal_window_ent_weight.delete(0, END)
	elif (float(cal_window_ent_height.get())>3):
		showerror("Failure","Enter Correct height")
		cal_window_ent_height.delete(0, END)
	elif (float(cal_window_ent_weight.get())>500):
		showerror("Failure","Enter Correct Weight")
		cal_window_ent_weight.delete(0, END)
	
	
	else:
		name=cal_window_ent_name.get()
		age=int(cal_window_ent_age.get())
		phone=cal_window_ent_phone.get()
		res = g.get()
		if res == 1:
			gender = "Male"
		else:
			gender = "Female"

		wt=float(cal_window_ent_weight.get())
		ht=float(cal_window_ent_height.get())
		BMI = round(wt / pow(ht, 2), 3)
		if (BMI < 18.5):
			showinfo("Your BMI is calculated", "BMI = " + str(round(BMI, 3)) + "\nYou are underweight :( ")
		elif (18.5 <= BMI < 25):
			showinfo("Your BMI is calculated", "BMI = " + str(round(BMI, 3)) + "\nYou are Normal :( ")
		elif (25 <= BMI < 30):
			showinfo("Your BMI is calculated", "BMI = " + str(round(BMI, 3)) + "\nYou are overweighted :( ")
		elif (30 <= BMI < 40):
			showinfo("Your BMI is calculated", "BMI = " + str(round(BMI, 3)) + "\nYou are obese :( ")
		elif (BMI >= 40):
			showinfo("Your BMI is calculated", "BMI = " + str(round(BMI, 3)) + "\nYou are morbidly obese :( ")
		cal_window_ent_name.delete(0, END)
		cal_window_ent_age.delete(0, END)
		cal_window_ent_phone.delete(0, END)
		cal_window_ent_height.delete(0, END)
		cal_window_ent_weight.delete(0, END)

		try:
			mydb = mysql.connector.connect(host="localhost", user="root", password="abc123")
			mycursor = mydb.cursor()

			mycursor.execute("CREATE DATABASE IF NOT EXISTS BMI_Database")
			mycursor.execute("use BMI_Database")
			mycursor.execute("CREATE TABLE IF NOT EXISTS BMI(name varchar(100), age tinyint unsigned, mobile varchar(10), gender ENUM('Male', 'Female'), height double, weight double, bmi double)")
				
			sql = "INSERT INTO BMI values(%s, %s, %s, %s, %s, %s, %s)"
			val = (name, age,phone, gender, ht, wt, BMI)
			mycursor.execute(sql, val)

			mydb.commit()
		except Exception as e:
			showerror("OOPS!", e)
		count_records()
	
#======================================================================================================================================================
	
def f6():
	if (convert_window_ent_feet.get()=="" or convert_window_ent_inch.get()==""):
		showerror("Failure","Please fillout details ")
	elif ((convert_window_ent_feet.get()).isdigit()==False):
		showerror("Failure","Enter correct Height in feet")
		convert_window_ent_feet.delete(0, END)
	elif ((convert_window_ent_inch.get()).isdigit()==False):
		showerror("Failure","Enter correct height in inch")
		convert_window_ent_inch.delete(0, END)
	elif ((int(convert_window_ent_feet.get()) <= 0) or (int(convert_window_ent_feet.get()) > 10)):
		showerror("Failure", "Feet should be in (1-10) ")
		convert_window_ent_feet.delete(0, END) 
	elif ((int(convert_window_ent_inch.get()) < 0) or (int(convert_window_ent_inch.get()) > 11)):				
		showerror("Failure", "Inch should be in (0-11)")
		convert_window_ent_inch.delete(0, END)
	else:
		ft=float(convert_window_ent_feet.get())
		inch=float(convert_window_ent_inch.get())
		height_in_metre = ft * 0.3048 + inch * 0.0254
		showinfo("Result", "Height in Metres : " + str(round(height_in_metre, 3)))
		convert_window_ent_feet.delete(0, END)
		convert_window_ent_inch.delete(0, END)			
			
#======================================================================================================================================================
def f7():
	view_window_data.configure(state ='normal')
	view_window.deiconify()
	root.withdraw()
	view_window_data.delete(1.0,END)
	info=""
	con=None
	try:
		mydb = mysql.connector.connect(host="localhost", user="root", password="abc123")
		mycursor=mydb.cursor()
		mycursor.execute("use bmi_database")
		mycursor.execute("select * from bmi")
		data=mycursor.fetchall()

		for d in data:
			info= info+" Name = "+ str(d[0]) +", Age = " + str(d[1]) + ", Mobile No = " +str(d[2]) +"\nGender =  " +str(d[3]) + " Height = " + str(d[4]) + " Weight = " + str(d[5]) +"\n========================================="
		view_window_data.configure(state ='normal') 
		view_window_data.insert(INSERT,info)
		view_window_data.configure(state ='disabled') 

	except Exception as e:
		showerror('Failure',e)

#======================================================================================================================================================
def f8():
	root.deiconify()
	view_window.withdraw()

#======================================================================================================================================================
def f9():
	today = date.today()
	# Textual month, day and year	
	d2 = today.strftime("%B %d, %Y")
	
	t = time.localtime()
	current_time = time.strftime("%H-%M-%S", t)
	
	a = "Data_" + str(d2) + "_" + str(current_time) + ".csv "
	file_location = f"'D:/SQL 2021/Project/BMI_DATA/{ a }'" 
	try:
		mydb = mysql.connector.connect(host="localhost", user="root", password="abc123")
		mycursor = mydb.cursor()
		mycursor.execute("use BMI_Database")
		mycursor.execute("select 'Name', 'Age', 'Mobile Number', 'Gender', 'Height', 'Weight', 'BMI' union all select * into OUTFILE" + file_location + "fields terminated by ',' from bmi")
		showinfo("Data Exported!", "Data has been saved in csv file")
	except Exception as e:
		showerror("OOPS!", e)
#======================================================================================================================================================
count = 0
def count_records():
	try:
		mydb = mysql.connector.connect(host="localhost", user="root", password="abc123")
		mycursor = mydb.cursor()

		mycursor.execute("use BMI_Database")
		mycursor.execute("select count(*) from bmi")
		count = mycursor.fetchall()
	except Exception as e:
		showerror("OOPS!", e)
	return count[0][0]

#======================================================================================================================================================

dt=datetime.datetime.now()
dt.hour
if dt.hour < 12:
	d3 = 'Good Morning'
elif 12 <= dt.hour < 18:
	d3 = 'Good Afternoon'
else:
	d3 = 'Good Evening'

#======================================================================================================================================================

splash=Tk()
splash.after(4000,splash.destroy)
splash.configure(background="red")
splash.wm_attributes('-fullscreen','true')
msg=Label(splash,text="BMI\n by \nMihir", font=('calibri',110,'bold'),fg='white',bg="red")
msg.pack()
splash.mainloop()
#======================================================================================================================================================
root=Tk()
root.title("BMI PROJECT")
root.geometry("650x650+400+25")

image1=PhotoImage(file=r"D:\SQL 2021\Project\mihir.gif")
Image_lb1=Label(root,image=image1)
Image_lb1.place(x=0,y=0)

label_dt=Label(root,text=dt,font=('Arial',20,'bold'),fg='red')
label_greet=Label(root,text= d3,font=('Arial',20,'bold'),fg='red')

btn_calbmi = Button(root,text="Calculate BMI",font=('Arial',20,'bold'),width=11,fg='red',borderwidth=9,command=f1)
btn_viewhist = Button(root,text="View History",font=('Arial',20,'bold'),width=11,fg='red',borderwidth=9,command=f7)
btn_expdata = Button(root,text="Export Data",font=('Arial',20,'bold'),width=11,fg='red',borderwidth=9,command=f9)

label_count=Label(root,text="Count : " + str(count_records()),font=('Arial',20,'bold'),fg='red')

label_dt.pack(pady=15)
label_greet.pack(pady=20)
btn_calbmi.pack(pady=10)
btn_viewhist.pack(pady=10)
btn_expdata.pack(pady=10)
label_count.pack(pady=15)
#======================================================================================================================================================

cal_window=Toplevel(root)
cal_window.title("Calculate BMI")
cal_window.geometry("700x600+400+25")
Image_lb2=Label(cal_window,image=image1)
Image_lb2.place(x=0,y=0)

cal_window_lbl_name= Label(cal_window,text="Enter Name",font=('Arial',20,'bold'))
cal_window_ent_name=Entry(cal_window,bd=5,font=('Arial',20,'bold'))

cal_window_lbl_age=Label(cal_window,text="Enter Age",font=('Arial',20,'bold'))
cal_window_ent_age=Entry(cal_window,bd=5,font=('Arial',20,'bold'))

cal_window_lbl_phone=Label(cal_window,text="Enter Phone",font=('Arial',20,'bold'))
cal_window_ent_phone=Entry(cal_window,bd=5,font=('Arial',20,'bold'))

cal_window_lbl_gender=Label(cal_window,text="Gender",font=('Arial',20,'bold'))

g=IntVar()
g.set(1)

male_rb = Radiobutton(cal_window, text = "Male", variable = g, value = 1, font = ('Arial', 20, 'bold'))
female_rb = Radiobutton(cal_window, text = "Female", variable = g, value = 2, font = ('Arial', 20, 'bold'))

cal_window_lbl_height=Label(cal_window,text="Enter Height in mtr ",font=('Arial',20,'bold'))
cal_window_ent_height=Entry(cal_window,bd=5,font=('Arial',20,'bold'))
cal_window_btn_convert=Button(cal_window,text="Convert",font=('Arial',20,'bold'),borderwidth=5,width=8,command=f3)

cal_window_lbl_weight=Label(cal_window,text="Enter Weight in kg",font=('Arial',20,'bold'))
cal_window_ent_weight=Entry(cal_window,bd=5,font=('Arial',20,'bold'))

cal_window_btn_cal=Button(cal_window,text="Calculate",font=('Arial',20,'bold'),borderwidth=9,command=f5)
cal_window_btn_back=Button(cal_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f2)

cal_window_lbl_name.place(x=15,y=25)
cal_window_ent_name.place(x=290,y=25)
cal_window_lbl_age.place(x=15,y=100)
cal_window_ent_age.place(x=290,y=100)
cal_window_lbl_phone.place(x=15,y=170)
cal_window_ent_phone.place(x=290,y=170)
cal_window_lbl_gender.place(x=15,y=230)
male_rb.place(x=290,y=230)
female_rb.place(x=400,y=230)
cal_window_lbl_height.place(x=15,y=280)
cal_window_ent_height.place(x=290,y=280)
cal_window_btn_convert.place(x=290,y=330)
cal_window_lbl_weight.place(x=15,y=410)
cal_window_ent_weight.place(x=290,y=410)
cal_window_btn_cal.place(x=10,y=470)
cal_window_btn_back.place(x=200,y=470)
cal_window.withdraw()

#======================================================================================================================================================
convert_window=Toplevel(root)
convert_window.title("Convert")
convert_window.geometry("700x600+400+25")
Image_lb2=Label(convert_window,image=image1)
Image_lb2.place(x=0,y=0)

convert_window_lbl_feet= Label(convert_window,text="Enter Height in Feet",font=('Arial',20,'bold'))
convert_window_ent_feet=Entry(convert_window,bd=5,font=('Arial',20,'bold'))
convert_window_lbl_inch=Label(convert_window,text="Enter Height in Inch",font=('Arial',20,'bold'))
convert_window_ent_inch=Entry(convert_window,bd=5,font=('Arial',20,'bold'))
convert_window_btn_convert=Button(convert_window,text="Convert",font=('Arial',20,'bold'),borderwidth=9,command=f6)
convert_window_btn_back=Button(convert_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f4)

convert_window_lbl_feet.pack(pady=10)
convert_window_ent_feet.pack(pady=10)
convert_window_lbl_inch.pack(pady=10)
convert_window_ent_inch.pack(pady=10)
convert_window_btn_convert.pack(pady=10)
convert_window_btn_back.pack(pady=10)

convert_window.withdraw()

#======================================================================================================================================================
view_window=Toplevel(root)
view_window.title("View Records")
view_window.geometry("700x600+400+25")
Image_lb3=Label(view_window,image=image1)
Image_lb3.place(x=0,y=0) 

view_window_data=ScrolledText(view_window,width=45,height=15,font=('Arial',18,'bold'), foreground = 'dark blue')
view_window_btn_back=Button(view_window,text="Back",font=('Arial',20,'bold'),borderwidth=9,command=f8)
view_window_data.pack(pady=10)
view_window_btn_back.pack(pady=10)
view_window.withdraw()

root.mainloop()

