from cProfile import label
from this import d
import tkinter as tk
from tkinter import *
from unittest import result
import numpy as np
import pandas as pd
from tkinter import *
from tkinter.filedialog import askopenfilename
import csv
from tkinter import ttk, filedialog
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.pyplot import subplot


root = tk.Tk()
root.title('CS111 Final Project: Pandas')
root.geometry("1300x700")
root.resizable(False, False)
# Create frame
frame1 = Frame(root)
frame1.pack(pady=1)
frame2 = Frame(root)
frame2.place(x=40,y=305)
frame3_frame = Frame(root)
frame3_frame.place(x=900,y=340)
frame3 = LabelFrame(frame3_frame)
frame3.pack()




def getdata():
    while True:
        try:
            x = my_tree.focus()
            y = my_tree.item(x, 'values')
            info = 'Name: {}\nClub: {}\nAge: {}\nPosition: {}\nMarket value: {}\nFPL value: {}\nNationality: {}\n\n'.\
                format(y[0], y[1], y[2], y[3], y[5], y[7], y[11])
            textbox.insert(END, info)
            return
        except IndexError:
            pass
            break

def cleardata():
    textbox.delete("1.0","end")


# create scrollbar for Text
scrollbar1 = Scrollbar(frame2)
# Text box to show infor:
textbox = Text(frame2, height=20, width=80,yscrollcommand=scrollbar1.set)
textbox.pack( side=LEFT)


scrollbar1.pack(side=RIGHT, fill=Y)
scrollbar1.configure(command=textbox.yview)

# create treeview scrollbar
    # Scrollbar fill Y
scrollbar2 = Scrollbar(frame1)
# add some style
style = ttk.Style()

# pick a theme
style.theme_use('default')

# configure the treeview color
style.configure("Treeview", background = '#D3D3D3',foreground = 'black', rowheight=25,fieldbackground='#D3D3D3')
# change selected color
style.map('Treeview',background=[('selected','#347083')])

# Create tree
my_tree = ttk.Treeview(frame1,yscrollcommand=scrollbar2.set,selectmode='extended')

# Create the TEXT to let them know where is table
text = Label(frame1,text='TABLE',font=('Helvetica','20'),height=8,width=70,bg='#347079')
text.pack()

# create striped row tags
my_tree.tag_configure('oddrow',background='white')
my_tree.tag_configure('evenrow',background='lightblue')

count = 0

flag = True
def tostring():
    df['age'] = df['age'].astype(str)
    df['position_cat'] = df['position_cat'].astype(str)
    df['market_value'] = df['market_value'].astype(str)
    df['page_views'] = df['page_views'].astype(str)
    df['fpl_value'] = df['fpl_value'].astype(str)
    df['fpl_sel'] = df['fpl_sel'].astype(str)
    df['fpl_points'] = df['fpl_points'].astype(str)
    df['region'] = df['region'].astype(str)
    df['age_cat'] = df['age_cat'].astype(str)
    df['club_id'] = df['club_id'].astype(str)
    df['big_club'] = df['big_club'].astype(str)
    df['new_signing'] = df['new_signing'].astype(str)
def tonumber():
    df['age'] = df['age'].astype(int)
    df['position_cat'] = df['position_cat'].astype(float)
    df['market_value'] = df['market_value'].astype(float)
    df['page_views'] = df['page_views'].astype(float)
    df['fpl_value'] = df['fpl_value'].astype(float)
    # df['fpl_sel'] = df['fpl_sel'].str.strip('%').astype(float)
    df['fpl_points'] = df['fpl_points'].astype(float)
    df['region'] = df['region'].astype(float)
    df['age_cat'] = df['age_cat'].astype(float)
    df['club_id'] = df['club_id'].astype(float)
    df['big_club'] = df['big_club'].astype(float)
    df['new_signing'] = df['new_signing'].astype(float)


# Open file & put into tree
def file_open():
    global df,count,df_rows,flag,flag_to_open
    filename = filedialog.askopenfilename(initialdir="C:/",title="Open a file",
                                          filetype=(("csv files", "*.csv"),
                                                    ("All Files", "*.*")))
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_csv(filename)
            flag = True
            tostring()

        except ValueError:
            my_label.config(text="File couldn't be opened. Try again!")
        except FileNotFoundError:
            my_label.config(text="File couldn't be found. Try again!")
    # Clear old tree before open a new one
    clear_tree()
    # Set up new tree
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"
    # Loop thru column list for headers
    for column in my_tree["column"]:
        if column == 'name':
            my_tree.column(column, width=155)
        elif column == 'club':
            my_tree.column(column, width=100)
        elif column == 'age':
            my_tree.column(column, width=30)
        elif column == 'position':
            my_tree.column(column, width=55)
        elif column == 'position_cat':
            my_tree.column(column, width=70)
        elif column == 'market_value':
            my_tree.column(column, width=80)
        elif column == 'page_views':
            my_tree.column(column, width=70)
        elif column == 'fpl_value':
            my_tree.column(column, width=60)
        elif column == 'fpl_sel':
            my_tree.column(column, width=60)
        elif column == 'fpl_points':
            my_tree.column(column, width=70)
        elif column == 'region':
            my_tree.column(column, width=47)
        elif column == 'nationality':
            my_tree.column(column, width=90)
        elif column == 'new_foreign':
            my_tree.column(column, width=80)
        elif column == 'age_cat':
            my_tree.column(column, width=50)
        elif column == 'club_id':
            my_tree.column(column, width=50)
        elif column == 'big_club':
            my_tree.column(column, width=60)
        elif column == 'new_signing':
            my_tree.column(column, width=75)
        my_tree.heading(column, text=column)
    
    # Put data in treeview
    df_rows = df.to_numpy().tolist()

    # Delete LABLE (TEXT)
    text.destroy()
    # Pack the treeview finally
    my_tree.pack(fill=Y, side=LEFT)
    scrollbar2.pack(side=RIGHT, fill=Y)
    scrollbar2.configure(command=my_tree.yview)
    for record in df_rows:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('oddrow',))

        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('evenrow',))
        # create increment counter
        count += 1


