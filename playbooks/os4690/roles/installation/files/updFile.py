def changeBat(fileDirectory, wordToFind, wordToChange, incremento):
    with open(fileDirectory,'r') as archivo:
        i=0
        j=0
        pos=[]
        for linea in archivo:
            if linea == wordToFind:
                print("match")
                pos.append(i)
                j=j+1
            i=i+1
        print("posicion del cambio = ", pos)

    contenido = open(fileDirectory).read().splitlines()
    for index in range(len(pos)):
        print(pos[index])
        contenido.insert(pos[index]-incremento,wordToChange)
    f = open(fileDirectory, "w")
    f.writelines("\n".join(contenido))

changeBat('/mnt/c/ace3d/install.bat','MENU\n','AUTO.BAT', 0)
changeBat('/mnt/c/ace3d/1.bat','MENU\n','CLS\n9.BAT', 2)
changeBat('/mnt/c/ace3d/1.bat','menu\n','CLS\n9.BAT', 0)
