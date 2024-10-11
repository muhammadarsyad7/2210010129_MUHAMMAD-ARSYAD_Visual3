import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("#007FFF")
window=sg.Window(title="profile",
                 layout=[[sg.Text("NPM          : 2210010129")],
                         [sg.Text("Nama         : MUHAMMAD ARSYAD")],
                         [sg.Text("Kelas        : 5N Reguler Banjarmasin")],
                         [sg.Text("Matkull      : pempograman Visual 3")]],
                 size=(400,200))
window()
window.close()