def clear_tree():
    for record in my_tree.get_children():
        my_tree.delete(record)

count1 = 0
# search and add data into TREEVIEW
def search():
    global count1,get_club,flag

    var1_receive = variable1.get()
    grouping = df.groupby(var1_receive)

    var2_receive = variable2.get()
    get_club = grouping.get_group(var2_receive)
    get_club = get_club.to_numpy().tolist()
    # clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    for record in get_club:
        if count1 % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count1, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('oddrow',))

        else:
            my_tree.insert(parent='', index='end', iid=count1, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('evenrow',))
        # create increment counter
        count1 += 1

count2 = 0
def reset():
    global count2,flag

    for record in my_tree.get_children():
        my_tree.delete(record)
    for record in df_rows:
        if count2 % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count2, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('oddrow',))

        else:
            my_tree.insert(parent='', index='end', iid=count2, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('evenrow',))
        # create increment counter
        count2 += 1
# Button of show and clear personal information of focused row
Button(frame3, text='Show Information', command=getdata).pack(padx=10,pady=10)
Button(frame3, text='Clear Information', command=cleardata).pack(padx=10,pady=10)


# Create 2 entry boxes for user to enter (with labels)
String1 = tk.StringVar()
String2 = tk.StringVar()


# funtion to open entry
def enter_column_name():
    global variable1,variable2,frame_enter
    frame_enter = Toplevel(root)
    frame_enter.title('GROUPING AND SORTING')
    frame_enter.geometry('400x200')
    frame_enter.resizable(False,False)
    # Create label frame
    label_frame_enter = LabelFrame(frame_enter, text='Enter column name to GROUP or SORT')
    label_frame_enter.pack(padx=10,pady=10)
    variable1 = Entry(label_frame_enter,font=('Helvetica',16), textvariable=String1)
    variable1.pack(padx=15,pady=15)
    # Button ENTER come to show BUTTON (Sort by or Show Grouping)
    btn_Enter = Button(label_frame_enter,text='--Next--',command=choose_option)
    btn_Enter.pack(pady=5)
    # Button reset
    btn_reset = Button(frame_enter,text='Reset',command=reset)

def choose_option():
    global variable1, variable2,frame_choose,frame_enter
    frame_enter.forget(frame_enter)
    frame_choose = Toplevel(root)
    frame_choose.title('GROUPING AND SORTING')
    frame_choose.geometry('400x200')
    frame_choose.resizable(False,False)
    label_frame_choose = LabelFrame(frame_choose, text='CHOOSE OPTION')
    label_frame_choose.pack(padx=10, pady=10)
    # Button show SORTING
    btn_show_sorting = Button(label_frame_choose,text='SORTING',command=sort_value)
    btn_show_sorting.pack(padx=15,pady=8)
    # Button show step Grouping
    btn_show_grouping = Button(label_frame_choose,text='GROUPING',command=grouping_function)
    btn_show_grouping.pack(padx=15,pady=8)
    # Button back to enter column name
    btn_back_enter_cloumn = Button(label_frame_choose,text='BACK',command=back_funtion_to_enter_column_name)
    btn_back_enter_cloumn.pack(padx=15,pady=8)

# Function to BACK FUNCTION TO EN TER COLUMN NAME
def back_funtion_to_enter_column_name():
    global variable1, variable2, frame_enter,frame_choose
    frame_choose.forget(frame_choose)
    frame_enter = Toplevel(root)
    frame_enter.title('GROUPING AND SORTING')
    frame_enter.geometry('400x200')
    frame_enter.resizable(False,False)
    # Create label frame
    label_frame_enter = LabelFrame(frame_enter, text='Enter column name to GROUP or SORT')
    label_frame_enter.pack(padx=10, pady=10)
    variable1 = Entry(label_frame_enter, font=('Helvetica', 16), textvariable=String1)
    variable1.pack(padx=15, pady=15)
    # Button NEXT come to show BUTTON (Sort by or Show Grouping)
    btn_Enter = Button(label_frame_enter, text='--Next--', command=choose_option)
    btn_Enter.pack(pady=5)

