import player


class Ai:
    isFirst = False
    MAX_DEPTH = 0

    def __init__(self, isFirst, MAX_DEPTH):
        self.isFirst = isFirst
        self.MAX_DEPTH = MAX_DEPTH

    def action(self, board):
        if self.isFirst:
            score, move = maxPlay(board, 0, self.MAX_DEPTH, -50, 50)
        else:
            score, move = minPlay(board, 0, self.MAX_DEPTH, -50, 50)
        newBoard, event = player.move(board, move)
        return newBoard, event, False, move


def isEnd(aiboard):
    if sum(aiboard[:6]) == 0 or sum(aiboard[7:13]) == 0:
        return True
    return False


def maxPlay(aiBoard, curDepth, maxDepth, alpha, beta):
    if isEnd(aiBoard) or (curDepth == maxDepth):
        return curState(aiBoard), -1

    maxScore, maxMove = -50, 0
    for i in range(6):

        if aiBoard[i] == 0:
            continue

        newAiBoard, event = player.move([aiBoard[j] for j in range(14)], i)

        if event:
            score, move = maxPlay(newAiBoard, curDepth+1, maxDepth,
                                  alpha, beta)
        else:
            score, move = minPlay(newAiBoard, curDepth+1, maxDepth,
                                  alpha, beta)

        if maxScore < score:
            maxScore = score
            maxMove = i

        alpha = max(alpha, maxScore)

        if maxScore > beta:
            break
    return maxScore, maxMove


def minPlay(aiBoard, curDepth, maxDepth, alpha, beta):
    if isEnd(aiBoard) or (curDepth == maxDepth):
        return curState(aiBoard), -1

    minScore, minMove = 50, 0
    for i in range(7, 13):

        if aiBoard[i] == 0:
            continue

        newAiBoard, event = player.move([aiBoard[j] for j in range(14)], i)

        if event:
            score, move = minPlay(newAiBoard, curDepth+1, maxDepth,
                                  alpha, beta)
        else:
            score, move = maxPlay(newAiBoard, curDepth+1, maxDepth,
                                  alpha, beta)

        if minScore > score:
            minScore = score
            minMove = i

        beta = min(beta, minScore)

        if minScore < alpha:
            break
    return minScore, minMove


def curState(board):
    return sum(board[:7]) - sum(board[7:14])
