from inc.chessengine import *
from Tkinter import *
import Pmw
from tkMessageBox import showinfo
from PIL.ImageTk import PhotoImage
from tkFileDialog import askopenfilename

__author__="Hollgam and Vinchkovsky"
__description__="A reder for PGN files."
__version__="0.3"

###VARS
stopOnWhite = 1
firstMove = 1
maxNumber = -1
tempCounter = 0


### end of VARS

class PGN_GUI(Frame):

    def __init__(self):

        Frame.__init__(self)
        Pmw.initialise()

        self.lightColor = "#F0D9B5"
        self.darkColor = "#B58863"
        self.lastMoveColor1 = "#FBF4A1"
        self.lastMoveColor2 = "#E9DC42"
        self.takenPiecesBackground = "white"
        self.sideBarWidth = 220
        self.boardFliped  = 0
        self.currentPosition = createStartPosition()

        self.font1 = "14"
        self.infoRightFont = "Helvetica 9 bold"
        self.infoLeftFont = "Helvetica 9"

        self.colorSelected = "#eff6b2"
        self.prevButton = Button()

        self.takenPiecesWhiteImages = []
        self.takenPiecesBlackImages = []
        self.infoLabelsData = []

        self.noBlackLastMove = 0

        self.middleListPos = 7
        self.buttonHC = 1.0

        self.gameLine = "1."
        #self.gameInfo = {'White': '', 'WhiteElo': '', 'Black': '', 'BlackElo': '', 'Event': '', 'Site': '', 'Date': '', 'TimeControl': '', 'Round': '', 'Result': '', 'Termination': ''}
        self.gameInfoKeys = ['White', 'Black', 'WhiteElo', 'BlackElo', 'Event', 'Site', 'Date', 'TimeControl', 'Round', 'Result', 'Termination']
        #self.gameInfoKeys.sort()

        try:
            self.imageEmpty = PhotoImage(file = "img/set1/default/empty.gif")
            self.imageWhiteRock = PhotoImage(file = "img/set1/default/wr.png")
            self.imageBlackRock = PhotoImage(file = "img/set1/default/br.png")
            self.imageWhiteBishop = PhotoImage(file = "img/set1/default/wb.png")
            self.imageBlackBishop = PhotoImage(file = "img/set1/default/bb.png")
            self.imageWhiteKnight = PhotoImage(file = "img/set1/default/wn.png")
            self.imageBlackKnight = PhotoImage(file = "img/set1/default/bn.png")
            self.imageWhiteQueen = PhotoImage(file = "img/set1/default/wq.png")
            self.imageBlackQueen = PhotoImage(file = "img/set1/default/bq.png")
            self.imageWhiteKing = PhotoImage(file = "img/set1/default/wk.png")
            self.imageBlackKing = PhotoImage(file = "img/set1/default/bk.png")
            self.imageWhitePawn = PhotoImage(file = "img/set1/default/wp.png")
            self.imageBlackPawn = PhotoImage(file = "img/set1/default/bp.png")

            self.imageTakenWhiteRock = PhotoImage(file = "img/set1/taken/wr.png")
            self.imageTakenBlackRock = PhotoImage(file = "img/set1/taken/br.png")
            self.imageTakenWhiteBishop = PhotoImage(file = "img/set1/taken/wb.png")
            self.imageTakenBlackBishop = PhotoImage(file = "img/set1/taken/bb.png")
            self.imageTakenWhiteKnight = PhotoImage(file = "img/set1/taken/wn.png")
            self.imageTakenBlackKnight = PhotoImage(file = "img/set1/taken/bn.png")
            self.imageTakenWhiteQueen = PhotoImage(file = "img/set1/taken/wq.png")
            self.imageTakenBlackQueen = PhotoImage(file = "img/set1/taken/bq.png")
            self.imageTakenWhitePawn = PhotoImage(file = "img/set1/taken/wp.png")
            self.imageTakenBlackPawn = PhotoImage(file = "img/set1/taken/bp.png")
        except:
            print "Falied to load files from \\img\\set1 folder"


        self.pack(expand=YES, fill=BOTH)
        self.master.resizable(0, 0)
        self.master.title('PyGN')
        self.master.iconbitmap('img/favicon.ico')


        # HEADER
        self.headerFrame = Frame(self)
        self.headerFrame.grid(column=0 , row=0, sticky = W+N)
        self.myBalloon = Pmw.Balloon(self)
        self.choices = Pmw.MenuBar(self.headerFrame, balloon=self.myBalloon)
        self.choices.pack(side=LEFT, fill=X)

        # create File menu and items
        self.choices.addmenu("Game", "Game")
        self.choices.addmenuitem("Game", "command", "Load new File", command=self.loadGame, label="Load")
        self.choices.addmenuitem("Game", 'separator')
        self.choices.addmenuitem("Game", "command", "Exit this game", command=self.exitGame, label="Exit")

        self.choices.addmenu("View", "Change the way it looks")
        #flip board
        self.choices.addmenuitem("View", "command", "Flip board", command=self.flipBoard, label="Flip board")


        # create Options menu and items
        self.choices.addmenu("Options", "Twik this program")


        #color scheme
        self.choices.addcascademenu("Options", "Pieces Style")
        self.selectedColorScheme = StringVar()
        self.selectedColorScheme.set("Set 1")
        self.choices.addmenuitem("Pieces Style", "radiobutton", label="Set 1", variable=self.selectedColorScheme, command=self.changeColorScheme)
        self.choices.addmenuitem("Pieces Style", "radiobutton", label="Set 2", variable=self.selectedColorScheme, command=self.changeColorScheme)

        #board color
        self.choices.addcascademenu("Options", "Board colors")
        self.selectedBoardColor = StringVar()
        self.selectedBoardColor.set("Brown")
        self.choices.addmenuitem("Board colors", "radiobutton", label="Brown", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Light", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Green", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Blue", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Grey", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Red", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Orange", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Pink", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Purple", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Tan", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Black & White", variable=self.selectedBoardColor, command=self.changeBoardColor)
        self.choices.addmenuitem("Board colors", "radiobutton", label="Winboard", variable=self.selectedBoardColor, command=self.changeBoardColor)

        #board size
        self.choices.addcascademenu("Options", "Board size")
        self.selectedBoardSize = StringVar()
        self.selectedBoardSize.set("Default")
        self.choices.addmenuitem("Board size", "radiobutton", label="Small", variable=self.selectedBoardSize, command=self.changeBoardSize)
        self.choices.addmenuitem("Board size", "radiobutton", label="Default", variable=self.selectedBoardSize, command=self.changeBoardSize)
        self.choices.addmenuitem("Board size", "radiobutton", label="Large", variable=self.selectedBoardSize, command=self.changeBoardSize)

        self.choices.addmenuitem("Options", 'separator')
        # add items to Options/ShowLastMove
        self.choices.addcascademenu("Options", "Show last move")
        self.selectedShowLastMove = StringVar()
        self.selectedShowLastMove.set("Yes")
        self.choices.addmenuitem("Show last move", "radiobutton", label="Yes", variable=self.selectedShowLastMove, command=self.changeShowLastMove)
        self.choices.addmenuitem("Show last move", "radiobutton", label="No", variable=self.selectedShowLastMove, command=self.changeShowLastMove)