# This is step after you choose GROUPING
def grouping_function():
    global variable1, variable2,frame_choose,frame_grouping
    frame_choose.forget(frame_choose)
    frame_grouping = Toplevel(root)
    frame_grouping.title('GROUPING')
    frame_grouping.geometry('400x200')
    frame_grouping.resizable(False,False)
    label_frame_grouping = LabelFrame(frame_grouping, text='GROUP YOU WANT TO SHOW')
    label_frame_grouping.pack(padx=10, pady=10)
    variable2 = Entry(label_frame_grouping,font=('Helvetica',16), textvariable=String2)
    variable2.pack(padx=15,pady=15)
    Button(label_frame_grouping, text="Show Grouping", command=search).pack(pady=5)
    # Button to back the step before
    btn_back = Button(frame_grouping,text='Back',command=back_funtion_to_choose_option)
    btn_back.pack(padx=15)
    # BACK TO MAIN DATA
    button_to_back = Button(frame_grouping, text='Reset', command=reset)
    button_to_back.pack(pady=5)
    # BUTTON to sort after use Button (SHOW GROUPING)
    btn_sort = Button(frame_grouping, text='SORT', command=sort_after_grouping1)
    btn_sort.place(x=350,y=18)

# Funtion to BACK FUNCTION TO CHOOSE OPTION
def back_funtion_to_choose_option():
    global variable1, variable2, frame_choose, frame_enter,frame_grouping
    frame_grouping.forget(frame_grouping)
    frame_choose = Toplevel(root)
    frame_choose.title('GROUPING AND SORTING')
    frame_choose.geometry('400x200')
    frame_choose.resizable(False,False)
    label_frame_choose = LabelFrame(frame_choose, text='CHOOSE OPTION')
    label_frame_choose.pack(padx=10, pady=10)
    # Button show SORTING
    btn_show_sorting = Button(label_frame_choose, text='SORTING', command=sort_value)
    btn_show_sorting.pack(padx=15, pady=8)
    # Button show step Grouping
    btn_show_grouping = Button(label_frame_choose, text='GROUPING', command=grouping_function)
    btn_show_grouping.pack(padx=15, pady=8)
    # Button back to enter column name
    btn_back_enter_cloumn = Button(label_frame_choose, text='BACK', command=back_funtion_to_enter_column_name)
    btn_back_enter_cloumn.pack(padx=15, pady=8)
count3 = 0
# Sort function
def sort_value():
    global count3,flag
    tonumber()
    # Just sort with Variable1(này là chỉ sort cột) get
    var1_receive = variable1.get()
    if var1_receive == 'club':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        enter_column_name()
    elif var1_receive == 'name':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        enter_column_name()
    elif var1_receive == 'position':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        enter_column_name()
    elif var1_receive == 'nationality':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        enter_column_name()

    df_sort = df.sort_values(by=var1_receive, ascending=True)
    df_sort = df_sort.to_numpy().tolist()
    # clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    for record in df_sort:
        if count3 % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count3, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('oddrow',))

        else:
            my_tree.insert(parent='', index='end', iid=count3, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('evenrow',))
        # create increment counter
        count3 += 1

count4 = 0
String3 = StringVar()
# SORT by GROUPING
def sort_after_grouping1():
    global frame_grouping,var_3,frame_sort_grouping,flag
    tonumber()
    frame_grouping.forget(frame_grouping)
    frame_sort_grouping = Toplevel(root)
    frame_sort_grouping.title('SORTING')
    frame_sort_grouping.geometry('400x200')
    frame_sort_grouping.resizable(False,False)
    label_frame_sorting = LabelFrame(frame_sort_grouping, text='Enter Data You Want To Sort')
    label_frame_sorting.pack(padx=10, pady=10)
    var_3 = Entry(label_frame_sorting, font=('Helvetica', 16), textvariable=String3)
    var_3.pack(padx=10,pady=10)
    # Button to sort after grouping
    final_button_to_sorting = Button(label_frame_sorting, text='Sorting',command=sort_after_grouping2)
    final_button_to_sorting.pack(padx=10,pady=10)
    # Button back to grouping function
    btn_back_gfunc= Button(frame_sort_grouping,text='Back',command=back_to_gfunc)
    btn_back_gfunc.pack()
    # BUTTON back the step before
    btn_back_bfstep = Button(frame_sort_grouping, text='Reset', command=back_to_bf_step)
    btn_back_bfstep.pack(padx=5,pady=5)
def back_to_bf_step():
    global count1, get_club, flag
    var1_receive = variable1.get()
    grouping = df.groupby(var1_receive)

    var2_receive = variable2.get()
    get_club = grouping.get_group(var2_receive)
    get_club = get_club.to_numpy().tolist()
    # clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    for record in get_club:
        if count1 % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count1, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('oddrow',))

        else:
            my_tree.insert(parent='', index='end', iid=count1, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('evenrow',))
        # create increment counter
        count1 += 1
