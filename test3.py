from tkinter import *
from PIL import ImageTk, Image  # type "Pip install pillow" in your terminal to install ImageTk and Image module
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Connect to the database
connection = sqlite3.connect('user.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fullname TEXT,
                    email TEXT UNIQUE,
                    password TEXT
                )''')

connection.commit()
connection.close()

def register_user():
    # Get user input from entry fields
    full_name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirmPassword_entry.get()

    # Check if any of the fields are empty
    if not full_name or not email or not password or not confirm_password:
        messagebox.showerror("Empty Fields", "Please fill in all the fields")
        return

    # Connect to the database
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    # Check if the email already exists
    cursor.execute('''SELECT * FROM user WHERE email = ?''', (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        messagebox.showerror("Registration Error", "Email already exists")
    else:
        # Insert user data into the database
        cursor.execute('''INSERT INTO user (fullname, email, password) VALUES (?, ?, ?)''', (full_name, email, password))
        connection.commit()
        messagebox.showinfo("Success", "User registered successfully")

    # Close the database connection
    connection.close()

# Associer la fonction de connexion au bouton de connexion

window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
window.resizable(0, 0)
window.title('Login and Registration Page')

# Window Icon Photo
icon = PhotoImage(file='img/pic-icon.png')
window.iconphoto(True, icon)

LoginPage = Frame(window)
RegistrationPage = Frame(window)

for frame in (LoginPage, RegistrationPage):
    frame.grid(row=0, column=0, sticky='nsew')


def show_frame(frame):
    frame.tkraise()


show_frame(LoginPage)

from tkinter import StringVar

# Définir les variables textvariables
Email = StringVar()
Password = StringVar()

# =====================================================================================================================
# =====================================================================================================================
# ==================== LOGIN PAGE =====================================================================================
# =====================================================================================================================
# =====================================================================================================================
from tkinter import messagebox

def login_user():
    # Récupérer les données entrées dans les champs d'entrée
    email = email_entry2.get()
    password = password_entry2.get()

    # Vérifier si les champs d'entrée ne sont pas vides
    if not email or not password:
        messagebox.showerror("Login Error", "Veuillez entrer votre email et votre mot de passe.")
        return

    # Se connecter à la base de données
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()

    # Exécuter la requête pour vérifier l'utilisateur dans la base de données
    cursor.execute('''SELECT * FROM user WHERE email = ? and password= ?''', (email, password))
    user_data = cursor.fetchall()

    # Fermer la connexion à la base de données
    connection.close()

    # Vérifier si l'utilisateur a été trouvé dans la base de données
    if user_data:
        messagebox.showinfo("Success", "Connexion réussie!")
        # Fermer la fenêtre LoginPage
        window.withdraw()
        admin_window = AdminWindow(window)

        # Vous pouvez naviguer vers la prochaine page ou effectuer toute autre action ici
    else:
        messagebox.showerror("Login Error", "Email ou mot de passe incorrect.")



design_frame1 = Listbox(LoginPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame1.place(x=0, y=0)

design_frame2 = Listbox(LoginPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame2.place(x=676, y=0)

design_frame3 = Listbox(LoginPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame3.place(x=75, y=106)

design_frame4 = Listbox(LoginPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=676, y=106)

# ====== Email ====================
email_entry2 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2,textvariable=Email)
email_entry2.place(x=134, y=170, width=256, height=34)
email_entry2.config(highlightbackground="black", highlightcolor="black")
email_label2 = Label(design_frame4, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label2.place(x=130, y=140)

# ==== Password ================== 
password_entry2 = Entry(design_frame4, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2,textvariable=Password)
password_entry2.place(x=134, y=250, width=256, height=34)
password_entry2.config(highlightbackground="black", highlightcolor="black")
password_label2 = Label(design_frame4, text='• Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
password_label2.place(x=130, y=220)


# function for show and hide password
def password_command():
    if password_entry2.cget('show') == '•':
        password_entry2.config(show='')
    else:
        password_entry2.config(show='•')


# ====== checkbutton ==============
checkButton = Checkbutton(design_frame4, bg='#f8f8f8', command=password_command, text='show password')
checkButton.place(x=140, y=288)


# ========= Buttons ===============
SignUp_button = Button(LoginPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=lambda: show_frame(RegistrationPage), borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)

# ===== Welcome Label ==============
welcome_label = Label(design_frame4, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)


# ======= top Login Button =========
login_button = Button(LoginPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0,command=login_user, activebackground='#1b87d2', cursor='hand2')
login_button.place(x=845,  y=175)

login_line = Canvas(LoginPage, width=60, height=5, bg='#1b87d2')
login_line.place(x=840, y=203)

# ==== LOGIN  down button ============
loginBtn1 = Button(design_frame4, fg='#f8f8f8', text='Login', bg='#1b87d2', font=("yu gothic ui bold", 15),
                   cursor='hand2',command=login_user, activebackground='#1b87d2')
loginBtn1.place(x=133, y=340, width=256, height=50)


# ======= ICONS =================

# ===== Email icon =========
email_icon = Image.open('img/email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=105, y=174)

# ===== password icon =========
password_icon = Image.open('img/pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=105, y=254)

# ===== picture icon =========
picture_icon = Image.open('img/pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame4, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('img/vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame3, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)


# ===================================================================================================================
# ===================================================================================================================
# === FORGOT PASSWORD  PAGE =========================================================================================
# ===================================================================================================================
# ===================================================================================================================


import sqlite3
from tkinter import Toplevel, Entry, Label, Button, messagebox

def forgot_password():
    # Créer une nouvelle fenêtre
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.iconbitmap('img/aa.ico')
    win.configure(background='#f8f8f8')
    win.resizable(0, 0)

    def update_password():
        # Récupérer les données saisies par l'utilisateur
        email = email_entry3.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry3.get()

        # Vérifier si les champs sont vides
        if not email or not new_password or not confirm_password:
            messagebox.showerror("Error", "Veuillez remplir tous les champs.")
            return

        # Vérifier si les mots de passe correspondent
        if new_password != confirm_password:
            messagebox.showerror("Error", "Les mots de passe ne correspondent pas.")
            return

        # Connecter à la base de données
        connection = sqlite3.connect('user.db')
        cursor = connection.cursor()

        # Vérifier si l'e-mail existe dans la base de données
        cursor.execute('''SELECT * FROM user WHERE email = ?''', (email,))
        user_data = cursor.fetchone()

        if user_data:
            # Mettre à jour le mot de passe
            cursor.execute('''UPDATE user SET password = ? WHERE email = ?''', (new_password, email))
            connection.commit()
            messagebox.showinfo("Success", "Mot de passe mis à jour avec succès.")
            win.destroy()
        else:
            messagebox.showerror("Error", "L'e-mail fourni n'existe pas dans la base de données.")

        # Fermer la connexion à la base de données
        connection.close()

    # Champ d'entrée pour l'email
    email_entry3 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry3.place(x=40, y=30, width=256, height=34)
    email_entry3.config(highlightbackground="black", highlightcolor="black")
    email_label3 = Label(win, text='• Email account', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    email_label3.place(x=40, y=0)

    # Champ d'entrée pour le nouveau mot de passe
    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # Champ d'entrée pour confirmer le nouveau mot de passe
    confirm_password_entry3 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    confirm_password_entry3.place(x=40, y=190, width=256, height=34)
    confirm_password_entry3.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label3 = Label(win, text='• Confirm Password', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
    confirm_password_label3.place(x=40, y=160)

    # Bouton pour mettre à jour le mot de passe
    update_pass = Button(win, fg='#f8f8f8', text='Update Password', bg='#1b87d2', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2', command=update_password)
    update_pass.place(x=40, y=240, width=256, height=50)

# Bouton "Forgot password"
forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', command=forgot_password, cursor="hand2")
forgotPassword.place(x=290, y=290)



# =====================================================================================================================
# =====================================================================================================================
# =====================================================================================================================


# =====================================================================================================================
# =====================================================================================================================
# ==================== REGISTRATION PAGE ==============================================================================
# =====================================================================================================================
# =====================================================================================================================

design_frame5 = Listbox(RegistrationPage, bg='#0c71b9', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame5.place(x=0, y=0)

design_frame6 = Listbox(RegistrationPage, bg='#1e85d0', width=115, height=50, highlightthickness=0, borderwidth=0)
design_frame6.place(x=676, y=0)

design_frame7 = Listbox(RegistrationPage, bg='#1e85d0', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame7.place(x=75, y=106)

design_frame8 = Listbox(RegistrationPage, bg='#f8f8f8', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame8.place(x=676, y=106)

# ==== Full Name =======
name_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
name_entry.place(x=284, y=150, width=286, height=34)
name_entry.config(highlightbackground="black", highlightcolor="black")
name_label = Label(design_frame8, text='•Full Name', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
name_label.place(x=280, y=120)

# ======= Email ===========
email_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
email_entry.place(x=284, y=220, width=286, height=34)
email_entry.config(highlightbackground="black", highlightcolor="black")
email_label = Label(design_frame8, text='•Email', fg="#89898b", bg='#f8f8f8', font=("yu gothic ui", 11, 'bold'))
email_label.place(x=280, y=190)

# ====== Password =========
password_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
password_entry.place(x=284, y=295, width=286, height=34)
password_entry.config(highlightbackground="black", highlightcolor="black")
password_label = Label(design_frame8, text='• Password', fg="#89898b", bg='#f8f8f8',
                       font=("yu gothic ui", 11, 'bold'))
password_label.place(x=280, y=265)


def password_command2():
    if password_entry.cget('show') == '•':
        password_entry.config(show='')
    else:
        password_entry.config(show='•')


checkButton = Checkbutton(design_frame8, bg='#f8f8f8', command=password_command2, text='show password')
checkButton.place(x=290, y=330)


# ====== Confirm Password =============
confirmPassword_entry = Entry(design_frame8, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
confirmPassword_entry.place(x=284, y=385, width=286, height=34)
confirmPassword_entry.config(highlightbackground="black", highlightcolor="black")
confirmPassword_label = Label(design_frame8, text='• Confirm Password', fg="#89898b", bg='#f8f8f8',
                              font=("yu gothic ui", 11, 'bold'))
confirmPassword_label.place(x=280, y=355)

# ========= Buttons ====================

SignUp_button = Button(RegistrationPage, text='Sign up', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                       command=register_user, borderwidth=0, activebackground='#1b87d2', cursor='hand2')
SignUp_button.place(x=1100, y=175)


SignUp_line = Canvas(RegistrationPage, width=60, height=5, bg='#1b87d2')
SignUp_line.place(x=1100, y=203)

# ===== Welcome Label ==================
welcome_label = Label(design_frame8, text='Welcome', font=('Arial', 20, 'bold'), bg='#f8f8f8')
welcome_label.place(x=130, y=15)

# ========= Login Button =========
login_button = Button(RegistrationPage, text='Login', font=("yu gothic ui bold", 12), bg='#f8f8f8', fg="#89898b",
                      borderwidth=0, activebackground='#1b87d2', command=lambda: show_frame(LoginPage), cursor='hand2')
login_button.place(x=845, y=175)

# ==== SIGN UP down button ============
signUp2 = Button(design_frame8, fg='#f8f8f8', text='Sign Up', bg='#1b87d2', font=("yu gothic ui bold", 15),
                  command=register_user,cursor='hand2', activebackground='#1b87d2')
signUp2.place(x=285, y=435, width=286, height=50)

# ===== password icon =========
password_icon = Image.open('img/pass-icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
password_icon_label.image = photo
password_icon_label.place(x=255, y=300)

# ===== confirm password icon =========
confirmPassword_icon = Image.open('img/pass-icon.png')
photo = ImageTk.PhotoImage(confirmPassword_icon)
confirmPassword_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
confirmPassword_icon_label.image = photo
confirmPassword_icon_label.place(x=255, y=390)

# ===== Email icon =========
email_icon = Image.open('img/email-icon.png')
photo = ImageTk.PhotoImage(email_icon)
emailIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
emailIcon_label.image = photo
emailIcon_label.place(x=255, y=225)

# ===== Full Name icon =========
name_icon = Image.open('img/name-icon.png')
photo = ImageTk.PhotoImage(name_icon)
nameIcon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
nameIcon_label.image = photo
nameIcon_label.place(x=252, y=153)

# ===== picture icon =========
picture_icon = Image.open('img/pic-icon.png')
photo = ImageTk.PhotoImage(picture_icon)
picture_icon_label = Label(design_frame8, image=photo, bg='#f8f8f8')
picture_icon_label.image = photo
picture_icon_label.place(x=280, y=5)

# ===== Left Side Picture ============
side_image = Image.open('img/vector.png')
photo = ImageTk.PhotoImage(side_image)
side_image_label = Label(design_frame7, image=photo, bg='#1e85d0')
side_image_label.image = photo
side_image_label.place(x=50, y=10)




# =====================================================================================================================
# ==================== DATABASE CONNECTION ============================================================================
# =====================================================================================================================
# =====================================================================================================================




class AdminWindow:
    #def ouvrir_fenetre_order(self):
       #pass
    #def ouvrir_fenetre_adminEmployes(self):
        #pass
    #def ouvrir_fenetre_adminProduit(self):
        #pass


    def __init__(self,parent):
            self.parent = parent
            self.admin_window = tk.Toplevel(parent)
            self.admin_window.title("Fenêtre principale")
            self.admin_window.geometry('2200x800')  # Modifié la taille pour mieux s'adapter aux éléments
            self.create_widgets()
            self.conn = sqlite3.connect('gestionStock.db')
            self.cursor = self.conn.cursor()
            self.create_tables()
            self.close_login_page()
    def close_login_page(self):
        # Vérifier si la fenêtre LoginPage est ouverte et la fermer
        if LoginPage.winfo_exists():
            LoginPage.destroy()
    def create_tables(self):
# Création de la table 'produit'
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                prix INTEGER,
                                name TEXT UNIQUE,
                                Quantite INTEGER NOT NULL,
                                Description TEXT
                                )''')

        # Création de la table 'employee'
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Employes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                fonction TEXT,
                                nameComplet TEXT,
                                matricule TEXT,
                                Tel INTEGER,
                                AutreInfo  TEXT
                                )''')

        # Création de la table 'command'
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Commandes (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                id_employe INTEGER,
                                id_produit INTEGER,
                                quantite INTEGER,
                                date_commande DATE,
                                FOREIGN KEY (id_employe) REFERENCES Employes(id),
                                FOREIGN KEY (id_produit) REFERENCES Products(id)
                            )''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Fournisseur (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                NomProduitF TEXT UNIQUE,
                                Quantite INTEGER,
                                Remarques TEXT,
                                DateCreation DATE
                            )''')

        # Commit des changements
        self.conn.commit()

    #----------------------------------------------------------------------------------------------------------------------------------------

    def create_widgets(self):
        # Background Image
        bg_image2 = Image.open('img/coverRes.jpg').resize((3750,2500))  # Redimensionner l'image pour s'adapter à la fenêtre
        self.bg_image2 = ImageTk.PhotoImage(bg_image2)
        self.admin_canvas = tk.Canvas(self.admin_window, width=1300, height=700)
        self.admin_canvas.pack(expand=True, fill='both')
        self.bg_image_id2 = self.admin_canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image2)

        # Obtenir les dimensions de la fenêtre parente
        width = self.admin_window.winfo_width()
        height = self.admin_window.winfo_height()

        # Title
        self.text_canvas = self.admin_canvas.create_text(width/2, 150, text="Gestion De Stock", font=('cooper black', 20, 'bold'), fill="blue")

        # Logo
        logo_image = Image.open('img/logo2023.png').resize((150, 60))  # Ajuster la taille du logo
        self.logo_image = ImageTk.PhotoImage(logo_image)
        self.logo_label = self.admin_canvas.create_image(width * 0.1, height * 0.1, anchor=tk.NW, image=self.logo_image)

        # Clock
        self.clock_label = self.admin_canvas.create_text(width * 0.85, 20, text="", font=('cooper black', 12, 'bold'), fill="white")
        #quitter 
        self.iconProduit = ImageTk.PhotoImage(Image.open('img/package.png').resize((50, 25)))
        self.bouton1 = tk.Button(self.admin_window, text="Products", font=('cooper black', 12, 'bold'), command=lambda: self.ouvrir_fenetre_adminProduit(), image=self.iconProduit, compound=tk.LEFT)
        self.bouton1.place(relx=0.85, rely=0.35)
        
        self.iconEmployee = ImageTk.PhotoImage(Image.open('img/employee.png').resize((50, 25)))
        self.bouton2 = tk.Button(self.admin_window, text="Employés", font=('cooper black', 12, 'bold'),  command=lambda: self.ouvrir_fenetre_adminEmployes(), image=self.iconEmployee, compound=tk.LEFT)
        self.bouton2.place(relx=0.85, rely=0.30)
        
        self.iconOrder = ImageTk.PhotoImage(Image.open('img/package.png').resize((50, 25)))
        self.bouton3 = tk.Button(self.admin_window, text="Passer commander", font=('cooper black', 12, 'bold'),  command=lambda: self.ouvrir_fenetre_order(), image=self.iconOrder, compound=tk.LEFT)
        self.bouton3.place(relx=0.25, rely=0.75)
        
        self.iconFournisseur = ImageTk.PhotoImage(Image.open('img/employee.png').resize((50, 25)))
        self.boutonF = tk.Button(self.admin_window, text="Fournisseur", font=('cooper black', 12, 'bold'),  command=lambda: self.ouvrir_fenetre_Fournisseur(), image=self.iconFournisseur, compound=tk.LEFT)
        self.boutonF.place(relx=0.62, rely=0.75)


        self.iconHistory = ImageTk.PhotoImage(Image.open('img/quitter.png').resize((40, 25)))
        self.bouton4 = tk.Button(self.admin_window, text="le Suivi", font=('cooper black', 12, 'bold'),  command=lambda: self.ouvrir_fenetre_Historique(), image=self.iconHistory, compound=tk.LEFT)
        self.bouton4.place(relx=0.85, rely=0.25)

        self.iconQuitter = ImageTk.PhotoImage(Image.open('img/quitter.png').resize((40, 25)))
        self.bouton5 = tk.Button(self.admin_window, text="Quitter", font=('cooper black', 12, 'bold'),  command=self.admin_window.destroy, image=self.iconQuitter, compound=tk.LEFT)
        self.bouton5.place(relx=0.85, rely=0.50)

