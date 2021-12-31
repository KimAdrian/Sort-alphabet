from pathlib import Path
import operator
from tkinter import Tk   
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt

def analyseFile():
 
 alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
 
 #open filepicker window
 Tk().withdraw() 
 filename = askopenfilename() 
 print("File: "+filename)

 text = Path(filename).read_text()
 text = text.replace('\n', '')
 
 #Dictionary to store alphabet and its frequency
 frequency = {}

 for i in alphabets:
     frequency[i] = text.count(i)

 #Sorting in acending order
 print("Frequency in acending order")
 frequency_tuples = sorted(frequency.items(), key = operator.itemgetter(1))
 #print(frequency_sorted)
 #Convert sorted tuple to dictionary
 frequency_sorted = {k: v for k, v in frequency_tuples}
 print(frequency_sorted)

 values = frequency_sorted.values()
 sum_values = sum(values)
 print("sum of frequencies: "+str(sum_values))
 
 #plot histogram
 plt.bar(list(frequency_sorted.keys()), frequency_sorted.values(), color='g')
 plt.title("File: "+filename+".\n Sorted in ascending order")
 plt.xlabel("alphabets")
 plt.ylabel("frequency")
 plt.show()

 

def main():
    analyseFile()

if __name__ == "__main__":     
    main()
