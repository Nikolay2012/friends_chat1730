import customtkinter as ctk
import modules.text_input as m_input
import modules.image_frame as m_img_frame
import modules.screen_app as m_app

sender_font = ctk.CTkFont(family= 'Calibri', size= 20, weight= 'bold')
sender_text_font = ctk.CTkFont(family= 'Calibri', size= 15, weight= 'normal')

class MessageFrame(ctk.CTkFrame):
    def __init__(self, sender, text, width, height, master, border_width, fg_color, bg_color, **kwargs):
        super().__init__(master= master, width= width, height= height, border_width= border_width, fg_color= fg_color, bg_color= bg_color, **kwargs)
        
        # self.IMAGE_FRAME = self.create_image(image= m_img_frame.image_message)
        
        self.SENDER = self.message_name_label(text= sender, text_color= 'black', fg_color= 'transparent')
        self.MESSAGE = self.message_text_label(text= text, text_color= 'black', fg_color= 'transparent')
        #
        # self.IMAGE_FRAME.place(x=0, y=0)
        
        self.SENDER.place(x= 10, y= 10)
        self.MESSAGE.place(x= 10, y= 40)
    
    def message_name_label(self, text, text_color, fg_color):
        return ctk.CTkLabel(
            master= self,
            text= text,
            font= sender_font,
            text_color= text_color,
            fg_color= fg_color,
            bg_color= 'transparent',
            # image= m_img_frame.image_message
            )
    #
    def message_text_label(self, text, text_color, fg_color):
        return ctk.CTkLabel(
            master= self,
            text= text,
            font= sender_text_font,
            text_color= text_color,
            fg_color= fg_color,
            bg_color= 'transparent'
        )
    #
    # def create_image(self, image):
        # bg_image_label = ctk.CTkLabel(master=self, text='', image=image)
        # return bg_image_label
#
message_frame = MessageFrame(
    sender= 'Николай',
    text= '123',
    width= m_img_frame.image_width,
    height= m_img_frame.image_height,
    master= m_app.main_app.FRAME4,
    border_width= 5,
    fg_color= 'Moccasin',
    bg_color= 'transparent'
)

message_frame2 = MessageFrame(
    sender= 'Максим',
    text= '123',
    width= m_img_frame.image_width,
    height= m_img_frame.image_height,
    master= m_app.main_app.FRAME4,
    border_width= 5,
    fg_color= 'Moccasin',
    bg_color= 'transparent'
)

message_frame.place(x= 10, y= 10, anchor=ctk.NW)
message_frame2.place(x= m_app.main_app.FRAME4._current_width - 10, y= 120, anchor= ctk.NE)
