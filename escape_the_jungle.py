import time
import sys
from random import randint
import webbrowser
import random

class style:
    bright = '\033[1m'
    underline = '\033[04m'
class colours:
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
        white = '\033[37m'
 
class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

def typewriter_sliced(text_list, delay):
    for row in text_list:
        for char in row:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

# random item
def random_item():
    global item_list
    global items_choice
    item_list = ["book", "key", "key"]
    items_choice = random.choice(item_list)

player_item = False

# character selection
player_character = ""  
a_an = ""  
player_name = ""
# Lives
player_lives = 3


###############################################################

def startgame():  
    
    title_text =[bg.black, fg.green, style.bright,"""
                                                     _________          _______ 
                                                     \__   __/|\     /|(  ____ \                 
                                                        ) (   | )   ( || (    \/                 
                                                        | |   | (___) || (__                     
                                                        | |   |  ___  ||  __)                    
                                                        | |   | (   ) || (                       
                                                        | |   | )   ( || (____/\                 
                                                        )_(   |/     \|(_______/                 
                                                                                            
                                        _________          _        _______  _        _______ 
                                        \__    _/|\     /|( (    /|(  ____ \( \      (  ____ }
                                           )  (  | )   ( ||  \  ( || (    \/| (      | (    \/
                                           |  |  | |   | ||   \ | || |      | |      | (__    
                                           |  |  | |   | || (\ \) || | ____ | |      |  __)   
                                           |  |  | |   | || | \   || | \_  )| |      | (      
                                        |\_)  )  | (___) || )  \  || (___) || (____/\| (____/|
                                        (____/   (_______)|/    )_)(_______)(_______/(_______/

                Created by: Jordan Webster, Saira Shaikh, Malak Dalia Chihneh, Robert Wantling, Zvi Schvarcz and Andrew Banjo.
                                                      
    """]
    typewriter_sliced(title_text, 0.0020)
    start_q = ["Would you like to survive the jungle? (yes/no): "]
    typewriter_sliced(start_q, 0.020)
    user_input = input("")
    if user_input.lower() == 'yes' or user_input.lower() == 'y':
        name_selection()
    elif user_input.lower() == 'no' or user_input.lower() == 'n':
        quiz_game()
    else:
        print('Please type yes or no')
        startgame()

######################################################################

def name_selection():
    global player_name
    print(fg.yellow, "\nLoading...")
    time.sleep(2.1)
    selection_text = [fg.lightgrey, "Please enter your name:"]
    typewriter_sliced(selection_text, 0.020)
    name = (input(""))
    player_name = name
    character_selection()


#######################################################################

def character_selection():
    global player_character
    global a_an
    intro_text = [bg.black, fg.lightgrey,"You've chosen to enter the jungle and now you have a choice to select one of two characters,\neach of whom has strengths and weaknesses that will assist you on your journey.\nFirst is the explorer, someone who seeks to discover the world with their strength and courage.\nSecond is the researcher, someone who takes more of an intellect approach to problems,\nrelying on wisdom and logic to assist her through life."]
    typewriter_sliced(intro_text, 0.020)
    choose_text = [fg.lightgrey, "Please choose a character, 1: explorer or 2: researcher"]
    typewriter_sliced(choose_text, 0.020)
    user_choice = str(input(""))
    if user_choice == "1":
        explorer_opt = [fg.lightgrey,"You have chosen the explorer!\nAn adenturous choice, you'll be equipped with ungodly strength and agility."]
        player_character = "explorer"
        explorer_fig = [bg.black,"""
                                         _____ _            _____           _                     
                                        |_   _| |          |  ___|         | |                    
                                          | | | |__   ___  | |____  ___ __ | | ___  _ __ ___ _ __ 
                                          | | | '_ \ / _ \ |  __\ \/ / '_ \| |/ _ \| '__/ _ \ '__|
                                          | | | | | |  __/ | |___>  <| |_) | | (_) | | |  __/ |   
                                          \_/ |_| |_|\___| \____/_/\_\ .__/|_|\___/|_|  \___|_|   
                                                                     | |                          
                                                                     |_|  

                                                              .-*""-*.  
                                                             /        \                        
                                                            :   .--. .-:   
                                                            |  /  _."._|   
                                                            |_:  'o  /o:   
                                                            :P       \ |                       
                                                            `-| `.  _' ;                       
                                                              |`.  `- /                        
                                                              ; |`-._/ 
                                                            _/  `.  :                          
                                                        .-' `-.     `+._._                    
                                                       .'       ``-  '  `-.`.                  
                                                      /              \     `.\                 
                                                      :                \      \:                
                                                      :     .-'         .L      ;            ._  
                                                      \    .'  \      /`)  `.   |\         /`\ \ 
                                                      |         :.   : '     ;  ; \       : :'  ;
                                                      |    :    | `--J      / ._/   ;    .-' /'-';
                                                      :    \    :_.-'     .'    :`. L_.-'    _.-' 
                                                      \      -.-'   /    / |`.  |  /  _.'  .'     
                                                       ;              .'  :  \ :        .'       
                                                       |        .'  .'   /    / \    .-'         
                                                       :      .'.-'`-- : -' :    `.-'            
                                                        \ _.-'       |    |                   
                                                         "  | \           |                   
                                                            ;  ;     c   :|                   
                """]
        typewriter_sliced(explorer_opt, 0.020)
        typewriter_sliced(explorer_fig, 0.0010)
        a_an = "an"
        displayintro()
    elif user_choice == "2":
        researcher_opt = [fg.lightgrey,"You have chosen the researcher! \nA strategic choice, you'll be equipped with intellect and a detailed knowledge of nature."]
        player_character = "researcher"
        researcher_fig = [bg.black,"""
                                   _____ _           ______                              _               
                                  |_   _| |          | ___ \                            | |              
                                    | | | |__   ___  | |_/ /___  ___  ___  __ _ _ __ ___| |__   ___ _ __ 
                                    | | | '_ \ / _ \ |    // _ \/ __|/ _ \/ _` | '__/ __| '_ \ / _ \ '__|
                                    | | | | | |  __/ | |\ \  __/\__ \  __/ (_| | | | (__| | | |  __/ |   
                                    \_/ |_| |_|\___| \_| \_\___||___/\___|\__,_|_|  \___|_| |_|\___|_|   

                                                                w*W*W*W*w
                                                                 (".".")
                                                                  //`\)
                                                                 (/o o\)
                                                                 (\_-_/) 
                                                                .-~'='~-.
                                                               |`~`"Y"`~`|
                                                              ( /(_ * _)\ )
                                                             ( /  )   (  \ )
                                                             \ \_/)\_/(\_/ / 
                                                              \/_) '*' (_\/
                                                                |       |
                                                                |       |
                                                                |   |   |
                                                                |   |   |
                                                                |   |   |
                                                                |   |   |
                                                                |   |   |
                                                                w*W*W*W*w
        """]
        typewriter_sliced(researcher_opt, 0.020)
        typewriter_sliced(researcher_fig, 0.0010)
        a_an = "a"
        displayintro()
    else:
        print("Please choose 1 or 2")
        character_selection()
    
