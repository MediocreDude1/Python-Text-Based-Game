#Imports needed modules for the QuickTime mechanic.
import random
import time
import string

def generate_random_sequence(length):
  """Generate a random sequence of keys."""
  #Defines a sequence of valid keys using ASCII letters and digits.
  keys = string.ascii_letters + "0123456789"
  #Chooses random keys to create a QuickTime sequence.
  return ''.join(random.choice(keys) for _ in range(length))

def time_event():
  """Execute the time event."""
  #Prompts the user to press a series of keys within 5 seconds.
  print("Press the following keys within 5 seconds:")
  sequence = generate_random_sequence(5)
  #Displays sequence for players.
  print(sequence)
  
  start_time = time.time()
  elapsed_time = 0
  
  while elapsed_time < 5:
    user_input = input("Your input: ")
    
    if user_input == sequence:
      print("Success! You entered the correct key!")
      return True
    
    elapsed_time = time.time() - start_time
    
  print("Time's up! You failed to enter the correct key.")
  return False