def back_to_gfunc():
    global variable1, variable2, frame_choose, frame_grouping,frame_sort_grouping,flag
    frame_sort_grouping.destroy()
    frame_grouping = Toplevel(root)
    frame_grouping.title('GROUPING')
    frame_grouping.geometry('400x200')
    frame_grouping.resizable(False,False)
    label_frame_grouping = LabelFrame(frame_grouping, text='GROUP YOU WANT TO SHOW')
    label_frame_grouping.pack(padx=10, pady=10)
    variable2 = Entry(label_frame_grouping, font=('Helvetica', 16), textvariable=String2)
    variable2.pack(padx=15, pady=15)
    Button(label_frame_grouping, text="Show Grouping", command=search).pack(pady=5)
    # Button to back the step before
    btn_back = Button(frame_grouping, text='Back', command=back_funtion_to_choose_option)
    btn_back.pack(padx=15)
    # BACK TO MAIN DATA
    button_to_back = Button(frame_grouping, text='Reset', command=reset)
    button_to_back.pack(pady=5)
    # BUTTON to sort after use Button (SHOW GROUPING)
    btn_sort = Button(frame_grouping, text='SORT', command=sort_after_grouping1)
    btn_sort.place(x=350, y=18)

def sort_after_grouping2():
    global count4, flag,var_3,get_club,df_rows,variable2,variable1
    # # Just sort with Variable1(này là chỉ sort cột) get
    variable3=var_3.get()
    var1_receive = variable1.get()
    var_2 = variable2.get()
    df_sort = df.sort_values(by=var1_receive)
    grouping = df_sort.groupby(var1_receive)
    get_club = grouping.get_group(var_2)
    if variable3 == 'club':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        back_to_gfunc()
    elif variable3 == 'name':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        back_to_gfunc()
    elif variable3 == 'position':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        back_to_gfunc()
    elif variable3 == 'nationality':
        messagebox.showerror('Error', 'This can\'t sort\nPlease choose another')
        eback_to_gfunc()
    df_sort1 = get_club.sort_values(by=variable3,ascending=True)
    df_sort1 = df_sort1.to_numpy().tolist()
    #     clear the treeview
    for record in my_tree.get_children():
        my_tree.delete(record)
    for record in df_sort1:
        if count4 % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count4, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('oddrow',))

        else:
            my_tree.insert(parent='', index='end', iid=count4, text='',
                           values=(record[0], record[1], record[2], record[3]
                                   , record[4], record[5], record[6]
                                   , record[7], record[8], record[9]
                                   , record[10], record[11], record[12]
                                   , record[13], record[14], record[15]
                                   , record[16]), tags=('evenrow',))
        # create increment counter
        count4 += 1

Button(frame3,text='Open Grouping \nAnd Sorting Window',command=enter_column_name).pack(padx=10,pady=10)



#Statistic
def statistic():
    global variable1, variable2, statistic_main
    while True:
        try:
            tonumber()
            statistic_main = Toplevel(root)
            statistic_main.title('Descritive Statistic')
            statistic_main.geometry('450x420')
            statistic_main.resizable(False,False)
                # Create label frame
            statistic_frame = LabelFrame(statistic_main, text='Column you want to focus')
            statistic_frame.pack(padx=10,pady=10)
            variable1 = Entry(statistic_frame,font=('Helvetica',16), textvariable=String1)
            variable1.pack(padx=15,pady=15)
            statistic_frame1 = LabelFrame(statistic_main, text='Data you want to show')
            statistic_frame1.pack(padx=10,pady=10)
            variable2 = Entry(statistic_frame1,font=('Helvetica',16), textvariable=String2)
            variable2.pack(padx=15,pady=15)
            #count
            Button(statistic_main, text="Count player", command=number_of_mem).pack(pady=5)
            # Button to find min max player
            Button(statistic_main, text='Find min', command=frame_for_min).pack(pady=5)
            Button(statistic_main, text='Find max', command=frame_for_max).pack(pady=5)
            #find mean
            Button(statistic_main, text='Mean', command=frame_for_mean).pack(pady=5)
            #find SUM market_value
            Button(statistic_main, text='Market value by club', command=frame_market_value).pack(pady=5)

            # BACK TO MAIN DATA
            button_to_back = Button(statistic_main, text='Reset', command=cleardata)
            button_to_back.pack(pady=5)
        except NameError:
            messagebox.showerror('Error','Please choose file first!')
        break
String7 = StringVar()
String8 = StringVar()
def frame_market_value():
    global variable1, variable2, statistic_main,frame_mv
    tonumber()
    statistic_main.forget(statistic_main)
    frame_mv = Toplevel(root)
    frame_mv.title('MARKET VALUE')
    frame_mv.geometry('350x300')
    frame_mv.resizable(False, False)
    # Create label frame
    label_frame_mv = LabelFrame(frame_mv, text='Column you want to focus')
    label_frame_mv.pack(padx=10, pady=10)
    variable7 = Entry(label_frame_mv, font=('Helvetica', 16), textvariable=String1)
    variable7.pack(padx=15, pady=15)
    label_frame_mv1 = LabelFrame(frame_mv, text='Data you want to show')
    label_frame_mv1.pack(padx=10, pady=10)
    variable8 = Entry(label_frame_mv1, font=('Helvetica', 16), textvariable=String2)
    variable8.pack(padx=15, pady=15)
    btn_do = Button(frame_mv,text='Show',command=market_value)
    btn_do.pack(padx=10,pady=10)
    #Btn Back
    btn_back = Button(frame_mv,text='Back',command=statistic_mv)
    btn_back.pack(padx=10,pady=10)