def displayintro():
    global a_an
    global player_character
    global player_name
    intro_text = [fg.lightgrey,f"                                                         WELCOME TO THE JUNGLE! \nYou are {player_name}, {a_an} {player_character} who has crash landed on a remote island. You boarded the plane with your team,\nbut due to the plane crashing you are the only remaining survivor. You are in the middle of the jungle, with multiple choices to be made.\nWill you be able to make the right ones?\n\nYou start with 3 lifes and must navigate through the dangerous and unfamiliar terrain, avoid wild animals and find your way back to civilization.\nChoose wisely and you may find a path to surival.\n'Arnold Schwarzenegger voice', \n'runnnn! get to civilization, do it nowwwww!"]
    term_fig = ["""
                                                              ______
                                                            <((((((\.)
                                                            /      . })
                                                            ;--..--._|}
                                          (\                '--/\--'  )
                                          \.\               | '-'  :'|
                                           \.\              . -==- .-|
                                            \.\              \.__.'   \--._
                                            [  \         __.--|       //  _/'--.
                                            \   \      .'-._ ('-----'/ __/      )
                                             \   \    /   __>|      | '--.      |
                                              \ . \   |   \   |     /    /      /
                                               \ ' \  /     \  |     |  _/     /
                                                \   \        \ |     | /      /
                                                 \   \       \        /      /
            """] 
    typewriter_sliced(intro_text, 0.020)
    typewriter_sliced(term_fig, 0.0020)
    crossroadsection()
    
###############################################################

def crossroadsection(): 
    crossroad_print = ["\033[92mYou've come to a crossroad and must decide what direction you would like to follow on your compass. Where would you like to go? \033[00m"] 
    userInput = ""  
    crossroad_print = [fg.lightgrey,"Your options are north, east, south or west:"] 
    typewriter_sliced(crossroad_print, 0.020)
    userInput = input("") 
    if userInput == "north":
        crossroad_print = ['\033[40m'"\nYou have chosen the North direction. You have been trekking through the jungle for some time now and start to hear some rustling ahead.\nAn outline of a ferocious beast starts to appear, that is less than 10 feet away with a menacing face.\n"'\033[40m'] 
        typewriter_sliced(crossroad_print, 0.020)
        north_option() 
    elif userInput == "east": # run function below 
        crossroad_print = ["\nYou have chosen to take the eastern path, you have been walking for a few hours and come to your first obstacle.\nThe first thing that strikes you is the deafening roar of rushing water."]
        typewriter_sliced(crossroad_print, 0.020)
        east_option() #  cross river function 
    elif userInput == "south": 
        crossroad_print = ["\nYou have chosen to head in the south direction of the jungle. As you walk deeper into the jungle, the dense vegetation closes in around you,\nforming a thickcanopy overhead. As darkness envelops the jungle, sunslight gradually struggles to pierce through and your surroundings become increasingly indistinct,\ndarkness encroaches..."]
        typewriter_sliced(crossroad_print, 0.020)
        south_option() # die option light match or be impaled 
    elif userInput == "west": 
        crossroad_print = ["\nYou have chosen to head west, which may be a thoughtful route, as it often leads you towards the setting sun,\na decision you may have to think twice about later."]
        typewriter_sliced(crossroad_print, 0.020)
        time.sleep(2)
        west_option() # clearing 
    else: 
        crossroad_print = ['\033[32m'"Please enter a valid option for the adventure game."'\033[32m']
        typewriter_sliced(crossroad_print, 0.020)
        crossroadsection()
        
        
###############################################################

