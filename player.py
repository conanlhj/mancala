class Player:
    isFirst = False

    def __init__(self, isFirst):
        self.isFirst = isFirst

    def action(self, board):
        print()
        print('\t      ┌─────────────────────┐')
        print('\t      │ 어디를 움직일까요?  │')
        print('\t      │   1 ~ 6 : 팟 선택   │')
        print('\t      │  0  : 메인화면으로  │')
        print('\t      └─────────────────────┘')

        userInput = input('\t\t> ')
        try:
            if 1 <= int(userInput) <= 6:
                userInput = int(userInput)-1
            elif int(userInput) == 0:
                return 0, 0, True
            else:
                return board, 3, False
        except ValueError:
            return board, 3, False

        if self.isFirst:
            newBoard, event = move(board, userInput)
        else:
            newBoard, event = move(board, 12-userInput)
        return newBoard, event, False


def move(board, pot):
    newBoard = [board[i] for i in range(14)]
    stones = newBoard[pot]
    newBoard[pot] = 0

    if stones == 0:
        return newBoard, 3

    cnt = 0
    while cnt < stones:
        nextPot = (pot+cnt+1) % 14

        if (nextPot == 6 and pot > 6) or (nextPot == 13 and pot < 6):
            stones += 1
        else:
            newBoard[nextPot] += 1
        cnt += 1

    lastPot = (pot+stones) % 14

    if lastPot == 6 or lastPot == 13:
        return newBoard, 1

    frontPot = 12-lastPot

    if (newBoard[lastPot] != 1 or pot//7 != lastPot//7 or
       newBoard[frontPot] == 0):
        return newBoard, 0

    newBoard[pot//7*7+6] += newBoard[frontPot] + 1
    newBoard[frontPot] = 0
    newBoard[lastPot] = 0
    return newBoard, 2
