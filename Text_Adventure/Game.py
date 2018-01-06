from __future__ import print_function

print("Welcome to Salvation: The Game")
name = raw_input("What's your name? ")
being = raw_input("Would you like to play as the Alien or the Human? ").lower()
question_beginning = "\n--- \n"
death = True

def breaker():
    '''Creates a visual breaker for the player to understand a section is over.'''
    print("_______________________________________________________________________________________________________________\n")

def human_environment_description():
    '''This is the description of the HUuman's scene'''
    print("In 2016 due to political unrest and poor funding towards the scientific community, scientists decided to take actions into their own hands.")
    print("Using the last of their funding they decided to reengineer the Ebola virus to create 'zombies'.")
    print("These zombies began to wander around mindlessly. Infecting anything that came in contact with their blood or saliva.")
    print("Eventually this virus mutated to create the horrors that only exist in movies and books. They began to exist in reality.")
    print("Because of these tendencies the world in the year 2020 is not filled with technical advancements and flying cars.")
    print("Instead it is a desolate wasteland, one filled with burning cars, and not a soul in sight.")
    print("Buildings that once stood tall now hang bent over, their metal frames twisted and scorched.")
    print("The only beings that wander this apocalyptic wasteland are those very same zombies. They drift around, destroying everything they can see.")
    print("They are always on the lookout for their next victims.")
    print("You, " + name + ", have survived the apocalypse for so long but now everyone has left you. You are on your own...")
    breaker()

def alien_environment_description():
    '''This is the description of the Alien's scene'''
    print("In 2030 due to political unrest and poor funding towards the scientific community, scientists decided to take actions into their own hands.")
    print("Using the last of their funding they decided to re-engineer the Bacterium 'Microbacterium leprosy' in order to create highly intellectual creatures, that would help sustain life and contribute to the society's issues.")
    print("Unfortunately, due to a technical problem, the experiment resulted in the creatures getting infected by leprosy and  taking form of 'zombies'.")
    print("Also the effect on the zombies was the opposite.")
    print("They began to wander around mindlessly, ruthlessly infecting anything that came in contact with their blood or saliva.")
    print("Eventually this disease mutated to create the horrors that only exist in movies and books.Now, they began to exist in reality.")
    print("Because of these tendencies the world in the year 2030 is not filled with technical advancements and flying cars.")
    print("Instead it is a desolate wasteland, one filled with burning cars, and not a soul in sight.")
    print("Buildings that once stood tall now hang bent over, their metal frames twisted and scorched.")
    print("The only beings that wander this apocalyptic wasteland are those very same zombies. They drift around with their bazookas, destroying everything they can see.")
    print("They are always on the lookout for their next victims.")
    print("You, " + name + ", have survived the apocalypse for so long but now everyone has left you. You are on your own...")
    breaker()

def play_again():
    '''play_again Asks the player whether they'd like to play again or not'''
    play = raw_input("Would you like to play again? (yes/no): ").lower()
    if play == 'yes' or play == 'y':
        being = raw_input("Would you like to play as the Alien or the Human? ").lower()
        text_adventure()
    else:
        print("Thanks for playing! We hope you enjoyed our game!")
        
def zombie_eat_death_function():
    '''Prints out strings that indicate that zombies have eaten the Human'''
    print("... AAAAAAAAAAAAAAAAAAAAAGGGGGGGGGGGHHHHHH... help... my braaai...")
    print( "You got eaten by zombies. They thought you tasted good.")
    play_again()
    
def zombie_ambush_death_function(death):
    '''Prints out strings that indicate that zombies have ambushed the Human'''
    print("You got ambushed by a bunch of zombies!")
    if death == True:
        zombie_eat_death_function()
    else:
        print("You survived the harrowing attack.")
        play_again()

def death_by_shooting():
    print("You got shot on sight.")
    play_again()

def explore():
    print("You round a corner")
    print("A man is sitting and tending to his wounds.")
    print("He looks up.")
    death_by_shooting()

def outside():
    print("You go outside and cover your eyes. You pick up sounds in the distance.")
    print("Is that snarling you hear?")
    death = True
    zombie_ambush_death_function(death)
  
def last_decision():
    print("You reach the 'Haven'!")
    print("You, %s, survived!") % (str(name))
  
def home():
    final_decision = raw_input(question_beginning + "Will you sprint across the field to the HAVEN or will you crawl towards the HAVEN? (crawl/sprint): ")
    if final_decision == 'sprint':
        last_decision()
        print("You made it! You, " + name + ", have found the Haven! You can now live peacefully forever.")
        print("You walk inside. Someone greets you. It doesn't matter who they are or what they say. You're home now and that's all that matters...")
        breaker()
        play_again()
        
    elif final_decision == 'crawl' or final_decision == 'c':
        death == True
        zombie_ambush_death_function(death)
    
def pull():
    '''Executes a decision based on your decision to pull out the weapon.'''
    print("You manage to shove aside the rubble and pull out a dust-covered sword.")
    print("You turn around swinging your sword wildly.")
    death = False
    zombie_ambush_death_function(death)
    print("You find a stary piece of leather and fashion it into a baldric in which to place your sword in.")
    print("Determined to make it to safety you press onward.")
    print("You encounter a worn and almost illegible poster on a wall.")
    print("You make out the words 'Haven' and 'north'.")
    print("Using the sun you track a course for the north hoping to reach this 'Haven'.")
    home()
    
