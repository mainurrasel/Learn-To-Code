#Computing Read Ease Score of Text from Chapter 1
import ch1text 
#Counting words
def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count
#Counting syllables
def count_syllables_in_word(word):
    count = 0

    endings = '.,;!?:)("'
    last_char = word[-1]
    
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word
    
    if len(processed_word) <= 3:
        return 1
    
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]
    
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False
    
    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
#Check the word to see if it ends in y or Y, and if so, increase the syllable count.
    if processed_word[-1] in 'yY':
        count = count + 1
        
    return count
#Counting sentences
def count_sentences(text):
    count = 0

    terminals = '.;?!'
    for char in text:
        if char in terminals:
            count = count + 1
    return count
#output results
def output_results(score):
    if score >= 90.0:
        print( "Reading level of 5th Grade")
    elif score >= 80.0:
        print ( "Reading level of 6th Grade")
    elif score >= 70.0:
        print( "Reading level of 7th Grade")
    elif score >= 60.0:
        print( "Reading level of 8-9th Grade")
    elif score >= 50.0:
        print( "Reading level of 10-12th Grade")
    elif score >= 30.0:
        print( "Reading level of College Student")
    else:
        print( "Reading level of College Graduate")

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)
#Add the formula below to our word, sentence, and syllable count code.
    score = (206.835 - 1.015 * (total_words / total_sentences)
             - 84.6 * (total_syllables / total_words))
    
    #print(total_words, 'words')
    #print(total_sentences, 'sentences')
    #print(total_syllables, 'syllables')
#And add a print statement so you can see the results.
    #print(score, 'reading ease score')
    output_results(score)
compute_readability(ch1text.text)