# NORTH OPTION
def north_option():
    global player_character
    global player_lives
    beast_text = [fg.white,"You now face three options:\n1) You can either slay the beast with your switchblade\n2) Try and evade the beast with stealth tactics\n3) Embrace your inner tarzan and opt to climb the mammoth tree beside you"]
    beast_img = [fg.yellow,"""
                                    :~-._                                                 _.-~:
                                    : :.~^o._        ________---------________        _.o^~.:.:
                                     : ::.`?88booo~~~.::::::::...::::::::::::..~~oood88P'.::.:
                                     :  ::: `?88P .:::....         ........:::::. ?88P' :::. :
                                      :  :::. `? .::.            . ...........:::. P' .:::. :
                                       :  :::   ... ..  ...       .. .::::......::.   :::. :
                                       `  :' .... ..  .:::::.     . ..:::::::....:::.  `: .'
                                        :..    ____:::::::::.  . . ....:::::::::____  ... :
                                       :... `:~    ^~-:::::..  .........:::::-~^    ~::.::::
                                       `.::. `\   (8)  b:::..::.:.:::::::d/  (8)   /'.::::'
                                        ::::.  ~-._v    |b.::::::::::::::d|    v_.-~..:::::
                                        `.:::::... ~~^?888b..:::::::::::d888P^~...::::::::'
                                        `.::::::::::....~~~ .:::::::::~~~:::::::::::::::'
                                          `..:::::::::::   .   ....::::    ::::::::::::,'
                                            `. .:::::::    .      .::::.    ::::::::'.'
                                              `._ .:::    .        :::::.    :::::_.'
                                              `-. :    .        :::::      :,-'
                                                    :.   :___     .:::___   .::
                                          ..--~~~~--:+::. ~~^?b..:::dP^~~.::++:--~~~~--..
                                            ___....--`+:::.    `~8~'    .:::+'--....___
                                          ~~   __..---`_=:: ___gd8bg___ :==_'---..__   ~~
                                           -~~~  _.--~~`-.~~~~~~~~~~~~~~~,-' ~~--._ ~~~-
                                              -~~            ~~~~~~~~~   _  ~~_  ~~-
    """]
    typewriter_sliced(beast_text, 0.020)
    typewriter_sliced(beast_img, 0.0010)
    q_text = [fg.white,"Please choose whether you want to slay the beast, evade the beast or climb the tree (slay/evade/climb): "]
    typewriter_sliced(q_text, 0.020)
    player_options = str(input(""))
    global end_game
    if player_options.lower() == "evade":
        sneak_text = [fg.white,"\nHoray! You've sneaked past the beast and have found yourself safely on an open path, with faint sounds of water close ahead."]
        typewriter_sliced(sneak_text, 0.020)
        time.sleep(2)
        east_option()
    elif player_options.lower() == "slay" and player_character == "researcher":
        lunch_text = ["Alas! You've got a brave heart, you've chosen to slay the beast where it stands.\nUnfortuantely, as your skills of a researcher dont stretch to hand to hand combat, you've become an easy lunch for the beast."]
        typewriter_sliced(lunch_text, 0.020)
        end_game() # title sequence 
    elif player_options.lower() == "slay" and player_character == "explorer":
        slay_explorer = ["Alas! You've got a brave heart, you've chosen to take on the beast. As you are well equipped for combat, you have injuried the beast and choose to ... \nfinish him!, but while doing so you have taken some damage, you have lost a life."]
        typewriter_sliced(slay_explorer, 0.020)
        player_lives -= 1
        slay_explorer= [fg.red, f"You now have {player_lives} lives remaining!"]
        typewriter_sliced(slay_explorer, 0.020)
        east_option()
    elif player_options.lower() == "climb":
        up_a_tree()  
    else: 
        print("Please input evade, slay or climb.")
        north_option()

###############################################################

# SOUTH OPTION
def south_option():
    match_q = [fg.yellow,"Would you like to light a match to help your visibility?"]
    choose_y_or_n = ["Choose an option yes or no? "]
    typewriter_sliced(match_q, 0.020)
    typewriter_sliced(choose_y_or_n, 0.020)
    player_options = input("")
    global end_game
    if player_options.lower() == "yes" or player_options.lower() == "y":
        time.sleep(2.1)
        explosion_text = [fg.red,"\nYou light the match and unknowingly ignites nearby plane fuel ......booooooommm... it scorches the earth with bloody remains as your skin drips off."]
        typewriter_sliced(explosion_text, 0.020)
        end_game()
    elif player_options.lower() == "no" or player_options.lower() == "n":
        time.sleep(2.1)
        impaled_text = [fg.red,"You opt not to light a match and the darkness becomes too overwhleming, the rustling of unseen creatures in the underbrush sends shivers down your spine and you start sweating profusely.\nYour scent becomes to tatsty for the lurking creatures to ignore, they pounce and surround you. In one quick movement you screech from the bottom of your lungs and cling on to the\n last bit of life you have left, but eventually you exhaust all physucal energy keeping them at bay and soon become supper for the king of the jungle..."]
        typewriter_sliced(impaled_text, 0.020)
        end_game() # title sequence 
    else: 
        print('\033[93m'"Please choose yes or no."'\033[93m')
        south_option()
        
###############################################################