#        # add items to Options/ShowNextMove
#        self.choices.addcascademenu("Options", "Show next move")
#        self.selectedShowNextMove = StringVar()
#        self.selectedShowNextMove.set("No")
#        self.choices.addmenuitem("Show next move", "radiobutton", label="Yes", variable=self.selectedShowNextMove, command=self.changeShowNextMove)
#        self.choices.addmenuitem("Show next move", "radiobutton", label="No", variable=self.selectedShowNextMove, command=self.changeShowNextMove)

#        # add items to Options/ShowLegalMoves
#        self.choices.addcascademenu("Options", "Show legal moves")
#        self.selectedShowLegalMoves = StringVar()
#        self.selectedShowLegalMoves.set("No")
#        self.choices.addmenuitem("Show legal moves", "radiobutton", label="Yes", variable=self.selectedShowLegalMoves, command=self.changeShowLegalMoves)
#        self.choices.addmenuitem("Show legal moves", "radiobutton", label="No", variable=self.selectedShowLegalMoves, command=self.changeShowLegalMoves)

        self.choices.addmenu("Help", "Help")
        self.choices.addmenuitem("Help", "command", command=self.showAbout, label="About")

        self.mainFrame = Frame(self)
        self.mainFrame.grid(column=0, row=1)

        self.frame1 = Frame(self.mainFrame)
        self.frame1.pack()

        self.buttonsFrame = Frame(self.mainFrame)
        self.createBoard()

        self.KeyWidth=12

        self.frame2 = Frame(self.mainFrame)
        self.frame2.pack(side = RIGHT, fill=BOTH, expand = YES)

        self.KeyStart = Button(self.frame2,text='|<',name='start',command = self.showStartPosition, state = DISABLED)
        self.KeyStart.pack(side=LEFT, fill=BOTH, expand=1)

        self.KeyBack5 = Button(self.frame2,text='<<',name='back5',command = self.moveBack5, state = DISABLED)
        self.KeyBack5.pack(side=LEFT, fill=BOTH, expand=1)

        self.KeyBack = Button(self.frame2,text='<',name='back',command = self.moveBack, state = DISABLED)
        self.KeyBack.pack(side=LEFT, fill=BOTH, expand=1)

        self.KeyForward = Button(self.frame2,text='>',name='forward', command = self.moveForward, state = DISABLED)
        self.KeyForward.pack(side=LEFT, fill=BOTH, expand=1)

        self.KeyForward5 = Button(self.frame2,text='>>',name='forward5', command = self.moveForward5, state = DISABLED)
        self.KeyForward5.pack(side=LEFT, fill=BOTH, expand=1)

        self.KeyEnd = Button(self.frame2,text='>|',name='load',command = self.showLastPosition, state = DISABLED)
        self.KeyEnd.pack(side=LEFT, fill=BOTH, expand=1)



        # Create and pack the NoteBook.
        self.notebook = Pmw.NoteBook(self)
        self.notebook.grid(column=1 , row=1,sticky=NW, rowspan=2)

        # Add the "Appearance" page to the notebook.
        self.movePage = self.notebook.add('Moves       ')
        self.notebook.tab('Moves       ').focus_set()

        self.sideBar = Frame(self.movePage, width=self.sideBarWidth, height=430)
        self.sideBar.grid(column=1 , row=1,sticky=NW, rowspan=2)
        self.sideBar.grid_propagate(False)

        #LIST OF MOVES
        self.moveListFrame = Frame(self.sideBar)
        self.moveListFrame.grid(row=0,column=0,sticky=NW)
        self.vscrollbar = Scrollbar(self.moveListFrame)
        self.vscrollbar.grid(row=0, column=1, sticky=N+S, pady=4)
        self.canvas = Canvas(self.moveListFrame,yscrollcommand=self.vscrollbar.set,height=315 ,width=196)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W, pady=4)
        self.vscrollbar.config(command=self.canvas.yview)
        self.frameList = Frame(self.canvas)
        self.canvas.create_window(0, 0, anchor=NW, window=self.frameList)
        self.frameList.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        #FRAME SHOWING TAKEN PIECES
        self.numberWhiteTaken = 0
        self.numberBlackTaken = 0
        self.takenPiecesContainer =  Frame(self.sideBar, bg = "black", width=self.sideBarWidth-8, height=102)
        self.takenPiecesContainer.grid(row=1,column=0,sticky=W, padx=4)

        self.takenPiecesFrame = Frame(self.takenPiecesContainer, bg = self.takenPiecesBackground, width=self.sideBarWidth-8, height=100)
        self.takenPiecesFrame.grid(row=0,column=0,sticky=W, padx=1, pady=1)
        self.takenPiecesFrame.grid_propagate(False)