def market_value():
    global df,variable7,variable8
    df['market_value'] = df['market_value'].astype(float)
    var7_receive = variable7.get()
    var8_receive = variable8.get()
    value_market = df.groupby(var7_receive).agg(Sum=('market_value','sum'))
    if var8_receive == 'Arsenal':
        textbox.insert(END, value_market[:1])
        textbox.insert(END,'\n')
    elif var8_receive == 'Bournemouth':
        textbox.insert(END, value_market[1:2])
        textbox.insert(END,'\n')
    elif var8_receive == 'Brighton+and+Hove':
        textbox.insert(END, value_market[2:3])
        textbox.insert(END, '\n')
    elif var8_receive == 'Burnley':
        textbox.insert(END, value_market[3:4])
        textbox.insert(END, '\n')
    elif var8_receive == 'Chelsea':
        textbox.insert(END, value_market[4:5])
        textbox.insert(END, '\n')
    elif var8_receive == 'Crystal+Palace':
        textbox.insert(END, value_market[5:6])
        textbox.insert(END, '\n')
    elif var8_receive == 'Everton':
        textbox.insert(END, value_market[6:7])
        textbox.insert(END, '\n')
    elif var8_receive == 'Huddersfield':
        textbox.insert(END, value_market[7:8])
        textbox.insert(END, '\n')
    elif var8_receive == 'Leicester+City':
        textbox.insert(END, value_market[8:9])
        textbox.insert(END, '\n')
    elif var8_receive == 'Liverpool':
        textbox.insert(END, value_market[9:10])
        textbox.insert(END, '\n')
    elif var8_receive == 'Manchester+City':
        textbox.insert(END, value_market[10:11])
        textbox.insert(END, '\n')
    elif var8_receive == 'Manchester+United':
        textbox.insert(END, value_market[11:12])
        textbox.insert(END, '\n')
    elif var8_receive == 'Newcastle+United':
        textbox.insert(END, value_market[12:13])
        textbox.insert(END, '\n')
    elif var8_receive == 'Southampton':
        textbox.insert(END, value_market[13:14])
        textbox.insert(END, '\n')
    elif var8_receive == 'Stoke+City':
        textbox.insert(END, value_market[14:15])
        textbox.insert(END, '\n')
    elif var8_receive == 'Swansea':
        textbox.insert(END, value_market[15:16])
        textbox.insert(END, '\n')
    elif var8_receive == 'Tottenham':
        textbox.insert(END, value_market[16:17])
        textbox.insert(END, '\n')
    elif var8_receive == 'Watford':
        textbox.insert(END, value_market[17:18])
        textbox.insert(END, '\n')
    elif var8_receive == 'West+Brom':
        textbox.insert(END, value_market[18:19])
        textbox.insert(END, '\n')
    elif var8_receive == 'West+Ham':
        textbox.insert(END, value_market[19:20])
        textbox.insert(END, '\n')
    else:
        textbox.insert(END, value_market)
        textbox.insert(END, '\n')
    # textbox.insert(END, value_market)
def statistic_mv():
    global frame_mv
    frame_mv.forget(frame_mv)
    statistic()
String4 = StringVar()

def frame_for_min():
    global statistic_main,variable4,frame_min
    statistic_main.forget(statistic_main)
    frame_min = Toplevel(root)
    frame_min.title('Min')
    frame_min.geometry('300x200')
    frame_min.resizable(False, False)
    label_frame_min = LabelFrame(frame_min, text='CLUB YOU WANT TO SHOW')
    label_frame_min.pack(padx=10, pady=10)
    variable4 = Entry(label_frame_min, font=('Helvetica', 16), textvariable=String4)
    variable4.pack(padx=15, pady=15)
    btn_to_show = Button(frame_min,text='Show',command=min)
    btn_to_show.pack(padx=10,pady=10)
    # Button back
    btn_back = Button(frame_min,text='Back',command=statistic_min)
    btn_back.pack()

