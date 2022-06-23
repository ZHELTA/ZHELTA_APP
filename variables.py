#Basic Window Settings
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 720
MIN_WINDOW_WIDTH = 700
WINDOW_TITLE = 'ZHELTA'
ICON = './icons/icon.ico'
X_RESIZE_WINDOW = True
Y_RESIZE_WINDOW = False
RELWIDTH=1.0
#Header Frame Settings 
HEADER_FRAME_BACKGROUND = '#17181A'
RELHEIGHT_HEADER_FRAME = 0.1
#Digital Frame Settings
DIGITAL_FRAME_BACKGROUND = '#1B1C1E'
RELHEIGHT_DIGITAL_FRAME = 0.5
#Functional Frame Settings
FUNCTIONAL_FRAME_BACKGROUND = '#17181A'
RELY_FUNCTIONAL_FRAME = RELHEIGHT_HEADER_FRAME + RELHEIGHT_DIGITAL_FRAME
RELHEIGHT_FUNCTIONAL_FRAME = 1 - (RELHEIGHT_HEADER_FRAME + RELHEIGHT_DIGITAL_FRAME) # Do not change!
#Button to search for JSON file 
TEXT_SEARCH_BUTTON = 'Choose the configuration file or drop it here'
BACKGROUND_SEARCH_BUTTON = '#17181A'
ACTIVEBACKGROUND_SEARCH_BUTTON = '#17181A'
FOREGROUND_SEARCH_BUTTON = '#E39417'
HEIGHT_SEARCH_BUTTON = 5
WIDTH_SEARCH_BUTTON = 40
PADY_SEARCH_BUTTON = 50