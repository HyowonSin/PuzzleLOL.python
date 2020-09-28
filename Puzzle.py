from bangtal import *


setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

Main = Scene('PuzzleLOL', 'Images/배경.png')
Mode = Scene("PuzzleLOL", 'Images/챔피언선택.png')
Map_Blitzcrank = Scene("PuzzleLOL", 'Images/블츠맵.png')

Start_Button = Object('Images/게임시작.png')
End_Button = Object('Images/게임종료.png')
ReStart_Button = Object('Images/한번더하기.png')
Ready_Button = Object('Images/준비완료.png')

Button_Blitzcrank = Object('Images/블츠버튼.png')
Button_Blitzcrank.locate(Mode, 380, 430)
Button_Blitzcrank.show()
Button_Yuumi = Object('Images/유미버튼.png')
Button_Yuumi.locate(Mode, 750, 430)
Button_Yuumi.show()
Button_Ezreal = Object('Images/이즈버튼.png')
Button_Ezreal.locate(Mode, 380, 270)
Button_Ezreal.show()
Button_Zed = Object('Images/제드버튼.png')
Button_Zed.locate(Mode, 750, 270)
Button_Zed.show()
Button_Aphelios = Object('Images/아펠버튼.png')
Button_Aphelios.locate(Mode, 380, 110)
Button_Aphelios.show()
Button_XayahRakan = Object('Images/자야라칸버튼.png')
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




def Button_Blitzcrank_onMouseAction(x, y, action):
    Map_Blitzcrank.enter()
    puzzle = []

    global blank
    blank = 6

    for i in range(9):
         filename = 'Images/블리츠크랭크/블리츠크랭크_'+str(i)+'.png'
         puzzle.append(Object(filename))
         x=380+200*(i%3)
         y=460-200*(i//3)
         puzzle[i].locate(Map_Blitzcrank, x, y)
         puzzle[i].show()
         puzzle[i].onMouseAction = lambda x, y, action, picture=puzzle[i], index=i : puzzleClick(x, y, action, picture, index)

    puzzle[blank].hide()


    #  zle[2])
# def swap(x, y):
#     z = x
#     x = y
#     y = z

    def puzzleClick(x, y, action, picture, index):
        global blank

        print(index)
        print(puzzle[index])
        print(puzzle[blank])
        # if index==blank - 3 or index==blank-1 or index==blank+1 or index==blank + 3:
        #     print("true")
        #     print("a", puzzle[i], puzzle[blank])
        #     puzzle[i], puzzle[blank] = puzzle[blank], puzzle[i]
        #     print("b", puzzle[i], puzzle[blank])
        puzzle[index].locate(Map_Blitzcrank, 380+200*(blank%3), 460-200*(blank//3))   
        puzzle[blank].locate(Map_Blitzcrank, 380+200*(index%3), 460-200*(index//3))        

        temp = Object('temp')
        temp = puzzle[index]

        puzzle[index] = puzzle[blank]
        puzzle[index].hide()

        puzzle[blank] = temp
        puzzle[blank].show()

        blank = index

        # swap(index, blank)

        # blank = i
        # swap(puzzle[i], puzzle[blank])

            

        # print(i)
        # print(blank)
        # print(puzzle[blank])
        # print(puzzle[1])
        # print(puzzle[2])

         




             


         


#for i in range(9):
#    def puzzle[i]_onMouseAction(x, y, action):
#        endGame()
#    puzzle[i].onMouseAction = puzzle[i]_onMouseAction



Ready_Button.show()




Button_Blitzcrank.onMouseAction = Button_Blitzcrank_onMouseAction



startGame(Main)