# EAST OPTION
def east_option():
    global player_lives
    global player_character
    river_img = ["""\033[96m
                                .. ........... .............  ........... . ..... ........ .......
                                ......  ....................%.... .... ..... .........%............
                                .@@@ ........ @@.... @@@@  . ............................  *  .....
                                ....@@ ..... @ .... @ .............   ....... .....; .... *** .....
                                .....\@\....@ .... @ ............................. #  .. *****  ...
                                @@@.. @@@@@  @@@@@@___.. ....... ...%..... ...  {###}  ******** ...
                                ....@-@..@ ..@......@@@\...... %...... ....... <## ####>******** ..
                                @@@@\...@ @ ........\@@@@ ..... ...... ....... {###}***********  ..
                                ....%..@  @@ /@@@@@ . ....... ...............<###########> *******
                                ...... .@-@@@@ ...V...... .. /  \. %.......... {#######}******* ***
                                ...... .  @@ .. ..v.. .. .../ ~  \........<###############>*******
                                ......... @@ .... .......  /      \ .......   {## ######}***** ****
                                ..%..... @@ .. .%.... . ../   ~~   \   ... <###################> ****
                                . .... . @@ . ...... _ . /          \........ {#############}********
                                .... ... @@ ... ..   /../  ~~        \....<################  #####>***
                                . .... ..@@@ ...... (  /         ~~   \...{##################}*****
                                ......... @@@  .... | /                \<##########################>**
                                @@@@ ....@@@  ...  _/    ~~~~           \{###   ##############}*****
                                @@@@@@@  @@@@@ .. / /           ~~~      \#############################>
                                @@@@@@@ @@@@@@@ @@@/     ~~~~             \.. @@@@@@  @@@@@@@  @@@@
                                @@@@@@###@@@@@### /                        \@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                @@@@@@@@###@##@@ /            ~~~~~         \@@@   @@@@@@@@@@@@@@@@@@@
                                @@@@@@@@@@@### @/     ~~~~                   \ @@@@@@@@@@@@@@@@@@@@@@@@
                                -@@@@@@@@@#####/                     ~~~~~    \@@@@@@@@@@@@@@@@@@@@@@@@@@
    \033[96m"""]
    river_text = [fg.white,"You come to a river in front of you, it's wide and turbulent, with huge whitecaps and whirlpools forming all over.\nThe water is murky and brown carrying debris making it impossible to see the bottom. You see no way around and have to cross it.\nThere are three possible ways you can get across the river: \n1) A rickety boat \n2) Slippery stones you can jump on \n3) Swim across, if you dare"]
    choose_text = [fg.white,"Choose 1, 2 or 3: "]
    typewriter_sliced(river_img, 0.0010)
    typewriter_sliced(river_text, 0.020)
    typewriter_sliced(choose_text, 0.020)
    options = input("")
    if options == "1":
        raft_text = ["\nYou've chosen the boat, you climb inside and inspect the boat and are quick to find a bottled scroll.\nYou unravel the scroll and find an inscription on it..."] 
        typewriter_sliced(raft_text, 0.020)
        scroll_art = ["""
                            _______________________
                          =(__    ___      __     _)=
                            |                     |
                            |        RIGHT        |
                            |         IS          |
                            |         NOT         |
                            |       ALWAYS        |
                            |        RIGHT        |
                            |__    ___   __    ___|
                          =(_______________________)= 
        """]
        typewriter_sliced(scroll_art, 0.020)
        raft_text_2 = ["You memomrise the information as it may come in handy later.\nThe current takes the boat and you are soon safely across the river!\n"]
        typewriter_sliced(raft_text_2, 0.020)
        
        west_option() 
    elif options == "2" and player_character == "researcher":
        stones_text_researcher = ["You've dared to take the slippery stones!\nAt first the rushing water threatens to pull you off balance, but years of ballet have given you the stability to make it across without any trouble."]
        stones_text = ["Congrats you made it! As you take a moment to catch your breath, you notice a mysterious opening in the forest ahead. You have no other option but to proceed ahead, into the depths of the thick foliage and overgrown plants."]
        typewriter_sliced(stones_text_researcher, 0.020)
        typewriter_sliced(stones_text, 0.020)
        west_option() 
    elif options == "2" and player_character == "explorer":
        stones_text_explorer = ['\033[31m'"You've dared to take the slippery stones!\nYears of skipping leg day have made you top heavy, resulting in you losing your footing and plunge into the river."'\033[31m']
        typewriter_sliced(stones_text_explorer, 0.020)
        player_lives -= 1
        if player_lives <= 0:
           out_of_lives = [fg.red, "Unlucky, you are out of lives!"]
           typewriter_sliced(out_of_lives, 0.020)
           end_game()
        else:
            riverbed_damage = ['\033[96m'"You took some damage from colliding into the riverbed as a result of the strong currents. You are still fit enough to carry on"'\033[96m' + fg.red, "but you lose a life."]
            remaining_lives = [fg.red,f"You now have {player_lives} lives remaining.\n"]
            typewriter_sliced(riverbed_damage, 0.020)
            typewriter_sliced(remaining_lives, 0.020)
            west_option()
    elif options == "3":
        opt_3 = [fg.red,'You think you are fit enough, and chance the swim across the river.\nSadly these waters are filled with flesh eating phiranas, who are quick to nibble at your underbelly.']
        shark_img = ["""
 
                            O     O                
            o o          .:/    
                o      ,,///;,   ,;/ 
                o   o)::::::;;///
                   >::::::::;;\ \ 
                    ''\|\||'" ';\ 
                        ';/              
                                      O     O
                                           /:.        o o           
                                 /;ˎ   ˎ;///ˎˎ      o               
                                    ///;;::::::(o   o               
                                    \ \;;::::::::<                  
                                    \;' "'\|\||''                   
                                          /;'                       
        '"""]
        typewriter_sliced(opt_3, 0.020)
        typewriter_sliced(shark_img, 0.0010)
        player_lives -= 1
        if player_lives == 0:
            opt_3_lives = [fg.red,"Unlucky, you are out of lives"]
            typewriter_sliced(opt_3_lives, 0.020)
            end_game()
        else:
            bruised_text = [fg.red,"Bruised and bloodied you notice a chunk of your belly is missing and swim frantically to the edge to climb out."]
            lose_life = [fg.red,"You have lost a life!"]
            lives_remaining_text = [f"You now have {player_lives} lives remaining."]
            typewriter_sliced(bruised_text, 0.020)
            typewriter_sliced(lose_life, 0.020)
            typewriter_sliced(lives_remaining_text, 0.020)
            time.sleep(2.1)
            west_option()
    else: 
        print('\033[96m'"Fool, please choose one of the 3 options."'\033[96m')
        east_option()
        
