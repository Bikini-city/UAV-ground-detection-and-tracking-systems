import json

def json_reader(j_path):
    with open(j_path) as f:
        data = json.load(f)
    return data

def header(width,height,code_file):
    # Set initial app startup codes
    with open(code_file,'a') as code:
        code.write(f'# Importing important libraries\n')
        code.write(f'import sys\n')
        code.write(f'from PyQt5 import QtWidgets\n')
        code.write(f'from PyQt5.QtWidgets import *\n')
        code.write(f'from PyQt5.QtGui import QPixmap\n')
        code.write(f'from PIL import Image\n')
        code.write(f'import io\n')
        code.write(f'import os\n')
        code.write(f'from folium import folium\n')
        code.write(f'from PyQt5.QtWebEngineWidgets import QWebEngineView\n')
        code.write(f'from PyQt5.QtCore import Qt\n')
        code.write(f'\n###################################\n')
        code.write(f'\n# Set up the application\n')
        code.write(f'app = QApplication(sys.argv)\n')
        code.write(f'# Set up the main window \n')
        code.write(f'curr_window = QtWidgets.QWidget()\n')
        code.write(f'curr_window.setGeometry({0}, {0}, {width}, {height})\n')

def tailer(code_file):
    with open(code_file, 'a') as code:
        code.write(f'\nif __name__ == "__main__":\n\tcurr_window.show()\n\tsys.exit(app.exec_())')

#### widgets
def getCheckbox(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the Checkbox\n')
        code.write(f'cb = QCheckBox(curr_window)\n')
        code.write(f'cb.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getDatePicker(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the date picker\n')
        code.write(f'cal = QCalendarWidget(curr_window)\n')
        code.write(f'cal.setGridVisible(True)\n')
        code.write(f'cal.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getImage(bounds,code_file,id):
    x_min,y_min,x_max,y_max = bounds
    size = (int(x_max - x_min), int(y_max - y_min))
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the image placeholder\n')
        code.write(f'os.makedirs("./images",exist_ok=True)\n')
        code.write(f'Image.new(mode="RGB", size={size}, color={0}).save(f"./images/img_{id}.jpg")\n')
        code.write(f'label = QLabel(curr_window)\n')
        code.write(f'label.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')
        code.write(f'label.setPixmap(QPixmap(f"./images/img_{id}.jpg"))\n')

def getInput(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    size = (int(x_max - x_min), int(y_max - y_min))
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the input field\n')
        code.write(f'inpt = QLineEdit(curr_window)\n')
        code.write(f'inpt.setText("There is some text here")\n')
        code.write(f'inpt.setGeometry({x_min}, {y_min}, {x_max}, {y_max})\n')
        code.write(f'inpt.setMaximumSize({size[0]}, {size[1]})\n')

def getListItem(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the list item field\n')
        code.write(f'mainList = QListWidget(curr_window)\n')
        code.write(f'mainList.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getMapView(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    coordinates = (51.74677969131641, 19.450116091689516)
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the mapview field\n')
        code.write(f'coordinates = (51.74677969131641, 19.450116091689516)\n')
        code.write(f'm = folium.Map(location={coordinates},zoom_start={13})\n')
        code.write(f'data = io.BytesIO()\n')
        code.write(f'm.save(data, close_file=False)\n')
        code.write(f'mapview = QWebEngineView(curr_window)\n')
        code.write(f'mapview.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getonOffSwitch(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the on/off switch: TODO\n')
        code.write(f'ofb = QPushButton(curr_window)\n')
        code.write(f'ofb.setCheckable(True)\n')
        code.write(f'ofb.setStyleSheet("background-color : lightgrey")\n')
        code.write(f'ofb.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getRadioButton(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the radio button\n')
        code.write(f'rb = QRadioButton(curr_window)\n')
        code.write(f'rb.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getSlider(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the slider button\n')
        code.write(f'sl = QSlider(Qt.Horizontal, curr_window)\n')
        code.write(f'sl.setFocusPolicy(Qt.StrongFocus)\n')
        code.write(f'sl.setTickPosition(QSlider.TicksBothSides)\n')
        code.write(f'sl.setTickInterval({10})\n')
        code.write(f'sl.setSingleStep({1})\n')
        code.write(f'sl.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')

def getText(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    size = (int(x_max - x_min), int(y_max - y_min))
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the text field\n')
        code.write(f'label = QLabel(curr_window)\n')
        code.write(f'label.setText("There is some text here")\n')
        code.write(f'label.setGeometry({x_min}, {y_min}, {x_max - x_min}, {y_max - y_min})\n')
        code.write(f'label.setMaximumSize({size[0]}, {size[1]})\n')
        code.write(f'label.setStyleSheet("border: 3px solid blue;")\n')

def getTextButton(bounds,code_file):
    x_min,y_min,x_max,y_max = bounds
    size = (int(x_max - x_min), int(y_max - y_min))
    with open(code_file, 'a') as code:
        code.write(f'\n# Codes for the text button\n')
        code.write(f'tbutton = QPushButton(curr_window)\n')
        code.write(f'tbutton.setText("Click Me")\n')
        code.write(f'tbutton.setGeometry({x_min}, {y_min}, {x_max}, {y_max})\n')
        code.write(f'# TODO: Check the best way to set the sizes\n')
        code.write(f'tbutton.setMaximumSize({size[0]}, {size[1]})\n')


def addUiElements(width,height,bounds,classes,classes_names,code_file):
    # Main Header
    header(width,height,code_file)
    # Body
    for i in range(len(bounds)):
        name = classes_names[int(classes[i])]
        if name == 'Image':
            getImage(bounds[i],code_file,i)
        elif name == 'Text Button':
            getText(bounds[i],code_file)
        elif name == 'Text':
            getText(bounds[i],code_file)
        elif name == 'Input':
            getInput(bounds[i],code_file)
        elif name == 'Date Picker':
            getDatePicker(bounds[i],code_file)
        elif name == 'Slider':
            getSlider(bounds[i],code_file)
        elif name == 'Radio Button':
            getRadioButton(bounds[i],code_file)
        elif name == 'Checkbox':
            getCheckbox(bounds[i],code_file)
        elif name == 'List Item':
            getListItem(bounds[i],code_file)
        elif name == 'Map View':
            getMapView(bounds[i],code_file)
        elif name == 'On/Off Switch':
            getonOffSwitch(bounds[i],code_file)

    # Tail
    tailer(code_file)