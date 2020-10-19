from bangtal import *
import random
import time

setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

Main = Scene('PuzzleLOL', 'Images/배경.png')
Mode = Scene("PuzzleLOL", 'Images/챔피언선택.png')
Map_Blitzcrank = Scene("PuzzleLOL", 'Images/블리츠크랭크/블츠맵.png')

Start_Button = Object('Images/게임시작.png')
End_Button = Object('Images/게임종료.png')
Ready_Button = Object('Images/준비완료.png')
Victory_Button = Object('Images/승리.png')
ReStart_Button = Object('Images/한번더하기.png')

global playing

Button_Blitzcrank = Object('Images/블리츠크랭크/블츠버튼.png')
Button_Blitzcrank.locate(Mode, 380, 430)
Button_Blitzcrank.show()
Button_Yuumi = Object('Images/유미/유미버튼.png')
Button_Yuumi.locate(Mode, 750, 430)
Button_Yuumi.show()
Button_Ezreal = Object('Images/이즈리얼/이즈버튼.png')
Button_Ezreal.locate(Mode, 380, 270)
Button_Ezreal.show()
Button_Zed = Object('Images/제드/제드버튼.png')
Button_Zed.locate(Mode, 750, 270)
Button_Zed.show()
Button_Aphelios = Object('Images/아펠리오스/아펠버튼.png')
Button_Aphelios.locate(Mode, 380, 110)
Button_Aphelios.show()
Button_XayahRakan = Object('Images/자야라칸/자야라칸버튼.png')
Button_XayahRakan.locate(Mode, 750, 110)
Button_XayahRakan.show()

Start_Button.locate(Main, 540, 70)
Start_Button.show()

def Start_Button_onMouseAction(x, y, action):
    Mode.enter()
Start_Button.onMouseAction = Start_Button_onMouseAction

End_Button.locate(Main, 540, 20)
End_Button.show()

def End_Button_onMouseAction(x, y, action):
    endGame()
End_Button.onMouseAction = End_Button_onMouseAction

def ReStart_Button_onMouseAction(x, y, action):
    Mode.enter()
ReStart_Button.onMouseAction = ReStart_Button_onMouseAction

def movable(index, n):
    if (index % n > 0 and index - 1 == blank) or \
        (index % n < n - 1 and index + 1 == blank) or \
        (index > n - 1 and index - n == blank) or \
        (index < n*n - n and index + n == blank):
        return True
    return False

def Button_Blitzcrank_onMouseAction(x, y, action):
    Victory_Button.hide()
    ReStart_Button.hide()
    Ready_Button.hide()

    global blank, n, map, playing
    blank = 6
    n = 3
    map = Map_Blitzcrank
    playing = 0

    map.enter()
    puzzle = []
    solution = []

    for i in range(n**2):
         filename = 'Images/블리츠크랭크/블리츠크랭크_'+str(i)+'.png'
         puzzle.append(Object(filename))
         solution.append(puzzle[i])
         x=380+200*(i%3)
         y=460-200*(i//3)
         puzzle[i].locate(map, x, y)
         puzzle[i].show()
         puzzle[i].onMouseAction = lambda x, y, action, obj=puzzle[i] : puzzleClick(x, y, action, obj)

    def puzzleClick(x, y, action, obj):
        global blank
        global n
        global map
        global playing
        
        for i, p in enumerate(puzzle):
            if p == obj:
                index = i

        if movable(index, n) and playing == 1:

            puzzle[index].locate(map, 380+200*(blank%3), 460-200*(blank//3))   
            puzzle[blank].locate(map, 380+200*(index%3), 460-200*(index//3))        

            puzzle[index] = puzzle[blank]
            puzzle[blank] = obj

            blank = index

            if completed():
                for i in range(n**2):
                    puzzle[i].hide()

                Victory_Button.locate(map, 330, 10)
                Victory_Button.show()
                ReStart_Button.setScale(1.1)
                ReStart_Button.locate(map, 585, 75)
                ReStart_Button.show()
                playing = 0
                
    def completed():
        global n

        for index in range(n**2):
            if puzzle[index] != solution[index]: 
                return False

        return True           

    Ready_Button.locate(map, 540, 10)
    Ready_Button.setScale(1.2)
    Ready_Button.show()

    def Ready_Button_onMouseAction(x, y, action):
        global blank, map
        global playing

        playing = 1
        Ready_Button.hide()
        puzzle[blank].hide()

        for i in range(2):
            index = Randomindex(blank)

            puzzle[index].locate(map, 380+200*(blank%3), 460-200*(blank//3))   
            puzzle[blank].locate(map, 380+200*(index%3), 460-200*(index//3))      

            temp2 = puzzle[index]
            puzzle[index] = puzzle[blank]
            puzzle[blank] = temp2

            blank = index   

    Ready_Button.onMouseAction = Ready_Button_onMouseAction         
    
def Randomindex(blank):
    global n

    if blank == 0:
        index = random.choice([blank + 1, blank + n])
    elif 0 < blank < n:
        index = random.choice([blank - 1, blank + 1, blank + n]) 
    elif blank == n - 1:
        index = random.choice([blank - 1, blank + n])
    elif blank % n == 0 and blank != 0 and blank != (n**2 - n):
        index = random.choice([blank - n, blank + 1, blank + n])
    elif blank % n == n - 1 and blank != (n -1) and blank != (n**2 - 1):
        index = random.choice([blank - n, blank - 1, blank + n])
    elif blank == n**2 - n:
        index = random.choice([blank - n, blank + 1])
    elif blank == n**2 - 1:
        index = random.choice([blank - n, blank - 1])
    elif n**2 - n < blank < n**2 - 1:
        index = random.choice([blank - n])
    else:
        index = random.choice([blank - n, blank - 1, blank + 1, blank + n])
    
    return index


Button_Blitzcrank.onMouseAction = Button_Blitzcrank_onMouseAction

startGame(Main)