###############################################################

# WEST OPTION
def west_option():
    global player_lives
    global player_character
    door_text = [fg.white,"You have been making your way through the thick of the jungle for some time now and visibility starts to get weaker.\nAt this point you are being guided more by touch than sight. All of sudden there's a distinct flicker that you catch at the corner of your eye. You reaffirm your footing and follow the faint light to\nthen find yourself in an opening, first impressions are of a religious undertone\nwhich shortly become confirmed when you explore the other side and find yourself standing in front of a decadent grand door.\n"]
    typewriter_sliced(door_text, 0.020)
    door_img = [fg.darkgrey,"""
                                                .-----.----.-----.  
                                               / /-.| |////| |.-\ \  
                                              / /|_|| |////| ||_|\ \   
                                             /  :   : |////| :   :  |
                                            /  /___:  |////|  :___\  |
                                           /   :   |_ |////| _|   :___\    
                                          /   /    |_||////||_|    \   \    
                                         /    :    |_||////||_|    :    |
                                        /____/____ |_||////||_| ____\____|
                                       /     :    |   |////|   |    :     |
                                      /     /     | _ |////| _ |     \     |
                                      \     :     || ||////|| ||     :     /
                                        \   /    .'-\ ||////|| /-`.    \   /
                 ------------------------'-'---------'-'----'-'---------'-'------------------------------
    """]
    typewriter_sliced(door_img, 0.0010)
    q_text = [fg.white,"After closer inspection, you notice what looks like an ancient relic engraved on the door frame.\nYou read it and discover a riddle.\nIt states... 'There are 12 fish and half of them drown. How many of them remain?\nA) 6\nB) 12"] 
    typewriter_sliced(q_text, 0.020)
    door_q = [fg.white,"Please choose a or b: "]
    typewriter_sliced(door_q, 0.020)
    option = input("")
    if option == "a":
        fall_through()   
    elif option == "b":
        correct_text = [fg.white,"Voila!\nAll of sudden your words echo across the space and the door magically opens.\nBefore your eyes you are presented with an empty space and feel an unnerving sense of doubt rush through your body.\n\n"]
        typewriter_sliced(correct_text, 0.020)
        time.sleep(2)
        tribal_encounter()
    else:
        print("Please choose a or b")
        west_option()
        
###############################################################
        
def fall_through():
    trap_door_text = [fg.red,"Unlucky! You're wrong, fish can not drown :).\nA trap door suddenly opens up beneath you and fall 5 metres into a pit."]
    typewriter_sliced(trap_door_text, 0.020)
    time.sleep(3)
    secret_door_text = [fg.white,"Thankfully, your fall is cushioned by a sack of wheat. After gathering yourself you assess the surrounding area and notice a slight draught. You run your finger along and locate the source, and discover a hinge to a secret door.\nYou are now posed with two options:\n1) Explore the secret passage \n2) Try to climb back out"]
    typewriter_sliced(secret_door_text, 0.020)
    climb_q = [fg.white,"Please choose option 1 or 2: "]
    typewriter_sliced(climb_q, 0.020)
    option = input("")
    if option == "2":
        west_option()
    elif option == "1":
        secret_passage()
    else:
        print("Please choose 1 or 2")
        fall_through()
    
###############################################################
    
