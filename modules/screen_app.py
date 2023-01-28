import customtkinter
#
class App(customtkinter.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        #
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.title("Головне вікно програми")


main_app = App(800, 600)