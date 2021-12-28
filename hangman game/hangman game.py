#Project HANGMAN:
 
old_letters_guessed = []            #contains all the letters that was guessed by the user
wrong_letters_guessed = []          #contains all the wrong letters that were given by the user 
#--------------------------------------------------------------------------------------------------------------------------------------------------------#
def presentation(): #returns the presentation screen
    
    '''present the presentation screen for the user.
    :return: presentation screen
    :rtype: str
    '''
    
    open_presentation = open(r"C:\Users\Gal\Desktop\Python learning\files exercise\Hangman Game\Presentation Screen.txt", "r")
    print(open_presentation.read())
    open_presentation.close()

presentation()	

#--------------------------------------------------------------------------------------------------------------------------------------------------------#
def choose_word(file_chosen , index_chosen): #returns the secret word 
    
    '''Reading through the file that was chosen by the user & based on the index that was chosen returns a word.
    :param file_chosen: words file that was chosen by user
    :param index_chosen: index in the file that was chosen by user
    :type file_chosen: path to file
    :type index_chosen: int
    :return: the secret word 
    :rtype: str
    '''

    file_open = open(file_chosen , "r")
    read_file = file_open.read()
    split_words = read_file.split(" ")    
   
    list_of_lists = []
    finished_list = []

    for word in split_words:
        list_of_lists.append(word.split())


    #if the index is greater than or equal to the length of the list , divide it by the length of the list and the left overs is the updated index  
    word_length = len(split_words)
    
    if int(index_chosen) >= word_length:
       index_updated = int(index_chosen) % word_length
    
    #the list starts from 1 but in case the username was mistaken to ask for index 0 we will understand and count it as index 1
    elif index_chosen == "0":
        index_updated = 1
        
    #but if the index is not greater or matching,the number stays the same  
    else:
        index_updated = int(index_chosen) 


    #the index that was given - 1 to make it start from 1
    len_minused = index_updated - 1
    #word in index 
    finished_list.append(split_words[len_minused])

    #returns the item that was selected by the user 
    return finished_list[0]

#--------------------------------------------------------------------------------------------------------------------------------------------------------#                       

def check_valid_input(letter_guessed , old_letters_guessed): #return boolian , whether the letter is breaking the rules or not 
    
    '''checks if the letter that was entered by user is valid based on the laws we set below and returns the answer.
    :param letter_guessed: letter that was entered by the user
    :param old_letters_guessed: list which contains all guessing that came from the user
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True / False based on the letter 
    :rtype: bool
    '''

    if len(letter_guessed) >= 2 or letter_guessed.isalpha() == False or letter_guessed in old_letters_guessed :       #special letter search should be equalled to none
        return False	
    else:
        return True 
	                                                
#--------------------------------------------------------------------------------------------------------------------------------------------------------#

def try_update_letter_guessed(letter_guessed, old_letters_guessed, wrong_letters_guessed, secret_word): #based on the boolian function above returns response 
    
    '''print to screen different results based on the answer from check_valid_input function.
    :param letter_guessed: letter that was guessed by the user
    :param old_letters_guessed: list which contains all the letters that were guessed by the user
    :param wrong_letters_guessed: list which contains all the letters that are valid, by the laws from check_valid_input func, but is wrong
    :param secret_word: string that was selected by the user input based on the index he entered 
    :type letter_guessed: str
    :type old_letters_guessed: list
    :type wrong_letters_guessed: list
    :type secret_word: str
    :return:(1)if the func check_valid_input == false , prints and x and below a row of the old letter that were guessed.
            (2)if the func check_valid_input == true , adds the letter that was guessed to old_letters_guessed list.
            (3)if the func check_valid_input == true but the letter isn't correct , prints sad smily face and adding that word to list which contains wrong letters
    :rtype:(1) str
           (2) list 
           (3) str
    '''

   
    if check_valid_input(letter_guessed , old_letters_guessed) == False:
       
        old_letters_guessed.append(letter_guessed)
        print('X')                                                            
        print('->'.join(sorted(old_letters_guessed)))       #the join here unpacks the list into string and declares its delimiters
        
    else:
        if letter_guessed not in secret_word: #if the letter that the user guessed is valid(returned as true from check valid func) but is not in the secret word
            print(":(\n")                     
            wrong_letters_guessed.append(letter_guessed)#we will add it to a new list which contains all the wrong valid letters that were guessed by the user
            old_letters_guessed.append(letter_guessed)
        else:
            old_letters_guessed.append(letter_guessed)
            
#--------------------------------------------------------------------------------------------------------------------------------------------------------#