def tribal_encounter():
    global player_character
    global player_lives
    tribe_walk = [fg.white,"You continue walking and explore the new space, you see a light suddenly ignites and a silhouette of a large figure emerges. You realise the figure is wearing an ancient headdress which resembles that of a Malecite chief."] 
    typewriter_sliced(tribe_walk, 0.020)
    ascii_chief = [fg.lightred,"""
                                                    WWWW.
                                                  WWWW""'
                                                .WWWW O O
                                            .WWWW"WW.'-. 
                                            WWWWWWWWWWWWW.
                                            WWWWWWWWWWWWWWW
                                            "WWWWWWWWWW"'\___
                                            /  /__ __/\___(  )
                                            (____( \X( mrf /||\  
                                            / /||\  /
                                            \______/
                                                \ | \ |  
                                                )|  \|
                                                (_|  /|
                                                |X| (X|  
                                                |X| |X'._  
                                               (__| (____)
   """]
    typewriter_sliced(ascii_chief, 0.0010)
    tribe_q = [fg.white,"Do you approach and try to converse with him or do you try and sneak past him?"]
    conv_sneak = ["A) Converse B) Sneak (a/b): "]
    typewriter_sliced(tribe_q, 0.020)
    typewriter_sliced(conv_sneak, 0.020)
    options = input("")
    if options == "a":
        a_ans = [fg.white,"You give your best efforts to try and communicate with the figure, but they seem hesitant to respond,\n muttering an unfamiliar language. However, despite the language barrier you tru to explain to him calmly that you mean no harm and that you are lost.\n After some time, you estabilish an understanding and they reveal that they have been watching you for some time.\nWith their guidance, you navigate in the direction of a secret passage."]
        typewriter_sliced(a_ans, 0.020)
        secret_passage()
    elif options == "b" and player_character == "researcher":
        fight_researcher = ["Despite your best efforts to sneak past and evade detection, you make too much noise and alert the chief who is quick to summon his men and although you muster up strength to fight them off, you take some damage in trying to escape." + fg.red, "\nYou lose two lives!"]
        typewriter_sliced(fight_researcher, 0.020)
        player_lives -= 2
        if player_lives <= 0:
            lost_lives_researcher = [fg.red, "Unlucky, you've lost all your lives!"]
            typewriter_sliced(lost_lives_researcher, 0.020)
            end_game()
        else:
            damaged_researcher = ["heavily damaged you are still able to carry on and make it to safety."]
            typewriter_sliced(damaged_researcher, 0.020)
            secret_passage()
    elif options == "b" and player_character == "explorer":   
         fight_explorer = ['\033[31m'"Despite your best efforts to sneak past and evade detection, you make too much noise and alert the chief\n who is quick to summon his men and although you muster up strength to fight them off,\n you take some damage in trying to escape, you lose one life"'\033[31m']
         typewriter_sliced(fight_explorer, 0.020)
         player_lives -= 1
         if player_lives <= 0:
            lost_lives_explorer = [fg.red, "Unlucky, you've lost all your lives!"]
            typewriter_sliced(lost_lives_explorer, 0.020)
            end_game()
         else:
            damaged_explorer = ["heavily damaged you are still able to carry on and make it to safety"]
            typewriter_sliced(damaged_explorer, 0.020)
            secret_passage()
    else:
        print("please choose a or b")
        tribal_encounter()
        
        
def up_a_tree():
    global player_character
    global player_lives
    global items_choice
    global player_item
    random_item()
    climbing_tree = [f"\nYou've taken a shot at climbing the behemoth tree and have some time to compose yourself to think of your next move. Being 40 metres up gets your hands sweating\nand your legs shaking, you see a {items_choice} on the ground, would you like to pick it up? yes or no?"]
    typewriter_sliced(climbing_tree, 0.020)
    player_options = input("")
    if player_options == "yes" and items_choice == "key":
        player_item = True
        item_yes = ["\nYou have picked up the key. Will this be helpful later on? Maybe.... "]
        typewriter_sliced(item_yes, 0.020)
    elif player_options == "no":
        item_no = ["\nYou have chosen not to burden yourself, is this a wise choice? Maybe..."]
        typewriter_sliced(item_no, 0.020)
    elif player_options == "yes" and items_choice != "key":
        # player_item = False
        item_book = ["You have have picked up the book. enjoy reading!!"]
        typewriter_sliced(item_book, 0.020)
    else:
        print("please choose yes or no")
        up_a_tree()
    canopy_text = ["\nYou can see the canopy ahead of you stretched as far as you can see and it looks safe enough to walk on.\nYou have two options:\n1) Walk along the canopy\n2) Climb back down (1/2)"]
    typewriter_sliced(canopy_text, 0.020)
    
    
    options = input("")
    if options == "1" and player_character == "explorer":
        fall_off = ['\033[31m'"A brazen choice, you start walking along the canopy and slowly notice that the trees beneath you start to crumble away.\n ARGHHHHHHH, you suddenly start free falling to the jungle floor and before you know it,\n you are back on ground level with the beast but have taken some damage in the fall and"'\033[31m' + fg.red, "have lost one life."]
        typewriter_sliced(fall_off, 0.020)
        player_lives -= 1
        lives_left_explorer = [fg.red, f"You now have {player_lives} lives left.\n"]
        typewriter_sliced(lives_left_explorer, 0.020)
        north_option()
    elif options == "1" and player_character == "researcher":
        canopy_walk = ["Success! You safely start walking along the canopy and after a few mintues of walking you come to a visibile opening, that has a clear access for a descent back to the jungle floor. As you start to climb down you notice that the visbility starts to darken and a wave of uncertainty and worry start to cast over you."]
        typewriter_sliced(canopy_walk, 0.020)
        south_option()
    elif options == "2":
        climb_down = [fg.white,"You've chosen to climb back down, after slowly struggling to climb down you finally make it back to the jungle floor. The beast is still there."]
        typewriter_sliced(climb_down, 0.020)
        north_option()
    else:
        print("Please choose 1 or 2.")
        up_a_tree()
     
###############################################################
     