def leave():
    '''Executes a decision based on your decision to not pull out the weapon.'''
    print("You manage to shove aside the rubble and pull out a dust-covered sword.")
    death = False
    zombie_ambush_death_function(death)

def shack_decision():
	'''Calls another function based on the decision to go to the shack'''
	print("The shack is filled with vicious and hungry rats that bite you everywhere. You ignore them.")
	print("You spot something blue in the corner")
	print("It's a pot with water in it!")
	print("Your thirst has been fulfilled. Now you can focus on other things.")
	explore_or_go_outside = raw_input(question_beginning + "Would you like to explore the shack further or step outside and search for a better shelter? (explore/outside): ").lower()
	if explore_or_go_outside == 'explore' or explore_or_go_outside == 'e':
	    explore()
	elif explore_or_go_outside == 'outside' or explore_or_go_outside == 'o':
	    outside()

def building_decision():
    '''Calls another function based on the decision to go to the building'''
    print("You slowly walk towards the building but the glint of something metallic catches your eye.")
    print("You slowly walk over to rubble to examine it.")
    print("You were right. It is something metallic.")
    print("You look around and find a wooden handle covered in dust a few inches nearby.")
    pull_or_not_pull = raw_input(question_beginning + "Would you like to pull out the weapon or not? (pull/leave): ").lower()
    if pull_or_not_pull == 'pull' or pull_or_not_pull == 'p':
        pull()
    elif pull_or_not_pull == 'leave' or pull_or_not_pull == 'l':
        leave()
        
def encounter_first_shelter():
    '''Executes another function with more choices based on the first shelter the player chooses the player makes.'''
    first_decision = raw_input(question_beginning + "Inside the ratty shack nearby or the blank, white building that looms in the distance? (shack/building): ").lower()
    if first_decision == 'shack' or first_decision == 's':
        shack_decision()
    elif first_decision == 'building' or first_decision == 'b':
        building_decision()



def alien_Hungry():
    '''This scene decides whether the human is about to die or not'''
    print("I'm on the way to my destination and have not spotted any zombies yet.")
    print("----------------------------")
    print("Whoah!... I've found yummy worms over the fence!")
    alien_Jump()
    
def alien_Jump():
    '''A decision, whether the player has to jump over a fence or not has to made'''
    
    After_alien_jump()
    
def After_alien_jump():
    '''The human is in a dilemma and seeks help'''
    jump = raw_input("Do you think I should jump over the fence and eat those slimy worms that make me salivate? (yes/no):" ).lower()
    if jump == 'yes' or jump =='y':
        alien_survive()
        play_again()
    elif jump == 'no' or jump == 'n':
         alien_final_conclusion()
         print("OOPS! You have been shot by the zombies." )
         play_again()

def alien_survive():
    '''The human survives'''
    print('Nice! You not only were lucky enough to never come across the zombies, but you have also managed to fulfill your hunger. You win!')
        
def alien_weapon():
    '''This line give the human an option to choose between two weapons.'''
    weapon = raw_input("Oh and I think I need weapons to kill the zombies, should I carry a bazooka or a sword? (Bazooka/Sword):").lower()
    if weapon == 'bazooka' or weapon =='b':
        alien_Hungry()
    else:
        print("Thanks for the suggestion!")
        alien_Hungry()
        


def alien_closer():
    if alien_question == 'closer' or alien_question == 'c':
        '''Actions after human decides to go to the farther building'''
    print("R: Alright, it'll take less time and energy to go for the closer one anyways.")
    alien_weapon()
    if alien_question == 'farther' or alien_question == 'f':
        print("R: It's pretty far, but it's doable. Let's hope for the best on the way there.")
    
   

def alien_farther():
    '''Actions after human decides to go to the farther building'''
    print("R: It's pretty far, but it's doable. Let's hope for the best on the way there.")
    

 
def alien_function():
    '''The alien(player) guides the human'''
    print("R:_________________ ")
    print(name + ": You shouldn't be hanging out here in the dark. The zombies are on the run. If you don't escape soon, they'll kill you! Do you have a place to go?")
    print( "R: Yeah, it seems that there's a building not too far away. And maybe another more solid looking one a little farther off?")
    alien_question = raw_input("Should I go to the building that's closer or the one that's a little farther? (closer/farther): ").lower
    alien_question()
    
def alien_question():
    if alien_question == 'closer' or alien_question == 'c':
        alien_closer()
    elif alien_question == 'farther' or alien_question == 'f':
        alien_farther()

    


        
def alien_final_conclusion():
    '''The human dies'''
    print("R: Ahhh! Save me..!.. my intes-tines...gasp... are burning!")

def text_adventure():
    r = "R:"
    if being == "human":
        human_environment_description()
        print("You wake up in a scorching environment and your mouth feels dry. You're first thought is to find some shelter away from the sun. Where will you go?")
        encounter_first_shelter()
    elif being == "alien":
        alien_environment_description()
        
        print("Static...")
        print("Comm secured")
        print("You find yourself stranded in the middle of nowhere and need  grub to stay alive. You also see a human approaching you.")
        print(r + "Hel... Any... ne... the.. re?")
        print(name + ": I'm a scientist. Who are you?..You look lost.")
        print(r + "I don't know I think my name started with an R.")
        print(name + ": Are you looking for someone or do you need to go anywhere?")
        alien_function()
        alien_closer()
        
        
        
text_adventure()



























