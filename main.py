import json
from msilib.schema import Font
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter.messagebox import showinfo
from tkinter.ttk import Style
from turtle import width
from variables import *

from header import Header

class App(object):

    def __init__(self):

        filetypes = (
            ('JSON file', '*.json'),
        )

        def browse_button():
            folder_path = StringVar()
            filename = filedialog.askopenfile(
                title="Open a .json file",
                filetypes=filetypes,
                initialdir='/'
            )
            folder_path.set(filename)
            if filename != "":
                showinfo(
                    title='Selected file',
                    message=filename.name
                )
                dragAndDropSection.destroy()
                insideValuesFrame = Frame(
                    functionalFrame, bg=FUNCTIONAL_FRAME_BACKGROUND)
                insideValuesFrame.place(relheight=RELHEIGHT_FUNCTIONAL_FRAME,
                                        relwidth=1)
                JSONfile = open(filename.name, 'r')
                datas = json.loads(JSONfile.read())
                for i in datas:
                    nameOfTheKeyboard = Label(insideValuesFrame,
                                              fg="green",
                                              text="Name: " + str(i['name']))
                    nameOfTheKeyboard.pack()
                    matrixOfTheKeyboard = Label(insideValuesFrame,
                                                fg="green",
                                                text="Matrix: " + str(i['layouts']))
                    matrixOfTheKeyboard.pack()
                JSONfile.close()

        # basic application window settings
        self.window = Tk()
        self.window.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.minsize(MIN_WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window.title(WINDOW_TITLE)
        self.window.resizable(X_RESIZE_WINDOW, Y_RESIZE_WINDOW)
        self.window.iconbitmap(ICON)
        style = Style(self.window)
        style.theme_use('clam')

        headerFrame = Header(self.window)
        headerFrame
        # build main sections, upper section is a digital section aka view section for all information, bottom section is our functional section for all interactive activities
        digitalFrame = Frame(self.window,
                             bg=DIGITAL_FRAME_BACKGROUND)
        digitalFrame.place(relheight=RELHEIGHT_DIGITAL_FRAME,
                           rely=RELHEIGHT_HEADER_FRAME,
                           relwidth=1)
        digitalFrame.config()
        functionalFrame = Frame(self.window, bg=FUNCTIONAL_FRAME_BACKGROUND)
        functionalFrame.place(rely=RELY_FUNCTIONAL_FRAME,
                              relheight=RELHEIGHT_FUNCTIONAL_FRAME,
                              relwidth=1)
        functionalFrame.config()

        # Button for searching JSON file with QMK information
        dragAndDropSection = Button(functionalFrame,
                                    text=TEXT_SEARCH_BUTTON,
                                    bg=BACKGROUND_SEARCH_BUTTON,
                                    activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                                    activeforeground=FOREGROUND_SEARCH_BUTTON,
                                    fg=FOREGROUND_SEARCH_BUTTON,
                                    height=HEIGHT_SEARCH_BUTTON,
                                    width=WIDTH_SEARCH_BUTTON,
                                    border=0,
                                    font=font.Font(size=15),
                                    command=browse_button)
        dragAndDropSection.pack(pady=PADY_SEARCH_BUTTON)
        dragAndDropSection.config()
        self.window.mainloop()


def main():
    app = App()


main()
