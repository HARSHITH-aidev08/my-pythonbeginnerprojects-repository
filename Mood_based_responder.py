username = (input(f"What's your username: 👤")) # enter your name 
print(f"Hi {username} 👋")
mood = (input(f"Hi what's your mood today 😊😢😡😨😳")).strip().lower() # enter your mood sorry but there are only sad, angry ,happy, embarrassed, scared
if mood == "sad":
    reason1 =(input(f"what's the reason for your sadness 😢"))
    print("Don't worry things will get better 🌈✨")
elif mood == "angry":
    reason2 =(input(f"what's the reason for your anger 😡"))
    print("Being angry isn't good 😤🧘")
elif mood == "scared":
     reason3 =(input(f"what's the reason for you being scared 😨"))
     print("Don't be scared face it off with your bravery 🛡️🦁")
elif mood == "embarrassed":
    reason4 =(input(f"what's the reason for you being embarassed 😳"))
    print("oh no! it happens to everyone 😅 — one day when you remember it you'll laugh 😂")
elif mood == "happy" :
    reason5 = (input(f"what's the reason for your happiness 😄"))
    print("oh that's a good news 🎉🌟")
elif mood == "tired":
    reason5 = (input("what's the reason for your tiredness 😴"))
    print("how about you take rest? 🛌 it is okay to take rest and rise again 🌞💪")
else : 
    print(f"Thanks for consulting me {username} 🙏 if you ever need help, I'm here for you 🤗")
    
# code after using ai to help me out with emojis .....
