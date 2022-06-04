print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
game_on = True
print("""Welcome to Treasure Island!
You are now going for a treasure hunt. 
Your mission is to find your way to the treasure. 
Choose your options wisely or you will end up DEAD.""") 
while game_on:
  left_or_right =  input("You are now on the island, where would you like to go 'LEFT' or 'RIGHT'? \n").lower()
  if left_or_right == "left":
    print("""    Woop, Woop I can see a lake from here After walking for 10 min, you reached the lake \n""")
    print("""what would you like to do? 'SWIM' or 'WAIT' for a boat?
  If you choose to SWIM you will reach the other side faster because the boat will depart after 2 hours""")
  else:
    print('''You faced the Dead Rabbits mafia, 
you were so brave defending yourself but, 
unfortunately, you could not take all the heat, 
RIP, GAME OVER
             o_-* BANG!  0
             |          /|
             |\       '/ 
  \n''')
    break
  lake =  input("").lower()
  if lake == "wait":
    print("""    This boat is incredible,
          I can see a castle, I must be close to the treasure.
         _~
      _~ )_)_~
      )_))_))_)
      _!__!__!_
      \______t/
    ~~~~~~~~~~~~~\n""")
  else:
    print("""    OMG nooooooooo, 
          
                      .-._   _ _ _ _ _ _ _ _
           .-''-.__.-'00  '-' ' ' ' ' ' ' ' '-.
           '.___ '    .   .--_'-' '-' '-' _'-' '._
            V: V 'vv-'   '_   '.       .'  _..' '.'.
              '=.____.=_.--'   :_.__.__:_   '.   : :
                      (((____.-'        '-.  /   : :
                                        (((-'\ .' /
                                      _____..'  .'
                                     '-._____.-' 
          Rest In Peace, GAME OVER\n""")
    break

  print("The castle have 3 door which one would you like to choose? 'RED', 'BLUE', or 'YELLOW'\n")
  print('''                                 |--__
                                 |
                                 X
                        |-___   / \       |--__
                        |      =====      |
                        X      | .:|      X
                       / \     | O |     / \
                      =====   |:  . |   =====
                      |.: |__| .   : |__| :.|
                      |  :|. :  ...   : |.  |
              __   __W| .    .  ||| .      :|W__  --
            -- __  W  WWWW______"""______WWWW   W -----  --
        -  -     ___  ---    ____     ____----       --__  -
            --__    --    --__     -___        __-   _''')
  
  
  door = input("").lower()
  if door == "red":
    print('''     (  .      )
             )           (              )
                   .  '   .   '  .  '  .
          (    , )       (.   )  (   ',    )
           .' ) ( . )    ,  ( ,     )   ( .
        ). , ( .   (  ) ( , ')  .' (  ,    )
       (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^''')
    print(""" AHHHHHHHHHHHHHHHHHHHHHH 
  You were burned by fire 
  REST IN PEACE, GAME OVER""")
    break
  if door == "blue":
    print('''
                     (    )
                    ((((()))
                    |o\ /o)|
                    ( (  _')
                     (._.  /\__
                    ,\___,/ '  ')
      '.,_,,       (  .- .   .    )
       \   \\     ( '        )(    )
        \   \\    \.  _.__ ____( .  |
         \  /\\   .(   .'  /\  '.  )
          \(  \\.-' ( /    \/    \)
           '  ()) _'.-|/\/\/\/\/\|
               '\\ .( |\/\/\/\/\/|
                 '((  \    /\    /
                 ((((  '.__\/__.')
                  ((,) /   ((()   )
                   "..-,  (()("   /
                    _//.   ((() ."
            _____ //,/" ___ ((( ', ___
                             ((  )
                              / /
                            _/,/'
                          /,/,"''')
    print(" The beast ate you, RIP GAME OVER")
    break
  if door == "yellow":
    print('''Yaaaaaaaay I HAVE FOUDN IT, I AM RICH''')
    print("""__________________
      .-'  \ _.-''-._ /  '-.
    .-/\   .'.      .'.   /\-.
   _'/  \.'   '.  .'   './  \'_
  :======:======::======:======:  
   '. '.  \     ''     /  .' .'
     '. .  \   :  :   /  . .'
       '.'  \  '  '  /  '.'
         ':  \:    :/  :'
           '. \    / .'
             '.\  /.'     
               '\/'""")
    break
  else:
    print("WRONG CHOICE THE GUARDS KICKED YOU OUT OF THE CASTLE AND YOU CAN RE-ENTER AGAIN, GAME OVER!")
    break
  