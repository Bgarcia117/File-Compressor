import PySimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")
# This usese a different type a button to access files

compress_button = sg.Button("Compress")

label2 = sg.Text("Select destination file:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

window.read()
window.close()