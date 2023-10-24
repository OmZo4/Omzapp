import tkinter as tk
import customtkinter as ctk
import loginpage as lgp
#import helper_functions as hf


ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


class ToDoList(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("OMZAPP BETA")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(( 3), weight=1)
        self.grid_columnconfigure((0,1, 2), weight=0)
        self.grid_rowconfigure((0, 1), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=f"OMZAPP BETA\n By Omzo", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="To Do App")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Coming soon")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="LOG OUT", command=self.go_back_home)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # creating widget for .self
        self.textbox = ctk.CTkTextbox(self, font=("arial", 20), fg_color="black", border_color="green", text_color="green")
        self.textbox.grid(row=0, column=3, columnspan=4,rowspan=3, padx=(20, 20), pady=(20, 0), sticky="nsew", command=self.show_txt())

        self.entry = ctk.CTkEntry(self, placeholder_text="Enter your idea")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", width=2, border_width=2, text="ADD", command=self.add_todo)
        self.main_button_1.grid(row=2, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_3 = ctk.CTkButton(master=self, fg_color="transparent", width=2, border_width=2, text="DEL", command=self.delete_item)
        self.main_button_3.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_button_2 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text="SAVE", command=self.save_txt)
        self.main_button_2.grid(row=3, column=3,columnspan=4, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.listbox = tk.Listbox(self,width=15, font=("arial", 20))
        self.listbox.grid(row=0, column=1, columnspan=2,rowspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")


        self.scrollable_frame_tasks = []
        with open('todo_list.txt', 'r') as f:
            self.scrollable_frame_tasks = [line.strip() for line in f]
        for i in range(len(self.scrollable_frame_tasks)):
            self.listbox.insert(len(self.scrollable_frame_tasks), self.scrollable_frame_tasks[i])

        # set default values
        self.sidebar_button_2.configure(state="disabled")


# functions

    def add_todo(self):
        todo = self.entry.get()
        self.listbox.insert(len(self.scrollable_frame_tasks), todo)
        self.scrollable_frame_tasks.append(todo)
        with open("todo_list.txt", "a") as f:
            f.write(f"\n{todo}")
        self.entry.delete(0, len(todo))

    def delete_item(self):
        item = self.listbox.curselection()
        self.listbox.delete(item[0])
        self.scrollable_frame_tasks.remove(self.scrollable_frame_tasks[item[0]])
        with open("todo_list.txt", "w") as f:
            for line in self.scrollable_frame_tasks:
                f.write(f"{line}\n")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def show_txt(self):
        with open('data.txt', 'r+') as f:
            content = f.read()
            self.textbox.insert('1.0', content)

    def save_txt(self):
        data = self.textbox.get('1.0', 'end')
        filename = "data.txt"

        with open(filename, "w") as f:
            f.write(data)

    def go_back_home(self):
        # Hide the current page instead of destroying it
        self.withdraw()
        # Create a new instance of the HomePage class to show the first page
        app = lgp.HomePage()
        app.mainloop()

