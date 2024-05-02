secret_num=54
guess_count=0
guess_limit=3


while guess_count<guess_limit:
    user_number = input("Enter a number between 1-100")
    guess_count+=1
    if user_number==secret_num:
        print("Welldone !!, You have guessed it correctly")
        break
else:
    print("Limit finish")


