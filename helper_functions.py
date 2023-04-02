import customtkinter as ctk
import loginpage as lgp
import todoapp as tda

def change_appearance_mode_event(self, new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)


def change_scaling_event(self, new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)

def go_back_home(self):
    # Hide the current page instead of destroying it
    self.withdraw()
    # Create a new instance of the HomePage class to show the first page
    app = lgp.HomePage()

def goto_todoapp(self):
    # Hide the current page instead of destroying it
    self.withdraw()
    # Create a new instance of the LoginPage class to show the first page
    app = tda.ToDoList()