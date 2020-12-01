File = open("Dicanory.txt","r")
FileText = File.read()

Dictionary = FileText.split()


KeyWordsForSentances = {
    "Compound": [
        "for",
        "and",
        "nor",
        "but",
        "or",
        "and",
        "yet",
        "so",
    ],
    "Complex": [
        #Causes
        "because",
        "if",
        "now that",
        #Time++
        "after",
        "as long as",
        "as",
        "before",
        "while",
        "when",
        "since",
        "untill",
    ],  
}