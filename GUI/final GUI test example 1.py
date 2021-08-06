from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import cv2
from PIL import Image, ImageTk

img_counter = 0

pathManulab = r"./"
pathConfirmNo = r"./"
pathConfirmYes = r"./"
pathSaveImages = r"./"

# Starting to read webcam feed
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
if not ret:
    print("failed to grab -Frame")

# Making the main window in Tkinter
mainWindow = Tk()
mainWindow.title("LUL.Py")

img_file = Image.open(pathManulab + "GUIOverlay9.png")
bg = ImageTk.PhotoImage(img_file)
w = bg.width()
h = bg.height()
mainWindow.geometry('%dx%d+0+0' % (w, h))
labelBg = Label(mainWindow, image=bg)
labelBg.place(x=0, y=0)

# Create a Label to capture the Video frames (this is the live preview)
lmain = Label(mainWindow)
lmain.place(x=640, y=150)
# Capture from camera
cap = cv2.VideoCapture(0)

# Creating a style to modify buttons
s = ttk.Style()
s.configure('my.TButton', font=('Georgia', 15))


# function for video streaming
def video_stream():
    global streamStatus
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    video_stream.var = img
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100, video_stream)


# Window to confirm usage of selected image
# This function needs implementation with the other code, 
# as it currently doesn't do anything with the image
def confirmYes(parent):
    def closeWindow():
        confirmYesWindow.destroy()
        parent.destroy()
        cv2.destroyAllWindows()

    confirmYesWindow = Toplevel()
    # Create background overlay
    bg = PhotoImage(
        file=pathConfirmYes + "ConfirmYesWindowOverlay.png")
    labelBg = Button(confirmYesWindow, image=bg, command=closeWindow)
    labelBg.pack()
    # Scales the window to be the same size as the background image
    w = bg.width()
    h = bg.height()
    confirmYesWindow.geometry('%dx%d+0+0' % (w, h))
    # Needs to run mainloop to load images
    confirmYesWindow.mainloop()


# Window to confirm image will not be used
def confirmNo(parent):
    def closeWindow():
        confirmNoWindow.destroy()
        parent.destroy()
        cv2.destroyAllWindows()

    confirmNoWindow = Toplevel()
    # Create background overlay
    bg = PhotoImage(
        file=pathConfirmNo + "ConfirmNoWindowOverlay.png")
    labelBg = Button(confirmNoWindow, image=bg, command=closeWindow)
    labelBg.pack()
    # Scales the window to be the same size as the background image
    w = bg.width()
    h = bg.height()
    confirmNoWindow.geometry('%dx%d+0+0' % (w, h))
    # Needs to run mainloop to load images
    confirmNoWindow.mainloop()


# This is activated when the "Webcam 1" button is pressed, currently inactive
def webcamButtonPressed():
    # This is activated when the "Webcam 1" button is pressed, currently inactive
    # This will need implementing with the other code
    print()


def confirmChooseWindow():
    # Toplevel object which will
    # be treated as a new window
    confirmChooseWindow = Toplevel(mainWindow)

    # Sets the title
    confirmChooseWindow.title("Confirm yes or no")

    # sets the geometry of toplevel
    confirmChooseWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(confirmChooseWindow,
          text="Use this image?").pack()
    confirmBtn = Button(confirmChooseWindow, text="Yes",
                        command=lambda: confirmYes(confirmChooseWindow))
    denyBtn = Button(confirmChooseWindow, text="No",
                     command=lambda: confirmNo(confirmChooseWindow))
    confirmBtn.pack()
    denyBtn.pack()


# Takes screenshot of webcam feed, then asks
# wether or not to use that image
def openChooseWindowImage():
    global img_counter
    # Grabs a frame/screenshot using openCV
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame")
    elif ret:
        print("Starting (hopefully)")
    img_name = pathSaveImages + "opencv_frame_{}.png".format(img_counter)

    # Use this instead if you want to use one file name
    # to make it easier to use that file for something
    # img_name = "C:/Users/Kristian/Python projects/Manulab/learn GUI/opencv_frame_ss.png"

    # Saves the image to the folder, and opens a window to show it
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    copyImage = cv2.imread(img_name)
    cv2.imshow("Image captured", copyImage)
    img_counter += 1

    # Starts function to open confirmation window
    confirmChooseWindow()


# Adding images for buttons
webcamPhotoRaw = ImageTk.PhotoImage(
    file=pathManulab + "\webcam.png", master=mainWindow)
imagePhotoRaw = ImageTk.PhotoImage(
    file=pathManulab + "landscapeSmall.png", master=mainWindow)

# Adding buttons for different functions
chooseSourceButton = Label(
    mainWindow, text="Choose image source!", font=("Arial", 35))
chooseSourceButton.place(x=722, y=700)

webcamButton = ttk.Button(mainWindow, text='Webcam 1', style='my.TButton',
                          image=webcamPhotoRaw, compound=LEFT, command=webcamButtonPressed)
webcamButtonW = 265
webcamButton.place(x=(1920 - webcamButtonW) / 2, y=780)
imageButton = ttk.Button(mainWindow, text='Image 1', style='my.TButton',
                         image=imagePhotoRaw, compound=LEFT, command=openChooseWindowImage)
imageButton.place(x=827, y=895)

mainWindow.bind("<p>", lambda e: mainWindow.destroy())

video_stream()
mainWindow.mainloop()
