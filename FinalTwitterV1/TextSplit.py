import fileinput
import shutil


def replace_method():
    print("replacing")
    file_path = 'NewFile.txt'
    try:
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                line = line.replace('Counter', '')
                line = line.replace('{', '')
                line = line.replace('(', '')
                line = line.replace('}', '')
                line = line.replace(')', '')
                line = line.replace(',', '\n')
                line = line.replace("'", "")
                line = line.replace(" ", "")
                print (line, end='')
                file.close()
                
                shutil.copy("NewFile.txt", "StockParsed.txt")
                print("done")
                
                
    except Exception as e:
        print (str(e))
        

replace_method()
