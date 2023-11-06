from tkinter import *
import os


window=Tk()

window.title("phone book")
main_frame=Frame(window)
sub_frame=LabelFrame(main_frame)
inner_details_frame=Label(sub_frame)
exception_frame=Frame(sub_frame)
path="./contacts"

#-----------frames----------------------------------------#
def sub_framer(frame_name):
    global sub_frame
    if sub_frame:
        sub_frame.destroy()
    sub_frame=LabelFrame(main_frame,text=f"{frame_name}")
    sub_frame.grid(row=1,column=0,columnspan=4)
    
    return sub_frame

def inner_details_framer():
    global inner_details_frame
    if inner_details_frame:
        inner_details_frame.destroy()
    if exception_frame:
        exception_frame.destroy()
    inner_details_frame=Label(sub_frame)

def exception_framer():
    global exception_frame
    if exception_frame:
        exception_frame.destroy()
    if inner_details_frame:
        inner_details_frame.destroy()
    exception_frame=Frame(sub_frame)

#-----------------other Function----------------------#
def search_function(name):
    try:
        f=open(f"{path}/{name}.txt","r")
        line=f.readlines()
        file_name=line[0]
        file_phonenum=line[1]

        inner_details_framer()
        inner_details_frame.grid(row=3,column=0,columnspan=4)

        Search_header_label=Label(inner_details_frame,text="Details",font="Verdana 13 bold underline")
        Search_header_label.grid(row=3,column=0,columnspan=4)

        search_name_label=Label(inner_details_frame,text="Name ")
        serach_phonenum_label=Label(inner_details_frame,text="Phone Number")

        searched_name_label=Label(inner_details_frame,text=f"{file_name}",fg="green")
        searched_phonenum_label=Label(inner_details_frame,text=f"{file_phonenum}",fg="green")

        search_name_label.grid(row=4,column=0,padx=10,pady=10)
        serach_phonenum_label.grid(row=5,column=0,padx=10,pady=10)

        searched_name_label.grid(row=4,column=1,padx=10,pady=10)
        searched_phonenum_label.grid(row=5,column=1,padx=10,pady=10)

        

    except:
        excepte_fun

def excepte_fun():
    exception_framer()
    exception_frame.grid(row=3,column=0,columnspan=4)
    except_label=Label(exception_frame,text="Name not found",fg="red")
    except_label.grid(row=3,column=0,columnspan=4)
#------------------ delete part----------------------#
def deleted_click(name):
    os.remove(f"{path}/{name}.txt")
    
    deleted_status=Label(sub_frame,text="Deleted",fg="red")
    deleted_status.grid(row=7,column=0,columnspan=4)

    delete_name_entry.delete(0,END)

def delete_info(name):
    try:
        search_function(name)

        for_deleting_button=Button(inner_details_frame,text="Press me for Deleting",fg="white",bg="red", command=lambda:deleted_click(name))
        for_deleting_button.grid(row=6,column=0,columnspan=4,padx=10,pady=10)
    except:
        excepte_fun()

def delete_button_click():

    sub_framer("delete")
    global delete_name_entry
    delete_name_label=Label(sub_frame,text="delete name")
    delete_name_label.grid(row=1,column=0,padx=10)

    delete_name_entry=Entry(sub_frame)
    delete_name_entry.grid(row=1,column=2,padx=20,pady=10)

    delete_submit_button=Button(sub_frame,text="Next", command=lambda:delete_info(delete_name_entry.get()))
    delete_submit_button.grid(row=2,column=2,pady=10)

#-------------------------Update Button----------------------------#
def update_submit_button_click(name,phone_number,update_name):
   
    print(update_name,name,phone_number)
    os.rename(f"{path}/{update_name}.txt",f"{path}/{name}.txt")
    f=open(f"{path}/{name}.txt","w")
    f.write(f"{name} \n{phone_number}")

    # edit_page_exit_button=Button(sub_frame,text="Back",command=sub_frame.quit())
    # edit_page_exit_button.grid(row=3,column=0,padx=10,pady=10)
    
