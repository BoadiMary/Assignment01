user_word=input("Enter a word ")
index=0
while index< len(user_word):
    print(user_word[index])
    index +=1
correctPassword="secret"
attemtsLeft=3
userAttempts=""
while attemtsLeft>0 and userAttempts!=correctPassword:
    userAttempts=input(f"Enter password(Attempts left: {attemtsLeft}): ")
    attemtsLeft -= 1
if userAttempts==correctPassword:
    print("Access Granted!")
elif attemtsLeft ==0:
    print("Access Denied!")
    