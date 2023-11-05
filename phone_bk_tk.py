from tkinter import *


window=Tk()

window.title("phone book")
main_frame=Frame(window)
sub_frame=LabelFrame(main_frame)
path="./contacts"

def sub_framer(frame_name):
    global sub_frame
    if sub_frame:
        sub_frame.destroy()
    sub_frame=LabelFrame(main_frame,text=f"{frame_name}")
    sub_frame.grid(row=1,column=0,columnspan=4)
    
    return sub_frame

#------------------ delete part----------------------#
def delete_button_click():
    sub_framer("delete")
    delete_name_label=Label(sub_frame,text="delete name")
    delete_name_label.grid(row=1,column=0,padx=10)

    delete_name=Entry(sub_frame)
    delete_name.grid(row=1,column=2,padx=20,pady=10)

    delete_submit_button=Button(sub_frame,text="Delete")
    delete_submit_button.grid(row=2,column=2,pady=10)




#-------------------------Update Button----------------------------#
def update_submit_click():
    updatename=update_name.get()
    updatedname=updated_name.get()  
    try:
        f=open(f"{path}/{updatename}.txt","r")
        line=f.readlines()
        file_name=line[0]
        file_phnnum=line[1]
    except:
        print("Nmme Not Found")
        not_found_label=Label(sub_frame,text="Name Not Found",fg="red")
        not_found_label.grid(row=4,column=0)
        

   

    update_name.delete(0,END)
    updated_name.delete(0,END)


def update_button_click():
    global update_name,updated_name
    sub_framer("Update ")
    update_name_label=Label(sub_frame,text="Update name")
    update_name_label.grid(row=1,column=0,padx=10)

    update_name=Entry(sub_frame)
    update_name.grid(row=1,column=2,padx=20,pady=10)


    updated_name_label=Label(sub_frame,text="Updated name")
    updated_name_label.grid(row=2,column=0,padx=10)

    updated_name=Entry(sub_frame)
    updated_name.grid(row=2,column=2,padx=20,pady=10)

    update_submit_button=Button(sub_frame,text="Submit",command=update_submit_click)
    update_submit_button.grid(row=3,column=2,padx=10,pady=10)
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

home_button=Button(main_frame,text="Home",fg="white",bg="violet",width=5,command=home_button_click)
Add_button=Button(main_frame,text="Add",fg="white",bg="orange",width=5,command=add_button_click)
Update_button=Button(main_frame,text="Update",fg="white",bg="#000C8C",width=5,command=update_button_click)
Delete_button=Button(main_frame,text="Delete",fg="white",bg="red",width=5,command=delete_button_click)

home_button.grid(row="0",column="0")
Add_button.grid(row="0",column="1")
Update_button.grid(row="0",column="2")
Delete_button.grid(row="0",column="3")

for widget in main_frame.winfo_children():
    widget.grid_configure(padx=10,pady=10)



window.mainloop()