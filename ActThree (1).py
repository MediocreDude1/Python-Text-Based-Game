#Imports modules to be used in this code.
import time
import random
from ActOne import *
from ActTwo import *
from ASCIIArt import *
from QuickTime import time_event
#Defines ActThree
def ActThree(player_name):
  #Begins the loop.
  while True:
    print(ActThree_banner())
    slow_write("VICTOR: What I'm saying is that those statues were from Doctor Who.")
    slow_write("LAS: There's no way that fictional monsters came to life, right?")
    slow_write("VICTOR: The similarites are uncanny. I know it when I see it.")
    time.sleep(1)
    print("1. It is the Weeping Angels.")
    fiction = input("> ")
    
    while fiction not in ['1']:
      print("Invalid option. Please select a valid option.")
      fiction = input("> ")
    if fiction=='1':
      slow_write(f"""{player_name.upper()}: Victor's right. These are the Weeping Angels from Doctor Who.
I had almost forgotten since the last cycle but these things happen when The End Times are approaching.
Fiction becomes reality and reality becomes fiction.""")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("LAS: What are you saying?")
    time.sleep(1)
    print("1. It is the beginning of The End Times.")
    print("2. We need to watch out for anything else.")
    end_times = input("> ")
    
    while end_times not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      end_times = input("> ")
    if end_times=='1':
      slow_write(f"{player_name.upper()}: I've lived through a few universal cycles and this sort of event signals the beginning of The End Times.")
      slow_write("LAS: What do you mean lived through universal cycles?")
    elif end_times=='2':
      slow_write(f"{player_name.upper()}: We need to watch out for anything else like that because there are bound to be more and deadlier creatures.")
      slow_write("LAS: How come you know so much?")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    time.sleep(1)
    print("1. Because I'm immortal.")
    immortal = input("> ")
    
    while immortal not in ['1']:
      print("Invalid option. Please select a valid option.")
      immortal = input("> ")
    if immortal=='1':
      slow_write(f"{player_name.upper()}: Because I'm immortal. I regenerate every time I'm nearly dead and as long as I'm not killed during the process I can live forever.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("LAS: You're immortal?! Victor did you know about this?")
    slow_write("VICTOR: Makes sense.")
    slow_write("LAS: Why'd you hide something like this from us.")
    time.sleep(1)
    print("1. Because I'm scared.")
    print("2. Because you are like bugs to me.")
    secret = input("> ")
    
    while secret not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      secret = input("> ")
    if secret=='1':
      slow_write(f"""{player_name.upper()}: I believe this to be the last secret I hold until I can trust somebody. And when that happens...
I'll have to watch them turn to nothing but dust.""")
    elif secret=='2':
      slow_write(f"""{player_name.upper()}: Because to me, you are like bugs. You come and go so fast that to tell you something like this...
I just can't.""")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("LAS: Wow. So you're immortal huh? How cool is that?")
    time.sleep(1)
    print("1. It's pretty cool.")
    print("2. It's not cool at all.")
    cool = input("> ")
    
    while cool not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
    if cool=='1':
      slow_write(f"{player_name.upper()}: You live for as long as I have and you see a lot of fantastic things.")
    elif cool=='2':
      slow_write(f"""{player_name.upper()}: No, it is not anything like that! You know what immortality is? It is like a battlefield.
Except I'm the only one left. Me alone.""")
      slow_write("LAS: I'm sorry, I didn't know you felt that way.")
      slow_write(f"{player_name.upper()}: ... It's okay.")
    else:
      print("Invalid option. Please select a valid option.")
      continue
    slow_write("VICTOR: We're here.")
    slow_write("Victor lands the Hummingbird near a small village. Almost immediately, Las leaves and runs towards the village.")
    slow_write("VICTOR: You know, now that your mission is complete, we can head back, the both of us. I'll split the money.")
    time.sleep(1)
    print("1. Then let's go then.")
    print("2. I think I'd like to stay for a bit.")
    stay_or_go = input("> ")
    
    while stay_or_go not in ['1', '2']:
      print("Invalid option. Please select a valid option.")
      stay_or_go = input("> ")
    if stay_or_go=='1':
      slow_write("VICTOR: So enthusiastic. Are you not going to say goodbye to Las?")
      time.sleep(1)
      print("1. Yes.")
      print("2. No.")
      goodbye = input("> ")
      
      while goodbye not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        goodbye = input("> ")
      if goodbye=='1':
        slow_write(f"{player_name.upper()}: I should, shouldn't I?")
        slow_write("You exit the Hummingbird and run after Las. Before she can enter the village you call out her name.")
        slow_write("LAS: What is it?")
        slow_write(f"{player_name.upper()}: We're gonna go now, me and Victor.")
        slow_write("LAS: Okay.")
        slow_write(f"{player_name.upper()}: Nothing else?")
        slow_write("LAS: You did everything you needed to do for me. Thank you.")
        time.sleep(1)
        print("1. Hug Las.")
        print("2. Leave.")
        hug_or_leave = input("> ")
        
        while hug_or_leave not in ['1', '2']:
          print("Invalid option. Please select a valid option.")
          hug_or_leave = input("> ")
        if hug_or_leave=='1':
          slow_write("You lean in for a hug with Las. She returns it.")
        elif hug_or_leave=='2':
          slow_write("You begin to turn around before saying something one last time.")
        else:
          print("Invalid option. Please select a valid option.")
          continue
        slow_write(f"{player_name.upper()}: Goodbye Las.")
        slow_write(f"LAS: Goodbye {player_name.upper()}.")
        slow_write("You walk off towards the Hummingbird.") 
      elif goodbye=='2':
        slow_write(f"{player_name.upper()}: No, I don't think I will.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      slow_write("You two turn the Hummingbird's engines back on and fly off.")
      slow_write("Eventually, you return to Eragrost VI and spend the rest of the universe's cycle remembering.")
      slow_write("It's not something that you do very often, but you felt like doing it, just for the rest of The End Times.")
      slow_write("Then you remember. No wonder Las seemed familiar. She was exactly like her. You chuckle to yourself as you watch the last of the stars die out.")
      slow_write(f"{player_name.upper()}: And I'd hoped there'd be stars this time.")
      slow_write("ENDING: I'd Hoped There'd Be Stars")
      time.sleep(2)
      print(StarsEnding_banner())
      time.sleep(1)
      print("1. Restart from Act Three.")
      print("2. Exit the game.")
      restart_or_exit = input("> ")
      
      while restart_or_exit not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        restart_or_exit = input("> ")
      if restart_or_exit=='1':
        continue
      elif restart_or_exit=='2':
        exit()
      else:
        print("Invalid option. Please select a valid option.")
        continue
      
    elif stay_or_go=='2':
      slow_write("VICTOR: Alright, take your time.")
      slow_write("You walk out take a look at the village.")
      slow_write("It was definitely one built on its agricultural business, with fields lined around the entire village.")
      slow_write("You walk further into the town until you find Las hugging somebody.")
      slow_write("VICTOR: That's her dad, the reason why she wanted to come home.")
      time.sleep(1)
      print("1. We brought her all the way here just to say goodbye?")
      print("2. I see. One more goodbye.")
      reason = input("> ")
      
      while reason not in ['1','2']:
        print("Invalid option. Please select a valid option.")
        reason = input("> ")
      if reason=='1':
        slow_write("VICTOR: Look, it might not seem important to you but to her, this was worth the entire thing.")
      elif reason=='2':
        slow_write("VICTOR: Yeah.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      slow_write("VICTOR: She's not only being hunted because she defied orders. She also has the capacity to carry out Project Overlord.")
      slow_write(f"{player_name.upper()}: Which is?")
      slow_write("VICTOR: Humanity's last effort to save themselves from the end of the universe. Using humans and their minds to try to change fate.")
      slow_write(f"{player_name.upper()}: It'll never work.")
      slow_write("VICTOR: And yet they'll still try. They're probably coming, even now.")
      time.sleep(1)
      print("1. I'll stay behind and protect the village.")
      save = input("> ")
      
      while save not in ['1']:
        print("Invalid option. Please select a valid option.")
        save = input("> ")
      if save=='1':
        slow_write("VICTOR: Why? Why would you even think of doing that?")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      time.sleep(1)
      print("1. To win.")
      print("2. To be kind.")
      win_or_kind = input("> ")
      
      while win_or_kind not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        win_or_kind = input("> ")
      if win_or_kind=='1':
        slow_write(f"{player_name.upper()}: I do this because I am sick and tired of the small people losing everything. I'm doing this so they can win. Just this once.")
      elif win_or_kind=='2':
        slow_write(f"""{player_name.upper()}: If I run away, good people will die. If I stay and fight, some of them... might live. Maybe not many, maybe not for long.
Hey, you know what? Maybe there's no point in any of this at all but it's the best I can do. So I'm gonna do it and I will stand here 
doing it until it kills me.""")
        slow_write("VICTOR: Is that Doctor Who?")
        slow_write(f"{player_name.upper()}: Yes.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      slow_write(f"VICTOR: ... You've changed {player_name}. But you've changed for the better. I'm sorry though, I can't fight alongside you. But I can give you good luck.")
      time.sleep(1)
      print("1. It's okay.")
      print("2. You should stop being a coward.")
      victor_leave = input("> ")
      
      while victor_leave not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        victor_leave = input("> ")
      if victor_leave=='1':
        slow_write("VICTOR: I'll miss you buddy. Come here.")
        slow_write("The two of you share one last hug before Victor returns to the Hummingbird, flying away into space.")
      elif victor_leave=='2':
        slow_write("VICTOR: Look at me. I don't age quite as gracefully as you do.")
        slow_write("With that Victor walks away, returning to the Hummingbird, flying away into space.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      time.sleep(2)
      slow_write("Some time later... ")
      slow_write("The Militarum forces land near the village, all the soldiers encircling the small village. However, there is nobody walking about in the village.")
      slow_write("Nobody except for one person.")
      slow_write(f"{player_name.upper()}: Sorry you lot. If you're looking for Las I'm afraid I've helped her hide away far from you soldiers.")
      slow_write("SOLDIER: AIM!")
      time.sleep(1)
      print("1. Activate explosives.")
      print("2. (Do nothing).")
      fight = input("> ")
      
      while fight not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
        fight = input("> ")
      if fight=='1':
        explosives = time_event()
        
        if explosives:
          slow_write("You set off explosives around the perimeter, blowing up the soldiers encircling the town.")
        else:
          slow_write("You try to set off the explosives and you do, but you end up getting shot.")
          slow_write("However, you quickly regenerate.")
        slow_write(f"{player_name.upper()}: Oh, you're gonna need more than that!")
        slow_write("You begin to explode even more explosives.")
        slow_write(f"{player_name.upper()}: Akuze! Mars! Jupiter! Sagor Ten! Oothusis! Even on Terra, you still lose!")
        slow_write("You are shot through the chest once, causing you to collapse on the floor.")
        slow_write("Then again and again.")
        slow_write("Your regeneration has already been negated.")
      elif fight=='2':
        slow_write("You do nothing and watch as multiple shots enter and leave your body.")
        slow_write("You collapse on the ground, your regeneration having already been negated by the sheer amount of shots that were fired into you.")
      else:
        print("Invalid option. Please select a valid option.")
        continue
      slow_write("So, it was now time.")
      slow_write("The soldiers move towards your body.")
      slow_write(f"{player_name.upper()}: With your final breath, you activate one last explosive.")
      slow_write("It engulfs every soldier in the radius, leaving nothing except ash and dust.")
      slow_write("But, in the middle of it all, your body still remains. Charred and battered, but still recognisable.")
      slow_write("When Las and the villagers would eventually return, they would find the body of their protector.")
      slow_write("Many cried, in joy or in sandness, but some, like Las looked towards the stars as if still looking for you.")
      slow_write("Afterall, there's no way an immortal man could die.")
      slow_write("ENDING: The Fall")
      time.sleep(2)
      print(TheFallEnding_banner())
      time.sleep(1)
      print("1. Restart from Act Three.")
      print("2. Exit game")
      result_continue = input("> ")
      
      while result_continue not in ['1', '2']:
        print("Invalid option. Please select a valid option.")
      if result_continue=='1':
        continue
      elif result_continue=='2':
        exit()
      else:
        print("Invalid option. Please select a valid opton.")
        continue
    else:
      print("Invalid option. Please select a valid option.")
      continue
      