from tkinter import *

import json
from watson_developer_cloud import VisualRecognitionV3
from PIL import Image, ImageTk

visual_recognition = VisualRecognitionV3( '2019-08-24', iam_apikey='Q9KKJtGYkQ1w3celHaxfDxSh9zTl0eRUvquSoY6UJfkx')

with open('in.jpg', 'rb') as images_file:
    faces_json = visual_recognition.detect_faces(images_file).get_result()
#print(json.dumps(faces_json, indent=2))

gender = faces_json["images"][0]["faces"][0]["gender"]["gender"]
print(gender)
def propFem(self):
    load = Image.open("img1.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(self, image=render)
    img.image = render
    img.place(x=0, y=0)

def propMas(self):
    load = Image.open("img2.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(self, image=render)
    img.image = render
    img.place(x=0, y=0)


class Window(Frame):

    def __init__(self, master=None):
       
        Frame.__init__(self, master)
     
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("InTarget")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)
        #if mudar
        if gender == "FEMALE":
            propFem(self)
        else:
            propMas(self)
    def client_exit(self):
        exit()
root = Tk()
#tamanho da tela
root.geometry("1200x720")

app = Window(root)
root.mainloop()  
