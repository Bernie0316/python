def main():
    mood = moods()
    print(f"You are {mood}")
    reader = CSV_reader()
    song = song_choose(mood, reader)
    print(f"You can listen {song}.")

def moods():     
    for item in ["1 - Angry", "2 - Sad", "3 - Happy"]:
        print(item)
    mood_now = input("What's your mood now?(1, 2, 3): ")
    if mood_now == "1":
        mood_now = "Angry"
    if mood_now == "2":
        mood_now = "Sad"
    if mood_now == "3":
        mood_now = "Happy"    
    return mood_now 

def CSV_reader():
    import csv
    with open("music_database.csv", 'rt') as file:
        file = csv.reader(file)
        file = next(file)
    return file

def song_choose(mood, reader):
    import random
    for lines in reader:
        data_mood = lines[0]
        data_singer = lines[1]
        data_song = lines[2]
    if mood == data_mood:
        song = random.choice(data_song)
        singer = random.choice(data_singer)
    song_push = f"{song} by {singer}"
    return song_push

if __name__ == "__main__":
    main()