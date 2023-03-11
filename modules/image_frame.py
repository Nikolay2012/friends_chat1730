from PIL import Image
import customtkinter as ctk
import modules.find_path_to_file as m_path

image_width = 300
image_height = 100


image_message = ctk.CTkImage(
    light_image= Image.open(m_path.find_path_to_file(filename="images/image_frame.png")),
    size= (image_width, image_height)
)