import customtkinter
from .read_json import read_json
import json

mainframe = customtkinter.CTk(fg_color="#008000")
#init mainframe 
main_config = read_json(name_file= "config.json")
# print(json.dumps(main_config, indent= 4))
#read json  to config  information 
WIDTH = main_config["main_frame"]["width"]
HEIGHT = main_config["main_frame"]["height"]
# init constants
mainframe.geometry(f"{WIDTH}x{HEIGHT}")