def secret_passage():
    tunnel_img = [fg.darkgrey,"""
                                                                .......
                                                          .-'''L   |   J'''-.
                                                       .'\     |   |   |     /'.
                                                     .'   \    J   |   F    /   '.
                                                   .'.     \    L  |  J    /     .'.
                                                  (   '.    \   |  |  |   /    .'   )
                                                 +-.    '.   \  J  |  F  /   .'    .-+
                                                J   '-.   '.  \ .L.|.J. /  .'   .-'   L
                                                L__    '-.  '.            .'  .-'    __J
                                               J   ""-__  '-.             .-'  __-""   L
                                               |        ""--|             |--""        |
                                               |------------      / \      ------------|
                                               |        __--|    /   \    |--__        |
                                               J   __-""  .-'   /     \   '-.  ""-__   F
                                                L""    .-'  .  /       \ '.  '-.    ""J
                                                                '''''''
                            """]
    typewriter_sliced(tunnel_img, 0.0010)
    tunnel_text = [fg.darkgrey,"You are on all fours and find yourself scurrying in a dark tunnel. You come to a T-junction and have make the decision whether you want to go right or left"]
    choice_r_l = [fg.darkgrey,"Please choose right or left: "]
    typewriter_sliced(tunnel_text, 0.020)
    typewriter_sliced(choice_r_l, 0.020)
    options = input("")
    if options == "right":
        light_at_end_tunnel = [fg.white,"\nAfter turning right and crawling for another few minutes, you start to notice a glimmer of light at the end of the tunnel.\nYou move faster as the tunnel slowly widens and you come out on to a small beachfront."]
        typewriter_sliced(light_at_end_tunnel, 0.020)
        beach_front = [fg.yellow,"""
                                     ___   ____
                                   /' --;^/ ,-_\     \ | /
                                  / / --o\ o-\ \}   --(_)--
                                 /-/-/|o|-|\-\|\|   / / | `
                                  '`  ` |-|   `` '
                                        |-|
                                        |-|O
                                        |-(\,__
                                     ...|-|\--,\_....
                                ,;;;;;;;;;;;;;;;;;;;;;;;;,.
                            ~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~=-.,__,.-=~'`^`'~=-.,__,.-==--^'~=-.,__,.-=~''
                               ~;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,   _,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,.-=~'`^`'~=-.,__,.-=~'
                          ~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`  ~`'^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^
                                ~'`^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=.;^`'~=-.,__,.-=~'`^`'~=-.,__,.-=~'`^`'~=-.,__,
                             
        """]
        typewriter_sliced(beach_front, 0.0010)
        time.sleep(3)
        boat_out()
    elif options == "left":
        starvation_text = ["\nAfter crawling for what seems like an eternity nothing looks familiar any more. With no water or food a sense of dread creeps in, you are completeley lost.\nA palpable sense of death consumes what life you have left, you accept that all hope is lost and you drop to the floor with exhaustion, your vision slowly turns to black as your life fades away into nothingness."]
        typewriter_sliced(starvation_text, 0.020)
        end_game()
    else:
        print("Please choose right or left")
        secret_passage()

###############################################################

def boat_out():
    global player_lives
    global player_name
    global player_item
    boat_text = [fg.lightgrey,"To your amazement, you see a small motor boat is moored to the beach, without hesitation you board it."]
    typewriter_sliced(boat_text, 0.020)
    if player_item == True: 
        engine_start = ["Success! You take the key you found earlier from your pocket, insert it into the ignition and start it up.\nTo your surprise the engine runs perfectly. You open \nthe throttle and head out into the open ocean!"]
        typewriter_sliced(engine_start, 0.020)
    else:
        no_key = ["You look around the boat and desperately try to find a key to start the engine. Unfortunately to no avail.\nYou have no other option but to turn back and find it.\n"]
        typewriter_sliced(no_key, 0.020)
        hint_function()

                                         
    well_done_txt = [fg.orange,"""
 __      __       .__  .__        .___                     
/  \    /  \ ____ |  | |  |     __| _/____   ____   ____   | | |
\   \/\/   // __ \|  | |  |    / __ |/  _ \ /    \_/ __ \  | | |
 \        /\  ___/|  |_|  |__ / /_/ (  <_> )   |  \  ___/   \|\|
  \__/\  /  \___  >____/____/ \____ |\____/|___|  /\___  >  ____
       \/       \/                 \/           \/     \/   \/\/"""]
    
    congrats_text = [fg.lightgrey,f"Congratulations {player_name}! you have escaped the jungle and find safe passage back to civilisation!"] 
    
    boat_img = [fg.lightgrey,"""    
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___/
           \               ""/ """]
    boat_water = [fg.blue,
    """     ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~
    """]
    typewriter_sliced(boat_text, 0.020)
    typewriter_sliced(well_done_txt, 0.0010)
    typewriter_sliced(congrats_text, 0.020)
    typewriter_sliced(boat_img, 0.0010)
    typewriter_sliced(boat_water, 0.0010)
    print(fg.lightgrey,"Do you want to play again? y/n")
    options = input("")
    if options == "y" or options == "yes":
        player_lives = 3
        startgame()
    elif options == "n" or options == "no":
        quiz_game()
    else:
        print("Please enter yes or no.")
        end_game()
        
def hint_function():
    hint = input("Would you like a hint? ")
    if hint == "yes":
        boat_out_hint = ["Go up the tree to find the key"]
        typewriter_sliced(boat_out_hint, 0.020)
        time.sleep(4)
        crossroadsection()
    elif hint == "no":
        boat_out_hint = ["Suit yourself, good luck!"]
        typewriter_sliced(boat_out_hint, 0.020)
        crossroadsection()
    else:
        boat_out_hint = ["Choose yes or no."]
        typewriter_sliced(boat_out_hint, 0.020)
        hint_function()