def min():
    global variable4
    tonumber()
    var1_receive = variable1.get()
    var2_receive = variable2.get()
    var4_receive = variable4.get()
    df_min = df.groupby(var1_receive).agg(Min=(var2_receive,'min'))
    if var4_receive == 'Arsenal':
        textbox.insert(END, df_min[:1])
        textbox.insert(END,'\n')
    elif var4_receive == 'Bournemouth':
        textbox.insert(END, df_min[1:2])
        textbox.insert(END,'\n')
    elif var4_receive == 'Brighton+and+Hove':
        textbox.insert(END, df_min[2:3])
        textbox.insert(END, '\n')
    elif var4_receive == 'Burnley':
        textbox.insert(END, df_min[3:4])
        textbox.insert(END, '\n')
    elif var4_receive == 'Chelsea':
        textbox.insert(END, df_min[4:5])
        textbox.insert(END, '\n')
    elif var4_receive == 'Crystal+Palace':
        textbox.insert(END, df_min[5:6])
        textbox.insert(END, '\n')
    elif var4_receive == 'Everton':
        textbox.insert(END, df_min[6:7])
        textbox.insert(END, '\n')
    elif var4_receive == 'Huddersfield':
        textbox.insert(END, df_min[7:8])
        textbox.insert(END, '\n')
    elif var4_receive == 'Leicester+City':
        textbox.insert(END, df_min[8:9])
        textbox.insert(END, '\n')
    elif var4_receive == 'Liverpool':
        textbox.insert(END, df_min[9:10])
        textbox.insert(END, '\n')
    elif var4_receive == 'Manchester+City':
        textbox.insert(END, df_min[10:11])
        textbox.insert(END, '\n')
    elif var4_receive == 'Manchester+United':
        textbox.insert(END, df_min[11:12])
        textbox.insert(END, '\n')
    elif var4_receive == 'Newcastle+United':
        textbox.insert(END, df_min[12:13])
        textbox.insert(END, '\n')
    elif var4_receive == 'Southampton':
        textbox.insert(END, df_min[13:14])
        textbox.insert(END, '\n')
    elif var4_receive == 'Stoke+City':
        textbox.insert(END, df_min[14:15])
        textbox.insert(END, '\n')
    elif var4_receive == 'Swansea':
        textbox.insert(END, df_min[15:16])
        textbox.insert(END, '\n')
    elif var4_receive == 'Tottenham':
        textbox.insert(END, df_min[16:17])
        textbox.insert(END, '\n')
    elif var4_receive == 'Watford':
        textbox.insert(END, df_min[17:18])
        textbox.insert(END, '\n')
    elif var4_receive == 'West+Brom':
        textbox.insert(END, df_min[18:19])
        textbox.insert(END, '\n')
    elif var4_receive == 'West+Ham':
        textbox.insert(END, df_min[19:20])
        textbox.insert(END, '\n')
    else:
        textbox.insert(END, df_min)
        textbox.insert(END, '\n')
# Function back Min
def statistic_min():
    global variable1,variable2,statistic_main,frame_min
    frame_min.forget(frame_min)
    statistic_main = Toplevel(root)
    statistic_main.title('Descritive Statistic')
    statistic_main.geometry('450x420')
    statistic_main.resizable(False,False)
        # Create label frame
    statistic_frame = LabelFrame(statistic_main, text='Enter Value 1')
    statistic_frame.pack(padx=10,pady=10)
    variable1 = Entry(statistic_frame,font=('Helvetica',16), textvariable=String1)
    variable1.pack(padx=15,pady=15)
    statistic_frame1 = LabelFrame(statistic_main, text='Enter Value 2')
    statistic_frame1.pack(padx=10,pady=10)
    variable2 = Entry(statistic_frame1,font=('Helvetica',16), textvariable=String2)
    variable2.pack(padx=15,pady=15)
    #count
    Button(statistic_main, text="Count player", command=number_of_mem).pack(pady=5)
    # Button to find min max player
    Button(statistic_main, text='Find min', command=frame_for_min).pack(pady=5)
    Button(statistic_main, text='Find max', command=frame_for_max).pack(pady=5)
    #find mean
    Button(statistic_main, text='Mean', command=mean_value).pack(pady=5)
    #find SUM market_value
    Button(statistic_main, text='Market value by club', command=market_value).pack(pady=5)

    # BACK TO MAIN DATA
    button_to_back = Button(statistic_main, text='Reset', command=cleardata)
    button_to_back.pack(pady=5)


String5 = StringVar()
def frame_for_max():
    global statistic_main,variable5,frame_max
    statistic_main.forget(statistic_main)
    frame_max = Toplevel(root)
    frame_max.title('Max')
    frame_max.geometry('300x200')
    frame_max.resizable(False, False)
    label_frame_max = LabelFrame(frame_max, text='CLUB YOU WANT TO SHOW')
    label_frame_max.pack(padx=10, pady=10)
    variable5 = Entry(label_frame_max, font=('Helvetica', 16), textvariable=String5)
    variable5.pack(padx=15, pady=15)
    btn_to_show = Button(frame_max, text='Show', command=max)
    btn_to_show.pack(padx=10, pady=10)
    # btn back
    btn_back = Button(frame_max,text='Back',command=statistic_max)
    btn_back.pack()

