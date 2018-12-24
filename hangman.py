# Python言語の基本から仕事のやり方まで独学プログラマー
    
# 10 Capter

import random

def hangman(word):
    wrong=0
    stages=["",
            "______   ",
            "|        ",
            "|     |  ",
            "|     0  ",
            "|    /|\ ",
            "|    / \ ",
            "|        "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("Wellcome to the 'Hangman'!")
    list_answer=list(input("You gess 10 words:"))
    
    while wrong < len(stages)-1:
        print("\n")
#        msg="Gess a word."
#       char=input(msg)
        char=random.choice(list_answer)
        if char in rletters:
            c_ind=rletters.index(char)
            board[c_ind]=char
            rletters[c_ind]="$"
        else:
            wrong +=1
        print("".join(board))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You are win.")
            print("".join(board))
            win=True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You are loser. The answer is {}.".format(word))            
    
hangman("tomi")
