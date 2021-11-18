import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import shutil



def EditText():
    
    original = r'Stocks.txt'
    target = r'NewFile.txt'
    
    shutil.copyfile(original, target)
    f = open("NewFile.txt", "w+")
    print("Opening")
    for wordlines in f:
        f.replace(",", "\n")
        print(wordlines + " : READ")
        print("-------------->")
        f.close()
    #Split at every " , "s
    

    #Remove word " Counter "
    
    
    #Remove special characters 
    
    

    
    
