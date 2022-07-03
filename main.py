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
                buttonToExit = Button(functionalFrame,text="Change Layout")
                buttonToExit.pack(pady=PADY_SEARCH_BUTTON)
                # insideValuesFrame = Frame(
                #     functionalFrame, bg=FUNCTIONAL_FRAME_BACKGROUND)
                # insideValuesFrame.place(relheight=RELHEIGHT_FUNCTIONAL_FRAME,
                #                         relwidth=1)
                JSONfile = open(filename.name, 'r')
                datas = json.loads(JSONfile.read())
                for i in datas:
                    matrixOfTheKeyboard = i['matrix']
                    layoutsOfTheKeyboard = i['layouts']
                    build_keyboard(matrixOfTheKeyboard, layoutsOfTheKeyboard)
                JSONfile.close()

        def build_keyboard(matrix, layouts):
            rows = matrix['rows']
            cols = matrix['cols']
            for i in range(0, cols):
                digitalFrame.columnconfigure(i, weight=1)
            for i in range(0, rows):
                digitalFrame.rowconfigure(i, weight=1)
            for i in range(0, rows):
                for j in range(0, cols):
                    keyFromKeyboard = Button(digitalFrame,
                                             text='',
                                             bg=BACKGROUND_SEARCH_BUTTON,
                                             activebackground=ACTIVEBACKGROUND_SEARCH_BUTTON,
                                             activeforeground=FOREGROUND_SEARCH_BUTTON,
                                             fg=FOREGROUND_SEARCH_BUTTON)  # text='{},{}'.format(i,j),height=5,width=5)
                    keyFromKeyboard.grid(
                        column=j, row=i, sticky=NSEW, padx=2, pady=2)
                    kl.append(keyFromKeyboard)

        kl = []
        # basic application window settings
        self.window = Tk()
        self.window.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window.minsize(MIN_WINDOW_WIDTH, WINDOW_HEIGHT)
        self.window.title(WINDOW_TITLE)
        self.window.resizable(X_RESIZE_WINDOW, Y_RESIZE_WINDOW)
        self.window.iconbitmap(ICON)
        style = Style(self.window)
        style.theme_use('clam')

        # Header Frame
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
