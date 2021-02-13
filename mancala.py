from os import system as sys
import player
import ai
import time


def introPage():
    while True:
        print('┌─────────────────────────────────────────────────────────────────────┐')
        print("│  __       __                                          __            │")
        print("│ /  \\     /  |                                        /  |           │")
        print("│ $$  \\   /$$ |  ______   _______    _______   ______  $$ |  ______   │")
        print("│ $$$  \\ /$$$ | /      \\ /       \\  /       | /      \\ $$ | /      \\  │")
        print("│ $$$$  /$$$$ | $$$$$$  |$$$$$$$  |/$$$$$$$/  $$$$$$  |$$ | $$$$$$  | │")
        print("│ $$ $$ $$/$$ | /    $$ |$$ |  $$ |$$ |       /    $$ |$$ | /    $$ | │")
        print("│ $$ |$$$/ $$ |/$$$$$$$ |$$ |  $$ |$$ \_____ /$$$$$$$ |$$ |/$$$$$$$ | │")
        print("│ $$ | $/  $$ |$$    $$ |$$ |  $$ |$$       |$$    $$ |$$ |$$    $$ | │")
        print("│ $$/      $$/  $$$$$$$/ $$/   $$/  $$$$$$$/  $$$$$$$/ $$/  $$$$$$$/  │")
        print('└─────────────────────────────────────────────────────────────────────┘')
        print("\t\t\t\t\t\t           __      __   ")
        print("\t\t\t\t\t\t /    __  (  / '_ / _   ")
        print("\t\t\t\t\t\t()(/     __)/)/(/(__)(/ ")
        print("\t\t\t\t\t\t  /           _/     /  \n\n")

        print('\t\t   ┌─────────────────────────┐')
        print('\t\t   │ < 1 >  Player vs Player │')
        print('\t\t   │ < 2 >  Player vs Ai     │')
        print('\t\t   │ < 3 >  Ai     vs Ai     │')
        print('\t\t   │ < 0 >  Exit Game        │')
        print('\t\t   └─────────────────────────┘')

        userInput = input("\n\t\t     > ")
        sys('cls')
        try:
            if 0 <= int(userInput) <= 3:
                return int(userInput)
        except ValueError:
            continue


def outroPage(board, winner):
    print('\n')
    if winner == 1:
        print('\t██████╗  ██╗    ██╗    ██╗██╗███╗   ██╗███████╗██╗')
        print('\t██╔══██╗███║    ██║    ██║██║████╗  ██║██╔════╝██║')
        print('\t██████╔╝╚██║    ██║ █╗ ██║██║██╔██╗ ██║███████╗██║')
        print('\t██╔═══╝  ██║    ██║███╗██║██║██║╚██╗██║╚════██║╚═╝')
        print('\t██║      ██║    ╚███╔███╔╝██║██║ ╚████║███████║██╗')
        print('\t╚═╝      ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝')
    elif winner == 2:
        print('\t██████╗ ██████╗     ██╗    ██╗██╗███╗   ██╗███████╗██╗')
        print('\t██╔══██╗╚════██╗    ██║    ██║██║████╗  ██║██╔════╝██╗')
        print('\t██████╔╝ █████╔╝    ██║ █╗ ██║██║██╔██╗ ██║███████╗██║')
        print('\t██╔═══╝ ██╔═══╝     ██║███╗██║██║██║╚██╗██║╚════██║╚═╝')
        print('\t██║     ███████╗    ╚███╔███╔╝██║██║ ╚████║███████║██╗')
        print('\t╚═╝     ╚══════╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝')
    else:
        print('\t████████╗██╗███████╗██████╗ ██╗')
        print('\t╚══██╔══╝██║██╔════╝██╔══██╗██╗')
        print('\t   ██║   ██║█████╗  ██║  ██║██╗')
        print('\t   ██║   ██║██╔══╝  ██║  ██║╚═╝')
        print('\t   ██║   ██║███████╗██████╔╝██╗')
        print('\t   ╚═╝   ╚═╝╚══════╝╚═════╝ ╚═╝')
    print('\n\n')
    p1Score = sum(board[:7])
    p2Score = sum(board[7:14])
    printBoard([0]*6+[p1Score]+[0]*6+[p2Score])
    input('\n 아무 키나 눌러서 진행하세요. > ')
    sys('cls')


