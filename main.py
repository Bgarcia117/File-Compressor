import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")
# This usese a different type a button to access files

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output")

label2 = sg.Text("Select destination file:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

while True:
        event, values = window.read()
        print(event, values)
        filepaths = values["files"].split(",")
        # since there can be multiple filepaths, they need to split apart
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output"].update(value="Compression completed!")

window.close()