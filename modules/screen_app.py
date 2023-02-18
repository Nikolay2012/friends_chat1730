import customtkinter
import modules.create_frame as m_frame
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
        self.resizable(False, False)
        self.title("Головне вікно програми")
        self.FRAME = m_frame.My_Frame(text= "Friendly Chat", master = self, width= 130, height= app_height - 20, border_width= 5)
        # self.FRAME = customtkinter.CTkFrame(master=self, width=300, height= app_height)
        
        self.FRAME.grid(row = 0, column = 0, padx = 20, pady = 10)
        # self.FRAME.pack(padx= 10, pady = 10, expand = True)
        # self.FRAME.place(relx = 0, rely= 0)

main_app = App(800, 600)