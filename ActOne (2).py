#Importing modules to be used in this file.
import time
import random
from ASCIIArt import *
from QuickTime import time_event

#Function for printing text slowly. Used later.
def slow_write(text, delay=0.03):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(delay)
  print()

#Defining ActOne in order to reference and use it in program.py.
def ActOne(player_name):
  #Loop used in order to restart game from beginning of Act One if player chooses so.
  while True:
    #Imports defined ASCII art from ASCIIArt.py
    print(vale_banner())
    time.sleep(2)
    #ASCII art builds on the atmosphere and tone of the game.
    print(ActOne_banner())
    #Use of quote builds atmosphere, tone as well as hint to the events of the story.
    print("""'As you come into this world, something else is also born.
  You begin your life, and it begins a journey towards you. It moves slowly, but it never stops.
  Wherever you go, whatever path you take, it will follow - never faster, never slower, always coming.
  You will run; it will walk. You will rest; it will not.
  One day you will linger in the same place for too long; you will sit too still or sleep too deep.
  And when, too late, you rise to go, you will notice a second shadow next to yours.
  Your life will then be over.'
  - The Doctor, Doctor Who""")
    
    #Slow_write used to give the text a nice typing effect.
    slow_write("Humanity has been at war for eons. War with aliens, beasts, beings of unfathomable power.")
    #Code uses player_name in order to reference inputted name from the beginning of the game.
    slow_write(f"Yet you, {player_name}, live on the outer planets, with the same lack of peace.")
    slow_write("You wake up to the sound of your doorbell ringing.")
    #Uses numbers in front of choices to select that choice in input.
    time.sleep(1)
    print("1. Check the door.")
    door = input("> ")
    
    #Choices can lead to different circumstances which can change how a situation plays out or even what ending you get.
    while door not in ['1']:
      print("Invalid option. Please select a valid option.")
      door = input("> ")
      
    if door=='1':
      slow_write("You go up to the front door and open it to find a middle-aged man staring at you.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    
    slow_write(f"{player_name}, it has been too long!")
    #player_name.upper() capitilises all the letters in player_name
    slow_write(f"{player_name.upper()}: Is that THE Victor?")
    slow_write("VICTOR: I'm sorry to intrude so early into your daily cycle, but I'm afraid I need your help.")
    #Utilisation of time.sleep allows for extra reading time and builds on the atmosphere.
    time.sleep(1)
    print("1. What is it?")
    print("2. Punch Victor in the face.")
    victor = input("> ")
    
    #This type of error handling comes in two parts. This is the first part which says if the choice is not '1' or '2', then it will be invalid.
    while victor not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      victor = input("> ")

    if victor=='1':
      slow_write(f"{player_name.upper()}: What do you want Victor?")
    elif victor=='2':
      slow_write("You raise your fist and launch it at Victor.")
      #time_event() is utilised multiple times in story files to add quick time event mechanics to the game to enhance gameplay.
      punch_victor = time_event()

      if punch_victor:
        slow_write("You managed to hit Victor straight in the face, sending him hurtling down your shack's steps.")
        slow_write("Victor stands up and returns to the front door as if nothing happened.")
        slow_write("VICTOR: You still hit hard.")
      else:
        slow_write("You tried to punch Victor but he moves his head out of the way before returning the strike.")
        slow_write("VICTOR: Guess you got rusty.")
      victor = input("> ")
    #Continues in the loop from the first part to handle any invalid inputs. This system is used for every other choice in the game.
    else:
      print("Invalid input. Please select from valid options.")
      continue
      

    slow_write("""VICTOR: I need to ask you for a favour.
As you know, I'm getting up there in age now so I can't do this job.""")
    time.sleep(1)
    print("1. What's the job?")
    print("2. What is it that you do again?")
    victor_2 = input("> ")
    
    
    while victor_2 not in ['1', '2']:
      print("Invalid input. Please select from valid inputs.")
      victor = ("> ")
      
    if victor_2=='1':
      slow_write("VICTOR: I need you to escort a woman for me.")
    elif victor_2=='2':
      slow_write("VICTOR: Mercenary, bounty hunter, gun for hire... All of that. It's the best that someone as old as me can accomplish.")
      victor_2 = input("> ")
    else:
      print("Invalid input. Please select from valid options.")
      continue
    slow_write("VICTOR: She's ex-militarum, but she wants to get to Lassos One.")
    slow_write(f"{player_name.upper()}: What's the bounty on her?")
    slow_write("VICTOR: 100 million credits.")
    time.sleep(1)
    print("1. I'll do it.")
    print("2. That's almost suicide.")
    accept = input("> ")

    while accept not in ['1', '2']:
      print("Invalid option. Please select fromv valid options.")
      accept = input("> ")
      
    if accept=='1':
      slow_write("""VICTOR: I feel like you're a bit softer than you used to be when we fought together.
Not that I'm complaining. You can find her further up where the village is. A ship will be waiting there to pick you up.""")
    elif accept=='2':
      slow_write(f"VICTOR: Please {player_name}, you're the only one who would do this.")
      time.sleep(1)
      print("1. Fine, I'll do it.")
      print("2. No.")
      beg = input("> ")
      
      while beg not in ['1', '2']:
        print("Invalid option. Please select valid option.")
      if beg=='1':
        slow_write("VICTOR: Thank goodness, I knew that you had a soft spot in you.")
      elif beg=='2':
        slow_write("VICTOR: I see. Sorry to bother you.")
        slow_write("Victor walks away and you close the door behind him.")
        slow_write("You return to your normal daily cycles of spending time in this little hut at the end of the universe.")
        slow_write("Years past, but they all seem like days to you.")
        slow_write("All the information you receive from the outside world is from online news.")
        slow_write("During these times, media outlets always break down, with those truthful few being the only ones remaining.")
        slow_write("It's always the same. The cycle always continues.")
        slow_write("The universe always ends no matter what you do.")
        slow_write("ENDING: The Cycle")
        time.sleep(2)
        #Each ending in the game has its own ASCII art.
        print(TheCycleEnding_banner())
        time.sleep(1)
        #Restart system to restart game from the beginning of the act.
        print("1. Restart from Act One.")
        print("2. Exit the game.")
        restart_option = input("> ")
        
        while restart_option not in ['1', '2']:
          print("Invalid option. Please select a valid option.")
          restart_option = input("> ")
          
        if restart_option=='1':
          continue
        elif restart_option=='2':
          exit()
        else:
          print("Invalid option. Please select a valid option.")
          continue
      else:
        print("Invalid option. Please select a valid option.")
        continue
    print("1. Where are you going to go?")
    print("2. What does the ship look like?")
    victor_question = input("> ")

    while victor_question not in ['1', '2']:
      print("Invalid option. Please select valid option.")
      victor_question = input("> ")
      
    if victor_question=='1':
      slow_write("VICTOR: I'll return to one of the Conclave planets, see if I can lay low for a while.")
    elif victor_question=='2':
      slow_write("VICTOR: It's one of the Hummingbirds. An older model, sure, but it'll get you pretty far undetected.")
      slow_write(f"{player_name.upper()}: Good.")
      victor_question = input("> ")
    else:
      print("Invalid option. Please select from valid options.")
      continue
    slow_write("VICTOR: Well I'd wish you good luck but... You don't even need it anyway.")
    slow_write("Victor waves his hand as he leaves for the rocky footpath ahead.")
    time.sleep(2)
    slow_write("SOME TIME LATER...")
    slow_write("You arrive at the local village where indeed, a Hummingbird was waiting.")
    time.sleep(1)
    print("1. Explore the village.")
    print("2. Examine the Hummingbird.")
    village_or_hummingbird = input("> ")

    while village_or_hummingbird not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      village_or_hummingbird = input("> ")
      
    if village_or_hummingbird=='1':
      slow_write("You go into the village.")
    elif village_or_hummingbird=='2':
      slow_write("You go up to the Hummingbird ship.")
      slow_write("It had a sleek, black design, with bug-like wings attached to the side, drooping off slighty.")
      slow_write("However, there was definitely some age to it. A bit of rust, a few loose nails. A constantly humming engine.")
      slow_write("After examination, you enter the village.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("It was small, with a few stalls set up.")
    slow_write("With this being a planet so far from Terra, it didn't get any supplies whatsoever.")
    slow_write("A perfect hiding place for someboy like the woman or you.")
    slow_write("With everybody wearing rags and covered in dirt, it was easy to spot the woman.")
    print("1. Are you who I'm supposed to escort?")
    print("2. Well, I expected somebody different.")
    woman = input("> ")

    while woman not in ['1', '2']:
      slow_write("UNKNOWN: Didn't quite hear you there. (Please select a valid option).")
      woman = input("> ")
    if woman=='1':
      slow_write("UNKNOWN: Depends who's asking.")
      slow_write(f"{player_name.upper()}: I was sent by Victor.")
    elif woman=='2':
      slow_write("UNKNOWN: What's that supposed to mean?")
      slow_write(f"{player_name.upper()}: Didn't expect a soldier.")
      slow_write("UNKNOWN: Ex-soldier.")
    else:
      slow_write("UNKNOWN: Didn't quite hear you there. (Please select a valid option).")
      continue
    slow_write("LAS: I'm Las Harkers. Nice to meet you. Nice to meet you.")
    slow_write("Las stretches out her hand.")
    print("1. Shake her hand.")
    print("2. Slap her hand away.")
    handshake = input("> ")

    while handshake not in ['1', '2']:
      slow_write("LAS: You gonna shake my hand or anything? {Please select a valid option.")
      handshake = input("> ")
      
    if handshake=='1':
      slow_write(f"{player_name.upper()}: Nice to meet you, I'm {player_name}.")
    elif handshake=='2':
      slow_write("LAS: Hey! What was that for?")
      slow_write(f"{player_name.upper()}: Don't like the look of of you.")
      slow_write("LAS: Excuse me?")
      slow_write(f"{player_name.upper()}: Anyways we're getting side-tracked.")
    else:
      slow_write("LAS: You gonna shake my hand or anything? (Please select a valid option.)")
      continue
    slow_write(f"{player_name.upper()}: So you want to make it back to Lassos One.")
    time.sleep(1)
    print("1. Then let's go then.")
    print("2. Why?")
    las = input("> ")

    while las not in ['1', '2']:
      print("Invalid input. Please select a valid option.")
      las = input("> ")
      
    if las=='1':
      slow_write("You try to turn around but you feel the barrel of a gun pointed at your head.")
    elif las=='2':
      slow_write(f"{player_name.upper()}: Can I ask why?")
      slow_write("LAS: Personal reasons.")
      las = input("> ")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("UNKNOWN: Turn around and I'll blow your head off. Now, you listen to what I say. Hand the girl over and we can be all good.")
    time.sleep(1)
    print("1. Hand over Las.")
    print("2. Tell Las to run.")
    head = input("> ")

    while head not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      head = input("> ")
      
    if head=='1':
        slow_write(f"{player_name.upper()}: Sure, I don't mind. Take her and leave me alone.")
        slow_write("LAS: What?")
        slow_write("Two other men emerge from the shadows and grab her from behind. They begin to drag her away while she screams.")
        slow_write("The townsfolks' only reaction are their stares.")
        slow_write("UNKNOWN: A pleasure.")
        slow_write("The unknown man leaves, returning to the shadows.")
        slow_write("You make your way back to the hut and lie down on your bed, trying to make up for lost sleep.")
        slow_write("You return to your normal daily cycles of spending time in this little hut at the end of the universe.")
        slow_write("Years past, but they all seem like days to you.")
        slow_write("All the information you receive from the outside world is from online news.")
        slow_write("During these times, media outlets always break down, with those truthful few being the only ones remaining.")
        slow_write("It's always the same. The cycle always continues.")
        slow_write("The universe always ends no matter what you do.")
        slow_write("ENDING: The Cycle")
        time.sleep(2)
        print(TheCycleEnding_banner())
        time.sleep(1)
        print("1. Restart from Act One.")
        print("2. Exit the game.")
        restart_option_2 = input("> ")
          
        while restart_option_2 not in ['1', '2']:
          print("Invalid option. Please select a valid option.")
          restart_option_2 = input("> ")
          
        if restart_option_2=='1':
          continue
        elif restart_option_2=='2':
          exit()
        else:
          print("Invalid option. Please select a valid option.")
          continue
    if head=='2':
        slow_write(f"{player_name.upper()}: RUN LAS!")
        slow_write("Las begins to sprint as the man behind you pulls the trigger, sending a bullet straight through your head.")
        slow_write("You collapse on the ground, blood pouring out.")
        slow_write("However, all it takes from you is a bit of effort for you to stand back up.")
        slow_write("The man still has his gun pointed at you, but now you're facing right down the barrel.")
        slow_write("You try to disarm him.")
        disarm = time_event()

        if disarm:
          slow_write("You manage to charge at the man and disarm him, you now pointing the gun at him.")
        else:
          slow_write("The man dodges to the side and empties the entire mag in you.")
          slow_write("You collapse on the ground, blood pouring out from all the holes in your body.")
          slow_write("This time though, you could feel your consciousness begin to fade.")
          slow_write("At least this time, you would have some peace.")
          slow_write("ENDING: Death in Heaven")
          time.sleep(1)
          print("1. Restart from Act One.")
          print("2. Exit the game.")
          restart_option_3 = input("> ")
          
          while restart_option_3 not in ['1', '2']:
            print("Invalid option. Please select from valid options.")
            restart_option_3 = input("> ")
            
          if restart_option_3=='1':
            continue
          elif restart_option_3=='2':
            exit()
          else:
            print("Invalid option. Please select from valid options.")
            continue
        time.sleep(1)
        print("1. Shoot.")
        print("2. Spare.")
        shoot_or_spare = input("> ")

        while shoot_or_spare not in ['1', '2']:
          print("Invalid option. Please select a valid option.")
          shoot_or_spare = input("> ")
          
        if shoot_or_spare=='1':
          slow_write("You shoot the man between his eyebrows with deadeye accuracy. He collapses on the floor.")
        elif shoot_or_spare=='2':
          slow_write(f"{player_name.upper()}: Run off, before I change my mind.")
          slow_write("The man begins to sprint the other way.")
        else:
          print("Invalid option. Please select a valid option.")
          continue
    else:
      print("Invalid option. Please select from valid options.")
      continue
    slow_write(f"{player_name.upper()}: LAS! Where are you?")
    slow_write("LAS: Over here.")
    slow_write(f"{player_name.upper()}: Good, we need to get to the Hummingbird now.")
    slow_write("You begin to sprint towards the Hummingbird, the enemy's pistol in your hand.")
    slow_write("You realise that two other mercenaries are chasing you.")
    time.sleep(1)
    print("1. Run for the Hummingbird.")
    print("2. Stay and fight.")
    run_or_stay = input("> ")

    while run_or_stay not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      run_or_stay = input("> ")
      
    if run_or_stay=='1':
      slow_write("You and Las continue to sprint for the Hummingbird.")
      slow_write("The two mercenaries begin to shoot at you, but you manage to dodge all the rounds until you reach the grassy plain where the Hummingbird is.")
      slow_write(f"{player_name.upper}: Get inside!")
    elif run_or_stay=='2':
      slow_write(f"{player_name.upper}: Get to the Hummingbird. I'll fight them off.")
      slow_write("LAS: But you'll die!")
      slow_write(f"{player_name.upper}: Let's just say I don't die easily.")
      slow_write("The two mercenaries stand in front of you, each with a plasma pistol pointed at you.")
      time.sleep(1)
      print("1. Shoot them.")
      print("2. Intimidate them.")
      shoot_or_intimidate = input("> ")

      while shoot_or_intimidate not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        shoot_or_intimidate = input("> ")
        
      if shoot_or_intimidate=='1':
        slow_write("You try to shoot at both of them before they can react.")
        double = time_event()

        if double:
          slow_write("You manage to hit both of them in their vital organs. They both collapse in pain, clutching their wounds and crying.")
          slow_write(f"{player_name.upper}: Guess my standard for mercenaries is too high.")
        else:
          slow_write("You try to shoot them only to hit one of them in the arm. However, the other manages to get one shot at you.")
          slow_write("It hits your heart. You begin to feel your body regenerating, trying to fix it, but the mercenary shoots you again.")
          slow_write("You collapse on the ground, blood pouring out from all the holes in your body.")
          slow_write("At least this time, you would have some peace.")
          slow_write("ENDING: Death in Heaven")
          time.sleep(2)
          print(DeathInHeavenEnding_banner())
          time.sleep(1)
          print("1. Restart from Act One.")
          print("2. Exit the game.")
          restart_option_4 = input("> ")

          while restart_option_4 not in ['1', '2']:
            print("Invalid option. Please select a valid option.")
            restart_option_4 = input("> ")
            
          if restart_option_4=='1':
            continue
          elif restart_option_4=='2':
            exit()
          else:
            print("Invalid option. Please select a valid option.")
            continue
            
      elif shoot_or_intimidate=='2':
        slow_write(f"""{player_name.upper()}: You have tried to hunt down this innocent woman and that is something that I'm not gonna let pass.
This was a decent plan, if only you didn't forget about one big mistake facing right at you.""")
        slow_write("MERCENARY: And what would that be?")
        slow_write(f"""{player_name.upper()}: Didn't anyone tell you? There is one thing you do not forget in a fight, if you're smart,
if you value your continued existence. If you have any plans of seeing tomorrow then there is one thing that you never, ever forget:
The Immortal.""")
        slow_write("The two mercenaries look at you skeptically, but you face them with eyes that pierced their souls.")
        slow_write("The mercenaries dropped their weapons and began to run away.")
        slow_write(f"{player_name.upper()}: Humans are so easy to control.")
        slow_write("You return to the Hummingbird and enter it. Las was already inside, sitting in the pilot's seat.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write(f"{player_name.upper()}: You know how to fly this thing?!")
    slow_write("LAS: Absolutely!")
    slow_write("The Hummingbird's wings begin to flap as the ship leaves the ground.")
    slow_write("However, a ship comes flying through the atmosphere, looking to ground you.")
    slow_write("LAS: Arm the guns!")
    time.sleep(1)
    print("1. Sure!")
    print("2. You don't tell me what to do.")
    air_guns = input("> ")

    while air_guns not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      air_guns = input("> ")
      
    if air_guns=='1':
      slow_write("You enter the seat and begin to tap away at the console controlling the Hummingbird's guns.")
    elif air_guns=='2':
      slow_write("LAS: Just do it please.")
      slow_write("You begrudgingly enter the seat and begin to tap away at the console controlling the Hummingbird's guns.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("The Hummingbird begins to whizz around as the other ship, a sleek, small jet begins to chase you.")
    slow_write("You try to aim your weapons and shoot it down.")
    air_fight = time_event()

    if air_fight:
      slow_write("You shoot the wings of the jet with extreme accuracy and it crashes into the ground below.")
      slow_write("Las steers the ship upwards, exiting the atmosphere or Eragrost VI.")
      #This is the end of Act One and if the player survives, 'survived' will be returned to see if they continue to the next act.
      return 'survived'
    else:
      slow_write("You try to hit the jet but miss all of your shots. Meanwhile, the jet launches two missiles at you. Blowing up the wings of your ship.")
      slow_write("You crash down only to be met by the dirt of the ground.")
      slow_write("At least this time, you would have some peace.")
      slow_write("ENDING: Death in Heaven")
      time.sleep(2)
      print(DeathInHeavenEnding_banner())
      time.sleep(1)
      print("1. Restart from Act One.")
      print("2. Exit")
      restart_option_5 = input("> ")
      
      while restart_option_5 not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        restart_option_5 = input("> ")
        
      if restart_option_5=='1':
        continue
      elif restart_option_5=='2':
        exit()
      else:
        print("Invalid option. Please select a valid option.")
        continue

          
        
              
        
      
     
  
