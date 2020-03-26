def knight(p1, p2, minX, maxX, minY, maxY, paths = []):
    p1L = list(p1)
    p2L = list(p2)
    def moveUpRight(p1L):
        if (ord(minY) <= ord(p1L[1]) + 2 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) + 1 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) + 2)
            p1LCopy[0] = chr(ord(p1L[0]) + 1)
            return p1LCopy
        else:
            return p1L
    def moveDownRight(p1L):
        if (ord(minY) <= ord(p1L[1]) - 2 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) + 1 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) - 2)
            p1LCopy[0] = chr(ord(p1L[0]) + 1)
            return p1LCopy
        else:
            return p1L
    def moveUpLeft(p1L):
        if (ord(minY) <= ord(p1L[1]) + 2 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) - 1 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) + 2)
            p1LCopy[0] = chr(ord(p1L[0]) - 1)
            return p1LCopy
        else:
            return p1L
    def moveDownLeft(p1L):
        if (ord(minY) <= ord(p1L[1]) - 2 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) - 1 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) - 2)
            p1LCopy[0] = chr(ord(p1L[0]) - 1)
            return p1LCopy
        else:
            return p1L
    def moveRightUp(p1L):
        if (ord(minY) <= ord(p1L[1]) + 1 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) + 2 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) + 1)
            p1LCopy[0] = chr(ord(p1L[0]) + 2)
            return p1LCopy
        else:
            return p1L
    def moveRightDown(p1L):
        if (ord(minY) <= ord(p1L[1]) - 1 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) + 2 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) - 1)
            p1LCopy[0] = chr(ord(p1L[0]) + 2)
            return p1LCopy
        else:
            return p1L
    def moveLeftUp(p1L):
        if (ord(minY) <= ord(p1L[1]) + 1 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) - 2 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) + 1)
            p1LCopy[0] = chr(ord(p1L[0]) - 2)
            return p1LCopy
        else:
            return p1L
    def moveLeftDown(p1L):
        if (ord(minY) <= ord(p1L[1]) - 1 <= ord(maxY)) & (ord(minX) <= ord(p1L[0]) - 2 <= ord(maxX)):
            p1LCopy = ['','']
            p1LCopy[1] = chr(ord(p1L[1]) - 1)
            p1LCopy[0] = chr(ord(p1L[0]) - 2)
            return p1LCopy
        else:
            return p1L
    def moveKnight(start, end, paths, lowestEndCount = 1000000000000, alreadyVisited = [], count = 0):
        if alreadyVisited == []:
            alreadyVisited.append(start)
        if start == end:
            # print(count, alreadyVisited, "\n")
            paths.append([count, alreadyVisited])
            if count < lowestEndCount:
                lowestEndCount = count
            # return count
            # print(paths, '\n')
        else:
            if count < lowestEndCount:
                if moveUpRight(start) == end or moveDownRight(start) == end or moveUpLeft(start) == end or moveDownLeft(start) == end or moveRightUp(start) == end\
                or moveRightDown(start) == end or moveLeftUp(start) == end or moveLeftDown(start) == end:
                    alreadyVisited.append(end)
                    paths.append([count + 1, alreadyVisited])
                else:
                    if (moveUpRight(start) != start) and (moveUpRight(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveUpRight(start))
                        moveKnight(moveUpRight(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if (moveDownRight(start) != start) and (moveDownRight(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveDownRight(start))
                        moveKnight(moveDownRight(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if moveUpLeft(start) != start and (moveUpLeft(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveUpLeft(start))
                        moveKnight(moveUpLeft(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if moveDownLeft(start) != start and (moveDownLeft(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveDownLeft(start))
                        moveKnight(moveDownLeft(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if moveRightUp(start) != start and (moveRightUp(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveRightUp(start))
                        moveKnight(moveRightUp(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if moveRightDown(start) != start and (moveRightDown(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveRightDown(start))
                        moveKnight(moveRightDown(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if moveLeftUp(start) != start and (moveLeftUp(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveLeftUp(start))
                        moveKnight(moveLeftUp(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)
                    if moveLeftDown(start) != start and (moveLeftDown(start) not in alreadyVisited):
                        alreadyVisitedCopy = alreadyVisited.copy()
                        alreadyVisitedCopy.append(moveLeftDown(start))
                        moveKnight(moveLeftDown(start), end, paths, lowestEndCount, alreadyVisitedCopy, count + 1)

    moveKnight(p1L, p2L, paths)
    countList = []
    smallestPaths = []
    for i in paths:
        countList.append(i[0])
    for i in paths:
        if(i[0] == min(countList)):
            smallestPaths.append(i)
    f = open("/home/dem/" + p1 + "-" + p2 + "-" + maxY + "x" + maxY + ".txt", 'w')
    f.write(str(smallestPaths))
    f.close()
    # return smallestPaths

knight('a1', 'd4', 'a', 'e', '1', '5')
