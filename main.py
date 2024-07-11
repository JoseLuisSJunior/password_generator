import customtkinter as ct
import secrets
import string
list_values = (['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25'])
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")
window = ct.CTk()
window.title("PASSWORD GENERATOR")
window.resizable(False, False)
window.geometry("500x650")
window.rowconfigure(0,weight=1)
window.columnconfigure([0,1],weight=1)
window.iconbitmap("padlock.ico")

tabview = ct.CTkTabview(window, width=490, height=590)
tabview.grid()
tabview.add("PASSWORD GENERATOR")
tabview.tab("PASSWORD GENERATOR").grid_columnconfigure([0,1],weight=1)



def create_password():
    itens = (string.ascii_letters + string.digits)
    password = [secrets.choice(itens) for i in range(int(option_menu.get()))]
    password = ''.join(password)
    textbox_newpassword.delete(index1='1.0', index2='end')
    textbox_newpassword.insert(index='1.0',text=password)
    with open('password.txt','a',newline='') as arquivo:
        arquivo.write(f' User: {user.get()} Site: {site.get()} Password: {password}\n')

user_text = ct.CTkLabel(tabview.tab('PASSWORD GENERATOR'), text = "What is the name of the registered user?")
user_text.grid(row=0,column=0,padx=10,pady=10)
user=ct.CTkEntry(tabview.tab('PASSWORD GENERATOR'))
user.grid(row=0,column=1,padx=10,pady=10,columnspan=3)
site_text = ct.CTkLabel(tabview.tab("PASSWORD GENERATOR"), text ="Which website was this password registered on?")
site_text.grid(row=1,column=0,padx=10,pady=10)
site = ct.CTkEntry(tabview.tab('PASSWORD GENERATOR'))
site.grid(row=1,column=1,padx=10,pady=10,columnspan=3)
save_site = ct.CTkButton(tabview.tab('PASSWORD GENERATOR'),text="SAVE ALL", command=None)
save_site.grid(row=7,column=0,padx=10,pady=10,columnspan=3)
label_text1 = ct.CTkLabel(tabview.tab("PASSWORD GENERATOR"), text="CHOOSE THE AMOUNT OF CHARACTERS")
label_text1.grid(row=2,column=0,padx=10,pady=10,columnspan=3)

option_menu = ct.CTkOptionMenu(tabview.tab("PASSWORD GENERATOR"), values=list_values)
option_menu.grid(row=3,column=0,padx=10,pady=10,columnspan=3)

button_password = ct.CTkButton(tabview.tab("PASSWORD GENERATOR"), text="Generate Password", command=create_password)
button_password.grid(row=4,column=0,padx=10,pady=10,sticky='nsew',columnspan=3)

label_passwordgenerate = ct.CTkLabel(tabview.tab("PASSWORD GENERATOR"), text="Password created")
label_passwordgenerate.grid(row=5,column=0,padx=10,pady=10,sticky='nsew',columnspan=3)

textbox_newpassword = ct.CTkTextbox(tabview.tab("PASSWORD GENERATOR"), width=10,height=10)
textbox_newpassword.grid(row=6,column=0,padx=10,pady=10,sticky='nsew',columnspan=3)

window.mainloop()