def end_game():
    global player_lives
    fatality_text = [fg.red, bg.black,"""
                                 _______  _______ _________ _______  _       __________________          _   
                                (  ____ \(  ___  )\__   __/(  ___  )( \      \__   __/\__   __/|\     /|( )  
                                | (    \/| (   ) |   ) (   | (   ) || (         ) (      ) (   ( \   / )| |  
                                | (__    | (___) |   | |   | (___) || |         | |      | |    \ (_) / | |  
                                |  __)   |  ___  |   | |   |  ___  || |         | |      | |     \   /  | |  
                                | (      | (   ) |   | |   | (   ) || |         | |      | |      ) (   (_)  
                                | )      | )   ( |   | |   | )   ( || (____/\___) (___   | |      | |    _   
                                |/       |/     \|   )_(   |/     \|(_______/\_______/   )_(      \_/   (_)  
    """]
    starvation_img = [fg.red, bg.black,"""
                                                             __________
                                                          .~#########/%/%;~
                                                         /############%/%;`|
                                                        /######/~\/~\%/%;,;,|
                                                       |#######\    /;;;;.,.|
                                                       |#########\/%;;;;;.,.|
                                              XX       |##/~~\####%;;;/~~\;,|       XX
                                            XX..X      |#|  o  \##%;/  o  |.|      X..XX
                                          XX.....X     |##\____/##%;\____/.,|     X.....XX
                                     XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
                                    X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
                                    X |.....X  @#%,.@     |######%/%;;;;,.|     @#%,.@  X.....| X
                                    X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
                                     X# \.X        @#%,.@                  @#%,.@        X./  #
                                      ##  X          @#%,.@              @#%,.@          X   #
                                    , "# #X            @#%,.@          @#%,.@            X ##
                                      `###X             @#%,.@      @#%,.@             ####'
                                     . ' ###             @#%.,@  @#%,.@              ###`"
                                       . ";"               @#%.@#%,.@                ;"` ' .
                                        '                    @#%,.@                   ,.
                                        ` ,                @#%,.@  @@                `
                                                            @@@  @@@  
    """]
    end_text = ["Clearly you need some help surviving, here is a handy link:"]
    typewriter_sliced(fatality_text, 0.0010)
    typewriter_sliced(starvation_img, 0.0010)
    typewriter_sliced(end_text, 0.020)     
    webbrowser.open_new_tab("https://www.beargrylls.com/")  
    play_again = [fg.lightgrey,"Do you want to play again? y/n"]
    typewriter_sliced(play_again, 0.020)
    options = input("")
    if options == "y" or options == "yes":
        player_lives = 3
        startgame()
    elif options == "n" or options == "no":
        quiz_game()
    else:
        print("Please enter yes or no.")
        end_game()


##########################################
# Quiz game

def quiz_game():
    quiz_img = ["""              
________        .__         ___________.__                 
\_____  \  __ __|__|_______ \__    ___/|__| _____   ____   
 /  / \  \|  |  \  \___   /   |    |   |  |/     \_/ __ \  
/   \_/.  \  |  /  |/    /    |    |   |  |  Y Y  \  ___/  
\_____\ \_/____/|__/_____ \   |____|   |__|__|_|  /\___  > 
       \__>              \/                     \/     \/        
    """]
    quiz_text_1 = ["Welcome to quiz game!!"]
    quiz_text_2 = ['NOTE: If your spelling is incorrect then it is considered as a wrong answer.']
    typewriter_sliced(quiz_img, 0.0010)
    typewriter_sliced(quiz_text_1, 0.020)
    typewriter_sliced(quiz_text_2, 0.020)
    score = 0
    question_no = 0
    playing = input('Do you want to play? ').lower()
    if playing == 'yes':
        question_no += 1
        ques = input(f'\n{question_no}. Who sings the song  welcome to the jungle ').lower()
        if ques == 'guns and roses':
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect!')
            print('current answer is --> guns and roses')

# ------1
        question_no += 1
        ques = input(f'\n{question_no}. Who is quoted in the description at the start the game ').lower()
    
        if ques == 'arnold': 
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect! hasta la vista - shotgun noise')
            print('current answer is --> arnold')

# -----2
        question_no += 1
        ques = input('\n{question_no}. Which character is intellectual in the game? ').lower()
    
        if ques == 'researcher':
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect!')
            print('current answer is --> researcher')

# -----3
        question_no += 1
        ques = input(f'\n{question_no}. Which character is blessed with strength in the game? ').lower()
    
        if ques == 'explorer':
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect!')
            print('current answer is --> explorer')


# -----4
        question_no += 1
        ques = input(f'\n{question_no}.  what item do you need for the boat? ').lower()
    
        if ques == 'key':
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect! ')
            print('current answer is --> key')


# ------5 
        question_no += 5
        ques = input(f'\n{question_no}. what happens if you go down the south section ? ').lower()
    
        if ques == 'you die'or 'die':
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect!')
            print(f'current answer is --> you die')

 # ------6 
        question_no += 6
        ques = input(f'\n{question_no}. what does the hint say? ').lower()
    
        if ques == 'right is not always right':
            score +=1
            print('correct! you got 1 point')
        
        else:
            print('Incorrect! did you get the riddle wrong too?')
            print(f'current answer is --> right is not always right')






    else:
        thanks_text = ["Thank you for playing"]
        typewriter_sliced(thanks_text, 0.020)
        quit()
    
    end_q_amount = [f'\nnumber of question is {question_no}']
    score_amount = [f'your score is {score}']
    typewriter_sliced(end_q_amount, 0.020)
    typewriter_sliced(score_amount, 0.020)
    try:
        percentage = (score *100)/question_no
    except ZeroDivisionError:
        print('0% quetions are correct')

    score_in_percentage = [f'{percentage}% questions are correct.']
    typewriter_sliced(score_in_percentage, 0.020)

startgame()

