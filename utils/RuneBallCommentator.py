
import pyttsx3
import random
import time
import sqlite3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # set the voice to the first voice in the list


engine = pyttsx3.init()
commentary = ("Welcome to Rune Ball")
engine.say(commentary)
engine.runAndWait() 

while True:

        conn=sqlite3.connect('player_database.db')
        C=conn.cursor()

        #Uncomment below for Forgotten Runes Games
        teams=['Wizards','Warriors','Kobolds','Beasts','Souls']

        # Uncomment below for Bitball Demo Games
        #teams=['Ghosts','Wizards','Conjurers','Omegas','Unicorns','Curves','Dragons','Frogs','Whales','NFT']

        #Define function that returns the mascot of team in parameters. Used to append to player names for team identification in gameplay.

        def teamtag(team):
                teamtag = team.upper()
                return teamtag

        t1dice = random.randint(0,4)
        t2dice = random.randint(0,4)
        while t1dice == t2dice:
                t2dice = random.randint(0,4)
        Team1name = teams[t1dice]
        Team2name = teams[t2dice]
                       

        #Define dice_roll function that accepts one argument that is equal to number of sides on dice rolled

        def dice_roll(d):
                result = random.randint(1,d)
                return result


        #Define Statgen function that rolls 4d6, drops the lowest number, and sums the remaining 3
        # def Statgen():
        #         dice = [dice_roll(6),dice_roll(6),dice_roll(6),dice_roll(6)]
        #         stat = []
        #         dice.sort()
        #         stat.append(dice[1])
        #         stat.append(dice[2])
        #         stat.append(dice[3])
        #         stat = stat[0]+stat[1]+stat[2]
        #         return stat
                
                
        #Create superclass Player
        class Player:
                def __init__(self,keeper,refnum,team):
                        self.refnum = refnum
                        self.team = team
                        (C.execute("SELECT name FROM players WHERE team=:team GROUP BY name HAVING refnum=:refnum",{"team":self.team,"refnum":self.refnum}))
                        self.name = C.fetchone()[0]
                        (C.execute("SELECT str_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.STR = C.fetchone()[0]
                        (C.execute("SELECT dex_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.DEX = C.fetchone()[0]
                        (C.execute("SELECT wis_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.WIS = C.fetchone()[0]
                        (C.execute("SELECT cha_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.CHA = C.fetchone()[0]
                        (C.execute("SELECT mag_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.MAG = C.fetchone()[0]
                        (C.execute("SELECT dmag_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.DMAG = C.fetchone()[0]
                        self.keeper = keeper
                        (C.execute("SELECT gk_mod FROM players WHERE name =:name",{"name":self.name}))
                        self.GK = C.fetchone()[0]
                        (C.execute("SELECT name FROM captains WHERE team =:team",{"team":self.team}))
                        if C.fetchone()[0] == self.name:
                                self.captain = True
                                
                        else:
                                self.captain = False

                        self.ini = dice_roll(20)+self.DEX
                        self.HP = 100
                        self.inv = []
                        self.graveyard = False
                        if self.team == Team1name:
                                self.name = "["+teamtag(self.team)+"] "+self.name
                        if self.team == Team2name:
                                self.name = "["+teamtag(self.team)+"] "+self.name
                        self.HPbar = "[===========]"

                def takedmg(self):
                        self.HP -= 5

                        if "cursed item" in self.inv:
                                print("☠️ CURSE", "\n A curse haunts",self.name ,"\n")
                                engine.say("A curse haunts "+self.name)
                                engine.runAndWait()
                                self.HP -=2

                        if self.HP >= 0:
                                if self.HP >= 90 and self.HP <= 100:
                                        self.HPbar = "[===========]"
                                if self.HP >= 80 and self.HP <= 90:
                                        self.HPbar = "[==========-]"
                                if self.HP >= 70 and self.HP <= 80:
                                        self.HPbar = "[=========--]"
                                if self.HP >= 60 and self.HP <= 70:
                                        self.HPbar = "[========---]"
                                if self.HP >= 50 and self.HP <= 60:
                                        self.HPbar = "[=======----]"
                                if self.HP >= 40 and self.HP <= 50:
                                        self.HPbar = "[======-----]"
                                if self.HP >= 30 and self.HP <= 40:
                                        self.HPbar = "[====-------]"
                                if self.HP >= 20 and self.HP <= 30:
                                        self.HPbar = "[===--------]"
                                if self.HP >= 10 and self.HP <= 20:
                                        self.HPbar = "[==---------]"
                                        engine.say(self.HP)
                                        engine.runAndWait()
                                if self.HP >= 1 and self.HP <= 10:
                                        self.HPbar = "[=----------]"
                                        engine.say(self.HP)
                                        engine.runAndWait()
                                if self.HP <= 0:
                                        self.HPbar = "[-----------]"
                                        print(self.name,"HP:\n","[❤️",self.HP,"]",self.HPbar ,"\n")
                                        print(self.name, "is gravely injured!" ,"\n")
                                        self.graveyard = True
                                        self.STR = -99
                                        self.DEX = -99
                                        self.WIS = -99
                                        self.CHA = -99
                                        self.MAG = -99
                                        self.DMAG = -99
                                        self.GK = -99
                                        self.ini = -99
                                print(self.name,"HP:\n","[❤️",self.HP,"]",self.HPbar ,"\n")
                                if self.HP <= 0:
                                        print("They carry on, but the sight isn't pretty." ,"\n")
                                        engine.say(self.name)
                                        engine.runAndWait()
                                        engine.say("is fading.")
                                
                        time.sleep(1)

                def hyped(self):
                        
                        print(self.name,"basks in the sound of the crowd chanting their name!" ,"\n")
                        engine.say(self.name+" basks in the sound of the crowd chanting their name!")
                        engine.runAndWait()
                        
                        time.sleep(1)
                        spin = dice_roll(7)
                        if spin == 1:
                                self.STR += 1
                                print("🔺",self.name,"feels a boost of energy! " ,"\n")
                                 
                                time.sleep(1)
                        if spin == 2:
                                self.DEX += 1
                                print("🔺",self.name,"gets an idea! " ,"\n")
                                
                                time.sleep(1)
                        if spin == 3:
                                self.WIS += 1
                                print("🔺",self.name, "understands. " ,"\n")
                                
                                time.sleep(1)
                        if spin == 4:
                                self.CHA += 1
                                print("🔺",self.name, "keeps spirit! " ,"\n")
                                
                                time.sleep(1)
                        if spin == 5:
                                self.MAG += 1
                                print("🔺",self.name, "learned a spell. " ,"\n")
                                
                                time.sleep(1)
                        if spin == 6:
                                self.DMAG += 1
                                print("🔺",self.name,"has a sly look about them. " ,"\n")
                        if spin == 7:
                                self.HP += 20
                                print("🔺",self.name,"gets a second wind! " ,"\n")
                                print(self.name,"HP:\n","[❤️",self.HP,"]",self.HPbar ,"\n")
                                time.sleep(1)

                def disappointed(self):
                        
                        print(self.name+"'s disappointment betrays them. " ,"\n")
                        engine.say(self.name+"'s disappointement betrays them.")
                        engine.runAndWait()

                        spin = dice_roll(6)
                        if spin == 1:
                                self.STR -= 1
                                 
                                print("🔻",self.name,"is getting tired..." ,"\n")
                                time.sleep(1)
                        if spin == 2:
                                 
                                self.DEX -= 1
                                print("🔻",self.name,"is slowing down..." ,"\n")
                                time.sleep(1)
                        if spin == 3:
                                 
                                self.WIS -= 1
                                print("🔻",self.name, "seems a bit rattled..." ,"\n")
                                time.sleep(1)
                        if spin == 4:
                                 
                                self.CHA -= 1
                                print("🔻",self.name, "is losing spirit..." ,"\n")
                                time.sleep(1)
                        if spin == 5:
                                 
                                self.MAG -= 1
                                print("🔻",self.name, "forgot a spell..." ,"\n")
                                time.sleep(1)
                        if spin == 6:
                                 
                                self.DMAG -= 1
                                print("🔻",self.name+"'s dark side is showing..." ,"\n")
                                time.sleep(1)

        swingcount = 0
        tipoff = True
        def fight(fighter1,fighter2):
                if tipoff == True:
                        
                        print("The two team captains struggle for control of the ball." ,"\n")
                if tipoff == False:
                        
                        print("A fight has broken out in the RuneBall Pit between",fighter1.name,"and",fighter2.name,"!" ,"\n")
                        engine.say("A fight has broken out in the RuneBall Pit between"+fighter1.name+"and"+fighter2.name)
                        engine.runAndWait()
                time.sleep(1)
                global swingcount
                while swingcount < 10:

                        if fighter2.HP < fighter1.HP:
                                def swing():
                                        global swingcount
                                        swingcount = swingcount
                                        swing = dice_roll(20) + fighter2.STR + fighter2.WIS + fighter2.DEX
                                        swingcount +=1
                                        if swing >= 15:
                                                
                                                
                                                print(fighter1.name,"takes a nasty hit." ,"\n")
                                                engine.say(fighter1.name+" takes a nasty hit.")
                                                engine.runAndWait()
                                                time.sleep(1)
                                                fighter1.takedmg()
                                        else:
                                
                                                if swing < 15 and swing > 10:
                                                        
                                                        print(fighter2.name,"grazes",fighter1.name+"." ,"\n")
                                                        time.sleep(1)

                                                        
                                                elif swing < 10 and swing > 5:
                                                        
                                                        print(fighter1.name,"quickly dodges an attack!" ,"\n")
                                                        time.sleep(1)
                                                        

                                                elif swing < 5 and swing > 0:
                                                        
                                                        print(fighter2.name+"'s fists meet the air." ,"\n")
                                                        time.sleep(1)
                                                        
                                                else:
                                                        
                                                        print("A weak attempt by",fighter2.name+"." ,"\n")
                                                        time.sleep(1)
                                                        
                                swing()
                                def combo():
                                        coin = dice_roll(2)
                                        if coin == 1:
                                                swing()
                                                
                                combo()
                                combo()


                        else:
                                def swing():
                                        global swingcount
                                        swingcount = swingcount
                                        swing = dice_roll(20) + fighter1.STR + fighter1.WIS + fighter1.DEX
                                        swingcount +=1
                                        if swing > 15:
                                                
                                                print(fighter2.name,"gets slugged!" ,"\n")
                                                engine.say(fighter2.name+" gets slugged!")
                                                engine.runAndWait()
                                                time.sleep(1)
                                                fighter2.takedmg()
                                        else:
                                                if swing < 15 and swing > 10:
                                                        
                                                        print(fighter1.name,"barely scratches",fighter2.name+"." ,"\n")
                                                        time.sleep(1)
                                                elif swing < 10 and swing > 5:
                                                        
                                                        print(fighter2.name,"is showing off their footwork." ,"\n")
                                                        time.sleep(1)

                                                elif swing < 5 and swing > 0:
                                                        
                                                        print(fighter1.name+" better keep their focus." ,"\n")
                                                        time.sleep(1)
                                                else:
                                                        
                                                        print("A sad display by",fighter1.name+"." ,"\n")
                                                        time.sleep(1)
                                swing()
                                def combo():
                                        coin = dice_roll(2)
                                        if coin == 1:
                                                swing()
                                combo()
                                combo()

                if swingcount >= 10:
                        if tipoff == True:
                                
                                print("The dust settles around the struggle..." ,"\n")
                        if tipoff == False:
                                
                                print("The bloodied players return to the game." ,"\n")
                                engine.say("The bloodied players return to the game.")
                                engine.runAndWait()
                        time.sleep(1)
                        swingcount = 0
                        


        def hyped(self):
                        print(self.name,"get hyped! 🔥" ,"\n")
                        
                        time.sleep(1)
                        for Player in self.team:
                                wheel = ["X",Player.STR,Player.DEX,Player.WIS,Player.CHA,Player.MAG,Player.DMAG]
                                spin = dice_roll(6)
                                if spin == 1:
                                        Player.STR += 1
                                        print("🔺",Player.name,"feels a boost of energy! " ,"\n")
                                         
                                        time.sleep(1)
                                if spin == 2:
                                        Player.DEX += 1
                                        print("🔺",Player.name,"gets an idea! " ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 3:
                                        Player.WIS += 1
                                        print("🔺",Player.name, "understands. " ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 4:
                                        Player.CHA += 1
                                        print("🔺",Player.name, "keeps spirit! " ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 5:
                                        Player.MAG += 1
                                        print("🔺",Player.name, "learned a spell. " ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 6:
                                        Player.DMAG += 1
                                        print("🔺",Player.name,"has a sly look about them. " ,"\n")
                                        
                                        time.sleep(1)
        
                        




        newlist=[]
        loopcount=0
        pos=[]
        silence = 0

        #Initialize scores
        ScoreA=0
        ScoreB=0

        #Initialize team pass counters
        TeamAPass=0
        TeamBPass=0

        #Initialize foul counter for both teams
        FoulA=0
        FoulB=0

        #Initialize run counter for both teams
        Aruncount=0
        Bruncount=0

        #How long the game lasts
        seconds = 1200

        #Make start time current time at beginning of game
        start_time = time.time()

        #Creates 10 named players

        P1 = Player(True,1,Team1name)
        P2 = Player(False,2,Team1name)
        P3 = Player(False,3,Team1name)
        P4 = Player(False,4,Team1name)
        P5 = Player(False,5,Team1name)
         
        P6 = Player(True,1,Team2name)
        P7 = Player(False,2,Team2name)
        P8 = Player(False,3,Team2name)
        P9 = Player(False,4,Team2name)
        P10 = Player(False,5,Team2name)

        #Puts them onto TeamA
        

        TeamA = [P1.name,P2.name,P3.name,P4.name,P5.name]
        PTeamA = [P1,P2,P3,P4,P5]
        print("Your captains are: " ,"\n")
        time.sleep(1)
        print(Team1name+":" ,"\n")
        for player in PTeamA:
                if player.captain == True:
                        captainA = player
                        time.sleep(1)
                        print(player.name ,"\n")

        for Player in PTeamA:
                if Player.keeper == True:
                        KeeperA = Player

        #Or TeamB
        time.sleep(1)
        TeamB = [P6.name,P7.name,P8.name,P9.name,P10.name]
        PTeamB = [P6,P7,P8,P9,P10]


        for Player in PTeamB:
                if Player.keeper == True:
                        KeeperB = Player

        
        print(Team2name+":" ,"\n")
        for player in PTeamB:
                if player.captain == True:
                        captainB = player
                        time.sleep(1)
                        print(player.name,"\n")      

        #Announce Teams                
        engine.say(Team1name)
        engine.runAndWait()
        engine.say("Versus")
        engine.runAndWait()                  
        engine.say(Team2name)
        engine.runAndWait()        
        time.sleep(1)
        # BenchA =[Player("GhostA1",False,Team1name),
        #         Player("GhostA2", False, Team1name)]
        # BenchB =[Player("GhostB1",False, Team2name)],
        #         Player("GhostB2",False,Team2name)]


        class Team1:
                name = Team1name
                team = PTeamA
                        


        class Team2:
                name = Team2name
                team = PTeamB
                


        def struggle():
                global tipoff
                
                print("The team captains prepare for tip off..." ,"\n")
                engine.say("The team captains prepare for tip off...")
                engine.runAndWait()
                time.sleep(1)
                
                print("The RuneBall is launched from the center diamond!" ,"\n")
                time.sleep(1)
              #  fight(captainA,captainB)
                time.sleep(1)
                if captainA.HP > captainB.HP:
                        
                        print(captainA.name,"wins the struggle and",Team1name,"have the ball." ,"\n")
                        engine.say(captainA.name)
                        engine.runAndWait()
                        engine.say("wins the struggle and"+Team1name)
                        engine.runAndWait()
                        engine.say("have the ball")
                        engine.runAndWait()

                        pos = ['Team A']
                else: 
                        
                        print(captainB.name,"wins the struggle and",Team2name,"have the ball." ,"\n")
                        engine.say(captainB.name)
                        engine.runAndWait()
                        engine.say("wins the struggle and"+Team2name)
                        engine.runAndWait()
                        engine.say("have the ball")
                        engine.runAndWait()

                        pos = ['Team B']
                tipoff = False
                time.sleep(1)
        struggle()

        #start defining the game
        def gameloop():
                #Calls global scores and pass counters
                global ScoreA
                global ScoreB
                global TeamAPass
                global TeamBPass
                global FoulA
                global FoulB
                global Aruncount
                global Bruncount
                global captainA
                global captainB
                P1.ini = dice_roll(20)+P1.DEX
                P2.ini = dice_roll(20)+P2.DEX
                P3.ini = dice_roll(20)+P3.DEX
                P4.ini = dice_roll(20)+P4.DEX
                P5.ini = dice_roll(20)+P5.DEX
                P6.ini = dice_roll(20)+P6.DEX
                P7.ini = dice_roll(20)+P7.DEX
                P8.ini = dice_roll(20)+P8.DEX
                P9.ini = dice_roll(20)+P9.DEX
                P10.ini = dice_roll(20)+P10.DEX

        #Orders players by their initiatives
                T1order=[]
                T2order=[]
                Order = [
                        (P1,P1.name,P1.ini),
                        (P2,P2.name,P2.ini),
                        (P3,P3.name,P3.ini),
                        (P4,P4.name,P4.ini),
                        (P5,P5.name,P5.ini),
                        (P6,P6.name,P6.ini),
                        (P7,P7.name,P7.ini),
                        (P8,P8.name,P8.ini),
                        (P9,P9.name,P9.ini),
                        (P10,P10.name,P10.ini),]
                Ordered = sorted(Order, key=lambda player: player[2])
                #print(Ordered ,"\n")
                for player in Ordered: 
                        if player[1] in TeamA:
                                T1order.append(player[1])
                                
                for player in Ordered: 
                        if player[1] in TeamB:
                                T2order.append(player[1])
                                
                                        
                

        #Unpacks first and last tuple in "Ordered" list       

                (player1,firstname,firstini)=Ordered[9]
                (player2,secondname,secondini)=Ordered[8]
                (player3,thirdname,thirdini)=Ordered[7]
                (player4,fourthname,fourthini)=Ordered[6]
                (player5,fifthname,fifthini)=Ordered[5]
                (player6,sixthname,sixthini)=Ordered[4]
                (player7,seventhname,seventhini)=Ordered[3]
                (player8,eighthname,eightini)=Ordered[2]
                (player9,ninthame,ninthini)=Ordered[1]
                (player10,lastname, lastini)=Ordered[0]

                def getini():
                        

                        P1.ini = dice_roll(20)+P1.DEX
                        P2.ini = dice_roll(20)+P2.DEX
                        P3.ini = dice_roll(20)+P3.DEX
                        P4.ini = dice_roll(20)+P4.DEX
                        P5.ini = dice_roll(20)+P5.DEX
                        P6.ini = dice_roll(20)+P6.DEX
                        P7.ini = dice_roll(20)+P7.DEX
                        P8.ini = dice_roll(20)+P8.DEX
                        P9.ini = dice_roll(20)+P9.DEX
                        P10.ini = dice_roll(20)+P10.DEX

                #Orders players by their initiatives

                        Order = [
                                (P1,P1.name,P1.ini),
                                (P2,P2.name,P2.ini),
                                (P3,P3.name,P3.ini),
                                (P4,P4.name,P4.ini),
                                (P5,P5.name,P5.ini),
                                (P6,P6.name,P6.ini),
                                (P7,P7.name,P7.ini),
                                (P8,P8.name,P8.ini),
                                (P9,P9.name,P9.ini),
                                (P10,P10.name,P10.ini),]
                        Ordered = sorted(Order, key=lambda player: player[2])

                        for player in Ordered: 
                                if player in TeamA:
                                        T1order.append(player[1])
                        for player in Ordered: 
                                if player in TeamB:
                                        T2order.append(player[1])
                        for player in Ordered:
                                if player[0].graveyard == True:
                                        if player[0].name not in newlist:
                                                newlist.append(player[0].name)

                                        player[0].ini = -99
                                        return Ordered
                                        print(Ordered ,"\n")

                #Unpacks first and last tuple in "Ordered" list       

                        (player1,firstname,firstini)=Ordered[9]
                        (player2,secondname,secondini)=Ordered[8]
                        (player3,thirdname,thirdini)=Ordered[7]
                        (player4,fourthname,fourthini)=Ordered[6]
                        (player5,fifthname,fifthini)=Ordered[5]
                        (player6,sixthname,sixthini)=Ordered[4]
                        (player7,seventhname,seventhini)=Ordered[3]
                        (player8,eighthname,eightini)=Ordered[2]
                        (player9,ninthame,ninthini)=Ordered[1]
                        (player10,lastname, lastini)=Ordered[0] 

                def loot():
                        q = dice_roll(100)
                        gains = 0
                        quality = ""
                        if q >=31 and q <=80:
                                quality = "rusted"
                                gains = 1
                        if q >=81 and q <=95:
                                quality = "worn"
                                gains = 2
                        if q >=96 and q <=100:
                                quality = "used"
                                gains = 3

                        
                        print(player1.name,"looks around for loot... 📦\n")
                        engine.say(player1.name+"looks around for loot...")
                        engine.runAndWait()

                        time.sleep(1)

                        lootroll = dice_roll(20)
                        if lootroll == 20 :
                                inventory = player1.inv
                                

                                #print(player1.inv ,"\n")
                                print("...and found something. 🗡️" ,"\n")
                                engine.say("...and found something.")
                                engine.runAndWait()
                                quality
                                Player = player1
                                wheel = ["X",Player.STR,Player.DEX,Player.WIS,Player.CHA,Player.MAG,Player.DMAG]
                                spin = dice_roll(6)
                                if spin == 1:
                                        
                                        Player.STR += gains
                                        print(Player.name,"finds a",quality,"power cell and feels a boost of energy!  🔺") ,"\n" 
                                        
                                        time.sleep(1)
                                if spin == 2:
                                        Player.DEX += gains
                                        print(Player.name,"finds a",quality,"drive kit and gets an idea! 🔺" ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 3:
                                        Player.WIS += gains
                                        print(Player.name, "finds a",quality,"neurodoc chip and installs it. 🔺" ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 4:
                                        Player.CHA += gains
                                        print(Player.name,"finds a",quality,"talisman and keeps spirit! 🔺" ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 5:
                                        Player.MAG += gains
                                        print(Player.name, "finds a",quality,"magicapsule container and imbibes the remainder of its contents. 🔺" ,"\n")
                                        
                                        time.sleep(1)
                                if spin == 6:
                                        Player.DMAG += gains
                                        print(Player.name, "finds a",quality,"modkit with a dark purpose. 🔺" ,"\n")
                                        
                                        time.sleep(1)        
                                        time.sleep(1)

                                item = str(quality+"item")
                                if item not in inventory:
                                        inventory.append(item)

                        elif lootroll == 1:
                                inventory = player1.inv
                                if "cursed item" not in inventory:
                                        inventory.append("cursed item")
                                #print(player1.inv ,"\n")
                                time.sleep(1)
                                print("...and didn't like what they found. ☠️" ,"\n")
                                engine.say("...and didn't like what they found.")
                                engine.runAndWait()
                        else:
                                print("...but found nothing." ,"\n")
                                engine.say("...but found nothing.")
                                engine.runAndWait()
                                time.sleep(1)
                                

                #Will define a function that compares teams' weighted stats and pits 
                #them against each other in a struggle *

                # def war():
                #      print("!WAR!")   ,"\n" 
                

                #defines a function that calls a penalty shot to occur
                def penalty():
                        global ScoreA
                        global ScoreB
                        if player1.name in TeamA and player2.name in TeamA:
                                while player1.name in TeamA and player2.name in TeamA:
                                        Ordered.pop(len(Ordered)-1)
                                        Ordered.insert(0,0,)
                                        return Ordered
                                
                        if player1.name in TeamB and player2.name in TeamB:
                                while player1.name in TeamB and player2.name in TeamB:
                                        Ordered.pop(len(Ordered)-1)
                                        Ordered.insert(0,0,)
                                        return Ordered
                                
                        #condition for player1 to score for TeamA
                        if player1.name in TeamA:
                                
                                print(player1.name,"approaches the center diamond for a penalty shot." ,"\n")
                                engine.say(player1.name+"approaches the center diamond for a penalty shot")
                                engine.runAndWait()
                                time.sleep(1)
                                
                                print(KeeperB.name,"clears the",Team2.name,"Ring." ,"\n")
                                time.sleep(1)
                                
                                print("The sound of grinding metal fills the air." ,"\n")
                                time.sleep(1)
                                
                                print("The",Team2.name,"Ring tilts to a horizontal position." ,"\n")
                                time.sleep(1)
                                
                                print(player1.name,"lines up their trajectory..." ,"\n")
                                time.sleep(1)
                                
                                print("...and launches the ball!" ,"\n")
                                time.sleep(1)
                                
                                print("(The",Team2.name,"keeper braces as they watch helplessly)" ,"\n")
                                commentary = ("The",Team2.name,"keeper braces as they watch helplessly.")
                                engine.say(commentary)
                                engine.runAndWait()
                                time.sleep(1)
                                roll = dice_roll(20)

                                if player1.MAG+roll >= 24:

                                        ScoreA+=4
                                        
                                        print("🧿",player1.name,"scores 4 for the",Team1.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 4 for the",Team1.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                      
                                        
                                        roll = dice_roll(3)
                                        if roll == 3:
                                                if player1.team == Team1name:
                                                        hyped(Team1)
                                                if player1.team == Team2name:
                                                        hyped(Team2)
                                        time.sleep(1)
                                        player1.hyped()
                                        
                                elif player1.MAG+roll >= 20:
                                        ScoreA+=3
                                        
                                        print("🧿",player1.name,"scores 3 for the",Team1.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 3 for the",Team1.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                        
                                        
                                       
                                elif player1.MAG+roll >= 15:
                                        ScoreA+=2
                                        
                                        print("🧿",player1.name,"scores 2 for the",Team1.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 2 for the",Team1.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                        
                                        
                                        
                                elif player1.MAG+roll >= 10:
                                        ScoreA+=1
                                        
                                        print("🧿",player1.name,"scores 1 for the",Team1.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 1 for the",Team1.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                       
                                        
                                        
                                else:
                                        
                                        print("An unfortunate miss." ,"\n")
                                        engine.say("An unfortunate miss.")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        disappointed = dice_roll(3)
                                        if disappointed == 1:
                                                player1.disappointed()
                                        
                                        print("The",Team2.name,"keeper returns to their position." ,"\n")
                                        time.sleep(1)
                                        
                                        print("Play resumes." ,"\n")
                                        time.sleep(1)
                                        


                        #Condition for player1 to score for TeamB
                        else:
                                
                                print(player1.name,"approaches the center diamond for a penalty shot." ,"\n")
                                engine.say(player1.name+"approaches the center diamond for a penalty shot.")
                                engine.runAndWait()
                                time.sleep(1)
                                
                                print(KeeperA.name,"clears the",Team1.name,"Ring." ,"\n")
                                time.sleep(1)
                                
                                print("The crowd roars in anticipation." ,"\n")
                                time.sleep(1)
                                
                                print("The",Team1.name,"Ring tilts to a horizontal position." ,"\n")
                                time.sleep(1)
                                
                                print(player1.name,"lines up their trajectory..." ,"\n")
                                time.sleep(1)
                                
                                print("...and launches the ball!" ,"\n")
                                time.sleep(1)
                                
                                print("(The",Team1.name,"keeper braces as they watch helplessly)" ,"\n")
                                commentary = ("The",Team1.name,"keeper braces as they watch helplessly.")
                                engine.say(commentary)
                                engine.runAndWait()
                                
                                time.sleep(1)
                                roll = dice_roll(20)
                

                                if player1.MAG+roll >= 24:
                                        ScoreB+=4
                                        
                                        print("🧿",player1.name,"scores 4 for the",Team2.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 4 for the",Team2.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                        
                                        
                                        roll = dice_roll(3)
                                        if roll == 3:
                                                if player1.team == Team1name:
                                                        hyped(Team1)
                                                if player1.team == Team2name:
                                                        hyped(Team2)
                                        time.sleep(1)
                                        player1.hyped()
                                        
                                elif player1.MAG+roll >= 20:
                                        ScoreB+=3
                                        
                                        print("🧿",player1.name,"scores 3 for the",Team2.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 3 for the",Team2.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                       
                                        
                                        
                                elif player1.MAG+roll >= 15:
                                        ScoreB+=2
                                        
                                        print("🧿",player1.name,"scores 2 for the",Team2.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 2 for the",Team2.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                      
                                        
                                        
                                elif player1.MAG+roll >= 10:
                                        ScoreB+=1
                                        
                                        print("🧿",player1.name,"scores 1 for the",Team2.name,"!" ,"\n")
                                        commentary = (player1.name,"scores 1 for the",Team2.name,"!")
                                        engine.say(commentary)
                                        engine.runAndWait()
                                        time.sleep(1)
                                        
                                        print(Team1.name, ": ",ScoreA ,"\n")
                                        engine.say(Team1.name)
                                        engine.say(ScoreA)
                                        engine.runAndWait()
                                        
                                        print(Team2.name, ": ",ScoreB ,"\n")
                                        engine.say(Team2.name)
                                        engine.say(ScoreB)
                                        engine.runAndWait()
                                     
                                        
                                        
                                else:
                                        
                                        print("An unfortunate miss." ,"\n")
                                        engine.say("An unfortunate miss.")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        disappointed = dice_roll(3)
                                        if disappointed == 1:
                                                player1.disappointed()
                                        
                                        print("The",Team1.name,"keeper returns to their position." ,"\n")
                                        time.sleep(1)
                                        
                                        print("Play resumes." ,"\n")
                                        time.sleep(1)
                
                #Series of checks for game loop
                
                def checks():
                        global FoulA
                        global FoulB
                        global TeamAPass
                        global TeamBPass
                        global ScoreB
                        global ScoreA
                        global Aruncount
                        global Bruncount
                        global newlist
                        global loopcount
                        global pos
                        global previous
                        global silence
                        global Player
                        global captainA
                        global captainB
                        
                        
                        #Checks length of newlist. If all players have appeared in text and have been added to newlist, starts a new round.
                        #Additionally, Players now look for loot at the beginning of each new round.
                        if len(newlist)>=10:
                                newlist=[]
                                getini()
                                #
                                #New round console check
                                #print("IT'S A NEW ROUND!" ,"\n")
                                time.sleep(1)
                                loot()

                        # Checks for players with 0 HP and removes them from the initiative ordering list (Ordered)
                        for player in Ordered:
                                if player[0].graveyard == True:
                                        if player[0].name not in newlist:
                                                newlist.append(player[0].name)

                                        Ordered.remove(player)


                        #Checks for team possession

                        if pos == ['TeamA']:
                                while player1.name not in TeamA:
                                                Ordered.pop()
                                                Ordered.insert(0,0,)
                                                return Ordered
                                pos = []
                        if pos == ['TeamB']:
                                while player1.name not in TeamB:
                                                Ordered.pop()
                                                Ordered.insert(0,0,)
                                                return Ordered
                                pos = []

                        #Checks for keeper to "make sure they stay in their ring" (don't appear in text making plays)
                                
                        if player1.keeper == True:
                                if player1.name not in newlist:
                                        newlist.append(player1.name)
                                Ordered.pop()
                                return Ordered
                        if player2.keeper == True:
                                if player2.name not in newlist:
                                        newlist.append(player2.name)
                                Ordered.pop()
                                return Ordered

                        #Ensures that players don't tackle other players on their team   

                        while player1.team == Team1name and player2.team == Team1name:
                                move = (len(Ordered)-1)
                                Ordered.pop(move)
                                return Ordered
                        #
                        
                        while player1.team == Team2name and player2.team == Team2name:
                                move = (len(Ordered)-1)
                                Ordered.pop(move)
                                return Ordered
                        #Conditions for tackles and fouls to occur


                        if player2.DMAG+dice_roll(20) > player1.WIS+dice_roll(20):

                                
                                print(player1.name,"gets tackled by",player2.name,"\n")
                                engine.say(player1.name+" gets tackled.")
                                engine.runAndWait()
                                time.sleep(1)
                                player1.takedmg()
                                time.sleep(1)
                                #if player2.DMAG+dice_roll(20) > player1.WIS+dice_roll(20):
                                item = []
                                q = dice_roll(100)
                                quality = ""
                                if q >=0 and q <=80:
                                        quality = "rusted"
                
                                if q >=81 and q <=95:
                                        quality = "old"
                                        
                                if q >=96 and q <=100:
                                        quality = "used"
                                item = quality+"item"
                                inv = player1.inv
                                if item in inv:
                                        inv.remove(item)
                                        inv2 = player2.inv
                                        print(player1.name+"'s inventory becomes lighter. ⏏️" ,"\n")
                                        #print(inv ,"\n")
                                        time.sleep(1)
                                        if item not in inv2:
                                                inv2.append(item)
                                        
                                        
                                        #print(inv2 ,"\n")
                                
                                                print(player2.name+"'s inventory becomes heavier. 💎" ,"\n")
                                                time.sleep(1) 

                                
                                print("Hard to believe the referee let them get away with that one..." ,"\n")
                                engine.say("The referee was looking away.")
                                engine.runAndWait()
                                time.sleep(1)
                                dice = dice_roll(8)
                                if dice == 8:
                                        fight(player1,player2)
                                if player2.name in TeamA:
                                        
                                        print(Team1.name,"have the ball!" ,"\n")
                                        engine.say(Team1.name+" have the ball!")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        pos=[]
                                        pos.append("TeamA")
                                        
                                
                                elif player2.name in TeamB:
                                        
                                        print(Team2.name,"have the ball!" ,"\n")
                                        engine.say(Team2.name+" have the ball!")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        pos=[]
                                        pos.append("TeamB")

                                elif player10.name in TeamA:
                                        
                                        print(Team1.name,"have the ball!" ,"\n")
                                        engine.say(Team1.name+" have the ball!")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        pos=[]
                                        pos.append("TeamA")
                                        
                                else:
                                        
                                        print(Team2.name,"have the ball!" ,"\n")
                                        engine.say(Team2.name+" have the ball!")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        pos=[]
                                        pos.append("TeamB")
                                time.sleep(1)
                                        
                        elif player2.STR+dice_roll(20) > player1.WIS+dice_roll(20): 
                                
                                print("* S M A S H *" ,"\n")
                                time.sleep(1)
                                
                                print("Some obvious roughing from",player2.name,"results in a foul." ,"\n")
                                engine.say("Some obvious roughing from"+player2.name)
                                engine.runAndWait()
                                engine.say("results in a foul.")
                                engine.runAndWait()
                                time.sleep(1)
                                player1.takedmg()
                                time.sleep(1)
                                if player2.name in TeamA:
                                        FoulA+=1
                                        
                                        #Foul console check
                                        print("🚩",Team1.name,"Fouls: ",FoulA ,"\n")
                                        engine.say(Team1.name+" fouls:")
                                        engine.runAndWait()
                                        engine.say(FoulA)
                                        engine.runAndWait()
                                        time.sleep(1)
                                else:
                                        FoulB+=1
                                        
                                        #Foul console check
                                        print("🚩",Team2.name,"Fouls: ",FoulB ,"\n")
                                        engine.say(Team2.name+" fouls:")
                                        engine.runAndWait()
                                        engine.say(FoulB)
                                        engine.runAndWait()
                                        time.sleep(1)
                                if FoulA==3:
                                        penalty()
                                        FoulA=0
                                if FoulB==3:
                                        penalty()
                                        FoulB=0

                        #Huge set of conditions for different passing outcomes
                        #This first set is a successful pass to a teammate.
                        #It's followed by a bunch of code that checks the team's pass counter, and if the team makes four 
                        #successful passes, the receiving Player of the fourth pass takes a shot.
                        #I should have made all of that into a function because I call it a lot, but I didn't and here we are.

                        if player1.STR+dice_roll(20) >= player2.STR+dice_roll(20): 
                                
                                print(player1.name,"gets the ball and launches it." ,"\n")
                                engine.say(player1.name+" gets the ball and launches it")
                                engine.runAndWait()
                                time.sleep(1)
                                if player3.DEX+dice_roll(20)>=10:
                                        
                                        print(thirdname+" receives!" ,"\n")
                                        engine.say(thirdname+" receives!")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        if player1.name in TeamA and player3.name in TeamA:
                                                TeamAPass+=1
                                                #Pass Count console check
                                                #print(Team1.name, "pass count = ",TeamAPass ,"\n")
                                                time.sleep(1)
                                                if TeamAPass == 4:
                                                        
                                                        print(player3.name,"makes a quick play!" ,"\n")
                                                        engine.say(player3.name+"makes a quick play!")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print("The",Team2.name,"keeper braces." ,"\n")
                                                        commentary = ("The",Team2.name,"keeper braces.")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperB.GK+kroll > player3.DEX+roll:
                                                                
                                                                print(KeeperB.name,"saves!" ,"\n")
                                                                engine.say(KeeperB.name+"saves!" )
                                                                engine.runAndWait()
                                                                TeamAPass=0
                                                                time.sleep(1)
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreA+=4
                                                                
                                                                print("🧿",player3.name,"scores 4 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 4 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                               
                                                                
                                                                TeamAPass=0
                                                                player3.hyped()
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreA+=3
                                                                
                                                                print("🧿",player3.name,"scores 3 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 3 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                                
                                                                
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreA+=2
                                                                
                                                                print("🧿",player3.name,"scores 2 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 2 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                               
                                                                
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreA+=1
                                                                
                                                                print("🧿",player3.name,"scores 1 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 1 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                                
                                                                
                                                                TeamAPass=0
                                                        else:
                                                                
                                                                print("The",Team2.name,"keeper blocks the shot!" ,"\n")
                                                                engine.say("The keeper blocks the shot")
                                                                engine.runAndWait()
                                                                TeamAPass=0
                                                                time.sleep(1)
                                                        
                                        elif player1.name in TeamB and player3.name in TeamB:
                                                
                                                TeamBPass+=1
                                                #Pass Count console check
                                                #print(Team2.name,"pass count = ",TeamBPass ,"\n")
                                                time.sleep(1)
                                                if TeamBPass == 4:
                                                        
                                                        print(player3.name,"sends it!" ,"\n")
                                                        engine.say(player3.name+"sends it!")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print("The",Team1.name,"keeper braces." ,"\n")
                                                        commentary = ("The",Team1.name,"keeper braces.")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                                
                                                                print(KeeperA.name,"saves!" ,"\n")
                                                                engine.say(KeeperA.name+"saves!" )
                                                                engine.runAndWait()
                                                                TeamBPass=0
                                                                time.sleep(1)        
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreB+=4
                                                                
                                                                print("🧿",player3.name,"scores 4 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 4 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                                
                                                                
                                                                TeamBPass=0
                                                                player3.hyped()
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreB+=3
                                                                
                                                                print("🧿",player3.name,"scores 3 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 3 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                               
                                                                
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreB+=2
                                                                
                                                                print("🧿",player3.name,"scores 2 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 2 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                                
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreB+=1
                                                                
                                                                print("🧿",player3.name,"scores 1 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 1 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                        
                                                                
                                                                TeamBPass=0
                                                        else:
                                                                
                                                                print("The",Team1.name,"keeper blocks the shot!" ,"\n")
                                                                engine.say("The keeper blocks the shot")
                                                                engine.runAndWait()
                                                                TeamBPass=0
                                                                time.sleep(1)

                                        #Interceptions occur when a pass happens and a player from the opposing team is in the receiving position
                                                        
                                        elif player1.name in TeamA and player3.name in TeamB:
                                                TeamBPass+=1
                                                
                                                print("A nice interception for the",Team2.name+"!" ,"\n")
                                                commentary = ("A nice interception for the",Team2.name+"!")
                                                engine.say(commentary)
                                                engine.runAndWait()
                                                time.sleep(1)
                                                #Pass Count console check
                                                #print(Team2.name," pass count = ",TeamBPass ,"\n")
                                                time.sleep(1)
                                                if TeamBPass == 4:
                                                        
                                                        print(player3.name,"takes a shot!" ,"\n")
                                                        engine.say(player3.name)
                                                        engine.runAndWait()
                                                        engine.say("takes a shot!")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print("The",Team1.name,"keeper braces." ,"\n")
                                                        commentary = ("The",Team1.name,"keeper braces.")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperA.GK+kroll > player3.DEX+roll:
                                                                
                                                                print(KeeperA.name,"saves!" ,"\n")
                                                                engine.say(KeeperA.name+"saves!" )
                                                                engine.runAndWait()
                                                                TeamBPass=0
                                                                time.sleep(1)
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreB+=4
                                                                
                                                                print("🧿",player3.name,"scores 4 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 4 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                               
                                                                
                                                                TeamBPass=0
                                                                player3.hyped()
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreB+=3
                                                                
                                                                print("🧿",player3.name,"scores 3 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 3 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                        
                                                                
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreB+=2
                                                                
                                                                print("🧿",player3.name,"scores 2 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 2 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                        
                                                                
                                                                TeamBPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreB+=1
                                                                
                                                                print("🧿",player3.name,"scores 1 for the",Team2.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 1 for the",Team2.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                        
                                                                
                                                                TeamBPass=0
                                                        else:
                                                                
                                                                print("The",Team1.name,"keeper blocks the shot!" ,"\n")
                                                                engine.say("The keeper blocks the shot")
                                                                engine.runAndWait()
                                                                TeamBPass=0
                                                                time.sleep(1)
                                        else:
                                                TeamAPass+=1
                                                
                                                print("A nice interception for the",Team1.name+"!" ,"\n")
                                                commentary = ("A nice interception for the",Team1.name+"!")
                                                engine.say(commentary)
                                                engine.runAndWait()
                                                time.sleep(1)
                                                #Pass count console check
                                                #print(Team1.name,"pass count = ",TeamAPass ,"\n")
                                                time.sleep(1)
                                                if TeamAPass == 4:
                                                        
                                                        print(player3.name,"takes a shot!" ,"\n")
                                                        engine.say(player3.name)
                                                        engine.runAndWait()
                                                        engine.say("takes a shot!")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print("The",Team2.name,"keeper braces." ,"\n")
                                                        commentary = ("The",Team2.name,"keeper braces.")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        roll = dice_roll(20)
                                                        kroll = dice_roll(20)
                                                        if KeeperB.GK+kroll > player3.DEX+roll:
                                                                
                                                                print(KeeperB.name,"saves!" ,"\n")
                                                                engine.say(KeeperB.name+"saves!" )
                                                                engine.runAndWait()
                                                                TeamAPass=0
                                                                time.sleep(1)
                                                        elif player3.DEX+roll >= 20:
                                                                ScoreA+=4
                                                                
                                                                print("🧿",player3.name,"scores 4 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 4 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                              
                                                                TeamAPass=0
                                                                player3.hyped()
                                                        elif player3.DEX+roll >= 15:
                                                                ScoreA+=3
                                                                
                                                                print("🧿",player3.name,"scores 3 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 3 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                                
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 12:
                                                                ScoreA+=2
                                                                
                                                                print("🧿",player3.name,"scores 2 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 2 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                             
                                                                
                                                                TeamAPass=0
                                                        elif player3.DEX+roll >= 10:
                                                                ScoreA+=1
                                                                
                                                                print("🧿",player3.name,"scores 1 for the",Team1.name,"!" ,"\n")
                                                                commentary = (player3.name,"scores 1 for the",Team1.name,"!")
                                                                engine.say(commentary)
                                                                engine.runAndWait()
                                                                time.sleep(1)
                                                                
                                                                print(Team1.name, ": ",ScoreA ,"\n")
                                                                engine.say(Team1.name)
                                                                engine.say(ScoreA)
                                                                engine.runAndWait()
                                                                
                                                                print(Team2.name, ": ",ScoreB ,"\n")
                                                                engine.say(Team2.name)
                                                                engine.say(ScoreB)
                                                                engine.runAndWait()
                                                        
                                                                
                                                                TeamAPass=0
                                                        else:
                                                                
                                                                print("The",Team2.name,"keeper blocks the shot!" ,"\n")
                                                                engine.say("The keeper blocks the shot")
                                                                engine.runAndWait()
                                                                TeamAPass=0
                                                                time.sleep(1)                              
                                
                                #If neither a successful pass nor interception occur, the ball is fumbled.

                                else:
                                        
                                        print(thirdname,"attempts a catch but fumbles the ball!" ,"\n")
                                        engine.say(thirdname+"Fumbles")
                                        engine.runAndWait()
                                        time.sleep(1)
                                        if (player4.name and player1.name in TeamA) or (player4.name and player1.name in TeamB):
                                                
                                                print(player4.name,"recovers the ball!" ,"\n")
                                                engine.say(player4.team+"recover the ball")
                                                engine.runAndWait()
                                                time.sleep(1)
                                                pos = []
                                                if player4.name in TeamA:
                                                        pos.append('TeamA')
                                                else:
                                                        pos.append('TeamB')

                                        else:
                                                
                                                print(player4.name,"grabs the live ball!" ,"\n")
                                                time.sleep(1)
                                                pos = []
                                                if player4.name in TeamA:
                                                        pos.append('TeamA')
                                                else:
                                                        pos.append('TeamB')

                                if player1.name not in newlist:
                                        newlist.append(player1.name)
                                if player2.name not in newlist:
                                        newlist.append(player2.name)
                                if player3.name not in newlist:
                                        newlist.append(player3.name)

                        #This condition occurs when Player 1 fails the strength test against Player 2
                        
                        else: 
                                silence += 1
                                
                                if silence == 4:
                                        print("A peculiar silence falls over the crowd." ,"\n")
                                        time.sleep(1)
                                if silence == 6:
                                        print("The silence is palpable." ,"\n")
                                        time.sleep(1)   
                                        
                                if silence == 8:
                                        print("It appears our captains are dispensing Knowledge to their teams. 📚" ,"\n")
                                        engine.say("It appears our captains are dispensing Knowledge to their teams.")
                                        engine.runAndWait()
                                        
                                        time.sleep(1)
                                        silence = 0
                                        die1=dice_roll(4)
                                        die2=dice_roll(4)
                                        Gifted = [PTeamA[die1],PTeamB[die2]]

                                        #Implementation of Captains. Could do more here if Captain attribute was actually assigned to a specific player on each team.

                                        for Player in Gifted:
                                                wheel = ["X",Player.STR,Player.DEX,Player.WIS,Player.CHA,Player.MAG,Player.DMAG]
                                                spin = dice_roll(6)
                                                if spin == 1:
                                                        Player.STR += 1
                                                        print(Player.name,"feels a rush of adrenaline! 🔺\n") 
                                                        engine.say(Player.name+" feels a rush of adrenaline!")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                if spin == 2:
                                                        Player.DEX += 1
                                                        print(Player.name,"is visibly psyched! 🔺" ,"\n")
                                                        engine.say(Player.name+" is visibly psyched!")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                if spin == 3:
                                                        Player.WIS += 1
                                                        print(Player.name, "takes notes. 🔺" ,"\n")
                                                        engine.say(Player.name+" takes notes.")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                if spin == 4:
                                                        Player.CHA += 1
                                                        print(Player.name+"'s spirit is content. 🔺" ,"\n")
                                                        engine.say(Player.name+"'s spirit is content.")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                if spin == 5:
                                                        Player.MAG += 1
                                                        print(Player.name, "has honed their craft. 🔺" ,"\n")
                                                        engine.say(Player.name+ " has honed their craft.")
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                if spin == 6:
                                                        Player.DMAG += 1
                                                        print(Player.name,"might use that knowledge to a nefarious end. 🔺" ,"\n")
                                                        engine.say(Player.name+" might use that knowledge to a nefarious end.")
                                                        engine.runAndWait()
                                                        time.sleep(1)

                                        print("The Players take to the Pit!" ,"\n")
                                        
                                        time.sleep(1)
                                        silence = 0
                               
                                gameloop()

                        #Sets up conditions for surprise shots on the opponent's ring
                        #When a team has a player in the first and second initiative position, they get a point
                        #When a team has three of these points, the player in the second position takes a surprise shot of opportunity

                        if player1.name in TeamA and player2.name in TeamA:
                                        if Aruncount==0:
                                                
                                                print(player1.name, "positions themselves for a shot on the",Team2.name,"Ring!" ,"\n")
                                                engine.say(player1.name+"positions themselves for a shot")
                                                engine.runAndWait()
                                                time.sleep(1)
                                                Aruncount+=1
                                        elif Aruncount==1:
                                                
                                                print("The",Team2.name,"look worried." ,"\n")
                                                time.sleep(1)
                                                Aruncount+=1
                                        elif Aruncount==2:
                                                
                                                print(Team2.name,"need to make a play to stop",player1.name,"!" ,"\n")
                                                time.sleep(1)
                                                Aruncount+=1
                                        else:
                                                time.sleep(1)
                                                # 
                                                # print("!A RUN TO THE MAX!" ,"\n")
                                                
                                                print(player2.name,"takes the ball and goes for the goal!" ,"\n")
                                                
                                                print("The",Team2.name,"keeper braces." ,"\n")
                                                commentary = ("The",Team2.name,"keeper braces.")
                                                engine.say(commentary)
                                                engine.runAndWait()
                                                time.sleep(1)
                                                roll = dice_roll(20)
                                                kroll = dice_roll(20)
                                                if KeeperB.GK+kroll > player2.DEX+roll:
                                                        
                                                        print(KeeperB.name,"saves!" ,"\n")
                                                        engine.say(KeeperB.name+"saves!" )
                                                        engine.runAndWait()
                                                        TeamAPass=0
                                                        time.sleep(1)
                                                elif player2.DEX+roll >= 20:
                                                        ScoreA+=4
                                                        
                                                        print("🧿",player2.name,"scores 4 for the",Team1.name,"!" ,"\n")
                                                        commentary =  (player2.name,"scores 4 for the",Team1.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                
                                                        
                                                        TeamAPass=0
                                                        player2.hyped()
                                                elif player2.DEX+roll >= 15:
                                                        ScoreA+=3
                                                        
                                                        print("🧿",player2.name,"scores 3 for the",Team1.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 3 for the",Team1.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                        
                                                        
                                                        TeamAPass=0
                                                elif player2.DEX+roll >= 12:
                                                        ScoreA+=2
                                                        
                                                        print("🧿",player2.name,"scores 2 for the",Team1.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 2 for the",Team1.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                        
                                                        
                                                        TeamAPass=0
                                                elif player2.DEX+roll >= 10:
                                                        ScoreA+=1
                                                        
                                                        print("🧿",player2.name,"scores 1 for the",Team1.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 1 for the",Team1.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                       
                                                        
                                                        TeamAPass=0
                                                else:
                                                        
                                                        print("The",Team2.name,"keeper blocks the shot!" ,"\n")
                                                        engine.say("The keeper blocks the shot")
                                                        engine.runAndWait()
                                                        TeamAPass=0
                                                        time.sleep(1)
                                                Aruncount=0
                        
                        
                        #Same code but for Team B        

                        elif player1.name in TeamB and player2.name in TeamB:
                                        if Bruncount==0:
                                                
                                                print(player1.name, "positions themselves for a shot on the",Team1.name,"Ring!" ,"\n")
                                                engine.say(player1.name+"positions themselves for a shot.")
                                                engine.runAndWait()
                                                time.sleep(1)
                                                Bruncount+=1
                                        elif Bruncount==1:
                                                
                                                print("The",Team1.name,"look worried." ,"\n")
                                                Bruncount+=1
                                        elif Bruncount==2:
                                                
                                                print(Team1.name,"need to make a play to stop",player1.name,"!" ,"\n")
                                                Bruncount+=1
                                        else:   
                                                time.sleep(1)
                                                # 
                                                # print("!B RUN TO THE MAX!" ,"\n")
                                                
                                                print(player2.name,"takes the ball and goes for the goal!" ,"\n")
                                                
                                                print("The",Team1.name,"keeper braces." ,"\n")
                                                commentary = ("The",Team1.name,"keeper braces.")
                                                engine.say(commentary)
                                                engine.runAndWait()
                                                time.sleep(1)
                                                roll = dice_roll(20)
                                                kroll = dice_roll(20)
                                                if KeeperA.GK+kroll > player2.DEX+roll:
                                                        
                                                        print(KeeperA.name,"saves!" ,"\n")
                                                        engine.say(KeeperA.name+"saves!" )
                                                        engine.runAndWait()
                                                        TeamBPass=0
                                                        time.sleep(1)        
                                                elif player2.DEX+roll >= 20:
                                                        ScoreB+=4
                                                        
                                                        print("🧿",player2.name,"scores 4 for the",Team2.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 4 for the",Team2.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                        
                                                        
                                                        TeamBPass=0
                                                        player2.hyped()
                                                elif player2.DEX+roll >= 15:
                                                        ScoreB+=3
                                                        
                                                        print("🧿",player2.name,"scores 3 for the",Team2.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 3 for the",Team2.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                        
                                                        
                                                        TeamBPass=0
                                                elif player2.DEX+roll >= 12:
                                                        ScoreB+=2
                                                        
                                                        print("🧿",player2.name,"scores 2 for the",Team2.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 2 for the",Team2.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                        
                                                        
                                                        TeamBPass=0
                                                elif player2.DEX+roll >= 10:
                                                        ScoreB+=1
                                                        
                                                        print("🧿",player2.name,"scores 1 for the",Team2.name,"!" ,"\n")
                                                        commentary = (player2.name,"scores 1 for the",Team2.name,"!")
                                                        engine.say(commentary)
                                                        engine.runAndWait()
                                                        time.sleep(1)
                                                        
                                                        print(Team1.name, ": ",ScoreA ,"\n")
                                                        engine.say(Team1.name)
                                                        engine.say(ScoreA)
                                                        engine.runAndWait()
                                                        
                                                        print(Team2.name, ": ",ScoreB ,"\n")
                                                        engine.say(Team2.name)
                                                        engine.say(ScoreB)
                                                        engine.runAndWait()
                                                      
                                                        TeamBPass=0
                                                else:
                                                        
                                                        print("The",Team1.name,"keeper blocks the shot!" ,"\n")
                                                        engine.say("The keeper blocks the shot")
                                                        engine.runAndWait()
                                                        TeamBPass=0
                                                        time.sleep(1)
                                                Bruncount=0
                                        
                        
                        
                

                        #Ensures players that appeared in this text loop are counted as having taken a turn (moved to newlist)

                        if player1.name not in newlist:
                                newlist.append(player1.name)
                        if player2.name not in newlist:
                                newlist.append(player2.name)
                        if player3.name not in newlist:
                                newlist.append(player3.name) 

                        current_time = time.time()
                        elapsed_time = current_time - start_time
                        
                        time.sleep(1)
                
                checks()

                #Sets scores to current scores before looping again        
                ScoreA=ScoreA
                ScoreB=ScoreB         

        #Creates loop that calls gameloop() for x amount of seconds and prints the final score when game time runs out
        game = True
        this=False
        half=True
        
        while game == True:
                half=False
                current_time = time.time()
                elapsed_time = current_time - start_time

                if seconds-elapsed_time >= 0:
                        if elapsed_time < seconds-elapsed_time:
                                last = round(seconds-elapsed_time)
                                if round(seconds-elapsed_time) != round(last):
                                        
                                        print(round(seconds-elapsed_time) ,"\n")

                # HALF TIME! HALF TIME! HALF TIME! (This makes Half Time work)

                if elapsed_time >= 580 and elapsed_time <= 620:
                        half=True


                while half==True:
                        tipoff = True
                        
                        print("IT'S HALFTIME!" ,"\n")
                        engine.say("It's Half Time!")
                        engine.runAndWait()
                        time.sleep(1)
                        count=15
                        while half == True:
                                
                                time.sleep(1)
                                
                                print(count ,"\n")
                                count-=1
                                time.sleep(1)

                                if count <= 5 and count > 0:
                                        engine.say(count)
                                        engine.runAndWait() 
                                
                                print("HALF!" ,"\n")
                                time.sleep(1)
                                
                                print(count ,"\n")
                                time.sleep(1)
                                count-=1

                                if count <= 5 and count > 0:
                                        engine.say(count)
                                        engine.runAndWait() 
                                
                                print("TIME!" ,"\n")
                                time.sleep(1)

                                
                                

                                if count <= 0:
                                        half=False

                                        # captain = captainA
                                        # sustaincaptainA = True
                                        # for player in PTeamA:
                                                
                                        #         if int(player.CHA) > int(captain.CHA) and int(player.MAG) >= int(captain.MAG):

                                        #                 if player.name == captain.name:
                                                                
                                        #                         print("No new captain takes the",Team1.name,"helm today!" ,"\n")
                                        #                         time.sleep(1)
                                                                
                                        #                         print(captain.name,"remains your team captain." ,"\n")
                                        #                         sustaincaptainA = True
                                        #                 else:
                                        #                         sustaincaptainA = False
                                        #                         print("It appears there has been a coup in the",Team1name,"locker room during Half Time... 🤼" ,"\n")
                                        #                         time.sleep(1)
                                                
                                        #                         print(captainA.name,"is your new",Team1name,"captain." ,"\n")
                                        #                 samecaptA = False

                                        #                 #Coup console check for Team A
                                        #                 #print(player.name ,"\n")

                                        # if sustaincaptainA == False:
                                        #         captain.captain = False
                                        #         captain = player
                                        #         player.captain = True
                                                
                                                
                                        # else:
                                        #         hyped(Team1)
                                        # print("We'll see how they fare in the second half." ,"\n")

                                        # time.sleep(1)

                                        # for player in PTeamB:
                                        #         sustaincaptainB = True
                                        #         captain = captainB
                                        #         if int(player.CHA) > int(captain.CHA) and int(player.MAG) >= int(captain.MAG):

                                        #                 if player.name == captain.name:
                                                                
                                        #                         print("No new captain takes the",Team1.name,"helm today!" ,"\n")
                                        #                         time.sleep(1)
                                                                
                                        #                         print(captain.name,"remains your team captain." ,"\n")
                                        #                         sustaincaptainB = True
                                        #                 else:
                                        #                         sustaincaptainB = False


                                        #                 #Coup console check for Team B
                                        #                 #print(player.name ,"\n")

                                        #         if sustaincaptainB == False:
                                        #                 captain.captain = False
                                        #                 captain = player
                                        #                 player.captain = True
                                                
                                        #         print("It appears there has been a coup in the",Team1name,"locker room during Half Time... 🤼" ,"\n")
                                        #         time.sleep(1)
                                                
                                        #         print(captainB.name,"is your new",Team1name,"captain." ,"\n")
                                        #         samecaptB = False
                                        # else:
                                        #         samecaptB = True
                                        # if samecaptB == True:
                                        #         hyped(Team2)
                                        # print("We'll see how they fare in the second half." ,"\n")
                                        if ScoreA >= (ScoreB+3):
                                            engine.say(Team1name+" get hyped")
                                            engine.runAndWait()
                                            hyped(Team1)

                                        if ScoreB >= (ScoreA+3):
                                            engine.say(Team2name+" get hyped")
                                            engine.runAndWait()
                                            hyped(Team2)

                                        time.sleep(1)
                                        
                                        tipoff = True
                                        struggle()

                                        gameloop()      
                                                        

                #print("."*100,"[",round(seconds-elapsed_time),"]","\n")
                gameloop()

                
                #Prints score and winning team at the end of the game time. Counts 30 seconds and then starts a new game.

                if elapsed_time>seconds:
                        
                        print("The Game has ended." ,"\n")
                        def gettcountA():
                                tcountA = []
                                return tcountA
                        tcountA = 0
                        tcountB = 0
                        for player in PTeamA:
                                gettcountA()
                                if player.HP > 0:
                                        tcountA += 1
                                        
                        if tcountA == 5:
                                ScoreA += 1
                                print(Team1name,"are awarded an additional point for their determination! \n")
                                engine.say(Team1name+"receive a determination point.")
                                time.sleep(1)
                                

                        def gettcountB():
                                tcountB = []
                                return tcountB

                        for player in PTeamB:
                                gettcountB()
                                if player.HP > 0:
                                        tcountB += 1
                                        
                        if tcountB == 5:
                                ScoreB += 1
                                print(Team2name,"are awarded an additional point for their determination! \n")
                                engine.say(Team2name+"receive a determination point.")
                                engine.runAndWait()
                                time.sleep(1)
                            
                        
                        print(Team1.name,": ",ScoreA ,"\n")
                        engine.say(Team1.name)
                        engine.runAndWait()
                        engine.say(ScoreA)
                        engine.runAndWait()

                        print(Team2.name,": ",ScoreB ,"\n")
                        engine.say(Team2.name)
                        engine.runAndWait()
                        engine.say(ScoreB)
                        engine.runAndWait()

                        if ScoreA>ScoreB:
                                
                                print(Team1.name,"win the Game." ,"\n")
                                engine.say(Team1.name+"win the Game.")
                                engine.runAndWait()
                        elif ScoreA<ScoreB:
                                
                                print(Team2.name,"win the Game." ,"\n")
                                engine.say(Team2.name+"win the Game.")
                                engine.runAndWait()
                        else:
                                
                                print("The Game ends in a tie." ,"\n")
                                engine.say("The Game ends in a tie.")
                                engine.runAndWait()

                        game = False
                        count = 30
                        this=True   
                while this == True:
                        time.sleep(1)
                        count = count-1
                        
                        print(count ,"\n")
                        if count <=5 and count > 0:
                                engine.say(count)
                                engine.runAndWait()
                        if count <= 0:
                                
                                
                                time.sleep(1)
                                this =False
                                seconds = 1200
                                game = False

        

        



