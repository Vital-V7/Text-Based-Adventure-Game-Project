import os
os.system("clear")
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds):
    time.sleep(seconds)

def intro():
    clear_screen()
    print("""
        **************************
               GRAVE   YARD
                 ENTRANCE
        **************************       
        
        
        
        After being made fun of about being a scaredy cat
        you decided to go to the local graveyard to prove to 
        yourself that you are not a coward.\n
        """)
    points_OI = input("Do you go to the 'Shed' the 'catacombs' or 'leave' the graveyard?\n").lower()
    
    if points_OI == 'shed':
        
        SD()
    elif points_OI == 'catacombs':
        
        catacombs()
    elif points_OI == 'leave':
        
        lose("""
            You think ot yourself that this was too much for
            you and decide to leave the graveyard and go home.
            \n
            Coward\n
            """)
    else:
        print("⚠️Words in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly.⚠️\nTry again.")
        pause(4.0)
        intro()
 
 #SD means shed   
def SD():
    clear_screen()
    print("""
        ***************
             SHED
        ***************
        
        
        You enter the old shed and every other step you make creaks the floor board underneath you.
        You see another door at the end of the shed and a closet to your left.\n
        """)
    In_shed = input("Do you go to the 'door' or see what's in the 'closet'?\n").lower()
    
    if In_shed == 'door':
        
        behind_SD()
    elif In_shed == 'closet':
        
        lose("""
            As you walk to the closet you feel a strong pain in your left leg, and you
            fall. Looking at your leg you see a beartrap latched onto your ankle, screaming you
            attract the attention of a groundskeeper.
            After you got caught you were taken to a hospital\n
            You may not be a coward but you are a idiot.\n
            """)
        
    else:
        print("⚠️Words in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly.⚠️\nTry again.\n")
        pause(4.0)
        SD()

def behind_SD():
    clear_screen()
    print("""
          *******************
              BEHIND THE
                 SHED
          *******************
        After going behind the shed you hear walking inside the
        shed and start looking for places to hide\n
        """)
    b_SD = input("Do you go behind the 'boxes', run over and jump the 'fence' of the graveyard, or run to the 'catacombs'\n ").lower()
    if b_SD == 'boxes':
        
        lose("""
            As you run to hide behind the boxes you hear
            the walking getting louder, you see a ray of light coming around the box,
            then you see a man, a groundskeeper, he drags you to the entrance
            of the graveyard and throws you out, he yells telling you to never come back.\n
            """)
    elif b_SD == 'fence':
        
        win("""
            You sprint to the fence, and after climbing it you hear yelling behind you, still
            running away from the graveyard you don't look back.
            Thinking to yourself that that was scary enough for you for the day and go home.\n
            """)
    elif b_SD == 'catacombs':
        
        print("""
            You start to run to the catacombs, almost tripping while making you way
            there.\n
            """)
        pause(4.0)
        catacombs()
    else:
        print("⚠️Words in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly.⚠️\nTry again.\n")
        behind_SD()

def catacombs():
    clear_screen()
    print("""
        *****************
            CATACOMBS
        *****************
        After walking down the stairs you hear a clank sound behind you,
        checking to see what it was you try to open the gate leading to the
        catacombs but it was locked. Going down the stairs of the catacombs you come across two halls,
        one infront of you with a few lanterns lighting up the hall or a dark
        hall to your left that's too hard to see the end of it.\n
        """)
    Inside_CC = input("Walk down the 'bright hallway' or the 'dark hallway'?\n").lower()
    if Inside_CC == 'bright hallway':
        
        br_CC()
    elif Inside_CC == 'dark hallway':
        
        lose("""
            After walking down the dark hallway it gets to a point
            where you can't see anything and the light from the previous hall
            is long gone. Lost you try to walk back to where you came but
            it was to hard to find your sense of direction and you walk into a wall.
            On the ground you give up and accept your fate, lost to the catacombs.\n
            """)

    else:
        print("⚠️Words in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly.⚠️\nTry again.\n")
        pause(4.0)
        catacombs()

#CC means catacombs
def br_CC():
    clear_screen()
    print("""
        ******************
            BRIGHT HALL
               WAY
        ******************
        walking down the hallway you see skeletons and bones on the walls and behind some gates.
        When you made it to the end of the hallway you see another crossroad with to paths,
        a stair case leading up, and a stair case going down that was too
        dark to see the bottom of it.\n
        """)
    sp_stair_case = input("Do you go down the stairs leading 'up' or the stairs going 'down'?\n").lower()
    if sp_stair_case == 'up':
        
        win("""
            After walking up the stairs for quite some time you see
            light coming from the top. Picking up pace you finally made it to another
            entrance to the catacombs, opening the gates to leave
            you decided that was more then enough for you and start walking home.\n
            """)
    elif sp_stair_case == 'down':
        
        lose("""
            After making it to the end of the stairs you start walking
            forward still in darkness, walking down a path to your
            right, then another to your left, you start to feel lost.
            After spend what feels like days stuck in darkness your body begins to
            stop working, and you give up, taken by the catacombs.\n
            """)
    else:
         print("⚠️Words in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly.⚠️\nTry again.\n")
         pause(4.1)
         br_CC()

def lose(reason):
    print(reason)
    print("\nYou have failed.")
    Play_Again()

def Play_Again():
    play_again = input("Do you want play again?\n 'yes' or 'no'\n").lower()
    if play_again == 'yes':
         intro()
    elif play_again == 'no':
        print("Thanks for playing my game!")
    else:
        print("⚠️Words in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly.⚠️\nTry again.\n")
        pause(4.0)
        Play_Again()

def win(reason):
    print("You have won!\n")
    Play_Again()

def keyA():
    key_place = input("""
          'intro'
          'SD'
          'behind_SD'
          'catacombs'
          'br_CC'
          """).lower()
    if key_place == 'intro':
        intro()
    elif key_place == 'sd':
        SD()
    elif key_place == 'behind_sd':
        behind_SD()
    elif key_place == 'catacombs':
        catacombs()
    elif key_place == 'br_cc':
        br_CC()
    else:
        keyA()
began = input("""
                     welcome to my...
              _______________________________
                   ADVENTURE    GAME
                         PROJECT
              _______________________________           
              
              Type 'start' to began.\nWords in 'Single qoutes' is what you type into the terminal and make sure you type them in exactly. """).lower()
if began == 'start':
    
    intro()

elif began == 'key':
    keyA()

else:
    print("Just gonna start it anyways")
    intro()
