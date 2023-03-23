print("Welcome to the quiz  game")

permission = input("Do you want to play?")
if permission.lower() != "yes":
    quit()
print("Okay let's play ")
print("use full chemical names ")
score = 0
answer = input("What are the product of the reaction between methane and chlorine   ").lower()
if answer == "methane and hydrochloric acid" or "CH4+HCl" or "methane and hydrogen chloride" or " hydrochloric acid and methane":
    print('Correct')
    score+=1
else:
    print("Soma soma soma kijana masiku yazidi haribika ")
answer = input("Vicinal dihalide+ ___= alkene +____    ").lower()
if answer ==  "Zn and ZnX2" or "ZnX2 and Zn" or "ZnandZnX2" or "ZnX2andZn" or "zinc and zinc dihalide":
    print('Correct')
    score+=1
else:
    print("Soma soma soma kijana masiku yazidi haribika ")
answer = input("What are the product of the reaction between alkene and ozone   ").lower()
if answer == "aldehyde and ketone" or "ketone and aldehyde":
    print('Correct')
    score+=1
else:
    print("Soma soma soma kijana masiku yazidi haribika   ")
answer = input("What are the products of the reacton between sodium ethanoate and sodium hyroxide using soda lime as a catalyst   ").lower()
if answer == "methane, sodium carbonate and carbon(iv) oxide" or "sodium carbonate, methane and carbon(iv)oxide":
    print('Correct')
    score+=1
else:
    print("Soma soma soma kijana masiku yazidi haribika ")
answer = input("What is formed when ethanal is reduced using NaBH4   ")
if answer == "ethanol":
    print('Correct')
    score+=1
else:
    print("Soma soma soma kijana masiku yazidi haribika ")
answer = input("What is the main product fromed between ethanolic potassium hyroxide and methylpropane    ").lower()
if answer == "propene":
    print('Correct')
    score+=1
else:
    print("Soma soma soma kijana masiku yazidi haribika ")
print(score)


    