def for_editing(update_name):
    sub_framer("Editing page")
    Edit_name_label=Label(sub_frame,text="Name")
    Edit_phonenum_label=Label(sub_frame,text="Phone Number")

    Edit_name_label.grid(row=1,column=0,padx=10,pady=10)
    Edit_phonenum_label.grid(row=2,column=0,padx=10,pady=10)

    Edited_name_entry=Entry(sub_frame)
    Edited_phonenum_entry=Entry(sub_frame)

    f=open(f"{path}/{update_name}.txt")
    lines=f.readlines()
    phone=lines[1]

    

    Edited_name_entry.grid(row=1,column=1,padx=10,pady=10)
    Edited_phonenum_entry.grid(row=2,column=1,padx=10,pady=10)

    Edit_submit_button=Button(sub_frame,text="Submit",fg="white",bg="green",command=lambda:update_submit_button_click(Edited_name_entry.get(),Edited_phonenum_entry.get(),update_name))
    Edit_submit_button.grid(row=3,column=1,padx=10,pady=10)

    Edited_name_entry.insert(0,update_name)
    Edited_phonenum_entry.insert(0,phone)

def update_next_click():
   try:
        name=update_name.get()
        search_function(name)

        for_editing_button=Button(inner_details_frame,text="Press me for Editing",fg="white",bg="#000C8C",command=lambda:for_editing(name))
        for_editing_button.grid(row=6,column=0,columnspan=4,padx=10,pady=10)
   except:
        excepte_fun()

def update_button_click():
    global update_name
    sub_framer("Update ")
    update_name_label=Label(sub_frame,text="Update name")
    update_name_label.grid(row=1,column=0,padx=10,pady=10)

    update_name=Entry(sub_frame)
    update_name.grid(row=1,column=2,padx=10,pady=10)

    update_submit_button=Button(sub_frame,text="Next",command=update_next_click)
    update_submit_button.grid(row=2,column=2,padx=10,pady=10)


#---------------------Search Buttton------------------------------#


def search_submit_click():
    
    name=search_name.get()
    search_function(name)

    search_name.delete(0,END)


def search_button_click():
    sub_framer("Search")
    global search_name
    search_name_label=Label(sub_frame,text="Name")
    search_name_label.grid(row=1,column=0,padx=10)

    search_name=Entry(sub_frame)
    search_name.grid(row=1,column=1,padx=20,pady=10)

    search_submit_button=Button(sub_frame,text="Submit",command=search_submit_click)
    search_submit_button.grid(row=2,column=1,padx=10,pady=10)

#---------------------ADD button fun-------------------------------#
def contact_submit_click(name,phone):
    add_name=name
    add_phone=phone
    f=open(f"{path}/{name}.txt","a")
    f.write(f"{name} \n{phone}")

    name_entry.delete(0,END)
    phonenum_entry.delete(0,END)

    
def add_button_click():   # in frame
    sub_framer("Add Contact")
    global name_entry,phonenum_entry
    name_to_add_label=Label(sub_frame,text="Name ")
    name_to_add_label.grid(row=1,column=0,padx=10)

    name_entry=Entry(sub_frame)
    name_entry.grid(row=1,column=2,padx=20,pady=10)

    phonenum_add_label=Label(sub_frame,text="phone No. ")
    phonenum_add_label.grid(row=2,column=0,padx=10)

    phonenum_entry=Entry(sub_frame)
    phonenum_entry.grid(row=2,column=2,padx=20,pady=10)

    contact_submit_button=Button(sub_frame,text="Submit",command=lambda:contact_submit_click(name_entry.get(),phonenum_entry.get()))
    contact_submit_button.grid(row=3,column=2,pady=10)
#----------------------Home button fun --------------------------------#
def home_button_click():
    sub_framer("Home")
    
    home_label=Label(sub_frame,text="Hello User")
    home_label.grid(row=1,column=2,padx=30,pady=30)
#----------------------Button---------------------------

main_frame.pack(padx=20,pady=20)

home_button=Button(main_frame,text="Home",fg="white",bg="dark violet",width=7,command=home_button_click)
Add_button=Button(main_frame,text="Add",fg="white",bg="orange",width=7,command=add_button_click)
Search_button=Button(main_frame,text="Search",fg="white",bg="green",width=7,command=search_button_click)
Update_button=Button(main_frame,text="Update",fg="white",bg="#000C8C",width=7,command=update_button_click)
Delete_button=Button(main_frame,text="Delete",fg="white",bg="red",width=7,command=delete_button_click)

home_button.grid(row="0",column="0")
Add_button.grid(row="0",column="1")
Search_button.grid(row="0",column="2")
Update_button.grid(row="0",column="3")
Delete_button.grid(row="0",column="4")



for widget in main_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

for widget in sub_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

for widget in inner_details_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)

sub_framer("Home")
    
home_label=Label(sub_frame,text="Hello User")
home_label.grid(row=1,column=2,padx=30,pady=30)

window.mainloop()