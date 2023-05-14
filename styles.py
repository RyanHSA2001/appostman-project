
light_blue_button_stylesheet = """
QPushButton{
    background-color: rgb(0, 168, 243);
    color: rgb(255, 255, 255);
    border-radius:5px

}

QPushButton:hover
{
    background-color: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
}
"""

green_button_stylesheet = """
QPushButton{
    background-color: rgb(3, 165, 3);
    color: rgb(255, 255, 255);
    border-radius:5px
}

QPushButton:hover
{
    background-color: rgb(255, 255, 255);
    color: rgb(0, 0, 0);
}
"""

gray_button_stylesheet = """
QPushButton{
background-color: rgb(116, 116, 116);
color: rgb(255, 255, 255);
border-radius:5px

}

QPushButton:hover
{
background-color: rgb(255, 255, 255);
	color: rgb(0, 0, 0);
}
"""

dark_messagebox_stylesheet = """
QMessageBox {
    background-color: rgb(49, 49, 49);
    color: white;
}

QMessageBox QPushButton {
    background-color: gray;
    color: white;
    padding: 5px 15px;
    border-radius: 5px;
    min-width: 50px;
    min-height: 20px;
}

QMessageBox QPushButton:hover {
    background-color: lightgray;
}

QMessageBox QLabel {
    background-color: rgb(49, 49, 49);
    color: white;
}

"""