def printBoard(board, turn='r', event=0):
    eventDict = {0: ' '*13, 1: ' Bonus Turn! ', 2: '   Capture!  '}
    colors = {'P1': '\033[93m', 'P2': '\033[96m', 'event': '\033[91m',
              'r': '\033[0m', 'P1pot': '\033[33m', 'P2pot': '\033[36m'}

    turn = colors[turn]+turn+colors['r']
    if event:
        event = colors['event']+eventDict[event]+colors['r']
    else:
        event = colors['r']+eventDict[event]

    print('┌─────────────────────────────────────────────────┐')
    print('│       '+colors['P2pot']+'┌─' +
          colors['P2']+'1'+colors['P2pot']+'─┐ ┌─'+colors['P2']+'2' +
          colors['P2pot']+'─┐ ┌─'+colors['P2']+'3'+colors['P2pot']+'─┐ ┌─' +
          colors['P2']+'4'+colors['P2pot']+'─┐ ┌─'+colors['P2']+'5' +
          colors['P2pot']+'─┐ ┌─'+colors['P2']+'6'+colors['P2pot']+'─┐' +
          colors['r']+'       │')
    print('│       '+colors['P2pot']+'│'+colors['r']+'%2d ' % board[12] +
          colors['P2pot']+'│ │'+colors['r']+'%2d ' % board[11] +
          colors['P2pot']+'│ │'+colors['r']+'%2d ' % board[10] +
          colors['P2pot']+'│ │'+colors['r']+'%2d ' % board[9] +
          colors['P2pot']+'│ │'+colors['r']+'%2d ' % board[8] +
          colors['P2pot']+'│ │'+colors['r']+'%2d ' % board[7] +
          colors['P2pot']+'│'+colors['r']+'       │')
    print('│       '+colors['P2pot']+'└───┘ └───┘ └───┘ └───┘ └───┘ └───┘' +
          colors['r']+'       │')
    print('│ '+colors['P2pot']+'┌─'+colors['P2']+'P' +
          colors['P2pot']+'─┐                                     ' +
          colors['P1pot']+'┌─'+colors['P1']+'P'+colors['P1pot']+'─┐' +
          colors['r']+' │')
    if 'P1' in turn or 'P2' in turn:
        print('│ '+colors['P2pot']+'│'+colors['r']+'%2d ' % board[13] +
              colors['P2pot']+'│'+colors['r']+'     현재 턴 : '+turn+'   ' +
              event+'    '+colors['P1pot']+'│'+colors['r']+'%2d' % board[6] +
              colors['P1pot']+' │'+colors['r']+' │')
    else:
        print('│ '+colors['P2pot']+'│'+colors['r']+'%2d ' % board[13] +
              colors['P2pot']+'│'+colors['r']+'                    ' +
              event+'    '+colors['P1pot']+'│'+colors['r']+'%2d' % board[6] +
              colors['P1pot']+' │'+colors['r']+' │')

    print('│ '+colors['P2pot']+'└─'+colors['P2']+'2' +
          colors['P2pot']+'─┘                                     ' +
          colors['P1pot']+'└─'+colors['P1']+'1'+colors['P1pot']+'─┘' +
          colors['r']+' │')

    print('│       '+colors['P1pot']+'┌─' +
          colors['P1']+'1'+colors['P1pot']+'─┐ ┌─'+colors['P1']+'2' +
          colors['P1pot']+'─┐ ┌─'+colors['P1']+'3'+colors['P1pot']+'─┐ ┌─' +
          colors['P1']+'4'+colors['P1pot']+'─┐ ┌─'+colors['P1']+'5' +
          colors['P1pot']+'─┐ ┌─'+colors['P1']+'6'+colors['P1pot']+'─┐' +
          colors['r']+'       │')

    print('│       '+colors['P1pot']+'│'+colors['r']+'%2d ' % board[0] +
          colors['P1pot']+'│ │'+colors['r']+'%2d ' % board[1] +
          colors['P1pot']+'│ │'+colors['r']+'%2d ' % board[2] +
          colors['P1pot']+'│ │'+colors['r']+'%2d ' % board[3] +
          colors['P1pot']+'│ │'+colors['r']+'%2d ' % board[4] +
          colors['P1pot']+'│ │'+colors['r']+'%2d ' % board[5] +
          colors['P1pot']+'│'+colors['r']+'       │')

    print('│       '+colors['P1pot']+'└───┘ └───┘ └───┘ └───┘ └───┘ └───┘' +
          colors['r']+'       │')

    print('└─────────────────────────────────────────────────┘')