def max():
    global variable5
    tonumber()
    var1_receive = variable1.get()
    var2_receive = variable2.get()
    var5_receive = variable5.get()
    df_max = df.groupby(var1_receive).agg(Max=(var2_receive, 'max'))
    if var5_receive == 'Arsenal':
        textbox.insert(END, df_max[:1])
        textbox.insert(END, '\n')
    elif var5_receive == 'Bournemouth':
        textbox.insert(END, df_max[1:2])
        textbox.insert(END, '\n')
    elif var5_receive == 'Brighton+and+Hove':
        textbox.insert(END, df_max[2:3])
        textbox.insert(END, '\n')
    elif var5_receive == 'Burnley':
        textbox.insert(END, df_max[3:4])
        textbox.insert(END, '\n')
    elif var5_receive == 'Chelsea':
        textbox.insert(END, df_max[4:5])
        textbox.insert(END, '\n')
    elif var5_receive == 'Crystal+Palace':
        textbox.insert(END, df_max[5:6])
        textbox.insert(END, '\n')
    elif var5_receive == 'Everton':
        textbox.insert(END, df_max[6:7])
        textbox.insert(END, '\n')
    elif var5_receive == 'Huddersfield':
        textbox.insert(END, df_max[7:8])
        textbox.insert(END, '\n')
    elif var5_receive == 'Leicester+City':
        textbox.insert(END, df_max[8:9])
        textbox.insert(END, '\n')
    elif var5_receive == 'Liverpool':
        textbox.insert(END, df_max[9:10])
        textbox.insert(END, '\n')
    elif var5_receive == 'Manchester+City':
        textbox.insert(END, df_max[10:11])
        textbox.insert(END, '\n')
    elif var5_receive == 'Manchester+United':
        textbox.insert(END, df_max[11:12])
        textbox.insert(END, '\n')
    elif var5_receive == 'Newcastle+United':
        textbox.insert(END, df_max[12:13])
        textbox.insert(END, '\n')
    elif var5_receive == 'Southampton':
        textbox.insert(END, df_max[13:14])
        textbox.insert(END, '\n')
    elif var5_receive == 'Stoke+City':
        textbox.insert(END, df_max[14:15])
        textbox.insert(END, '\n')
    elif var5_receive == 'Swansea':
        textbox.insert(END, df_max[15:16])
        textbox.insert(END, '\n')
    elif var5_receive == 'Tottenham':
        textbox.insert(END, df_max[16:17])
        textbox.insert(END, '\n')
    elif var5_receive == 'Watford':
        textbox.insert(END, df_max[17:18])
        textbox.insert(END, '\n')
    elif var5_receive == 'West+Brom':
        textbox.insert(END, df_max[18:19])
        textbox.insert(END, '\n')
    elif var5_receive == 'West+Ham':
        textbox.insert(END, df_max[19:20])
        textbox.insert(END, '\n')
    else:
        textbox.insert(END, df_max)
        textbox.insert(END, '\n')

# Function back MAX
def statistic_max():
    global variable1,variable2,statistic_main,frame_max
    frame_max.forget(frame_max)
    statistic_main = Toplevel(root)
    statistic_main.title('Descritive Statistic')
    statistic_main.geometry('450x420')
    statistic_main.resizable(False,False)
        # Create label frame
    statistic_frame = LabelFrame(statistic_main, text='Enter Value 1')
    statistic_frame.pack(padx=10,pady=10)
    variable1 = Entry(statistic_frame,font=('Helvetica',16), textvariable=String1)
    variable1.pack(padx=15,pady=15)
    statistic_frame1 = LabelFrame(statistic_main, text='Enter Value 2')
    statistic_frame1.pack(padx=10,pady=10)
    variable2 = Entry(statistic_frame1,font=('Helvetica',16), textvariable=String2)
    variable2.pack(padx=15,pady=15)
    #count
    Button(statistic_main, text="Count player", command=number_of_mem).pack(pady=5)
    # Button to find min max player
    Button(statistic_main, text='Find min', command=frame_for_min).pack(pady=5)
    Button(statistic_main, text='Find max', command=frame_for_max).pack(pady=5)
    #find mean
    Button(statistic_main, text='Mean', command=mean_value).pack(pady=5)
    #find SUM market_value
    Button(statistic_main, text='Market value by club', command=market_value).pack(pady=5)

    # BACK TO MAIN DATA
    button_to_back = Button(statistic_main, text='Reset', command=cleardata)
    button_to_back.pack(pady=5)

# calculate num ber player
def number_of_mem():
    global df, variable1
    var1_receive = variable1.get()
    groups = df.groupby(var1_receive)
    var2_receive = variable2.get()
    get_club = groups.get_group(var2_receive)
    members = '{}: {} players\n'.format(var2_receive,get_club[var1_receive].count())
    textbox.insert(END, members)
    # textbox.insert(END, '\n')


String6 = StringVar()
def frame_for_mean():
    global statistic_main,variable4,frame_min,variable6,frame_mean
    statistic_main.forget(statistic_main)
    frame_mean = Toplevel(root)
    frame_mean.title('Min')
    frame_mean.geometry('300x200')
    frame_mean.resizable(False, False)
    label_frame_mean = LabelFrame(frame_mean, text='CLUB YOU WANT TO SHOW')
    label_frame_mean.pack(padx=10, pady=10)
    variable6 = Entry(label_frame_mean, font=('Helvetica', 16), textvariable=String6)
    variable6.pack(padx=15, pady=15)
    btn_to_show = Button(frame_mean,text='Show',command=mean_value)
    btn_to_show.pack(padx=10,pady=10)
    # Button back
    btn_back = Button(frame_mean,text='Back',command=statistic_mean)
    btn_back.pack()
