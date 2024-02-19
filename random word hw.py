from tkinter import *
import random

root=Tk()

root.title("Random word generator")
root.geometry("500x500")


list1 = ["food" , "hello" , "speaker" , "word" , "peptide", "sharp", "mouthwash", "turkey", "Uganda", "fire-ant", "membrane", "mitochondria"]
print(list1)

def random_number():
    random_no = random.randint(0, 4)
    print(random_no)
    random_lucky_friend = list1[random_no]
    print("Random Word Generator :  " + random_lucky_friend)
    
btn1 = Button(root)
btn1 = Button(root, text="Generate Random Word", command = random_number)
btn1.place(relx= 0.5,rely = 0.5, anchor = CENTER)

root.mainloop()