def getDifficulty(str=''):
    while True:
        print(str+'Ai의 난이도를 정해주세요!')
        userInput = input('1 ~ 12 까지의 난이도가 있습니다.  > ')
        sys('cls')
        try:
            if 1 <= int(userInput) <= 12:
                return int(userInput)
        except ValueError:
            continue


def getGamemode2Input():
    while True:
        print('누가 선 플레이어가 될까요?')
        print(' < 1 > 플레이어')
        print(' < 2 > Ai\n')
        userInput = input('> ')
        sys('cls')
        try:
            if 1 <= int(userInput) <= 2:
                break
        except ValueError:
            continue
    difficulty = getDifficulty()
    return int(userInput), difficulty


def getGamemode3Input():
    difficulty1 = getDifficulty('P1 ')
    difficulty2 = getDifficulty('P2 ')
    return difficulty1, difficulty2


def getFirstPlayer(gamemode):
    if gamemode == 1:
        p1, p2 = player.Player(True), player.Player(False)
    elif gamemode == 2:
        userInput, difficulty = getGamemode2Input()
        if userInput == 0:
            return False
        elif userInput == 1:
            p1, p2 = player.Player(True), ai.Ai(False, difficulty)
        else:
            p1, p2 = ai.Ai(True, difficulty), player.Player(False)
    else:
        difficulty1, difficulty2 = getGamemode3Input()
        p1, p2 = ai.Ai(True, difficulty1), ai.Ai(False, difficulty2)
    return p1, p2


def isEnd(board):
    if sum(board[:6]) == 0 or sum(board[7:13]) == 0:
        if sum(board[:6]) > sum(board[7:13]):
            return 1
        elif sum(board[:6]) < sum(board[7:13]):
            return 2
        else:
            return 3
    return 0


def game(gamemode):
    p1, p2 = getFirstPlayer(gamemode)
    board = [4]*6+[0]+[4]*6+[0]
    # board = [0]*14
    isEvent, turn = 0, 1

    while True:
        printBoard(board, 'P1' if turn % 2 else 'P2', isEvent % 3)

        if turn % 2:
            if isinstance(p1, ai.Ai):
                newBoard, isEvent, endSignal, move = p1.action(board)
                print('┌────────────────────────────┐')
                print('│ P1 Ai는', move+1, '에서 움직입니다. │')
                print('└────────────────────────────┘')
                input(" 아무 키나 눌러 진행하세요. > ")
            else:
                newBoard, isEvent, endSignal = p1.action(board)
        else:
            if isinstance(p2, ai.Ai):
                newBoard, isEvent, endSignal, move = p2.action(board)
                print('┌────────────────────────────┐')
                print('│ P2 Ai는', 13-move, '에서 움직입니다. │')
                print('└────────────────────────────┘')
                input(" 아무 키나 눌러 진행하세요. > ")
            else:
                newBoard, isEvent, endSignal = p2.action(board)

        sys('cls')

        if endSignal:
            return False

        board = [newBoard[i] for i in range(14)]
        state = isEnd(board)
        if state:
            outroPage(board, state)
            return False

        if not isEvent:
            turn += 1


def main():
    while True:
        userInput = introPage()
        if userInput == 0 or game(userInput):
            break
    print('Game Ended\n')
    print('github.com/conanlhj')
