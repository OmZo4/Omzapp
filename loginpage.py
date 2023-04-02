import customtkinter as ctk
import todoapp as tda

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


class HomePage(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x350")
        self.title("OMZAPP v1.0")

        # create user and paswword
        self.username = "admin"
        self.password = "password"

        # create label and buttonsand entrys for the login page
        self.label = ctk.CTkLabel(self, text="Welcome OMAR")
        self.label.pack(pady=20)

        self.entry1 = ctk.CTkEntry(self, placeholder_text="enter username")
        self.entry1.pack(pady =20)
        self.entry2 = ctk.CTkEntry(self, placeholder_text="enter password")
        self.entry2.pack(pady =20)

        self.button1 = ctk.CTkButton(self, text="LOGIN", command=self.validate_cred)
        self.button1.pack(pady =20)

        self.warning_label = ctk.CTkLabel(self, text=" ")
        self.warning_label.pack(pady=(2, 2))



    def validate_cred(self):
        usertoken = self.entry1.get()
        passtoken = self.entry2.get()
        if usertoken == self.username and passtoken == self.password:
            self.goto_todoapp()
            print("connected")
        else:
            self.warning_label.configure(text="destroying all data in 10s",text_color="red" )
            print("refused")

    def goto_todoapp(self):
        # Hide the current page instead of destroying it
        self.withdraw()
        # Create a new instance of the LoginPage class to show the first page
        app = tda.ToDoList()


if __name__ == "__main__":
    app = HomePage()
    app.mainloop()