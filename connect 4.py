columnfill = [0, 0, 0, 0, 0, 0, 0]
row = [
       ["-", "-", "-", "-", "-", "-", "-"], 
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ]
n = 1
nn = 0

def showboard(board):
    for i in range(len(board)):
        print(board[i])
def place(s,c):
    rowc = row[5-columnfill[c]]
    rowc[c] = s
    row[5-columnfill[c]] = rowc
    columnfill[c] = columnfill[c] + 1
def wincheck(colour, bank):
    win = 0
    for i in range(len(bank)):
        count = 0
        for j in range(len(bank[0])):
            if bank[i][j] == colour:
                 count = count + 1
            else:
                count = 0
            if count >= 4:
                win = win + 1
    return win

p1name = str(input("Player 1, enter your name.   "))
p2name = str(input("Player 2, enter your name.   "))
playernames = [p1name, p2name]
matchscores = [0, 0]

ww = 0
while ww != "n" and ww != "N":
    columnfill = [0, 0, 0, 0, 0, 0, 0]
    row = [
       ["-", "-", "-", "-", "-", "-", "-"], 
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ["-", "-", "-", "-", "-", "-", "-"],
       ]
    n = 1
    w = 0
    active = 8
    print(playernames[nn%2] + " has the first turn.")
    while w == 0:
        if n % 2 == 0:
            turn = "R"
        else:
            turn = "Y"
        print(turn)
        movevalid = 0
        while movevalid == 0:
            placechoice = str(input())
            if len(placechoice) == 1:
                active = int(placechoice) - 1
            if active < 7 and columnfill[active] < 6:
                place(turn, active)
                showboard(row)
                movevalid = 1
            else:
                print("invalid move")

        column = list()
        diagonalup = list()
        diagonaldown = list()
        for i in range(7):
            column1 = list()
            for j in range(6):
                column1.append(row[j][i])
            column.append(column1)
        for i in range(3):
            diagonal1 = list()
            diagonal3 = list()
            for j in range(2-i):
                diagonal1.append("0")
                diagonal3.append("0")
            for j in range(4+i):
                diagonal1.append(row[j][3+i-j])
                diagonal3.append(row[j][3-i+j])
            diagonalup.append(diagonal1)
            diagonaldown.append(diagonal3)
            diagonal2 = list()
            diagonal4 = list()
            for j in range(6-i):
                diagonal2.append(row[5-j][1+i+j])
                diagonal4.append(row[5-j][5-i-j])
            for j in range(i):
                diagonal2.append("0")
                diagonal4.append("0")
            diagonalup.append(diagonal2)
            diagonaldown.append(diagonal4)

        wins = wincheck(turn, row) + wincheck(turn, column) + wincheck(turn, diagonalup) + wincheck(turn, diagonaldown)
        if wins >= 1:
            print(turn + " wins")
            w = 1
            if turn == "Y":
                matchscores[nn%2] = matchscores[nn%2] + 1
            else:
                matchscores[(nn+1)%2] = matchscores[(nn+1)%2] + 1
        if n >= 42:
            w = 1
            matchscores[0] = matchscores[0] + 0.5
            matchscores[1] = matchscores[1] + 0.5
        n = n + 1
    for i in range(2):
        print(playernames[i]+ "   " + str(matchscores[i]))
    ww = str(input("Play again? (Y/n)   "))
    nn = nn + 1
