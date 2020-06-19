board = {
    'top-L' : ' ',
    'top-M' : ' ',
    'top-R' : ' ',
    'mid-L': ' ',
    'mid-M': ' ',
    'mid-R': ' ',
    'bot-L': ' ',
    'bot-M': ' ',
    'bot-R': ' ',
}

user_inputs = ['top-L','top-M','top-R','mid-L','mid-M','mid-R','bot-L','bot-M','bot-R',]

entered_inputs = []

flag = True

def printboard(b):
    print("")
    print('\t\t'+b['top-L']+'|'+b['top-M']+'|'+b['top-R'])
    print('\t\t-----')
    print('\t\t'+b['mid-L']+'|'+b['mid-M']+'|'+b['mid-R'])
    print('\t\t-----') 
    print('\t\t'+b['bot-L']+'|'+b['bot-M']+'|'+b['bot-R'])
    print("")

while True:
    print('where do you want to enter')
    print('top = top row || mid = middle row || bot = bottom row')
    print('L = left cell || M = middle cell || R = right cell')
    printboard(board)
    data = input()
    if data in user_inputs and not(data in entered_inputs):
        
        entered_inputs.append(data)

        if flag:
            board[data] = 'x'
            flag = False
        else:
            board[data] = 'o'
            flag = True
    else:
        print("\ncheck the spelling plz!! or it may be filled you cant overwrite it sorry:(\n")

    if board['top-L']==board['top-M']==board['top-R']!=' ' or board['mid-L']==board['mid-M']==board['mid-R']!=' ' or board['bot-L']==board['bot-M']==board['bot-R']!=' ' or board['top-L']==board['mid-L']==board['bot-L'] !=' 'or board['top-M']==board['mid-M']==board['bot-M']!=' ' or board['top-R']==board['mid-R']==board['bot-R']!=' ' or board['top-L']==board['mid-M']==board['bot-R']!=' ' or board['top-R']==board['mid-M']==board['bot-L']!=' ':
        printboard(board)
        print(board[data]+' won the match\n')
        print('do you want to play one more!!!')
        again = input('y/n : ')
        if again != 'y':

            break
        else:
            board = {
                'top-L' : ' ',
                'top-M' : ' ',
                'top-R' : ' ',
                'mid-L': ' ',
                'mid-M': ' ',
                'mid-R': ' ',
                'bot-L': ' ',
                'bot-M': ' ',
                'bot-R': ' ',
            }
            entered_inputs = []
