import datetime as dt

def check_date():
    date_today = dt.date.today()
    date_today = str(date_today)
    return date_today

def has_mood_for_today():
    today = check_date()
    try:
        with open("data/mood_diary.txt", "r") as f:
            mood_diary = f.readlines()
            for line in mood_diary:
                if today in line:
                    return True
    except FileNotFoundError:
        return False
    return False

def getNumberFromMood(mood):
    if mood == "happy":
        return 2
    if mood == "relaxed":
        return 1
    if mood == "apathetic":
        return 0
    if mood == "sad":
        return -1
    if mood == "angry":
        return -2

def getMoodFromNumber(num):
    if num == 2:
        return "happy"
    if num == 1:
        return "relaxed"
    if num == 0:
        return "apathetic"
    if num == -1:
        return "sad"
    if num == -2:
        return "angry"
    

def save_mood(mood):
    with open("data/mood_diary.txt", "a") as f:
        f.write(f"{check_date()} {getNumberFromMood(mood)}\n")

def diagnose_mood():
    happy_count = 0
    sad_count = 0
    apathetic_count = 0
    with open("data/mood_diary.txt", "r") as f:
        mood_diary = f.readlines()
        if len(mood_diary) < 7:
            return
        else:
            last_seven_moods = mood_diary[-7:]
            sum_moods = 0
            for line in last_seven_moods:
                date, number = line.split()
                sum_moods += int(number)
                if int(number) == 2:
                    happy_count += 1
                elif int(number) == -1:
                    sad_count += 1
                elif int(number) == 0:
                    apathetic_count += 1

        average_mood = round(sum_moods / 7)
        if happy_count >= 5:
            print("Your diagnosis: manic!")
        elif sad_count >= 4:
            print("Your diagnosis: depressive!")
        elif apathetic_count >= 6:
            print("Your diagnosis: schizoid!")
        else:
            print(f"Your diagnosis: {getMoodFromNumber(average_mood)}!")
        
        
def assess_mood():
    if has_mood_for_today():
        print("Sorry, you have already entered your mood today.")
        return
    else:
        mood_list = ["happy", "relaxed", "apathetic", "sad", "angry"]
        mood = input("How are you feeling today? (Please enter happy, relaxed, apathetic, sad, or angry): ")
        while mood not in mood_list:
            print("Invalid input. Please try again.")
            mood = input("How are you feeling today? (Please enter happy, relaxed, apathetic, sad, or angry): ")
        save_mood(mood)
        diagnose_mood()
            
        