#----------------------------------------------------------------
# Définition de la fonction on_select au niveau global
 

#----------------------------------------------------------------
        def update_tree_window(tree):
            # Se connecter à la base de données
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()

            # Récupérer les données de la base de données
            Products = []
            cursor.execute('SELECT name, Quantite FROM Products')
            rows = cursor.fetchall()
            for row in rows:
                product_name = row[0]
                quantity = row[1]
                status = "Disponible" if quantity > 0 else "Indisponible"
                remaining = quantity if quantity > 0 else 0
                Products.append((product_name, quantity, status, remaining))

            # Effacer les anciennes données du Treeview
            for item in tree.get_children():
                tree.delete(item)

            # Insérer les nouvelles données dans le Treeview
            #for product in Products:
                #tree.insert("", tk.END, values=product)
            for product in Products:
                status_text = product[2]
                if status_text == "Disponible":
                    tree.insert("", tk.END, values=product, tags=('green',))
                elif status_text == "Indisponible":
                    tree.insert("", tk.END, values=product, tags=('red',))
                else:
                    tree.insert("", tk.END, values=product)

            # Définition des couleurs
            tree.tag_configure('black', foreground='green')
            tree.tag_configure('red', foreground='red')

            # Fermer la connexion à la base de données
            conn.close()

            # Planifier une mise à jour périodique après un certain délai (par exemple, toutes les 5 secondes)
            self.admin_window.after(1000, update_tree_window, tree)

        # Définir la fonction pour ouvrir la fenêtre de l'arbre
        def open_tree_window():
            # Se connecter à la base de données
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()

            # Récupérer les données de la base de données
            Products = []
            cursor.execute('SELECT name, Quantite FROM Products')
            rows = cursor.fetchall()
            for row in rows:
                product_name = row[0]
                quantity = row[1]
                status = "Disponible" if quantity > 0 else "Indisponible"
                remaining = quantity if quantity > 0 else 0
                Products.append((product_name, quantity, status, remaining))

            # Créer le Treeview avec les données récupérées
            tree = ttk.Treeview(self.admin_canvas, columns=('name', 'Quantite', 'Status', 'Reste'), show='headings', height=23)
            tree.heading('name', text='Name')
            tree.heading('Quantite', text='Quantite')
            tree.heading('Status', text='Status')
            tree.heading('Reste', text='Reste')
            for col in tree['columns']:
                tree.column(col, anchor='center')
            for col in tree['columns']:
                tree.column(col, anchor='center', width=150)
            # Insérer les données dans le Treeview
            for product in Products:
                tree.insert("", tk.END, values=product)

            # Fermer la connexion à la base de données
            conn.close()
            def resize_tree(event):
                        width = event.width
                        height = event.height
                        # Réajuster la taille et la position du Treeview en conséquence
                        tree.place(x=width//4, y=height//4, width=width//2, height=height//2)

        # Placer le Treeview sur le canevas
                        tree.place(x=width//4, y=height//4, width=width//2, height=height//2)

            # Placer le Treeview sur le canevas
            #tree.place(x=220, y=100, width=880, height=500)
            self.admin_canvas.bind('<Configure>', resize_tree)
            # Lancer la mise à jour périodique des données du Treeview
            update_tree_window(tree)
#----------------------------------------------------------------
#----------------------------------------------------------------
        open_tree_window()
        def update_clock():
            now = datetime.now().strftime("%A, %B %Y %H:%M:%S")
            self.admin_canvas.itemconfig(self.clock_label, text=now)
            self.admin_window.after(1000, update_clock)

        update_clock()

        # Resize event binding
        self.admin_window.bind('<Configure>', self.resize)

#----------------------------------------------------------------
    # Fonction pour ouvrir la fenêtre adminProduit
    def ouvrir_fenetre_adminProduit(self, event=None):
        import tkinter as tk
        from tkinter import ttk
        
        root = tk.Tk()
        root.title("Sélection des Products")
        root.geometry('2150x350')
        root.configure(bg='snow2')

        frame = tk.Frame(root, bd=2, relief='ridge')  # Ajoute un cadre avec une bordure et un relief
        frame.place(x=280, y=10)

        tree = ttk.Treeview(frame, columns=('id','prix', 'name','Quantite','Description'), show='headings', height=15)
        tree.heading('id', text='id')
        tree.heading('prix', text='Prix')
        tree.heading('name', text='Name')
        tree.heading('Quantite', text='Quantite')
        tree.heading('Description', text='Description')

        # Centrer les valeurs dans toutes les colonnes
        for col in tree['columns']:
            tree.column(col, anchor='center')

        tree.pack(fill='both', expand=True)


        conn = sqlite3.connect('gestionStock.db')
        cursor = conn.cursor()

        Products = []
        cursor.execute('SELECT id,prix, name, Quantite, Description FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            Products.append((row[0], row[1],row[2],row[3],row[4]))
            tree.insert("", tk.END, values=row)
        
      

        combo = ttk.Combobox(root, values=[produit[0] for produit in Products])
        combo.place(x=5, y=10)

        def close_app():
            result = messagebox.askquestion("Fermer", "Voulez-vous vraiment fermer l'application?")
            if result == 'yes':
                root.destroy()    
# Définition de la fonction on_select au niveau global
        def on_select(event):
            selected_item = tree.selection()[0]  # Obtenir l'élément sélectionné dans le TreeView
            values = tree.item(selected_item, 'values')  # Obtenir les valeurs de l'élément sélectionné
            print("Element sélectionné :", values)  # Afficher les valeurs dans la console (vous pouvez les utiliser comme nécessaire)

        def populate_combo():
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM Products")
            rows = cursor.fetchall()
            conn.close()

            # Récupérer uniquement les noms des produits à partir des résultats de la requête
            product_names = [row[0] for row in rows]

            # Mettre à jour les valeurs de la Combobox avec les noms des produits
            combo['values'] = product_names

        def search_keyword():
            keyword = combo.get()
            
            # Effacer les résultats précédents dans le TreeView
            tree.delete(*tree.get_children())
            
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()
            
            # Requête pour rechercher les résultats correspondants au nom dans la base de données
            cursor.execute("SELECT id, prix, name, Quantite, Description FROM Products WHERE name LIKE ?", ('%' + keyword + '%',))
            rows = cursor.fetchall()
            
            # Insérer les résultats dans le TreeView
            for row in rows:
                tree.insert("", tk.END, values=row)
            
            conn.close()

            # Sélectionner automatiquement le premier élément dans le TreeView s'il existe
            if rows:
                tree.selection_set(tree.get_children()[0])

        # Créer une liaison de sélection au TreeView pour appeler une fonction lorsque la sélection change
        tree.bind("<<TreeviewSelect>>", on_select)

        # Appeler la fonction pour remplir la Combobox avec les noms des produits
        populate_combo()
        search_button = ttk.Button(root, text="Rechercher", command=search_keyword)
        search_button.place(x=150, y=8)
            # Création du bouton de fermeture
        close_button = ttk.Button(root,width=20, text="Fermer", command=close_app)
        close_button.place(x=5, y=230)
        def save():
            messagebox.showinfo("Succès", "Opération effectuée avec succès!")
        
        save_button = ttk.Button(root,width=20, text="Enregistrer", command=save)
        save_button.place(x=5, y=200)

        def add_produit():
            def save_produit():
             
                new_prix = prix_entry.get()
                new_name = name_entry.get()
                new_quantite = quantite_entry.get()
                new_description = description_entry.get()

                # Ajouter la nouvelle produit à la liste d'Products
                Products.append((new_prix, new_name, new_quantite, new_description))

                # Ajouter la nouvelle ligne à la Treeview
                tree.insert("", tk.END, values=(new_prix, new_name, new_quantite, new_description))
                
                conn = sqlite3.connect('gestionStock.db')
                cursor = conn.cursor()

                # Enregistrer les modifications dans la base de données
                cursor.execute("INSERT INTO Products (prix, name, Quantite, Description) values (?, ?, ?, ?)", (new_prix, new_name, new_quantite, new_description))
                conn.commit()
                # Actualiser les données dans le Treeview
                tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
                cursor.execute('SELECT id,prix, name, Quantite, Description FROM Products')
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)

                conn.close()

                # Fermer la fenêtre
                add_window.destroy()

            # Créer une nouvelle fenêtre pour saisir le nom et le prix de la nouvelle produit
            #add_window = tk.Toplevel(root)
            # Créer une nouvelle fenêtre pour saisir le nom, le prix, la quantité et la description de la nouvelle produit
            add_window = tk.Toplevel(root)
            add_window.geometry("400x280")
            add_window.title("Ajouter une produit")

            # Calculer les coordonnées pour centrer la fenêtre sur l'écran
            window_width = add_window.winfo_reqwidth()
            window_height = add_window.winfo_reqheight()
            position_right = int(add_window.winfo_screenwidth() / 2 - window_width / 2)
            position_down = int(add_window.winfo_screenheight() / 2 - window_height / 2)

            # Définir la position de la fenêtre
            add_window.geometry("+{}+{}".format(position_right, position_down))

            # Titre centré en haut de la fenêtre
            title_label = ttk.Label(add_window, text="Ajouter une produit", font=("Helvetica", 14, "bold"))
            title_label.grid(row=0, column=0, columnspan=2, padx=(70, 20), pady=(10, 20), sticky="nsew")

            # Utilisation d'une grille pour disposer les éléments de manière plus organisée
            prix_label = ttk.Label(add_window, text="Entrez le prix de la nouvelle produit :")
            prix_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
            name_label = ttk.Label(add_window, text="Entrez le nom de la nouvelle produit :")
            name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

            quantite_label = ttk.Label(add_window, text="Entrez le quantité de la nouvelle produit :")
            quantite_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

            description_label = ttk.Label(add_window, text="Entrez le description de la nouvelle produit :")
            description_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

            # Entry Widgets
            prix_entry = ttk.Entry(add_window)
            prix_entry.grid(row=1, column=1, padx=5, pady=5)

            name_entry = ttk.Entry(add_window)
            name_entry.grid(row=2, column=1, padx=5, pady=5)

            quantite_entry = ttk.Entry(add_window)
            quantite_entry.grid(row=3, column=1, padx=5, pady=5)

            description_entry = ttk.Entry(add_window)
            description_entry.grid(row=4, column=1, padx=5, pady=5)

            # Ajouter un bouton pour enregistrer la modification dans la base de données
            save_button = ttk.Button(add_window, text="Enregistrer", command=save_produit)
            save_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

            ret_button = ttk.Button(add_window, text="Quitter", command=add_window.destroy)
            ret_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

        add_produit_button = ttk.Button(root,width=20, text="Ajouter une Produit", command=add_produit)
        add_produit_button.place(x=5, y=140)

        def modify_produitB():
            selected_item = tree.selection()
            if selected_item:
                values = tree.item(selected_item)['values']
                if values:
                    selected_id = values[0]  # Supposons que l'ID est le premier élément dans vos données
                    selected_produit = None

                    for produit in Products:
                        if produit[0] == selected_id:  # Assurez-vous que l'ID correspond
                            selected_produit = produit
                            break

                    if selected_produit:
                       # Créer une nouvelle fenêtre pour modifier le nom, le prix, la quantité et la description du produit sélectionné
                        modify_window = tk.Toplevel(root)
                        modify_window.geometry("300x400")
                        modify_window.title("Modifier une Produit")

                        # Calculer les coordonnées pour centrer la fenêtre sur l'écran
                        window_width = modify_window.winfo_reqwidth()
                        window_height = modify_window.winfo_reqheight()
                        position_right = int(modify_window.winfo_screenwidth() / 2 - window_width / 2)
                        position_down = int(modify_window.winfo_screenheight() / 2 - window_height / 2)

                        # Définir la position de la fenêtre
                        modify_window.geometry("+{}+{}".format(position_right, position_down))

                        # Titre centré en haut de la fenêtre
                        title_label = ttk.Label(modify_window, text="Modifier une Produit", font=("Helvetica", 14, "bold"))
                        title_label.grid(row=0, column=0, columnspan=2,padx=(70, 20), pady=(10, 20), sticky="nsew")

                        # Utilisation d'une grille pour disposer les éléments de manière plus organisée
                        prix_label = ttk.Label(modify_window, text="Prix actuel :")
                        prix_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

                        name_label = ttk.Label(modify_window, text="Nom actuel:")
                        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

                        quantite_label = ttk.Label(modify_window, text="Quantité actuelle:")
                        quantite_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

                        description_label = ttk.Label(modify_window, text="Description actuelle:")
                        description_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

                        # Entry Widgets
                        prix_entry = ttk.Entry(modify_window)
                        prix_entry.insert(tk.END, selected_produit[1])  # Insérer le prix du produit
                        prix_entry.grid(row=1, column=1, padx=5, pady=5)

                        name_entry = ttk.Entry(modify_window)
                        name_entry.insert(tk.END, selected_produit[2])  # Insérer le nom du produit
                        name_entry.grid(row=2, column=1, padx=5, pady=5)

                        quantite_entry = ttk.Entry(modify_window)
                        quantite_entry.insert(tk.END, selected_produit[3])  # Insérer la quantité du produit
                        quantite_entry.grid(row=3, column=1, padx=5, pady=5)

                        description_entry = ttk.Entry(modify_window)
                        description_entry.insert(tk.END, selected_produit[4])  # Insérer la description du produit
                        description_entry.grid(row=4, column=1, padx=5, pady=5)

                        # Bouton pour enregistrer les modifications
                        
                        def update_produit():
                            new_prix = prix_entry.get()
                            new_name = name_entry.get()
                            new_quantite = quantite_entry.get()
                            new_description = description_entry.get()

                            # Créer un nouveau tuple avec les valeurs mises à jour
                            updated_produit = (selected_id, new_prix, new_name, new_quantite, new_description)

                            # Trouver l'index du produit dans la liste Products
                            index = Products.index(selected_produit)

                            # Remplacer l'ancien tuple par le nouveau dans la liste Products
                            Products[index] = updated_produit

                            # Mettre à jour le produit dans la base de données
                            conn = sqlite3.connect('gestionStock.db')
                            cursor = conn.cursor()
                            cursor.execute("UPDATE products SET prix = ?, name = ?, Quantite = ?, Description = ? WHERE id = ?", (new_prix, new_name, new_quantite, new_description, selected_id))
                            conn.commit()

                            # Mettre à jour la Treeview avec les nouvelles valeurs
                            tree.item(selected_item, values=updated_produit)
    

                            # Fermer la fenêtre de modification
                            modify_window.destroy()


                        update_button = ttk.Button(modify_window, text="Enregistrer", command=update_produit)
                        update_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

                        # Bouton pour quitter
                        ret_button = ttk.Button(modify_window, text="Quitter", command=modify_window.destroy)
                        ret_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

                        

                    else:
                        # Afficher un message d'erreur si le produit n'est pas trouvé
                        messagebox.showerror("Erreur", "Produit introuvable.")
                else:
                    # Afficher un message d'erreur si aucune produit n'est sélectionnée dans la Treeview
                    messagebox.showerror("Erreur", "Aucune produit sélectionnée.")
            else:
                # Afficher un message d'erreur si aucune produit n'est sélectionnée dans la Treeview
                messagebox.showerror("Erreur", "Aucune produit sélectionnée.")

        modify_button = ttk.Button(root, width=20, text="Modifier le Produit", command=modify_produitB)
        modify_button.place(x=5, y=110)

        # Fonction pour supprimer une produit sélectionnée
        def delete_produit():
            selected_items = tree.selection()
            if selected_items:
                for item in selected_items:
                    values = tree.item(item)['values']
                    if values:
                        selected_id = values[0]

                        # Supprimer la commande correspondante de la base de données
                        cursor.execute("DELETE FROM Products WHERE id=?", (selected_id,))

                        # Confirmer la transaction
                        conn.commit()

                        # Supprimer la ligne de Treeview
                        tree.delete(item)

                # Actualiser les données dans le Treeview
                tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
                cursor.execute('SELECT id,prix, name, Quantite, Description FROM Products')
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)
            else:
                print("No item selected in Treeview!")
                

        delete_button = ttk.Button(root,width=20, text="Supprimer le Produit", command=delete_produit)
        delete_button.place(x=5, y=170)
        

        # Fermer la connexion à la base de données à la fin du programme
       

        root.mainloop()
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    def ouvrir_fenetre_adminEmployes(self, event=None):
        import tkinter as tk
        from tkinter import ttk
        from tkinter import messagebox
        root = tk.Tk()
        root.title("Sélection de Employes")
        root.geometry('1500x300')

        tree = ttk.Treeview(root, columns=('N*','fonction', 'nameComplet','matricule','Tel','AutreInfo'), show='headings', height=15)
        tree.heading('N*', text='N*')
        tree.heading('fonction', text='Fonction')
        tree.heading('nameComplet', text='Employes')
        tree.heading('matricule', text='Matricule')
        tree.heading('Tel', text='Telephone')
        tree.heading('AutreInfo', text='AutreInfo')
        tree.place(x=280, y=10)
        for col in tree['columns']:
                tree.column(col, anchor='center')
        for col in tree['columns']:
                tree.column(col, anchor='center', width=150)

        conn = sqlite3.connect('gestionStock.db')
        cursor = conn.cursor()
        Employes = []
        
        cursor.execute('SELECT id,fonction,nameComplet,matricule,Tel, AutreInfo FROM Employes')
        rows = cursor.fetchall()
        for row in rows:
            Employes.append((row[0], row[1], row[2], row[3], row[4],row[5]))
            tree.insert("", tk.END, values=row)


        combo = ttk.Combobox(root, values=[Employe [1] for Employe in Employes])
        combo.place(x=5, y=10)

        def add_Employe():
            def save_Employe():
                new_fonction = fonction_entry.get()
                new_nameComplet = nameComplet_entry.get()
                new_matricule = matricule_entry.get()
                new_Tel = tel_entry.get()
                new_AutreInfo = autreInfo_entry.get()

                # Ajouter la nouvelle produit à la liste d'Produits
                Employes.append((new_fonction, new_nameComplet, new_matricule, new_Tel, new_AutreInfo))

                # Ajouter la nouvelle ligne à la Treeview
                tree.insert("", tk.END, values=(new_fonction, new_nameComplet, new_matricule, new_Tel, new_AutreInfo))
                conn = sqlite3.connect('gestionStock.db')
                cursor = conn.cursor()
                # Enregistrer les modifications dans la base de données
                cursor.execute("INSERT INTO Employes (fonction, nameComplet, matricule, Tel, AutreInfo) values (?, ?, ?, ?, ?)", (new_fonction, new_nameComplet, new_matricule, new_Tel, new_AutreInfo))
                conn.commit()
                # Actualiser les données dans le Treeview
                tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
                cursor.execute('SELECT id,fonction,nameComplet,matricule,Tel, AutreInfo FROM Employes')
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)

                conn.close()
        

                # Fermer la fenêtre
                add_window.destroy()

            # Créer une nouvelle fenêtre pour saisir le nom et le prix de la nouvelle produit
            # Créer une nouvelle fenêtre pour saisir le nom et le prix du nouvel employé
            add_window = tk.Toplevel(root)
            add_window.title("Ajouter un Employé")
            add_window.geometry("420x280")

            # Calculer les coordonnées pour centrer la fenêtre sur l'écran
            window_width = add_window.winfo_reqwidth()
            window_height = add_window.winfo_reqheight()
            position_right = int(add_window.winfo_screenwidth() / 2 - window_width / 2)
            position_down = int(add_window.winfo_screenheight() / 2 - window_height / 2)

            # Définir la position de la fenêtre
            add_window.geometry("+{}+{}".format(position_right, position_down))

            # Titre centré en haut de la fenêtre
            title_label = ttk.Label(add_window, text="Ajouter un Employé", font=("Helvetica", 14, "bold"))
            title_label.grid(row=0, column=0, columnspan=2, padx=(90, 20), sticky="nsew")

            # Utilisation d'une grille pour disposer les éléments de manière plus organisée
            fonction_label = ttk.Label(add_window, text="Entrez la fonction du nouvel employé :")
            fonction_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

            nameComplet_label = ttk.Label(add_window, text="Entrez le nom du nouvel employé :")
            nameComplet_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

            matricule_label = ttk.Label(add_window, text="Entrez le matricule du nouvel employé :")
            matricule_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

            tel_label = ttk.Label(add_window, text="Entrez le téléphone du nouvel employé :")
            tel_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

            autreInfo_label = ttk.Label(add_window, text="Entrez d'autres informations sur le nouvel employé :")
            autreInfo_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

            # Entry Widgets
            fonction_entry = ttk.Entry(add_window)
            fonction_entry.grid(row=1, column=1, padx=5, pady=5)

            nameComplet_entry = ttk.Entry(add_window)
            nameComplet_entry.grid(row=2, column=1, padx=5, pady=5)

            matricule_entry = ttk.Entry(add_window)
            matricule_entry.grid(row=3, column=1, padx=5, pady=5)

            tel_entry = ttk.Entry(add_window)
            tel_entry.grid(row=4, column=1, padx=5, pady=5)

            autreInfo_entry = ttk.Entry(add_window)
            autreInfo_entry.grid(row=5, column=1, padx=5, pady=5)

            # Ajouter un bouton pour enregistrer les informations dans la base de données
            save_button = ttk.Button(add_window, text="Enregistrer", command=save_Employe)
            save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

            ret_button = ttk.Button(add_window, text="Quitter", command=add_window.destroy)
            ret_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10, sticky="ew")


        add_produit_button = ttk.Button(root,width=20, text="Ajouter un Employé", command=add_Employe)
        add_produit_button.place(x=5, y=140)
    # Création du bouton de recherche
        def close_app():
            result = messagebox.askquestion("Fermer", "Voulez-vous vraiment fermer l'application?")
            if result == 'yes':
                root.destroy()    
