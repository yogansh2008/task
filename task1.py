# #Task: Create Your Adventure Story
# Develop an interactive text-based adventure game in Python that engages players by
# letting them make choices to shape the story(Everyone must create a different story)

virat  = """WHAT YOU WANT 
            1. VIRAT COMPLETE HIS 100 CENTURIES only.  
            2. VIRAT PLAY WORLDCUP WINING SHOT AND COMPLETE HIS HUNDRED CENTURY.
           """
dhoni = """WHAT YOU WANT 
            1. DHONI MAKE A COMEBACK AND MAKE A CENTURY CENTURY IN IPL.
            2. DHONI PLAYS  A MATCH WINING KNOCK AND WIN THE CSK ITS 6TH TROPHY .
"""
name =" trent bolt"
country =" New Zealand"
virat1 =""" {}will come for the last bowl of the match.
India needed five runs to win the match I
India versus {} semifinal,
{} gave the cheese target of 350 run
Now Virat Kohli and Rohit Sharma make the partnership of 250 runs
rohit Sharma scored 156 runs And Virat Kohli 94 runs 
and only needed six runs to complete his 100th century and make history 
Of completing hundred centuries, {} bowled his last ball and Virat going down the ground and hit a flat six
and complete his 100 century and India won the match hur hurray"""

virat2 =""" Imagine Virat Kohli plays his first last World Cup 
he completed his 99th century 
Now the World Cup final against {} in {}
 {} gave the target of 310 runs to the Indian team
 While chasing Rohit Score 50 run and Shuman Gill and Virat Kohli make a partnership of 150 runs 
 Virat Kohli on strike with KL Rahul
 Virat Kohli on 96 run one bowl remained left and four runs needed to win India
 {} Bowled his last bowl of his over and also his career and Virat Kohli also plays his career last bowl
{} bowl up short pitch bow Virat Kohli lay back and hit Maximum Yeah.
 India won a World Cup after 16 years virat Kohli completed his 100th century Hooray Virat Kohli make history """


dhoni1 ="""" As we know Mahendra Singh Dhoni plays his last IPL and
 he played very Great knock of 94 runs till Against {} These great knocks come 
 when CSK is collapsed in 4th over and then the score was 19-4 and now the score is 156-7
 Mahender Singh Dhoni is on the strike and scored 94 runs and he want only six runs to complete his 100
 On the bowling hand {} come to bowl and he bowled a very grate yorker and 
 Mahender singh dhooni hit a helicopter shot and it goes out of the ground 
He completed his century Hooray"""

dhoni2 =""" We're coming back to the greatest  rivalry of IPL {} versus CSK
 now both team comes to an end
where both are fighting for win their title 
and Mahendra Singh Dhoni is on this strike ,last bowl of the Match and CSK needed four runs to win
{} comes to bowl he bowled a bouncer
and Mahendra Singh Dhoni make a great pull shot Yes it is a maximum CSK won the trophy for the 6th time 
Mahendra Singh Dhoni makes history again hurray!!!"""

# print(virat1.format(name,country))

print("""Imagine you are dreaming of a great cricketplayer
      Which player you want to read the story
      write 1: for Virat Kohli  
      write 2:Mahendra Singh Dhoni """)

a = int(input())

if a== 1:
    print(virat)
    a1 = int(input())
    if a1==1:
        print("""against which team
              1= australia 
              2 = new zealand """)
        a2= int(input())
        if a2==1:
            print(virat1.format("mitchel starc","Australia","Australia","mitchel starc"))
        else:
            print(virat1.format("Trent boult","NEWZEALAND","New Zealand","Trent boult"))

    else:
        print("""against which team
              1= australia 
              2 = new zealand """)
        a3= int(input())
        if a3==1:
            print(virat2.format("Australia","MELBOURN","Australia","mitchle starc","Mitchle starc"))
        else:
            print(virat2.format("south africa","capetown","south africa","Kagiso Rabada","Kagiso Rabada"))

else:
    print(dhoni)
    b1 = int(input())
    if b1==1:
        print("""against which team
              1= Mumbai Indians. 
              2 = Royal Challenger Bangaluru. """)
        b2= int(input())
        if b2==1:
            print(dhoni1.format("Mumbai Indians","jasprit bumrah"))
        else:
            print(dhoni1.format("Royal Challenger Bangaluru","Hazelwood"))
    else:
        print("""against which team
              1= Mumbai Indians 
              2 = Royal Challenger Bangaluru
              """)
        b3= int(input())
        if b3==1:
            print(dhoni2.format("Mumbai INdian","Jasprit Bumrah"))
        else:
            print(dhoni2.format("Royal Challenger Bangaluru","Hazelwood"))



     

