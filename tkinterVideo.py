from tkinter import *
from PIL import ImageTk, Image
import cv2


root = Tk()

# Create a frame
app = Frame(root, width=500, height=200, background="red")

app.grid()

# Create a label in the frame
lmain = Label(app)
lmain.grid()


# Capture from camera
cap = cv2.VideoCapture(0)

# function for video streaming
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret,cv2image = cv2.threshold(cv2image,180,255,0)


    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

button = Button(app, text='Stop', width=25, command=root.destroy)

#video_stream()
root.mainloop()
