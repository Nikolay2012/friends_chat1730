import customtkinter as ctk
import modules.screen_app as m_app

class MessageFrame(ctk.CTkFrame):
    def __init__(self, user_name, message_text, master, width, height, border_width, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, **kwargs)
        self.FONT_MESSAGE = ctk.CTkFont(family="Arial", size=12, weight="normal")
        self.FONT_USERNAME = ctk.CTkFont(family="Arial", size=15, weight="bold")
        self.MESSAGE_LABEL = self.message_label(message_text= message_text)
        self.USER_NAME_LABEL = self.username_label(username= user_name)
        
    
    def message_label(self, message_text):
        
        msg =  ctk.CTkLabel(master= self, text= message_text, font= self.FONT_MESSAGE, bg_color= "transparent")
        msg.place(x=100, y=100)
        return msg
        

    def username_label(self, username):
        user =  ctk.CTkLabel(master=self, text= username, font= self.FONT_USERNAME, text_color="orange", bg_color= "transparent")
        user.place(x= 0, y = 0)
        return user

message = MessageFrame(
    user_name= "User", 
    message_text= "hello, user", 
    master = m_app.main_app.FRAME4, 
    width= 200,
    height = 200,
    border_width= 2
)

message.place(x=m_app.main_app.FRAME4._current_width // 2, y = m_app.main_app.FRAME4._current_height // 2)