#        self.tekenPiecesHeader = Label(self.takenPiecesFrame, text = "           Taken pieces:", font=14, bg=self.takenPiecesBackground)
#        self.tekenPiecesHeader.grid(row=0,column=0, columnspan = 7, sticky=W, padx=1)
        self.showTakenPieces()



        #INFO ABOUT GAME
        self.infoPage = self.notebook.add('Info        ')

        self.infoFrame = Frame(self.infoPage)
        self.infoFrame.grid(row=0,column=0,sticky=NW)
        self.vscrollbarInfo = Scrollbar(self.infoFrame)
        self.vscrollbarInfo.grid(row=0, column=1, sticky=N+S, pady=4)
        self.canvasInfo = Canvas(self.infoFrame,yscrollcommand=self.vscrollbarInfo.set,height=418 ,width=196)
        self.canvasInfo.grid(row=0, column=0, sticky=N+S+E+W, pady=4)
        self.vscrollbarInfo.config(command=self.canvasInfo.yview)
        self.infoList = Frame(self.canvasInfo)
        self.canvasInfo.create_window(0, 0, anchor=NW, window=self.infoList)
        self.infoList.update_idletasks()
        self.canvasInfo.config(scrollregion=self.canvasInfo.bbox("all"))

        self.noInfoLabel = Label(self.infoList, text = "Load game to see info about it.", font=self.infoLeftFont)
        self.noInfoLabel.grid(row=0,column=0, sticky=W, padx=1)

        #NOTES
        self.infoPage = self.notebook.add('Notes       ')


        self.notebook.setnaturalsize()

    def createBoard(self):
        self.buttons = []
        color =0
        from inc.chessengine import moveNumber

        global lastPosition1
        global lastPosition2
        for i in range(8):
            self.buttons.append([])
            for j in range(8):
                if not color:
                    bgcolor = self.lightColor
                else:
                    bgcolor = self.darkColor
                buttonName = str(i) + "/" + str(j) + "/" + bgcolor
                self.buttons[-1] += [Label(self.buttonsFrame, name=buttonName, bd=1, background = bgcolor)]
                self.buttons[-1][-1].bind("<Button-1>", self.cellClicked)
                self.buttons[-1][-1].grid(column=j, row=i)
                if not color:
                    color = 1
                else:
                    color = 0
            if not color:
                color = 1
            else:
                color = 0

        #Black pieces
        self.buttons[0][-1].config(image = self.imageBlackRock)
        self.buttons[0][0].config(image = self.imageBlackRock)
        self.buttons[0][-2].config(image = self.imageBlackKnight)
        self.buttons[0][1].config(image = self.imageBlackKnight)
        self.buttons[0][-3].config(image = self.imageBlackBishop)
        self.buttons[0][2].config(image = self.imageBlackBishop)
        self.buttons[0][3].config(image = self.imageBlackQueen)
        self.buttons[0][4].config(image = self.imageBlackKing)
        for i in range(8):
            self.buttons[1][i].config(image = self.imageBlackPawn)

        #Empty cells
        for i in range(2,6):
            for j in range(8):
                self.buttons[i][j].config(image = self.imageEmpty)

        #White pieces

        self.buttons[-1][-1].config(image = self.imageWhiteRock)
        self.buttons[-1][0].config(image = self.imageWhiteRock)
        self.buttons[-1][-2].config(image = self.imageWhiteKnight)
        self.buttons[-1][1].config(image = self.imageWhiteKnight)
        self.buttons[-1][-3].config(image = self.imageWhiteBishop)
        self.buttons[-1][2].config(image = self.imageWhiteBishop)
        self.buttons[-1][3].config(image = self.imageWhiteQueen)
        self.buttons[-1][4].config(image = self.imageWhiteKing)
        for i in range(8):
            self.buttons[-2][i].config(image = self.imageWhitePawn)

        if self.selectedShowLastMove.get() == "Yes":
            try:
                if not self.boardFliped:
                    self.buttons[lastPosition1[0]][lastPosition1[1]].config(background = self.lastMoveColor1)
                    self.buttons[lastPosition2[0]][lastPosition2[1]].config(background = self.lastMoveColor2)
                if self.boardFliped:
                    self.buttons[-lastPosition1[0]-1][-lastPosition1[1]-1].config(background = self.lastMoveColor1)
                    self.buttons[-lastPosition2[0]-1][-lastPosition2[1]-1].config(background = self.lastMoveColor2)
            except:
                pass
            if moveNumber == 0:
                if lastPosition1 in [[0,0], [0,2], [0,4], [0,6], [1,1], [1,3], [1,5], [1,7], [2,0], [2,2], [2,4], [2,6], [4,0], [4,2], [4,4], [4,6], [6,0], [6,2], [6,4], [6,6], [3,1], [3,3], [3,5], [3,7], [5,1], [5,3], [5,5], [5,7], [7,1], [7,3], [7,5], [7,7]]:
                    default1 = self.lightColor
                else:
                    default1 = self.darkColor

                if lastPosition2 in [[0,0], [0,2], [0,4], [0,6], [1,1], [1,3], [1,5], [1,7], [2,0], [2,2], [2,4], [2,6], [4,0], [4,2], [4,4], [4,6], [6,0], [6,2], [6,4], [6,6], [3,1], [3,3], [3,5], [3,7], [5,1], [5,3], [5,5], [5,7], [7,1], [7,3], [7,5], [7,7]]:
                    default2 = self.lightColor
                else:
                    default2 = self.darkColor
                try:
                    if not self.boardFliped:
                        self.buttons[lastPosition1[0]][lastPosition1[1]].config(background = default1)
                        self.buttons[lastPosition2[0]][lastPosition2[1]].config(background = default2)
                    if self.boardFliped:
                        self.buttons[-lastPosition1[0]-1][-lastPosition1[1]-1].config(background = default1)
                        self.buttons[-lastPosition2[0]-1][-lastPosition2[1]-1].config(background = default2)

                except:
                    pass
        self.buttonsFrame.pack()


    def cellClicked(self, event ):
        pass

    def showLastPosition(self,firstTime=0):
        global maxNumber, stopOnWhite
        from inc.chessengine import board, moveNumber
        createStartPosition()
        if self.gameLine != 'ERROR':
            clearAll()
            lastPosition = playGame(self.gameLine)
            if type(lastPosition) != type(1):
                self.changeImages(lastPosition)
            else:
                invalidMove(lastPosition)
            from inc.chessengine import moveNumber
            maxNumber = moveNumber
            stopOnWhite = 1
            print maxNumber, moveNumber
            rows = maxNumber
            if firstTime:
                self.noBlackLastMove = 0
                self.buttonHC = self.buttonHC/(2.0*maxNumber)
                #self.vscrollbar = Scrollbar(self.moveListFrame)
                #self.vscrollbar.grid(row=0, column=1, sticky=N+S)
                #self.canvas = Canvas(self.moveListFrame,yscrollcommand=self.vscrollbar.set,height=300,width=150)
                #self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
                self.vscrollbar.config(command=self.canvas.yview)
                self.frameList = Frame(self.canvas)
                self.canvas.create_window(0, 0, anchor=NW, window=self.frameList)
                self.frameList.update_idletasks()
                self.canvas.config(scrollregion=self.canvas.bbox("all"))

                self.buttonsDic = {}

                for i in range(1,rows+1):
                    for j in range(1,4):
                        if j==1:
                            self.label = Label(self.frameList,text=str(i))
                            self.label.grid(row=i,column=j)
                        else:
                            if j==2:
                                posPoint = self.gameLine.find(" "+str(i)+".")+2+len(str(i))
                                posSpace = self.gameLine.find(" ",posPoint)
                                if posSpace == -1:
                                    posSpace = len(self.gameLine)
                                    self.noBlackLastMove = 1
                                self.button = Button(self.frameList, padx=22, text=self.gameLine[posPoint:posSpace], name=str(i)+"0",relief=GROOVE)
                                self.button.bind("<Button-1>",self.changePositionList)
                                self.button.grid(row=i, column=j, sticky='news')

                                self.buttonsDic[(i, j-2)] = self.button

                            elif j==3:
                                posEnd = self.gameLine.find(" "+str(i+1)+".", posSpace)
                                if i==maxNumber:
                                    posEnd = len(self.gameLine)
                                if not self.noBlackLastMove:
                                    self.button = Button(self.frameList, padx=22, text=self.gameLine[posSpace+1:posEnd], name=str(i)+"1",relief=GROOVE)
                                    self.button.grid(row=i, column=j, sticky='news')
                                    self.button.bind("<Button-1>",self.changePositionList)

                                    self.buttonsDic[(i, j-2)] = self.button

                self.canvas.create_window(0, 0, anchor=NW, window=self.frameList)
                self.frameList.update_idletasks()
                self.canvas.config(scrollregion=self.canvas.bbox("all"))

            self.canvas.yview(MOVETO,1.0)
            self.prevButton.config(background=self.canvas["background"])
            self.buttonsDic[(maxNumber,not self.noBlackLastMove)].config(background=self.colorSelected)
            self.prevButton=self.buttonsDic[(maxNumber,not self.noBlackLastMove)]

    def changePositionList(self,event):
        global stopOnWhite
        moveN = int(event.widget.winfo_name()[:len(event.widget.winfo_name())-1])
        color = event.widget.winfo_name()[-1]
        self.prevButton.config(background=self.canvas["background"])
        event.widget.config(background=self.colorSelected)
        self.prevButton=event.widget
        print moveN,color

        createStartPosition()
        if self.gameLine != 'ERROR':
            clearAll()
            if color=="0":
                stopOnWhite=1
            if color=="1":
                stopOnWhite=0
            changes = playGame(self.gameLine,moveN,stopOnWhite)
            if type(changes) != type(1):
                self.changeImages(changes)
            else:
                invalidMove(changes)
            stopOnWhite = not stopOnWhite


    def showStartPosition(self):
        global stopOnWhite
        from inc.chessengine import board, moveNumber
        self.currentPosition = board
        createStartPosition()
        clearAll()
        changes = playGame(self.gameLine , 0, 0)
        stopOnWhite = 1
        self.changeImages(changes)
        self.canvas.yview(MOVETO,0.0)
        self.prevButton.config(background=self.canvas["background"])


    def moveBack(self):
        global stopOnWhite, tempCounter
        from inc.chessengine import board, moveNumber
        if maxNumber-moveNumber>self.middleListPos-2:
