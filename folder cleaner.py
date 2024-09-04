import os
All=os.listdir()
os.makedirs("Docs")
os.makedirs("Images")
os.makedirs("Others")
Docs= []
Images= []
Others=[]
Videos= []
Audio= []


def addfiles(folder,ext):
    for file in All:
        if file.endswith(ext):
            folder.append(file)
            
addfiles(Docs,".txt")
addfiles(Docs,".docx")
addfiles(Images, ".png")
addfiles(Others, '.log')
addfiles(Others, '.cmd')
addfiles(Videos, '.mp4')
addfiles(Audio, '.mp3')


for i in Docs:
    os.replace(i, f'Docs/{i}')
for i in Videos:
    os.replace(i, f'Videos/{i}')
for i in Audio:
    os.replace(i, f'Audio/{i}')
for i in Images:
    os.replace(i, f'Images/{i}')
for i in Others:
    os.replace(i, f'Others/{i}')

print("Done!")