# Définition de la fonction on_select au niveau global
        def on_select(event):
            selected_item = tree.selection()[0]  # Obtenir l'élément sélectionné dans le TreeView
            values = tree.item(selected_item, 'values')  # Obtenir les valeurs de l'élément sélectionné
            print("Element sélectionné :", values)  # Afficher les valeurs dans la console (vous pouvez les utiliser comme nécessaire)

        def populate_combo():
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()
            cursor.execute("SELECT nameComplet FROM Employes")
            rows = cursor.fetchall()
            conn.close()

            # Récupérer uniquement les noms des produits à partir des résultats de la requête
            product_names = [row[0] for row in rows]

            # Mettre à jour les valeurs de la Combobox avec les noms des produits
            combo['values'] = product_names

        def search_keyword():
            keyword = combo.get()
            
            # Effacer les résultats précédents dans le TreeView
            tree.delete(*tree.get_children())
            
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()
            
            # Requête pour rechercher les résultats correspondants au nom dans la base de données
            cursor.execute("SELECT id,fonction,nameComplet,matricule,Tel, AutreInfo FROM Employes WHERE nameComplet LIKE ?", ('%' + keyword + '%',))
            rows = cursor.fetchall()
            
            # Insérer les résultats dans le TreeView
            for row in rows:
                tree.insert("", tk.END, values=row)
            
            conn.close()

            # Sélectionner automatiquement le premier élément dans le TreeView s'il existe
            if rows:
                tree.selection_set(tree.get_children()[0])

        # Créer une liaison de sélection au TreeView pour appeler une fonction lorsque la sélection change
        tree.bind("<<TreeviewSelect>>", on_select)

        # Appeler la fonction pour remplir la Combobox avec les noms des produits
        populate_combo()
        search_button = ttk.Button(root, text="Rechercher", command=search_keyword)
        search_button.place(x=150, y=8)
        # Fonction de fermeture de l'application
        search_button = ttk.Button(root, text="Rechercher", command=search_keyword)
        search_button.place(x=150, y=8)
            # Création du bouton de fermeture
        close_button = ttk.Button(root,width=20, text="Fermer", command=close_app)
        close_button.place(x=5, y=230)
        def save():
            messagebox.showinfo("Succès", "Opération effectuée avec succès!")
        
        save_button = ttk.Button(root,width=20, text="Enregistrer", command=save)
        save_button.place(x=5, y=200)

        def modify_Employe():
            selected_item = tree.selection()
            if selected_item:
                values = tree.item(selected_item)['values']
                if values:
                    selected_id = values[0]  # Supposons que l'ID est le premier élément dans vos données
                    selected_employe = None
                    for employe in Employes:
                        if employe[0] == selected_id:  # Assurez-vous que l'ID correspond
                            selected_employe = employe
                            break


                    # Vérifier si l'produit existe dans la liste d'Produits en utilisant soit le prix, soit le nom
                    if selected_employe:
                        # Créer une fenêtre de modification
                        # Créer une nouvelle fenêtre pour modifier les informations de l'employé
                        modify_window = tk.Toplevel(root)
                        modify_window.geometry("350x280")
                        modify_window.title("Modifier un Employé")

                        # Calculer les coordonnées pour centrer la fenêtre sur l'écran
                        window_width = modify_window.winfo_reqwidth()
                        window_height = modify_window.winfo_reqheight()
                        position_right = int(modify_window.winfo_screenwidth() / 2 - window_width / 2)
                        position_down = int(modify_window.winfo_screenheight() / 2 - window_height / 2)

                        # Définir la position de la fenêtre
                        modify_window.geometry("+{}+{}".format(position_right, position_down))

                        # Titre centré en haut de la fenêtre
                        title_label = ttk.Label(modify_window, text="Modifier un Employé", font=("Helvetica", 14, "bold"))
                        title_label.grid(row=0, column=0, columnspan=2, padx=(85, 20), sticky="nsew")

                        # Utilisation d'une grille pour disposer les éléments de manière plus organisée
                        fonction_label = ttk.Label(modify_window, text="Fonction actuelle :")
                        fonction_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

                        nameComplet_label = ttk.Label(modify_window, text="Nom actuel :")
                        nameComplet_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

                        matricule_label = ttk.Label(modify_window, text="Matricule actuel :")
                        matricule_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

                        tel_label = ttk.Label(modify_window, text="Téléphone actuel :")
                        tel_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

                        autreInfo_label = ttk.Label(modify_window, text="Autres informations actuelles :")
                        autreInfo_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

                        # Entry Widgets
                        fonction_entry = ttk.Entry(modify_window)
                        fonction_entry.insert(tk.END, selected_employe[1])
                        fonction_entry.grid(row=1, column=1, padx=5, pady=5)

                        nameComplet_entry = ttk.Entry(modify_window)
                        nameComplet_entry.insert(tk.END, selected_employe[2])
                        nameComplet_entry.grid(row=2, column=1, padx=5, pady=5)

                        matricule_entry = ttk.Entry(modify_window)
                        matricule_entry.insert(tk.END, selected_employe[3])
                        matricule_entry.grid(row=3, column=1, padx=5, pady=5)

                        tel_entry = ttk.Entry(modify_window)
                        tel_entry.insert(tk.END, selected_employe[4])
                        tel_entry.grid(row=4, column=1, padx=5, pady=5)

                        autreInfo_entry = ttk.Entry(modify_window)
                        autreInfo_entry.insert(tk.END, selected_employe[5])
                        autreInfo_entry.grid(row=5, column=1, padx=5, pady=5)


                        def update_Employe():
                            new_fonction = fonction_entry.get()
                            new_nameComplet = nameComplet_entry.get()
                            new_matricule = matricule_entry.get()
                            new_Tel = tel_entry.get()
                            new_AutreInfo = autreInfo_entry.get()

                            # Créer un nouveau tuple avec les valeurs mises à jour
                            updated_employe = (selected_id,new_fonction, new_nameComplet, new_matricule, new_Tel, new_AutreInfo)

                                                        # Trouver l'index du produit dans la liste Products
                            index = Employes.index(selected_employe)

                            # Remplacer l'ancien tuple par le nouveau dans la liste Products
                            Employes[index] = updated_employe

 

                            # Mettre à jour la Treeview avec les nouvelles valeurs
                            conn = sqlite3.connect('gestionStock.db')
                            cursor = conn.cursor()
                            # Mettre à jour les données dans la base de données
                            cursor.execute("UPDATE Employes SET fonction = ?, nameComplet = ?, matricule = ?, Tel = ?, AutreInfo = ? WHERE id = ?", (new_fonction, new_nameComplet, new_matricule, new_Tel, new_AutreInfo,selected_id))
                            conn.commit()
                            conn.close()
                            tree.item(selected_item, values=updated_employe)

                            # Fermer la fenêtre
                            modify_window.destroy()


                        # Bouton pour enregistrer les modifications
                        update_button = ttk.Button(modify_window, text="Enregistrer", command=update_Employe)
                        update_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

                        # Bouton pour quitter
                        ret_button = ttk.Button(modify_window, text="Quitter", command=modify_window.destroy)
                        ret_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

                    else:
                        # Afficher un message d'erreur si l'produit n'est pas trouvée dans la liste d'Produits
                        messagebox.showerror("Erreur", "produit introuvable dans la liste d'Produits.")
                else:
                    # Afficher un message d'erreur si aucune produit n'est sélectionnée dans la Treeview
                    messagebox.showerror("Erreur", "Aucune produit sélectionnée.")
            else:
                # Afficher un message d'erreur si aucune produit n'est sélectionnée dans la Treeview
                messagebox.showerror("Erreur", "Aucune produit sélectionnée.")

        modify_button = ttk.Button(root,width=20, text="Modifier un Employé", command=modify_Employe)
        modify_button.place(x=5, y=110)
        def delete_Employe():
            selected_items = tree.selection()
            if selected_items:
                for item in selected_items:
                    values = tree.item(item)['values']
                    if values:
                        selected_id = values[0]

                        # Supprimer la commande correspondante de la base de données
                        cursor.execute("DELETE FROM Employes WHERE id=?", (selected_id,))

                        # Confirmer la transaction
                        conn.commit()

                        # Supprimer la ligne de Treeview
                        tree.delete(item)

                # Actualiser les données dans le Treeview
                tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
                cursor.execute('SELECT id,fonction,nameComplet,matricule,Tel, AutreInfo FROM Employes')
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)
            else:
                print("No item selected in Treeview!")
                

        delete_produit_button = ttk.Button(root, text="Supprimer un Employé", command=delete_Employe)
        delete_produit_button.place(x=5, y=170)
        root.mainloop()

        # Fermer la connexion à la base de données SQLite3
        conn.close()