#            tempCounter += 1
            length = self.vscrollbar.get()[1]-self.vscrollbar.get()[0]
#            print self.vscrollbar.get()[0]-self.buttonHC, 1.0-length-3*self.buttonHC, self.buttonHC
#            self.canvas.yview(MOVETO,self.vscrollbar.get()[0]-self.buttonHC)
            self.canvas.yview(MOVETO,1.0-length-((maxNumber-moveNumber-self.middleListPos+2)*2-stopOnWhite)*self.buttonHC)
#            print "length:",self.vscrollbar.get()[1]-self.vscrollbar.get()[0], "changed:",tempCounter,"number:",moveNumber,"stop:",stopOnWhite,"var:",((maxNumber-moveNumber-self.middleListPos)*2-stopOnWhite)
#            print self.vscrollbar.get()[1]-self.vscrollbar.get()[0]
#            print self.vscrollbar.get()[0]-self.buttonHC

#            print 1.0-length-self.buttonHC
#            countA = ((maxNumber-moveNumber-self.middleListPos)*2-stopOnWhite)
#            a = 1.0-length- tempCounter*self.buttonHC
#            print self.vscrollbar.get()[0]-a, a
        else:
            self.canvas.yview(MOVETO,1.0)

        if not (stopOnWhite == 1 and moveNumber == 0):
            createStartPosition()
            if stopOnWhite == 0:
                playTo = moveNumber - 1
            else:
                playTo = moveNumber
            if self.gameLine != 'ERROR':
                clearAll()
                if playTo<0:
                    playTo = 0
                print playTo, stopOnWhite
                changes = playGame(self.gameLine, playTo, stopOnWhite)
                if stopOnWhite == 0:
                    stopOnWhite = 1
                else:
                    stopOnWhite = 0

                if type(changes) != type(1):
                    self.changeImages(changes)
                else:
                    invalidMove(changes)
            self.prevButton.config(background=self.canvas["background"])
            if not (playTo == 0 and stopOnWhite==1):
                self.buttonsDic[(playTo,stopOnWhite)].config(background=self.colorSelected)
                self.prevButton=self.buttonsDic[(playTo,stopOnWhite)]

    def moveBack5(self):
        global stopOnWhite

        self.canvas.yview(MOVETO,self.vscrollbar.get()[0]-self.buttonHC*10)

        from inc.chessengine import board, moveNumber
        if  moveNumber >= 5 and not (stopOnWhite == 0 and moveNumber == 5):
            createStartPosition()
            if stopOnWhite == 0:
                playTo = moveNumber - 5
            else:
                playTo = moveNumber - 5
            if self.gameLine != 'ERROR':
                clearAll()
                if playTo<0:
                    playTo = 0
                print playTo, not stopOnWhite
                changes = playGame(self.gameLine, playTo, not stopOnWhite)

                if type(changes) != type(1):
                    self.changeImages(changes)
                else:
                    invalidMove(changes)

            self.prevButton.config(background=self.canvas["background"])
            if not (playTo == 0 and stopOnWhite==1):
                self.buttonsDic[(playTo,stopOnWhite)].config(background=self.colorSelected)
                self.prevButton=self.buttonsDic[(playTo,stopOnWhite)]
        else:
            createStartPosition()
            if self.gameLine != 'ERROR':
                clearAll()
                changes = playGame(self.gameLine, 0, 0)
                stopOnWhite = 1
                if type(changes) != type(1):
                    self.changeImages(changes)
                else:
                    invalidMove(changes)
            self.prevButton.config(background=self.canvas["background"])



    def moveForward(self):
        global maxNumber
        global stopOnWhite

        from inc.chessengine import board, moveNumber
        print moveNumber, moveNumber == self.middleListPos
        if moveNumber >= self.middleListPos:
            print "GOGOGO"
            self.canvas.yview(MOVETO,self.vscrollbar.get()[0]+self.buttonHC)

        if not (moveNumber == maxNumber and stopOnWhite == 1):
            createStartPosition()
            if stopOnWhite == 0:
                playTo = moveNumber
            else:
                if moveNumber == maxNumber:
                    playTo = maxNumber
                else:
                    playTo = moveNumber+ 1
            if self.gameLine != 'ERROR':
                clearAll()
                changes = playGame(self.gameLine, playTo, stopOnWhite)
                if stopOnWhite == 0:
                    stopOnWhite = 1
                else:
                    stopOnWhite = 0
                if type(changes) != type(1):
                    self.changeImages(changes)
                else:
                    invalidMove(changes)
            self.prevButton.config(background=self.canvas["background"])
            self.buttonsDic[(playTo,stopOnWhite)].config(background=self.colorSelected)
            self.prevButton=self.buttonsDic[(playTo,stopOnWhite)]

    def moveForward5(self):
        global maxNumber

        self.canvas.yview(MOVETO,self.vscrollbar.get()[0]+self.buttonHC*10)

        global stopOnWhite
        from inc.chessengine import board, moveNumber
        if moveNumber <= maxNumber - 5:
            createStartPosition()
            if stopOnWhite == 0:
                playTo = moveNumber + 5
            else:
                if moveNumber == maxNumber:
                    playTo = maxNumber
                else:
                    playTo = moveNumber + 5
            if self.gameLine != 'ERROR':
                clearAll()
                changes = playGame(self.gameLine, playTo, not stopOnWhite)
                if type(changes) != type(1):
                    self.changeImages(changes)
                else:
                    invalidMove(changes)
            self.prevButton.config(background=self.canvas["background"])
            self.buttonsDic[(playTo,stopOnWhite)].config(background=self.colorSelected)
            self.prevButton=self.buttonsDic[(playTo,stopOnWhite)]
        else:
            createStartPosition()
            if self.gameLine != 'ERROR':    #CHECK IN POS IF END ON WHITE!!!!!!!!!!!!!!!!!!!!!!!!!!!
                clearAll()                  #MAYBE EXCEPT "0" SMTH OTHER!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                changes = playGame(self.gameLine, maxNumber, 0)
                stopOnWhite = 1
                if type(changes) != type(1):
                    self.changeImages(changes)
                else:
                    invalidMove(changes)
            self.prevButton.config(background=self.canvas["background"])
            self.buttonsDic[(maxNumber,1)].config(background=self.colorSelected)
            self.prevButton=self.buttonsDic[(maxNumber,1)]

    def changeImages(self, board):
        self.currentPosition = board

        for i in range(8):
            for j in range(8):
                self.buttons[i][j].destroy()

        for i in range(len(self.takenPiecesWhiteImages)):
            self.takenPiecesWhiteImages[i].destroy()

        for i in range(len(self.takenPiecesBlackImages)):
            self.takenPiecesBlackImages[i].destroy()

        self.numberWhiteTaken.destroy()
        self.numberBlackTaken.destroy()


        self.createBoard()

        if self.boardFliped  == 1:
            boardTemp = []
            for i in range(8):
                boardTemp.append([])
                for j in range(8):
                    boardTemp[i].append('em')

            for i in range(8):
                for j in range(8):
                     boardTemp[i][j] = board[-i-1][-j-1]

            board = boardTemp



        for i in range(8):
            for j in range(8):
                if board[i][j] == "em":
                    self.buttons[i][j].config(image = self.imageEmpty)
                elif board[i][j] == "bR":
                    self.buttons[i][j].config(image = self.imageBlackRock)
                elif board[i][j] == "wR":
                    self.buttons[i][j].config(image = self.imageWhiteRock)
                elif board[i][j] == "bN":
                    self.buttons[i][j].config(image = self.imageBlackKnight)
                elif board[i][j] == "wN":
                    self.buttons[i][j].config(image = self.imageWhiteKnight)
                elif board[i][j] == "bB":
                    self.buttons[i][j].config(image = self.imageBlackBishop)
                elif board[i][j] == "wB":
                    self.buttons[i][j].config(image = self.imageWhiteBishop)
                elif board[i][j] == "bQ":
                    self.buttons[i][j].config(image = self.imageBlackQueen)
                elif board[i][j] == "wQ":
                    self.buttons[i][j].config(image = self.imageWhiteQueen)
                elif board[i][j] == "bK":
                    self.buttons[i][j].config(image = self.imageBlackKing)
                elif board[i][j] == "wK":
                    self.buttons[i][j].config(image = self.imageWhiteKing)
                elif board[i][j] == "bP":
                    self.buttons[i][j].config(image = self.imageBlackPawn)
                elif board[i][j] == "wP":
                    self.buttons[i][j].config(image = self.imageWhitePawn)

        self.showTakenPieces()

    def changeShowLastMove(self):
        if self.selectedShowLastMove.get() == "Yes":
            try:
                self.buttons[lastPosition1[0]][lastPosition1[1]].config(background = self.lastMoveColor1)
                self.buttons[lastPosition2[0]][lastPosition2[1]].config(background = self.lastMoveColor2)
            except:
                pass
        elif self.selectedShowLastMove.get() == "No":

            if lastPosition1 in [[0,0], [0,2], [0,4], [0,6], [1,1], [1,3], [1,5], [1,7], [2,0], [2,2], [2,4], [2,6],\
            [4,0], [4,2], [4,4], [4,6], [6,0], [6,2], [6,4], [6,6], [3,1], [3,3], [3,5], [3,7], [5,1], [5,3], [5,5], [5,7], [7,1], [7,3], [7,5], [7,7]]:
                default1 = self.lightColor
            else:
                default1 = self.darkColor

            if lastPosition2 in [[0,0], [0,2], [0,4], [0,6], [1,1], [1,3], [1,5], [1,7], [2,0], [2,2], [2,4], [2,6],\
            [4,0], [4,2], [4,4], [4,6], [6,0], [6,2], [6,4], [6,6], [3,1], [3,3], [3,5], [3,7], [5,1], [5,3], [5,5], [5,7], [7,1], [7,3], [7,5], [7,7]]:
                default2 = self.lightColor
            else:
                default2 = self.darkColor
            try:
                self.buttons[lastPosition1[0]][lastPosition1[1]].config(background = default1)
                self.buttons[lastPosition2[0]][lastPosition2[1]].config(background = default2)
            except:
                pass

    def changeShowNextMove(self):
        pass

    def changeShowLegalMoves(self):
        pass

    def changeBoardColor(self):
        if self.selectedBoardColor.get() == "Brown":
            self.lightColor = "#F0D9B5"
            self.darkColor = "#B58863"
        elif self.selectedBoardColor.get() == "Light":
            self.lightColor = "white"
            self.darkColor = "grey"
        elif self.selectedBoardColor.get() == "Green":
            self.lightColor = "#EEEED2"
            self.darkColor = "#769656"
        elif self.selectedBoardColor.get() == "Blue":
            self.lightColor = "#ECECD7"
            self.darkColor = "#4D6D92"
        elif self.selectedBoardColor.get() == "Grey":
            self.lightColor = "#EFEFEF"
            self.darkColor = "#ABABAB"
        elif self.selectedBoardColor.get() == "Red":
            self.lightColor = "#F0D8BF"
            self.darkColor = "#BA5546"
        elif self.selectedBoardColor.get() == "Orange":
            self.lightColor = "#FCE4B2"
            self.darkColor = "#D08B18"
        elif self.selectedBoardColor.get() == "Pink":
            self.lightColor = "#FADDE1"
            self.darkColor = "#D097A1"
        elif self.selectedBoardColor.get() == "Purple":
            self.lightColor = "#EFEFEF"
            self.darkColor = "#8877B7"
        elif self.selectedBoardColor.get() == "Tan":
            self.lightColor = "#EDC9A2"
            self.darkColor = "#D3A36A"
        elif self.selectedBoardColor.get() == "Black & White":
            self.lightColor = "#FFFFFF"
            self.darkColor = "#000000"
        elif self.selectedBoardColor.get() == "Winboard":
            self.lightColor = "#C8C365"
            self.darkColor = "#77A26D"

        color = 0
        for i in range(8):
            for j in range(8):
                if not color:
                    bgcolor = self.lightColor
                else:
                    bgcolor = self.darkColor
                self.buttons[i][j].config(bg=bgcolor)
                if not color:
                    color = 1
                else:
                    color = 0
            if not color:
                color = 1
            else:
                color = 0

    def changeBoardSize(self):
        if self.selectedBoardSize.get() == "Small":
            if self.selectedColorScheme.get() == "Set 1":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set1/small/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set1/small/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set1/small/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set1/small/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set1/small/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set1/small/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set1/small/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set1/small/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set1/small/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set1/small/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set1/small/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set1/small/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set1/small/bp.png")
                except:
                    print "Falied to load files from \\img\\set1\\small folder"
            elif self.selectedColorScheme.get() == "Set 2":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set2/small/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set2/small/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set2/small/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set2/small/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set2/small/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set2/small/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set2/small/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set2/small/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set2/small/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set2/small/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set2/small/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set2/small/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set2/small/bp.png")
                except:
                    print "Falied to load files from \\img\\set2\\small folder"

            self.sideBar["height"] = 310
            self.canvas["height"] = 195
            self.canvasInfo["height"] = 298

        elif self.selectedBoardSize.get() == "Default":
            if self.selectedColorScheme.get() == "Set 1":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set1/default/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set1/default/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set1/default/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set1/default/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set1/default/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set1/default/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set1/default/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set1/default/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set1/default/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set1/default/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set1/default/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set1/default/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set1/default/bp.png")
                except:
                    print "Falied to load files from \\img\\set1\\default folder"
            elif self.selectedColorScheme.get() == "Set 2":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set2/default/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set2/default/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set2/default/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set2/default/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set2/default/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set2/default/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set2/default/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set2/default/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set2/default/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set2/default/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set2/default/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set2/default/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set2/default/bp.png")
                except:
                    print "Falied to load files from \\img\\set2\\default folder"
            self.sideBar["height"] = 430
            self.canvas["height"] = 315
            self.canvasInfo["height"] = 418

        elif self.selectedBoardSize.get() == "Large":
            if self.selectedColorScheme.get() == "Set 1":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set1/large/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set1/large/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set1/large/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set1/large/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set1/large/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set1/large/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set1/large/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set1/large/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set1/large/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set1/large/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set1/large/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set1/large/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set1/large/bp.png")
                except:
                    print "Falied to load files from \\img\\set1\\large folder"
            elif self.selectedColorScheme.get() == "Set 2":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set2/large/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set2/large/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set2/large/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set2/large/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set2/large/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set2/large/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set2/large/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set2/large/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set2/large/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set2/large/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set2/large/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set2/large/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set2/large/bp.png")
                except:
                    print "Falied to load files from \\img\\set2\\large folder"
            self.sideBar["height"] = 550
            self.canvas["height"] = 435
            self.canvasInfo["height"] = 538

        for i in range(8):
            for j in range(8):
                self.buttons[i][j].destroy()

        self.createBoard()

        global stopOnWhite
        from inc.chessengine import board, moveNumber
        playTo = moveNumber
        createStartPosition()
        if self.gameLine != 'ERROR':
            clearAll()
            changes = playGame(self.gameLine, playTo, not stopOnWhite)
            if type(changes) != type(1):
                self.changeImages(changes)
            else:
                invalidMove(changes)

        self.notebook.setnaturalsize()


    def changeColorScheme(self):
        if self.selectedColorScheme.get() == "Set 1":
            if self.selectedBoardSize.get() == "Small":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set1/small/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set1/small/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set1/small/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set1/small/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set1/small/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set1/small/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set1/small/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set1/small/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set1/small/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set1/small/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set1/small/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set1/small/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set1/small/bp.png")
                except:
                    print "Falied to load files from \\img\\set1\\small folder"
            elif self.selectedBoardSize.get() == "Default":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set1/default/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set1/default/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set1/default/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set1/default/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set1/default/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set1/default/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set1/default/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set1/default/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set1/default/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set1/default/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set1/default/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set1/default/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set1/default/bp.png")
                except:
                    print "Falied to load files from \\img\\set1\\default folder"
            elif self.selectedBoardSize.get() == "Large":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set1/large/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set1/large/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set1/large/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set1/large/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set1/large/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set1/large/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set1/large/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set1/large/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set1/large/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set1/large/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set1/large/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set1/large/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set1/large/bp.png")
                except:
                    print "Falied to load files from \\img\\set1\\large folder"

        elif self.selectedColorScheme.get() == "Set 2":
            if self.selectedBoardSize.get() == "Small":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set2/small/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set2/small/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set2/small/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set2/small/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set2/small/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set2/small/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set2/small/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set2/small/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set2/small/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set2/small/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set2/small/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set2/small/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set2/small/bp.png")
                except:
                    print "Falied to load files from \\img\\set2\\small folder"
            elif self.selectedBoardSize.get() == "Default":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set2/default/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set2/default/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set2/default/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set2/default/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set2/default/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set2/default/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set2/default/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set2/default/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set2/default/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set2/default/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set2/default/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set2/default/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set2/default/bp.png")
                except:
                    print "Falied to load files from \\img\\set2\\default folder"
            elif self.selectedBoardSize.get() == "Large":
                try:
                    self.imageEmpty = PhotoImage(file = "img/set2/large/empty.gif")
                    self.imageWhiteRock = PhotoImage(file = "img/set2/large/wr.png")
                    self.imageBlackRock = PhotoImage(file = "img/set2/large/br.png")
                    self.imageWhiteBishop = PhotoImage(file = "img/set2/large/wb.png")
                    self.imageBlackBishop = PhotoImage(file = "img/set2/large/bb.png")
                    self.imageWhiteKnight = PhotoImage(file = "img/set2/large/wn.png")
                    self.imageBlackKnight = PhotoImage(file = "img/set2/large/bn.png")
                    self.imageWhiteQueen = PhotoImage(file = "img/set2/large/wq.png")
                    self.imageBlackQueen = PhotoImage(file = "img/set2/large/bq.png")
                    self.imageWhiteKing = PhotoImage(file = "img/set2/large/wk.png")
                    self.imageBlackKing = PhotoImage(file = "img/set2/large/bk.png")
                    self.imageWhitePawn = PhotoImage(file = "img/set2/large/wp.png")
                    self.imageBlackPawn = PhotoImage(file = "img/set2/large/bp.png")
                except:
                    print "Falied to load files from \\img\\set2\\large folder"

        for i in range(8):
            for j in range(8):
                self.buttons[i][j].destroy()

        self.createBoard()

        global stopOnWhite
        from inc.chessengine import board, moveNumber
        playTo = moveNumber
        createStartPosition()
        if self.gameLine != 'ERROR':
            clearAll()
            changes = playGame(self.gameLine, playTo, not stopOnWhite)
            if type(changes) != type(1):
                self.changeImages(changes)
            else:
                invalidMove(changes)

    def showTakenPieces(self):
        from inc.chessengine import takenWhite, takenBlack

        self.takenPiecesWhiteImages = []
        self.takenPiecesBlackImages = []

        wP = 0
        wB = 0
        wN = 0
        wQ = 0
        bP = 0
        bN = 0
        wR = 0
        bR = 0
        bB = 0
        bQ = 0
        numberWhiteTaken = 0
        numberBlackTaken = 0

        #SORTING LISTS TO Q-R-B-N-P

        for i in takenWhite:
            if i == "P":
                wP += 1
                numberWhiteTaken += 1
            elif i == "R":
                wR += 1
                numberWhiteTaken += 5
            elif i == "N":
                wN += 1
                numberWhiteTaken += 3
            elif i == "B":
                wB += 1
                numberWhiteTaken += 3
            elif i == "Q":
                wQ += 1
                numberWhiteTaken += 9
        takenWhite = []
        for i in range(wQ):
            takenWhite += "Q"
        for i in range(wR):
            takenWhite += "R"
        for i in range(wB):
            takenWhite += "B"
        for i in range(wN):
            takenWhite += "N"
        for i in range(wP):
            takenWhite += "P"

        for i in takenBlack:
            if i == "P":
                bP += 1
                numberBlackTaken += 1
            elif i == "R":
                bR += 1
                numberBlackTaken += 5
            elif i == "N":
                bN += 1
                numberBlackTaken += 3
            elif i == "B":
                bB += 1
                numberBlackTaken += 3
            elif i == "Q":
                bQ += 1
                numberBlackTaken += 9
        takenBlack = []
        for i in range(bQ):
            takenBlack += "Q"
        for i in range(bR):
            takenBlack += "R"
        for i in range(bB):
            takenBlack += "B"
        for i in range(bN):
            takenBlack += "N"
        for i in range(bP):
            takenBlack += "P"

        #END OF SORTING LISTS
        for i in takenWhite:
            if i == "P":
                self.takenPiecesWhiteImages.append(Label(self.takenPiecesFrame, image = self.imageTakenBlackPawn, bg=self.takenPiecesBackground))
            elif i == "R":
                self.takenPiecesWhiteImages.append(Label(self.takenPiecesFrame, image = self.imageTakenBlackRock, bg=self.takenPiecesBackground))
            elif i == "N":
                self.takenPiecesWhiteImages.append(Label(self.takenPiecesFrame, image = self.imageTakenBlackKnight, bg=self.takenPiecesBackground))
            elif i == "B":
                self.takenPiecesWhiteImages.append(Label(self.takenPiecesFrame, image = self.imageTakenBlackBishop, bg=self.takenPiecesBackground))
            elif i == "Q":
                self.takenPiecesWhiteImages.append(Label(self.takenPiecesFrame, image = self.imageTakenBlackQueen,bg=self.takenPiecesBackground))

        for i in takenBlack:
            if i == "P":
                self.takenPiecesBlackImages.append(Label(self.takenPiecesFrame, image = self.imageTakenWhitePawn, bg=self.takenPiecesBackground))
            elif i == "R":
                self.takenPiecesBlackImages.append(Label(self.takenPiecesFrame, image = self.imageTakenWhiteRock, bg=self.takenPiecesBackground))
            elif i == "N":
                self.takenPiecesBlackImages.append(Label(self.takenPiecesFrame, image = self.imageTakenWhiteKnight, bg=self.takenPiecesBackground))
            elif i == "B":
                self.takenPiecesBlackImages.append(Label(self.takenPiecesFrame, image = self.imageTakenWhiteBishop, bg=self.takenPiecesBackground))
            elif i == "Q":
                self.takenPiecesBlackImages.append(Label(self.takenPiecesFrame, image = self.imageTakenWhiteQueen, bg=self.takenPiecesBackground))

        self.numberBlackTaken = Label(self.takenPiecesFrame, text = numberBlackTaken, font= self.font1, bg=self.takenPiecesBackground)
        self.numberBlackTaken.grid(column = 0, row = 0, sticky=W)
        self.numberBlackTakenBlank = Label(self.takenPiecesFrame, text = "", font= self.font1, bg=self.takenPiecesBackground)
        self.numberBlackTakenBlank.grid(column = 0, row = 1, sticky=W)

        lineCounter = 0
        colunmCounter  = 0
        for i in range(len(self.takenPiecesBlackImages)):
            lineCounter +=1
            if lineCounter <=8:
                self.takenPiecesBlackImages[i].grid(column = i+1, row = 0)
            else:
                colunmCounter += 1
                self.takenPiecesBlackImages[i].grid(column = colunmCounter, row = 1)


        self.numberWhiteTaken = Label(self.takenPiecesFrame, text = numberWhiteTaken, font= self.font1, bg=self.takenPiecesBackground)
        self.numberWhiteTaken.grid(column = 0, row = 2, sticky=W)
        self.numberWhiteTakenBlank = Label(self.takenPiecesFrame, text = "", font= self.font1, bg=self.takenPiecesBackground)
        self.numberWhiteTakenBlank.grid(column = 0, row = 3, sticky=W)

        lineCounter = 0
        colunmCounter = 0
        for i in range(len(self.takenPiecesWhiteImages)):
            lineCounter +=1
            if lineCounter <=8:
                self.takenPiecesWhiteImages[i].grid(column = i+1, row = 2)
            else:
                colunmCounter +=1
                self.takenPiecesWhiteImages[i].grid(column = colunmCounter, row = 3)

    def showInfoAboutGame(self):
        self.noInfoLabel.destroy()
        self.infoLabelsData = []
        self.infoLabels = []
        self.gameInfoKeys1 = self.gameInfo.keys()
        rowCounter = 0
        for key in self.gameInfoKeys:
            if key in self.gameInfoKeys1:
                    self.infoLabels += [Label(self.infoList, text = key, font=self.infoLeftFont, wraplength=70)]
                    self.infoLabels[-1].grid(row=rowCounter,column=0, sticky=W, padx=1)
                    self.infoLabelsData += [Label(self.infoList, text = self.gameInfo[key], font = self.infoRightFont, wraplength=152)]
                    self.infoLabelsData[-1].grid(row=rowCounter,column=1, sticky=W, padx=1)
                    rowCounter += 1


        for i in self.gameInfoKeys1:
            if i not in self.gameInfoKeys:
                self.infoLabelsData += [Label(self.infoList, text = self.gameInfo[i], font = self.infoRightFont, wraplength=152)]
                self.infoLabels += [Label(self.infoList, text = i, font=self.infoLeftFont)]
                self.infoLabels[-1].grid(row=rowCounter,column=0, sticky=W, padx=1)
                self.infoLabelsData[-1].grid(row=rowCounter,column=1, sticky=W, padx=1)
                rowCounter +=1

        self.infoList.update_idletasks()
        self.canvasInfo.config(scrollregion=self.canvasInfo.bbox("all"))
        #self.canvasInfo.yview(MOVETO,1.0)

    def flipBoard(self):
        self.boardFliped  = not self.boardFliped
        if self.gameLine != 'ERROR':
            self.changeImages(self.currentPosition)

    def showAbout(self):
        """Help-About"""
        showinfo("About", "Made by Hollgam and Vinchkovsky \nVersion: %s\nPython 2.6.1\nAdditional modules: Tkinter, tkMessageBox, PMW, PIL" % __version__)

    def loadGame(self):
        # window for choosing file to laod
        #fileToLoad = askopenfilename(title='Choose a file to load', filetypes=[('PGN files','*.pgn')])

        fileToLoad  = "1.pgn"
        self.gameLine = readFileLine(fileToLoad)
        self.gameInfo = readInfoFromFile(fileToLoad)
        self.makeButtonsActive()
        self.showLastPosition(1)
        self.showInfoAboutGame()

    def makeButtonsActive(self):
        self.KeyStart.config(state = ACTIVE)
        self.KeyBack5.config(state = ACTIVE)
        self.KeyBack.config(state = ACTIVE)
        self.KeyForward.config(state = ACTIVE)
        self.KeyForward5.config(state = ACTIVE)
        self.KeyEnd.config(state = ACTIVE)

    def exitGame(self, event=None):
        """Game-Exit"""
        self.destroy()
        sys.exit(1)