def print_hangman(num_of_tries): #printing the state of hangman based on the wrong answeres we recieve from the user  
    
    '''based on wrong the wrong answeres of the user prints back different states of the hangman.
    :param num_of_tries: the number of tries that the user was wrong
    :type num_of_tries: int
    :return: a string which is the value of the key, symbolizing different hangman states, based on the len of the wrong letters list 
    :rtype:string 
    '''
    
    hangman_photos = {1:"|\n|\n|\n|\n|" , 2:"|       |\n|       0\n|\n|\n|" , 3:"|       |\n|       0\n|       |\n|\n|" , 4:"|       |\n|       0\n|       |\n|      /|\ \n|\n|" , 5: "|       |\n|       0\n|       |\n|      /|\\\n|      /\n|" , 6:"|       |\n|       0\n|       |\n|      /|\ \n|      / \ \n|\n\nYOU LOST"}    #all states of the hangman 
    
    #printing state of hangman based on wrong guessing,printed using keys to pull values that are photos, from the dict 
    
    if num_of_tries == 1:
        print("x-------x")
        print(hangman_photos[1])
    
    elif num_of_tries == 2:
        print("x-------x")
        print(hangman_photos[2])
        
    elif num_of_tries == 3:
        print("x-------x")
        print(hangman_photos[3])
        
    elif num_of_tries == 4:
        print("x-------x")
        print(hangman_photos[4])
        
    elif num_of_tries == 5:
        print("x-------x")
        print(hangman_photos[5])
        
    elif num_of_tries == 6:
        print("x-------x")
        print(hangman_photos[6])

#--------------------------------------------------------------------------------------------------------------------------------------------------------#

def show_hidden_word(secret_word, old_letters_guessed): #assigning correct letters based on thier locations & always printing the current state 
	
    '''assigning letters that were guessed correctly by the user based on thier locations in the original word , and showing the current state after each iteration of the loop.
    :param secret_word: word that was chosen by user based on the index he entered
    :param old_letters_guessed: list which contains all the letters that were guessed by the user
    :return: string of the correct letters that were guessed so far in place, and letters that weren't will be replaced with blank underlines 
    :rtype: string 
    '''
    
    
    guessed_correctly_list = []
    
    for letter in secret_word:      #loops through the secret word , if theres a letter in the letters that were guessed that is in the secret word
        if letter in old_letters_guessed:
            guessed_correctly_list.append(letter) #we will add it to a new list that is for the correct letters 
        
        elif letter == "-":   #if theres separation sign in the secret_word we will automatically add it for the user to understand the secret word is made of two words 
            guessed_correctly_list.append(letter)
            
                
        else:
            guessed_correctly_list.append('_')  #if letter wasn't guessed yet it will print it as blank underline
    
    print('\n' + ' '.join(guessed_correctly_list)) #priniting current correct guessing state    

#--------------------------------------------------------------------------------------------------------------------------------------------------------#
 
def check_win(secret_word, old_letters_guessed): #returns winner and breaks the while loop, when all the correct letters have been guessed  
    
    '''checks when the user is winning based on the length of a list of all his correct letters so far.
    :param secret_word: word that was chosen by user based on the index he entered 
    :param old_letters_guessed: list which contains all the letters that were guessed by the user
    :type secret_word: str
    :type old_letters_guessed: list
    :return: if the length that is collecting correct words is matching in length to the length of the secret word , it means user guessed all words which means
             that the user won. if so it will return True . else the func will keep returning False , meaning that he haven't yet guessed all lettters of the word.
    :rtype: str
    '''
    
    correct_letters = []
    
    for letter in secret_word:                       
        if letter in old_letters_guessed:            #if a letter is in old_letters_guessed list 
            correct_letters.append(letter)         #add it to a list of the correct words
        
        elif letter == "-":                          #if letter is seperation mark, add it to the correct list
            correct_letters.append(letter)
        
        else:
            continue
            
    if len(correct_letters) == len(secret_word): #if the list that that contains only correct letters is equal to the length of the secret word the user won!
        
        return True
        
		
    else:
        return False

#--------------------------------------------------------------------------------------------------------------------------------------------------------#

def main():
    
    '''this part is for neccessery information for the whole code to work with, that we are getting from the user'''
    
    file_chosen = input("\nEnter file path: ") 
    index_chosen = input("Enter index: ")
    choose_word(file_chosen , index_chosen)
    print("\nLets Start!")
    print("\nx-------x")
        
    secret_word = choose_word(file_chosen,index_chosen)
    secret_word = secret_word.lower() #casting any value to lower incase it was capitalize
    show_hidden_word(secret_word, old_letters_guessed)#Calling for function once only for initial presentation of the len of the word with blank lines and if theres is , seperation also
    
#--------------------------------------------------------------------------------------------------------------------------------------------------------#   
    '''this part is responsible to loop all of the functions in the code until 1 of the 2 options will break it:
    
       1)the first option to break the loop is that the length of the wrong_letters_guessed list will be greater than 5 which means when the user lost.
       2)the second option to break the loop is that the func check_win will return true, and it will when the length of the list which contains the correct letters will 
         will be matching the length of the secret word, and when that happens the user will win.
    '''
         
    while (len(wrong_letters_guessed) <= 5) and (check_win(secret_word,old_letters_guessed) != True):
        
        letter_guessed = (input("\nGuess a letter : ")).lower()
        check_valid_input(letter_guessed , old_letters_guessed) 
        try_update_letter_guessed(letter_guessed , old_letters_guessed,wrong_letters_guessed,secret_word)
        num_of_tries = len(wrong_letters_guessed)
        print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
        if check_win(secret_word, old_letters_guessed) == True:
            print("\nYou Won")
        
#--------------------------------------------------------------------------------------------------------------------------------------------------------#             
main()