#----------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    def ouvrir_fenetre_order(self, event=None):
        import tkinter as tk
        from tkinter import ttk
        from tkinter import messagebox
        import sqlite3
        def cancel_order():
            # Fonction pour annuler la commande
            response = messagebox.askyesno("Confirmation", "Voulez-vous vraiment quitter ?")
            if response:
                root.destroy()
        def order():
            employee_name = employee_var.get()
            product_name = product_var.get()
            quantity = quantity_entry.get()
            # Vérifier si les champs sont vides
            if not employee_name or not product_name or not quantity:
                messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
                return

            # Se connecter à la base de données
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()

            # Récupérer l'ID de l'employé sélectionné
            cursor.execute("SELECT id FROM Employes WHERE nameComplet = ?", (employee_name,))
            id_employe = cursor.fetchone()
            if not id_employe:
                messagebox.showerror("Erreur", "Employé introuvable.")
                conn.close()
                return

            # Récupérer l'ID du produit sélectionné et sa quantité en stock
            cursor.execute("SELECT id, Quantite FROM Products WHERE name = ?", (product_name,))
            product = cursor.fetchone()
            if not product:
                messagebox.showerror("Erreur", "Produit introuvable.")
                conn.close()
                return
            elif int(product[1]) < int(quantity):
                messagebox.showerror("Erreur", "Quantité insuffisante en stock.")
                conn.close()
                return

            # Passer la commande et mettre à jour la quantité
            new_quantity = int(product[1]) - int(quantity)
            cursor.execute("UPDATE Products SET Quantite = ? WHERE id = ?", (new_quantity, product[0]))

            # Enregistrer la commande
            cursor.execute("INSERT INTO Commandes (id_employe, id_produit, quantite,date_commande) VALUES (?, ?, ?,?)", (id_employe[0], product[0], quantity,datetime.now().strftime("%A, %B %Y %H:%M:%S")))

            # Commit des changements et fermeture de la connexion à la base de données
            conn.commit()
            conn.close()

            # Afficher un message de succès
            messagebox.showinfo("Succès", "Commande passée avec succès!")

        

        conn = sqlite3.connect('gestionStock.db')
        cursor = conn.cursor()

        # Récupérer la liste des noms d'employés
        cursor.execute("SELECT nameComplet FROM Employes")
        employees = [row[0] for row in cursor.fetchall()]

        # Récupérer la liste des noms de produits
        cursor.execute("SELECT name FROM Products")
        products = [row[0] for row in cursor.fetchall()]

        conn.close()
        root = tk.Tk()
        root.title("Passer une Commande")
        root.geometry('400x200')

        employee_var = tk.StringVar(root)
        employee_label = ttk.Label(root, text="Nom de l'Employé :")
        employee_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        employee_menu = ttk.Combobox(root, textvariable=employee_var, values=employees, state="readonly")
        employee_menu.grid(row=0, column=1, padx=5, pady=5)

        product_var = tk.StringVar(root)
        product_label = ttk.Label(root, text="Nom du Produit :")
        product_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        product_menu = ttk.Combobox(root, textvariable=product_var, values=products, state="readonly")
        product_menu.grid(row=1, column=1, padx=5, pady=5)

        quantity_label = ttk.Label(root, text="Quantité :")
        quantity_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
        quantity_entry = ttk.Entry(root)
        quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        order_button = ttk.Button(root, text="Passer la Commande", command=order)
        order_button.grid(row=3, columnspan=2, padx=5, pady=5)

        cancel_button = ttk.Button(root, text="Quitter", command=cancel_order)
        cancel_button.grid(row=4, column=0, padx=5, pady=5)


        root.mainloop()
    #----------------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------------------------------------------------------------------------------------------------------
    def ouvrir_fenetre_Historique(self, event=None):
        import tkinter as tk
        from tkinter import ttk
        import sqlite3
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
        from reportlab.lib import colors

        # Fonction pour remplir le Treeview avec les données des commandes
        def fill_tree(tree, rows):
            # Insertion des données dans le Treeview
            for row in rows:
                tree.insert("", tk.END, values=row)

        # Fonction pour exporter les données au format PDF
        def export_to_pdf(rows):
            # Création du document PDF
            pdf_filename = "historique_commandes.pdf"
            pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)
            
            # Définition des données à inclure dans le tableau
            table_data = [["Id","Employé", "Produit", "Quantité", "Date de Commande"]] + rows
            
            # Création du tableau dans le document PDF
            table = Table(table_data)
            
            # Style du tableau
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])
            table.setStyle(style)
            
            # Construction du PDF
            pdf.build([table])
            
            # Message de confirmation
            print(f"Le fichier PDF '{pdf_filename}' a été créé avec succès!")

        # Création de la fenêtre
        historique_window = tk.Toplevel()
        historique_window.title("Historique des Commandes")
        historique_window.geometry('800x400')

        # Création du Treeview pour afficher les données
        tree = ttk.Treeview(historique_window, columns=("ID", "Employé", "Produit", "Quantité", "Date de Commande"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Employé", text="Employé")
        tree.heading("Produit", text="Produit")
        tree.heading("Quantité", text="Quantité")
        tree.heading("Date de Commande", text="Date de Commande")
        tree.pack(expand=True, fill="both")

        # Récupération des données de la base de données
        conn = sqlite3.connect('gestionStock.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Commandes.id, Employes.nameComplet, Products.name, Commandes.quantite, Commandes.date_commande 
                        FROM Commandes 
                        INNER JOIN Employes ON Commandes.id_employe = Employes.id 
                        INNER JOIN Products ON Commandes.id_produit = Products.id''')
        rows = cursor.fetchall()
        conn.close()

        # Remplissage du Treeview avec les données des commandes
        fill_tree(tree, rows)

        # Bouton pour exporter les données au format PDF
        export_button = ttk.Button(historique_window, text="Exporter en PDF", command=lambda: export_to_pdf(rows))
        export_button.pack()
    #----------------------------------------------------------------------------------------------------------------------------------------

    #----------------------------------------------------------------
    def ouvrir_fenetre_Fournisseur(self, event=None):
        import tkinter as tk
        from tkinter import ttk
        from tkinter import messagebox
        import sqlite3
        from datetime import datetime
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
        from reportlab.lib import colors
        from reportlab.lib.styles import getSampleStyleSheet
        import random
        import string
        from reportlab.lib.utils import ImageReader
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.platypus import Spacer
        root = tk.Tk()
        root.title("Sélection du Fournisseur")
        root.geometry('2150x320')
# Set background color
        root.configure(bg='lightblue')
        frame = tk.Frame(root, bd=2, relief='ridge')  # Ajoute un cadre avec une bordure et un relief
        frame.place(x=280, y=10)

        # Création du Treeview pour afficher les commandes réservées
        tree = ttk.Treeview(frame, columns=("ID", "Nom Produit", "Quantité", "Remarque", "Date de Création"), show="headings",selectmode='extended')
        tree.heading("ID", text="ID")
        tree.heading("Nom Produit", text="Nom Produit")
        tree.heading("Quantité", text="Quantité")
        tree.heading("Remarque", text="Remarque")
        tree.heading("Date de Création", text="Date de Création")
        for col in tree['columns']:
            tree.column(col, anchor='center')

        tree.pack(fill='both', expand=True)

        # Connexion à la base de données
        conn = sqlite3.connect('gestionStock.db')
        cursor = conn.cursor()
        FourniseuCommends = []
        cursor.execute('SELECT id, NomProduitF, Quantite, Remarques, DateCreation FROM Fournisseur')
        rows = cursor.fetchall()
        for row in rows:
            FourniseuCommends.append((row[0], row[1],row[2],row[3],row[4]))
            tree.insert("", tk.END, values=row)
        
        
        # Sélection du produit
        combo = ttk.Combobox(root, values=[produit[0] for produit in FourniseuCommends])
        combo.place(x=5, y=10)
        def add_produitFoornisseur():
            def save_produit():
                now = datetime.now().strftime("%B %Y %H:%M:%S")
                new_name = name_entry.get()
                new_quantite = quantite_entry.get()
                new_remarque = remarque_entry.get()

                # Ajouter la nouvelle produit à la liste d'Products
                FourniseuCommends.append((new_name, new_quantite, new_remarque, now))

                # Ajouter la nouvelle ligne à la Treeview
                tree.insert("", tk.END, values=(new_name, new_quantite, new_remarque, now))

                # Enregistrer les modifications dans la base de données
                cursor.execute("INSERT INTO Fournisseur (NomProduitF, Quantite, Remarques, DateCreation) VALUES (?, ?, ?, ?)",
                            (new_name, new_quantite, new_remarque, now))
                conn.commit()
            # Actualiser les données dans le Treeview
                tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
                cursor.execute('SELECT id, NomProduitF, Quantite, Remarques, DateCreation FROM Fournisseur')
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)

                # Fermer la fenêtre
                add_window.destroy()

            # Créer une nouvelle fenêtre pour saisir le nom, la quantité et la remarque de la nouvelle produit
            # Créer une nouvelle fenêtre pour saisir le nom, la quantité et la remarque du nouveau produit
            # Créer une nouvelle fenêtre pour saisir le nom, la quantité et la remarque du nouveau produit
            add_window = tk.Toplevel(root)
            add_window.geometry("500x200")
            add_window.title("Ajouter un produit")

            # Calculer les coordonnées pour centrer la fenêtre sur l'écran
            window_width = add_window.winfo_reqwidth()
            window_height = add_window.winfo_reqheight()
            position_right = int(add_window.winfo_screenwidth() / 2 - window_width / 2)
            position_down = int(add_window.winfo_screenheight() / 2 - window_height / 2)

            # Définir la position de la fenêtre
            add_window.geometry("+{}+{}".format(position_right, position_down))

            # Ajouter une marge autour du formulaire
            add_window.grid_rowconfigure(0, weight=1)
            add_window.grid_rowconfigure(5, weight=1)
            add_window.grid_columnconfigure(0, weight=1)
            add_window.grid_columnconfigure(2, weight=1)

            # Titre centré en haut de la fenêtre
            title_label = ttk.Label(add_window, text="Ajouter un produit", font=("Helvetica", 14, "bold"))
            title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="nsew")  # Utilisation de sticky pour centrer

            # Utilisation d'une grille pour disposer les éléments de manière plus organisée
            name_label = ttk.Label(add_window, text="Nom du nouveau produit:")
            name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

            quantite_label = ttk.Label(add_window, text="Quantité du nouveau produit:")
            quantite_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

            remarque_label = ttk.Label(add_window, text="Remarque sur le nouveau produit:")
            remarque_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

            # Entry Widgets
            name_entry = ttk.Entry(add_window)
            name_entry.grid(row=1, column=1, padx=5, pady=5)

            quantite_entry = ttk.Entry(add_window)
            quantite_entry.grid(row=2, column=1, padx=5, pady=5)

            remarque_entry = ttk.Entry(add_window)
            remarque_entry.grid(row=3, column=1, padx=5, pady=5)

            # Ajouter un bouton pour enregistrer la modification dans la base de données
            save_button = ttk.Button(add_window, text="Enregistrer", command=save_produit)
            save_button.grid(row=4, column=0, padx=5, pady=10, sticky="ew")

            ret_button = ttk.Button(add_window, text="Quitter", command=add_window.destroy)
            ret_button.grid(row=4, column=1, padx=5, pady=10, sticky="ew")


        def search_keyword():

            keyword = combo.get()
            # Effacer les résultats précédents dans le TreeView
            tree.delete(*tree.get_children())
            conn = sqlite3.connect('gestionStock.db')
            cursor = conn.cursor()
            # Requête pour rechercher les résultats correspondants dans la base de données
            cursor.execute("SELECT NomProduitF FROM Fournisseur WHERE NomProduitF LIKE ?", ('%'+keyword+'%',))
            rows = cursor.fetchall()
            # Insérer les résultats dans le TreeView
            for row in rows:
                tree.insert("", tk.END, values=row)
            conn.close()


        def export_to_pdf():
            # Actualiser les données dans le Treeview
            tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
            cursor.execute('SELECT id, NomProduitF, Quantite, Remarques, DateCreation FROM Fournisseur')
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row)

            # Créer un nom de fichier aléatoire pour le PDF
            random_filename = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".pdf"
            pdf_filename = random_filename
            pdf = SimpleDocTemplate(pdf_filename, pagesize=letter)

            # Préparation des données à inclure dans le tableau
            table_data = [["Nom Produit", "Quantité", "Remarques"]]
            for item in tree.get_children():
                values = tree.item(item)['values']
                if values:
                    nom_produit = values[1]
                    quantite = values[2]
                    remarques = values[3]
                    table_data.append([nom_produit, quantite, remarques])

            # Création du tableau dans le document PDF
            table = Table(table_data)

            # Style du tableau
            style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                ('GRID', (0, 0), (-1, -1), 1, colors.black)])
            table.setStyle(style)

        # Ajouter le logo
            logo_image_path = 'img/logo2023.png'  # Spécifiez le chemin de votre fichier image
            logo = Image(logo_image_path, width=100, height=100)  # Ajustez la largeur et la hauteur selon vos besoins

            
            styleSheet = getSampleStyleSheet()
            # Informations du fournisseur
            infos_fournisseur = [
                Paragraph("Nom du fournisseur : ...............", styleSheet['Normal']),
                Paragraph("Signature du fournisseur : ..........", styleSheet['Normal'])
            ]

            # Informations du responsable
            info_responsable = [
                Paragraph("Nom du responsable :..................", styleSheet['Normal']),
                Paragraph("Signature du responsable : ............", styleSheet['Normal'])
            ]

            # Espacement entre les deux ensembles d'informations
            spacer = Spacer(width=100, height=12)

            # Construction du PDF
            elements = [
                logo,
                spacer,
                table,
                [
                    info_responsable,  # Informations du responsable à gauche
                    spacer,  # Espacement entre les informations
                    infos_fournisseur,  # Informations du fournisseur à droite
                ],
                [
                    Spacer(1, 12),  # Espacement entre les informations et les signatures
                    Table([[Paragraph("Signature du responsable : ____________________", styleSheet['Normal']),
                            Paragraph("Signature du fournisseur : ____________________", styleSheet['Normal'])]],
                        colWidths=[250, 250])
                ]
            ]

            # Construction du PDF
            elements = [logo, table]+info_responsable + infos_fournisseur
            pdf.build(elements)

            # Affichage d'une boîte de message de confirmation
            messagebox.showinfo("Succès", f"Le fichier PDF '{pdf_filename}' a été créé avec succès!")
        # Bouton pour exporter en PDF
        def modify_produitFournisseur():
            selected_item = tree.selection()
            if selected_item:
                values = tree.item(selected_item)['values']
                if values:
                    selected_id = values[0]  # Supposons que l'ID est le premier élément dans vos données
                    selected_produit = None

                    for produit in FourniseuCommends:
                        if produit[0] == selected_id:  # Assurez-vous que l'ID correspond
                            selected_produit = produit
                            break

                    if selected_produit:
                        # Créer une nouvelle fenêtre pour modifier le nom, la quantité et la remarque du produit sélectionné
                        modify_window = tk.Toplevel(root)
                        modify_window.geometry("300x400")
                        modify_window.title("Modifier une Produit")

                        # Calculer les coordonnées pour centrer la fenêtre sur l'écran
                        window_width = modify_window.winfo_reqwidth()
                        window_height = modify_window.winfo_reqheight()
                        position_right = int(modify_window.winfo_screenwidth() / 2 - window_width / 2)
                        position_down = int(modify_window.winfo_screenheight() / 2 - window_height / 2)

                        # Définir la position de la fenêtre
                        modify_window.geometry("+{}+{}".format(position_right, position_down))

                        # Ajouter une marge autour du formulaire
                        modify_window.grid_rowconfigure(0, weight=1)
                        modify_window.grid_rowconfigure(7, weight=1)
                        modify_window.grid_columnconfigure(0, weight=1)
                        modify_window.grid_columnconfigure(2, weight=1)

                        # Titre centré en haut de la fenêtre
                        title_label = ttk.Label(modify_window, text="Modifier une Produit", font=("Helvetica", 14, "bold"))
                        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=(50, 20), sticky="nsew")  # Utilisation de sticky pour centrer

                        # Utilisation d'une grille pour disposer les éléments de manière plus organisée
                        name_label = ttk.Label(modify_window, text="Nom actuel:")
                        name_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

                        quantite_label = ttk.Label(modify_window, text="Quantité actuelle:")
                        quantite_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

                        remarque_label = ttk.Label(modify_window, text="Remarque actuelle:")
                        remarque_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

                        # Entry Widgets
                        name_entry = ttk.Entry(modify_window)
                        name_entry.insert(tk.END, selected_produit[1])  # Insérer le nom du produit
                        name_entry.grid(row=1, column=1, padx=5, pady=5)

                        quantite_entry = ttk.Entry(modify_window)
                        quantite_entry.insert(tk.END, selected_produit[2])  # Insérer la quantité du produit
                        quantite_entry.grid(row=2, column=1, padx=5, pady=5)

                        remarque_entry = ttk.Entry(modify_window)
                        remarque_entry.insert(tk.END, selected_produit[3])  # Insérer la remarque sur le produit
                        remarque_entry.grid(row=3, column=1, padx=5, pady=5)

                        # Ajouter un bouton pour enregistrer les modifications dans la base de données

                        def update_produit():
                            new_name = name_entry.get()
                            new_quantite = quantite_entry.get()
                            new_remarque = remarque_entry.get()

                            # Créer un nouveau tuple avec les valeurs mises à jour
                            updated_produit = (selected_id, new_name, new_quantite,new_remarque)

                            # Trouver l'index du produit dans la liste Products
                            index = FourniseuCommends.index(selected_produit)

                            # Remplacer l'ancien tuple par le nouveau dans la liste Products
                            FourniseuCommends[index] = updated_produit

                            # Mettre à jour le produit dans la base de données
                            if new_remarque:  # Vérifier si le champ remarque est vide ou non
                                cursor.execute("UPDATE Fournisseur SET NomProduitF = ?, Quantite = ?, Remarques = ? WHERE id = ?",
                                            (new_name, new_quantite, new_remarque, selected_id))
                            else:
                                cursor.execute("UPDATE Fournisseur SET NomProduitF = ?, Quantite = ? WHERE id = ?",
                                            (new_name, new_quantite, selected_id))
                            conn.commit()
                            # Mettre à jour la Treeview avec les nouvelles valeurs
                            tree.item(selected_item, values=updated_produit)

                            # Fermer la fenêtre de modification
                            modify_window.destroy()


                        update_button = ttk.Button(modify_window, text="Enregistrer",  command=update_produit)
                        update_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")

                        # Bouton pour quitter
                        ret_button = ttk.Button(modify_window, text="Quitter", command=modify_window.destroy)
                        ret_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="ew")



                    else:
                        # Afficher un message d'erreur si le produit n'est pas trouvé
                        messagebox.showerror("Erreur", "Produit introuvable.")
                else:
                    # Afficher un message d'erreur si aucune produit n'est sélectionnée dans la Treeview
                    messagebox.showerror("Erreur", "Aucune produit sélectionnée.")
            else:
                # Afficher un message d'erreur si aucune produit n'est sélectionnée dans la Treeview
                messagebox.showerror("Erreur", "Aucune produit sélectionnée.")
        # Fonction pour supprimer une produit sélectionnée
        def delete_produit():
            selected_items = tree.selection()
            if selected_items:
                for item in selected_items:
                    values = tree.item(item)['values']
                    if values:
                        selected_id = values[0]

                        # Supprimer la commande correspondante de la base de données
                        cursor.execute("DELETE FROM Fournisseur WHERE id=?", (selected_id,))

                        # Confirmer la transaction
                        conn.commit()

                        # Supprimer la ligne de Treeview
                        tree.delete(item)

                # Actualiser les données dans le Treeview
                tree.delete(*tree.get_children())  # Supprimer toutes les lignes actuelles du Treeview
                cursor.execute('SELECT id, NomProduitF, Quantite, Remarques, DateCreation FROM Fournisseur')
                rows = cursor.fetchall()
                for row in rows:
                    tree.insert("", tk.END, values=row)
            else:
                print("No item selected in Treeview!")

        def ajouter_produitAustockProdui():
            # Obtenir l'ID de la ligne sélectionnée dans le Treeview
            selected_items = tree.selection()
            
            if selected_items:
                for item in selected_items:

                # Obtenir les valeurs de la ligne sélectionnée
                    values = tree.item(item)['values']
                
                    if values and len(values) >= 3:  # Vérifier que values contient au moins 3 éléments (ID, Nom, Quantité)
                        # Récupérer le nom et la quantité du produit sélectionné
                        nom_produit = values[1]  # Supposons que le nom du produit soit le deuxième élément dans vos données
                        quantite_produit = values[2]  # Supposons que la quantité du produit soit le troisième élément dans vos données
                        
                        # Vérifier si le produit existe déjà dans la table Products
                        cursor.execute("SELECT * FROM Products WHERE name=?", (nom_produit,))
                        existing_product = cursor.fetchone()
                        
                        if existing_product:
                            # Si le produit existe, mettre à jour la quantité en ajoutant la quantité de la table Fournisseur
                            nouvelle_quantite = int(existing_product[3]) + quantite_produit  # Indice 3 pour la quantité
                            cursor.execute("UPDATE Products SET Quantite=? WHERE name=?", (nouvelle_quantite, nom_produit))
                        else:
                            # Si le produit n'existe pas, l'ajouter à la table Products
                            cursor.execute("INSERT INTO Products (name, Quantite, Prix, Description) VALUES (?, ?, '', '')", (nom_produit, quantite_produit))
                        
                        # Confirmer la transaction
                        conn.commit()
                        
                        # Supprimer le produit de la table Fournisseur
                        selected_id = values[0]  # Récupérer l'ID du produit sélectionné
                        cursor.execute("DELETE FROM Fournisseur WHERE id=?", (selected_id,))
                        conn.commit()
                        
                        
                    else:
                        messagebox.showerror("Erreur", "Les données sélectionnées ne sont pas complètes.")
            # Mettre à jour le Treeview
            else:
                messagebox.showerror("Erreur", "Aucun produit sélectionné dans le Treeview.")
            remplir_treeview()

        def remplir_treeview():
            # Supprimer toutes les lignes actuelles du Treeview
            for row in tree.get_children():
                tree.delete(row)

            # Récupérer les données de la base de données et les afficher dans le Treeview
            cursor.execute('SELECT id, NomProduitF, Quantite, Remarques, DateCreation FROM Fournisseur')
            rows = cursor.fetchall()
            for row in rows:
                tree.insert("", tk.END, values=row[:-1], iid=row[0], tags=("commande",), open=True)
        remplir_treeview()

        def close_app():
            result = messagebox.askquestion("Fermer", "Voulez-vous vraiment fermer l'application?")
            if result == 'yes':
                root.destroy()    

    #----------------------------------------------------------------------------------------------------------------------------------------
        add_produitFoornisseur_button = ttk.Button(root, width=20, text="Ajouter une Produit", command=add_produitFoornisseur)
        add_produitFoornisseur_button.place(x=5, y=140)

        search_button = ttk.Button(root, text="Rechercher", command=search_keyword)
        search_button.place(x=150, y=8)

        modify_button = ttk.Button(root, width=20, text="Modifier le Produit", command=modify_produitFournisseur)
        modify_button.place(x=5, y=110)

        delete_button = ttk.Button(root, width=20, text="Supprimer le Produit", command=delete_produit)
        delete_button.place(x=5, y=170)   
        
        AjtStockbutton = ttk.Button(root, width=20, text="AjtStock", command=ajouter_produitAustockProdui)
        AjtStockbutton.place(x=280, y=250)

        export_button = ttk.Button(root, text="Exporter en PDF", command=export_to_pdf)
        export_button.place(x=1190, y=250)

        close_button = ttk.Button(root,width=20, text="Fermer", command=close_app)
        close_button.place(x=1250, y=295)


    def resize(self, event):
        self.reposition_elements()
    #----------------------------------------------------------------------------------------------------------------------------------------

    def reposition_elements(self):
        # Obtenir les dimensions de la fenêtre parente
        width = self.admin_window.winfo_width()
        height = self.admin_window.winfo_height()
        # Repositionner les éléments
        self.admin_canvas.coords(self.text_canvas, width/2, 150)
        self.admin_canvas.coords(self.logo_label, width * 0.05, height * 0.02)
        self.admin_canvas.coords(self.clock_label, width * 0.85, 20)
        self.quit_button.place(relx=0.85, rely=0.4)
        self.bouton1.place(relx=0.85, rely=0.35)
        self.bouton2.place(relx=0.85, rely=0.3)
        self.bouton3.place(relx=0.85, rely=0.25)
        self.bouton4.place(relx=0.85, rely=0.40)
        self.bouton5.place(relx=0.85, rely=0.45)
        self.boutonF.place(relx=0.85, rely=0.55)
    #----------------------------------------------------------------------------------------------------------------------------------------


window.mainloop()