def invalidMove(type=0):
    """
    shows different errors in chess logic of moves
    """
    if not type:
        message = "ERROR"
    elif type==13:
        message = "OTHER PIECES ON THE WAY"
    elif type==2:
        message = "YOUR PIECE ON THE DESTINATION POINT"
    elif type==3:
        message = "x WAS NOT MENTIONED"
    elif type==4:
        message = "TRYING TO TAKE YOUR OWN PIECE"
    elif type==5:
        message = "TRYING TO TAKE AN EMPTY CELL"
    elif type==6:
        message = "MORE THAN ONE PIECE CAN MAKE A MOVE"
    elif type==7:
        message = "NO PIECE CAN MAKE A MOVE"
    elif type==8:
        message = "NO PIECE WITH THIS ADDITIONAL COORDINATES CAN MOVE"
    elif type==9:
        message = "CAN NOT MAKE A CASTLE"
    elif type==10:
        message = "CASTLE HAS ALREADY BEEN DONE"
    elif type==11:
        message = "CHECK FOR YOU CANT BE A RESULT OF YOUR MOVE"
    elif type==12:
        message = "BAD CHARS IN THE MOVE"
    elif type==14:
        message = 'WRONG NUMBER OF MOVE ENTERED'
    elif type==15:
        message = 'INCORRECT ORDER OF MOVE NUMBERS'
    elif type==16:
        message = 'INCORRECT QUANTITYOF MOVES'
    elif type==17:
        message = 'NO CHECK'
    elif type==18:
        message = 'CANNOT MOVE THERE BECAUSE OF THE CHECK'
    elif type==19:
        message = 'NO CHECKMATE: ENENY KING IS NOT UNDER ATTACK'
    elif type==20:
        message = 'NO CHECKMATE: ENENY CAN PROTECT HIS/HER KING'
    elif type==21:
        message = 'NO CHECKMATE: ENEMY KING CAN ESCAPE'
    elif type==22:
        message = 'KING IS UNDER ATTACK AFTER THIS MOVE'

    print message
    showinfo("Error", message)
    #sys.exit(1) #EXITS A PROGRAM HANDY FOR CHECKS
    return 1

def main():
    createStartPosition()
#    fileToLoad = "1.pgn"

    PGN_GUI().mainloop()

if __name__ == "__main__":
    main()