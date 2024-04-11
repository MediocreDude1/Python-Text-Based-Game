#Imports all modules needed including ActOne to continue on the game in chronological order.
import time
import random
from ActOne import *
from ASCIIArt import *
from QuickTime import time_event

#Function for printing text slowly. Used later.
def slow_write(text, delay=0.03):
  for char in text:
    print(char, end='', flush=True)
    time.sleep(delay)
  print()
  
#Defines ActTwo to be referenced in the program.py file. 
def ActTwo(player_name):
  while True:
    print(ActTwo_banner())
    slow_write("Las puts the ship on auto-pilot and exits the pilot's seat.")
    slow_write("She then sits next to you.")
    slow_write("LAS: You were pretty good with the guns back there, better than me for sure.")
    time.sleep(1)
    print("1. I used to serve.")
    print("2. Pure luck.")
    good_guns = input("> ")

    while good_guns not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      good_guns = input("> ")
      
    if good_guns=='1':
      slow_write("LAS: For the Militarum? How long ago was that?")
      slow_write(f"{player_name.upper()}: A very, very long time ago. Did for a bit of fun.")
      slow_write("LAS: I did something similar as well. Joined the Militarum to see the universe.")
      slow_write(f"{player_name.upper()}: It everything you expected?")
      slow_write("LAS: That and more.")
    elif good_guns=='2':
      slow_write("LAS: Seems hard to believe. You seem to have some sort of military training but I won't press about it.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
      
    time.sleep(1)
    print("1. Why did you leave the Militarum?")
    print("2. What was your first mission like?")
    las_life = input("> ")

    while las_life not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      las_life = input("> ")
      
    if las_life=='1':
      slow_write("""LAS: When I was originally serving, we were only ever after Synthetics. My unit at least.
But... Things have gotten worse on the Inner Planets and... They wanted me to kill someone.""")
      slow_write(f"{player_name.upper()}: But you didn't.")
      slow_write("LAS: Nope.")
    elif las_life=='2':
      slow_write("""LAS: It wasn't very much. There was a Synth unit hiding in a base on... Gidrran I believe.
Pretty anticlimatic but it was my first time on another world besides Lassos One and Terra.""")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    time.sleep(1)
    print("1. You know, you remind me of someone I used to know.")
    memory = input("> ")
    
    while memory not in ['1']:
      print("Invalid option. Please select a valid option.")
      memory = input("> ")
      
    if memory=='1':
      slow_write("LAS: Who?")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("My details are a bit hazy but all I remember was that she was nice like you. A good person.")
    slow_write("LAS: ... I see.")
    slow_write("The Hummingbird continued to soar through empty space before it arrived at a checkpoint planet known as Solshioc I.")
    slow_write("LAS: Could you handle the pilot stuff. If I get caught...")
    slow_write(f"{player_name.upper()}: Yep, I got it.")
    slow_write("A voice patched through the mic system in the Hummingbird.")
    slow_write("UNKNOWN: Hello, you are now entering Conclave space. Please identify yourself.")
    time.sleep(1)
    print(f"1. {player_name}.")
    print("2. Victor Pauci.")
    solschioc = input("> ")
    
    while solschioc not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      solschioc = input("> ")
      
    if solschioc=='1':
      slow_write(f"UNKNOWN: We have no record of you {player_name}. This your first time in Conclave space.")
      slow_write(f"{player_name.upper}: Yes, I live in the Outer Planets. Business here is to meet with an old friend.")
      slow_write(f"UNKNOWN: Copy that. You are clear for landing {player_name}.")
      slow_write("You land at Dock 41 and walk out.")
      slow_write("LAS: Can't even get fresh air with this helmet on.")
      time.sleep(1)
      print("1. I would prefer it with fresh air.")
      print("2. I prefer wearing helmets then choking.")
      air = input("> ")
      
      while air not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        air = input("> ")
        
      if air=='1':
        slow_write("LAS: Glad we're on the same page.")
      elif air=='2':
        slow_write("LAS: You're no fun at all.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      slow_write("The two of you walk into the city, a bustling one with neon signs and towering buildings everywhere. However, the dust flying around doesn't help with vision.")
      slow_write(f"{player_name.upper()}: It's been a while since I've been here. The buildings are taller and the advertisements are bigger.")
      slow_write("LAS: That's what you get with the power of two Suns.")
      slow_write("Even through all the dust, you could tell that this city was slowly decaying. Many were on the streets and many more had to work measely hours to feed themselves.")
      slow_write("LAS: I didn't know it was this bad out here.")
      time.sleep(1)
      print("1. Other planets are better.")
      print("2. This is how things are in the Conclave.")
      state = input("> ")
      
      while state not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        state = input("> ")
        
      if state=='1':
        slow_write("LAS: I would hope so, this is horrible.")
      elif state=='2':
        slow_write("LAS: I know that it not everything was right but... If it's like this everywhere, then it gives me more reason to keep running.")
        time.sleep(1)
        print("1. (Ignore)")
        print("2. What do you mean by that?")
        run = input("> ")
        
        while run not in ['1', '2']:
          print("Invalid option. Please select a valid option.")
          run = input("> ")
          
        if run=='1':
          slow_write("You ignore her statement and continue to wander about the city.")
        elif run=='2':
          slow_write("LAS: You don't need to know.")
        else:
          print("Invalid option. Please select a valid option.")
          continue
      else:
        print("Invalid option. Please select a valid option.")
        continue
      
      slow_write(f"{player_name.upper()}: Why did you even want to come here in the first place? We could've just flown through the relay.")
      slow_write("LAS: To see an old friend.")
      slow_write(f"{player_name.upper()}: Right, well...")
      time.sleep(2)
      print("BOOM!")
      time.sleep(1)
      slow_write("LAS: What was that?")
      slow_write(f"{player_name.upper()}: Sounds like the relay... Shutting down?")
      slow_write("LAS: Why would they do that?")
      slow_write(f"{player_name.upper()}: They shouldn't unless there was a giant armada coming through the other side.")
      slow_write("Las runs further into the city and you follow.")
      
    elif solschioc=='2':
      slow_write(f"{player_name.upper()}: I'm Victor Pauci.")
      slow_write("UNKNOWN: Mr Pauci, I'm gonna have to get you to land in Dock 52 please. We need to talk to you.")
      slow_write(f"{player_name.upper()}: Roger.")
      slow_write("You turn off the mic system.")
      slow_write("LAS: Why'd you use Victor's name?")
      slow_write(f"{player_name.upper()}: Why not?")
      slow_write("LAS: He's a wanted criminal!")
      slow_write(f"{player_name.upper()}: Oh.")
      slow_write("You land in Dock 51 and are greeted by a man wearing a suit holding a clipboard.")
      time.sleep(1)
      print("1. What's wrong?")
      print("2. I'm not Victor.")
      not_victor = input("> ")
      
      while not_victor not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        not_victor = input("> ")
      if not_victor=='1':
        slow_write("SUIT: According to my records, you look nothing like Victor Pauci. Nothing like him.")
        time.sleep(1)
        print("1. I don't age gracefully.")
        print("2. Yeah, I'm not.")
        not_victor_2 = input("> ")
        
        while not_victor_2 not in ['1', '2']:
          print("Invalid option. Please try again.")
          not_victor_2 = input("> ")
        if not_victor_2=='1':
          slow_write("SUIT: You really think I'm buying that. Identity theft is not a joke.")
        elif not_victor_2=='2':
          slow_write("SUIT: Then why didn't you say that to begin with. Identity theft is not a joke.")
        else:
          print("Invalid option. Please try again.")
          continue
      elif not_victor=='2':
        slow_write("Then why didn't you say that when you were in airspace. Identity theft is not a joke.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      time.sleep(2)
      print("BOOM!")
      time.sleep(1)
      slow_write("LAS: What was that?")
      slow_write("SUIT: Sounds like the relay... Shutting down?")
      slow_write("LAS: Why would they do that?")
      slow_write("SUIT: I don't... Excuse me, I need to go. DON'T MOVE!")
      slow_write("LAS: I reckon we check it out.")
      time.sleep(1)
      print("1. Sure.")
      print("2. No, it's too dangerous.")
      safe_or_danger = input("> ")
      
      while safe_or_danger not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        safe_or_danger = input("> ")
      if safe_or_danger=='1':
        slow_write("LAS: Then let's go!")
      elif safe_or_danger=='2':
        slow_write(f"{player_name.upper()}: We can't it's too dangerous for you!")
        slow_write("LAS: We need the relay to be working so we can get to Lassos One!")
        time.sleep(1)
        print("1. Fine, I'll come as well.")
        print("2. No, I'm staying here.")
        come_or_stay = input("> ")
        
        while come_or_stay not in ['1', '2']:
          print("Invalid option. Please select a valid option.")
          come_or_stay = input("> ")
        if come_or_stay=='1':
          slow_write("LAS: Good. Then let's go!")
        elif come_or_stay=='2':
          slow_write("LAS: Fine, whatever you want.")
          slow_write("Las runs off, disappearing into the dusty cities of Solshioc I.")
          slow_write("You begin to walk back to the Hummingbird, but not before finding a statue standing in front of you.")
          slow_write(f"{player_name.upper()}: Where'd you come from?")
          slow_write("One blink was all it took. Once you opened your eyes again, you could feel the statue's cold hands over your throat, beginning to twist.")
          slow_write("It breaks your neck, but your body begins to regenerate. However, the statue gives it one last twist before you lose consciousness forever.")
          slow_write("The last sight that you ever had was that of a smiling angel.")
          slow_write("ENDING: The Smiling Angel")
          time.sleep(2)
          print(SmilingAngelEnding_banner())
          print("1. Restart from Act Two.")
          print("2. Exit game.")
          restart_option_6 = input("> ")
          
          while restart_option_6 not in ['1', '2']:
            print("Invalid option. Please select a valid option.")
            restart_option_6 = input("> ")
          if restart_option_6=='1':
            continue
          elif restart_option_6=='2':
            exit()
          else:
            print("Invalid option. Please select a valid option.")
            continue
        else:
          print("Invalid option. Please try again.")
          continue
      else:
        print("Invalid option. Please select a valid option.")
      slow_write("The two of you leave Dock 52 and run into the dusty cities of Solshioc I.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("The dust covers your helmet's visor and you run closer to the centre of the city.")
    slow_write("Screaming fills the air but you can't see where it's coming from.")
    slow_write(f"LAS: {player_name.upper()}!")
    slow_write("You sprint to find Las in the clutches of a statue, its arm around her neck.")
    slow_write("LAS: Help!")
    time.sleep(1)
    print("1. Break the arm of the statue.")
    print("2. Examine the statue.")
    statue = input("> ")
    
    while statue not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      statue = input("> ")
    if statue=='1':
      slow_write("You go up to the statue and bring out the pistol you took from the mercenary.")
      slow_write("You point it at a specific spot and blow its arm off from the rest of its body, freeing Las.")
    elif statue=='2':
      slow_write("The statue had wings on its back and fangs coming out of its mouth.")
      slow_write("It seemed familiar, but you're not sure from where.")
      slow_write("LAS: Help please!")
      statue = input("> ")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("LAS: It moved while I wasn't looking. But it stopped when you came.")
    slow_write(f"{player_name.upper()}: So it only moves when you're not looking at it.")
    slow_write("LAS: There's probably a whole army of them in the streets. We best be heading to the relay.")
    slow_write(f"{player_name.upper()}: No, one of us should bring the ship here and the other should handle the relay.")
    slow_write("LAS: Which one do you want to do?")
    time.sleep(1)
    print("1. Bring the Hummingbird.")
    print("2. Turn on the relay.")
    ship_or_core = input("> ")
    
    while ship_or_core not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      ship_or_core = input("> ")
    if ship_or_core=='1':
      slow_write(f"{player_name.upper()}: I'll bring the Hummingbird over here.")
      slow_write("LAS: Be safe.")
      slow_write(f"{player_name.upper()}: You too.")
      slow_write("You begin to run back to the docks where the Hummingbird is.")
      slow_write("You sprint for the Hummingbird, finding yourself near the Docks. However, multiple angel statues block your way.")
      time.sleep(1)
      print("1. Sprint for the Hummingbird.")
      print("2. Shoot the angels.")
      sprint_or_shoot = input("> ")
      
      while sprint_or_shoot not in ['1', '2']:
        print("Invalid input. Please try again.")
        sprint_or_shoot = input("> ")
      if sprint_or_shoot=='1':
        slow_write("You try to sprint all the way through the angels to reach the Hummingbird.")
        sprint = time_event()
        
        if sprint:
          slow_write("You manage to evade the first few angels and are nearly at the foot of the Hummingbird.")
          slow_write("However, a couple still block your path.")
        else:
          slow_write("You try to evade the first few angels but one of the ones from behind grabs at your shirt and tugs at it.")
          slow_write("You fall down and the angels now have their hands on your throat.")
          slow_write("They twist and twist until you lose consciousness. Forever.")
          slow_write("The last thing you saw was the image of a smiling angel.")
          slow_write("ENDING: Smiling Angel")
          time.sleep(2)
          print(SmilingAngelEnding_banner())
          time.sleep(1)
          print("1. Restart from ActTwo.")
          print("2. Exit game.")
          restart_option_7 = input("> ")
          
          while restart_option_7 not in ['1', '2']:
            print("Invalid option. Please select a valid option.")
            restart_option_7 = input("> ")
          if restart_option_7=='1':
            continue
          elif restart_option_7=='2':
            exit()
          else:
            print("Invalid option. Please select a valid option.")
            continue
        sprint_2 = time_event()
        
        if sprint_2:
          slow_write("You successfully evade the rest of the angels and enter the Hummingbird, quickly closing the doors behind you.")
        else:
          slow_write("You try to evade the last couple of angels but one of them grabs on your shirt and tugs you down.")
          slow_write("You fall down adn the angels now have their hands on your throat.")
          slow_write("They twist and twist until you lose consciousness. Forever.")
          slow_write("The last thing you saw was the image of a smiling angel.")
          slow_write("ENDING: Smiling Angel")
          time.sleep(2)
          print(SmilingAngelEnding_banner())
          print("1. Restart from ActTwo.")
          time.sleep(1)
          print("2. Exit game.")
          restart_option_8 = input("> ")
          
          while restart_option_8 not in ['1', '2']:
            print("Invalid input. Please select a valid input.")
            restart_option_8 = input("> ")
          if restart_option_8=='1':
            continue
          elif restart_option_8=='2':
            exit()
          else:
            print("Invalid input. Please select a valid input.")
            continue
            
      elif sprint_or_shoot=='2':
        slow_write("You try to shoot down every angel.")
        shoot = time_event()
          
        if shoot:
          slow_write("You manage to, with deadeye accuracy, destroy every single one of the angels standing in your path, the rubble of their bodies scattered everywhere.")
        else:
          slow_write("You try to shoot all the angels but a few of them creep up to you when your not looking and grab your neck.")
          slow_write("They twist and twist until you lose consciousness. Forever")
          slow_write("The last thing you saw was the image of a smiling angel.")
          slow_write("ENDING: Smiling Angel")
          time.sleep(2)
          print(SmilingAngelEnding_banner())
          time.sleep(1)
          print("1. Restart from ActTwo.")
          print("2. Exit game.")
          restart_option_9 = input("> ")
            
          while restart_option_9 not in ['1', '2']:
            print("Invalid option. Please select a valid option.")
            restart_option_9 = input("> ")
          if restart_option_9=='1':
            continue
          elif restart_option_9=='2':
            exit()
          else:
            print("Invalid option. Please select a valid option.")
            continue
        slow_write("You enter the Hummingbird and begin to fly it.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      slow_write("You fly the Hummingbird over to the relay where you see Las and... Victor waving their hands at you.")
      slow_write("You drop some rope down and they climb back up.")
      slow_write(f"VICTOR: So how are we doing {player_name}?")
      time.sleep(1)
      print("1. Love it here.")
      print("2. Thought I was done seeing your ugly mug.")
      victor_answer = input("> ")
      
      while victor_answer not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        victor_answer = input("> ")
      if victor_answer=='1':
        slow_write("VICTOR: Well I did love it here as well until you guys did this.")
        slow_write("LAS: Hey, we didn't do this.")
        slow_write("VICTOR: I think we know you did.")
      elif victor_answer=='2':
        slow_write("VICTOR: Likewise.")
      slow_write("You pilot the Hummingbird through the relay, passing through the vortex.")
      slow_write("When you end up on the other side, you find yourself facing the luscious green and blue of Lassos One.")
      return 'survived ActTwo'

    elif ship_or_core=='2':
      slow_write(f"{player_name.upper()}: I'll turn on the relay.")
      slow_write("LAS: Be safe.")
      slow_write(f"{player_name.upper()}: You too.")
      slow_write("You begin to run for the centre of the city.")
      slow_write("You make it to the relay where there is a panel waiting for you with a few buttons.")
      slow_write("Before you can press anything you see that an angel statue is standing on the staircase above you.")
      slow_write("This gives you one shot to enter the buttons.")
      time.sleep(1)
      print("1. Turn on relay.")
      relay = input("> ")

      while relay not in ['1']:
        print("Invalid option. Please select a valid option.")
        relay = input("> ")
      if relay=='1':
        slow_write("You turn your eyes away and begin to turn on the relay.")
        relay_activation = time_event()

        if relay_activation:
          slow_write("The relay shudders back to life and you turn back around just in time for the angel to be leaning towards you, but not touching.")
        else:
          slow_write("The relay shudders back to life but you turn around to find that the angel already has its hand on your throat.")
        slow_write("Suddenly, a few bullets hit the angel's head and arms and blow it into bits.")
        slow_write("You peer behind the angel to see a familiar face holding a smoking gun.")
        slow_write("VICTOR: Everywhere you go, trouble follows.")
        time.sleep(1)
        print("1. VICTOR!")
        print("2. I didn't need your help.")
        victor_help = input("> ")

        if victor_help=='1':
          slow_write(f"{player_name.upper()}: Why are you here?!")
          slow_write("VICTOR: Told you that I'd be laying low at one of the Conclave cities.")
        elif victor_help=='2':
          slow_write("VICTOR: Maybe I could get a thanks.")
        slow_write("Suddenly, you hear the flapping of wings above you. The Hummingbird hangs above, with a rope thrown out from the side.")
        slow_write(f"{player_name.upper()}: That's my ride. Wanna come?")
        slow_write("VICTOR: Well since you made a mess of this entire city, sure.")
        slow_write("You both climb the rope back into the Hummingbird.")
        slow_write("LAS: How you boys doing?")
        time.sleep(1)
        print("1. Could be better.")
        print("2. Fantastic!")
        doing = input("> ")

        if doing=='1':
          slow_write(f"{player_name.upper()}: Could be doing better.")
          slow_write("VICTOR: Yeah especially with me saving you. Again.")
        elif doing=='2':
          slow_write("VICTOR: Still waiting on that thank you.")
        slow_write("LAS: Sure you are. Anyways, buckle your seatbelts cause we're going through the relay in 3.")
        slow_write("The relay passes through at the perfect angle and you travel through the vortex.")
        slow_write("When you reach the other side, you find yourself facing the luscious green and blue of Lassos One.")
        return 'survived ActTwo'
      else:
        print("Invalid option. Please select a valid option.")
        continue

    else:
      print("Invalid option. Please select a valid option.")
      continue
        

        
    
      