def mean_value():
    global variable6
    var1_receive = variable1.get()
    var2_receive = variable2.get()
    var6_receive = variable6.get()
    mean = df.groupby(var1_receive).agg(Mean = (var2_receive,'mean'))
    if var6_receive == 'Arsenal':
        textbox.insert(END, mean[:1])
        textbox.insert(END, '\n')
    elif var6_receive == 'Bournemouth':
        textbox.insert(END, mean[1:2])
        textbox.insert(END, '\n')
    elif var6_receive == 'Brighton+and+Hove':
        textbox.insert(END, mean[2:3])
        textbox.insert(END, '\n')
    elif var6_receive == 'Burnley':
        textbox.insert(END, mean[3:4])
        textbox.insert(END, '\n')
    elif var6_receive == 'Chelsea':
        textbox.insert(END, mean[4:5])
        textbox.insert(END, '\n')
    elif var6_receive == 'Crystal+Palace':
        textbox.insert(END, mean[5:6])
        textbox.insert(END, '\n')
    elif var6_receive == 'Everton':
        textbox.insert(END, mean[6:7])
        textbox.insert(END, '\n')
    elif var6_receive == 'Huddersfield':
        textbox.insert(END, mean[7:8])
        textbox.insert(END, '\n')
    elif var6_receive == 'Leicester+City':
        textbox.insert(END, mean[8:9])
        textbox.insert(END, '\n')
    elif var6_receive == 'Liverpool':
        textbox.insert(END, mean[9:10])
        textbox.insert(END, '\n')
    elif var6_receive == 'Manchester+City':
        textbox.insert(END, mean[10:11])
        textbox.insert(END, '\n')
    elif var6_receive == 'Manchester+United':
        textbox.insert(END, mean[11:12])
        textbox.insert(END, '\n')
    elif var6_receive == 'Newcastle+United':
        textbox.insert(END, mean[12:13])
        textbox.insert(END, '\n')
    elif var6_receive == 'Southampton':
        textbox.insert(END, mean[13:14])
        textbox.insert(END, '\n')
    elif var6_receive == 'Stoke+City':
        textbox.insert(END, mean[14:15])
        textbox.insert(END, '\n')
    elif var6_receive == 'Swansea':
        textbox.insert(END, mean[15:16])
        textbox.insert(END, '\n')
    elif var6_receive == 'Tottenham':
        textbox.insert(END, mean[16:17])
        textbox.insert(END, '\n')
    elif var6_receive == 'Watford':
        textbox.insert(END, mean[17:18])
        textbox.insert(END, '\n')
    elif var6_receive == 'West+Brom':
        textbox.insert(END, mean[18:19])
        textbox.insert(END, '\n')
    elif var6_receive == 'West+Ham':
        textbox.insert(END, mean[19:20])
        textbox.insert(END, '\n')
    else:
        textbox.insert(END, df_min)
        textbox.insert(END, '\n')
Button(frame3,text='Statistic Calculator',command=statistic).pack(padx=10,pady=10)
def statistic_mean():
    global variable1, variable2, statistic_main, frame_mean
    frame_mean.forget(frame_mean)
    statistic_main = Toplevel(root)
    statistic_main.title('Descritive Statistic')
    statistic_main.geometry('450x420')
    statistic_main.resizable(False, False)
    # Create label frame
    statistic_frame = LabelFrame(statistic_main, text='Enter Value 1')
    statistic_frame.pack(padx=10, pady=10)
    variable1 = Entry(statistic_frame, font=('Helvetica', 16), textvariable=String1)
    variable1.pack(padx=15, pady=15)
    statistic_frame1 = LabelFrame(statistic_main, text='Enter Value 2')
    statistic_frame1.pack(padx=10, pady=10)
    variable2 = Entry(statistic_frame1, font=('Helvetica', 16), textvariable=String2)
    variable2.pack(padx=15, pady=15)
    # count
    Button(statistic_main, text="Count player", command=number_of_mem).pack(pady=5)
    # Button to find min max player
    Button(statistic_main, text='Find min', command=frame_for_min).pack(pady=5)
    Button(statistic_main, text='Find max', command=frame_for_max).pack(pady=5)
    # find mean
    Button(statistic_main, text='Mean', command=frame_for_mean).pack(pady=5)
    # find SUM market_value
    Button(statistic_main, text='Market value by club', command=market_value).pack(pady=5)

    # BACK TO MAIN DATA
    button_to_back = Button(statistic_main, text='Reset', command=cleardata)
    button_to_back.pack(pady=5)
#show chart

def show_chart():
    global variable1,variable2,flag

    search1 = Toplevel(root)
    search1.title('Show Chart')
    search1.geometry('350x300')

    Button(search1, text="Pie chart", command=pie_chart).pack(pady=5)
    # Button(search1, text="Scatter", command=root.destroy).pack(pady=5)
    Button(search1, text='Bar chart', command=pie_chart).pack(pady=5)
    # Button(search1, text='Line chart', command=line_chart).pack(pady=5)
    # Button(search1, text='Histogram', command=root.destroy).pack(pady=5)
    button_to_back = Button(search1, text='Reset', command=reset)
    button_to_back.pack(pady=5)


def pie_chart():

    data = textbox.get('1.0','end')
    chart1 = data.plt.pie(subplots = True,figsize=(20,12), autopct='%.2f%%')
    textbox.insert(END, chart1)

def bar_chart():
    data = textbox.get('1.0','end')
    chart2 = data.plot(kind = 'bar')
    textbox.insert(END,chart2)

# def line_chart():
#     data = textbox.get('1.0','end')
#     chart3 = data.plot(kind = '')


Button(frame3, text='Show Chart', command=show_chart).pack(padx=10,pady=10)

# Add a menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
# search_menu.add_command(label='Search',command=lookup_records)
file_menu.add_command(label="Open", command=file_open)
# file_menu.add_command(label='Show Chart', command=chart_option)

file_menu.add_command(label='Exit',command=root.destroy)
# Add button
my_label = Label(frame1, text="")
my_label.pack()

root.mainloop()
