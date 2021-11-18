import io

from list import *


words = ["GME", "TNXP", "ABC", "APPL"]


with io.open("Text.txt", "a", encoding="utf-8", errors='ignore') as file:
            print("1")
            file.write("GME")
            print("2")
            file.close()
            print("3")
            print("4")



with io.open("Text.txt", "r", encoding="utf-8", errors='ignore') as file:
    file.readlines()
    print("5")
    
    
    wordlist = stocks
    '''
    file.readlines()
    
    wordlist.append(line)  
    '''              
    found_words = {}
    search_words = words
    
    print("6")
    for word in search_words:
        for item in wordlist:
            print("8")
            if word == item:
            #print("9")
                if word in found_words:
                    print("10")
                    found_words[word] += 1
                    print("11")
                else:
                    print("12")
                    found_words[word] = 1
                    print("13")
                    print(item + ':',found_words[word])
                    print("14")