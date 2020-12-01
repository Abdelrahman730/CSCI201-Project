from Lists import *
import tkinter


def Make_List_Of_Words (EnternedText):
    """ This function is used for makeing list of words that could match each word entered in the Essay"""
    
    List = []
    Count = 0
    EnternedText = EnternedText.lower()
    
    # Words is each word in the whole text ex:["Hello","World","Dahy","Mariam"]
    for Words in EnternedText.split() :
        # Check if there is empty Words in text
        if (Words != " "):
            # Make empty list in the List , ex:[[],[],[],[]]
            List.insert(Count,[])
            # Check if the Words is one charcter only so we put it at the List and go next word : ex:"a" , "b" , "c"
            if len(Words) == 1 :
                List[Count].append(Words)
                Count += 1
                continue               
            for Dictionary_Word in Dictionary :
                # Check if the Dictionary word have same string as User entered Word
                if (Dictionary_Word.find(Words.lower()) != -1)  :   
                    #Check if User Text is same as Dictionary word
                    if (Words.lower() == Dictionary_Word.lower()) :
                        #Make the list empty
                        List[Count] = []
                        #Add the user Words to the list
                        List[Count].append(Words)
                        break
                    # Check is the start of the Dictionary Word is the same charcters of User Word
                    if Dictionary_Word.startswith(Words.lower()) :
                        #Add the Dictionary word to the list
                        List[Count].append(Dictionary_Word)
            #Check if the list empty which will work in names usually ex:"Mariam","Ahmed","Mohammed"       
            if len(List[Count]) == 0:
                #Add the user text to the List
                List[Count].append(Words)
            Count += 1
    return List


def Make_New_Sentance (List):
    """ This function is used choosing best word for list it recives"""
    LoopCount = 0
    Best_Words_Data = []
    NewText = ""
    #Loop throught the List which we made at earlier function
    for x in List:
        #If the list contain one suitable Word then we escape the next progress
        if len(List[LoopCount]) == 1:
            #Add the word to the new text which will be puted at Edit_Box2
            NewText = NewText + " " + List[LoopCount][0]
            LoopCount = LoopCount + 1
            continue
        
        BestWord = ""
        
        #Loop throught each list in the big list
        for z in List[LoopCount]:
            #Check if the Best word empty or if the Best word is later at alphabetic
            if (BestWord > z) or (BestWord == "") :
                BestWord = z
        
        #Add the word to the new text which will be puted at Edit_Box2           
        NewText = NewText + " " + BestWord
        LoopCount = LoopCount + 1
        
        #Since the word is wrong we get it's start index here and end index in order to use at later function
        Begin_Index = (len(NewText)-5)
        End_Index = (Begin_Index+len(BestWord))
        #Add the Being Index and End Index to the list ex: [[10,15],[21,25]]
        Best_Words_Data.append([Begin_Index,End_Index])
        
    return NewText[1:],Best_Words_Data

def change_List_Into_String_With_New_Lines(List):
    """ Makeing the list show in multi lines """
    Text = ""
    #Loop throught the List
    for Index in range(0,len(List)):
        #Make each List show as str at new line to put it at Edit_Box3
        Text = Text + str(List[Index]) + "\n"
    return Text

def Check_Quality_Of_Paragraph (Text):
    """ Algorithm for checking the quality of paragraph """
    Compound = 0
    Complex = 0 
    Text = Text.lower()
    for Main in KeyWordsForSentances :
        for KeyWords in KeyWordsForSentances[Main]:
            #Check if the Keyword is between two spaces or with coma and space ex : ",or " " or "
            if (Text.find(" "+KeyWords+" ") != -1) or (Text.find(","+KeyWords+" ") != -1):
                if Main == "Compound" :
                    Compound += 1
                else:
                    Complex += 1
    # Check if User new text count of compound "and" complex is greater than 0 to give feed back of string
    if (Compound > 0) and (Complex > 0) :
        return "Excellent"
    # Check if User new text count of compound "or" complex is greater than 0 to give feed back of string
    elif (Compound > 0 and Complex == 0) or (Compound == 0 and Complex > 0) :
        return "Good"
    else:
        return "Bad"
        
        
def Num_Of_Differance (OldText,NewText):
    """ Calclaute the total mistakes at paragraph """
    List1 = OldText.split()
    List2 = NewText.split()
    Errors = 0
    #Loop throught the first Text (Edit_Box1)
    for i in range(len(List1)):
        #Check if Old Text  word is not the same as the New text word so we can count it as Error
        if List1[i].lower() != List2[i].lower() :
            Errors += 1
    return Errors


def Change_EditBox_Color(List,Edit_Box):
    #Loop throught the List ex:[[5,10],[15,20],[29,35]]
    for i in range(len(List)):
        Num1 = "1."+str(List[i][0])
        Num2 = "1."+str(List[i][1])
        #Add tag to the Edit_Box2 in order to color it by giveing the First Index and End Index
        Edit_Box.tag_add("start", Num1, Num2)
        # Color the taged Word
        Edit_Box.tag_config("start", background="red", foreground="black")

def Check_Essays ():
    """ The working function for the button """
    
    # Fixing text and put it at the other Text widget
    Text = Edit_Box1.get("1.0","end-1c")
    
    List_Of_Suitable_Words = Make_List_Of_Words(Text)
    NewText,WrongWordsIndex = Make_New_Sentance(List_Of_Suitable_Words)

    Edit_Box2.delete("1.0","end-1c")
    Edit_Box2.insert(1.0, NewText)    
    
    Edit_Box3.delete("1.0","end-1c")
    Edit_Box3.insert(1.0, change_List_Into_String_With_New_Lines(List_Of_Suitable_Words))
    
    # Check Quality
    
    Quality = Check_Quality_Of_Paragraph(NewText)
    var1.set("Quality: "+Quality)
    
    # Mistakes Count
    Mistakes_Count = Num_Of_Differance(Text,NewText)
    var2.set("Mistakes Count: "+str(Mistakes_Count))
    
    #Coloring the fixed words
    Change_EditBox_Color(WrongWordsIndex,Edit_Box2)
             
# ------------------------------------------------------ GUI ------------------------------------------------------#
window = tkinter.Tk()
window.title("Writing")
window.geometry("1024x768")
window.resizable(False,False)

Edit_Box1 = tkinter.Text(window, height=13.3, width=124)
Edit_Box1.pack()
Edit_Box1.place(x=10, y=10)

Edit_Box2 = tkinter.Text(window, height=13.3, width=124)
Edit_Box2.pack()
Edit_Box2.place(x=10, y=230)

Edit_Box3 = tkinter.Text(window, height=13.3, width=124)
Edit_Box3.pack()
Edit_Box3.place(x=10, y=470)


Check_Button1 = tkinter.Button(window,text ="Check Paragraph",width=15,height=2 ,command = Check_Essays )
Check_Button1.pack()
Check_Button1.place(x=10, y=700)

var1 = tkinter.StringVar()
Text_Label_1 = tkinter.Label(window,textvariable=var1 )
var1.set("Quality: ")
Text_Label_1.pack()
Text_Label_1.place(x=250, y=700)

var2 = tkinter.StringVar()
Text_Label_2 = tkinter.Label(window,textvariable=var2 )
var2.set("Mistakes Count: ")
Text_Label_2.pack()
Text_Label_2.place(x=500, y=700)

window.mainloop()
# ------------------------------------------------------ End Gui ------------------------------------------------------#