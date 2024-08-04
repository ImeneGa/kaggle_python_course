def word_search(doc_list, keyword):
    """
    This function takes a list of documents (each document is a string) and a keyword and returns list of the index values into the original list for all documents 
    containing the keyword.
    """
    tab = []
    tabf = []
    val = False
    i = 0
    key = keyword.lower()
    word2 = ''
    
    for words in doc_list:
        tab = words.split(' ')
        for word in tab:
            word2 = word.lower()
            if (key==word2) or ((key+',')==word2) or ((key+'.')==word2):
                val = True
        if val==True:
            tabf.append(i)
        i=i+1
        val= False
        
    return tabf

doc_list = ''
keyword = ''
tab = []

doc_list = input('Enter the list of documents you want to filter with a keyword\n')
tab = doc_list.split(' ')
keyword = input('Enter the keyword you are looking for\n')
print('The index of', keyword, 'in the list of documents is', word_search(tab, keyword))