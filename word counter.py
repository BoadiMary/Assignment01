def counting_app():
    user_input=input("enter your text: ")
    word_count=user_input.split()
    print("Number of words ",(len(word_count)))
    char_count=len(user_input)
    print("Number of characters ",(char_count))
    sentence_count=user_input.count('.')+user_input.count('!')+user_input.count('?')
    print("Number of sentence ",sentence_count)
counting_app()    