import datetime
import webbrowser
import random
import os

def process_command(command):
    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {now}"

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "hello" in command:
        return "Hello! How can I help you?"

    elif "stop" in command or "quit" in command or "exit" in command:
        return "Goodbye!"
    
    elif "play" in command:
        # ⚠️ IMPORTANT: Change this to the actual path of your music folder!
        # Use 'r' before the string to handle backslashes correctly on Windows.
        music_folder = r"C:\Users\YourUsername\Music" 
        
        try:
            # 1. Get a list of all audio files in the folder
            songs = [file for file in os.listdir(music_folder) if file.endswith(('.mp3', '.wav'))]
            
            if not songs:
                return "Your music folder is empty or has no mp3 files."

            # 2. If you just say "play" or "play music", pick a random song
            if command.strip() == "play" or command.strip() == "play music":
                song_to_play = random.choice(songs)
            
            # 3. If you ask for a specific song (e.g., "play shape of you")
            else:
                requested_song = command.replace("play", "").strip()
                
                # Search for the requested song in your folder
                matches = [s for s in songs if requested_song in s.lower()]
                
                if matches:
                    song_to_play = matches[0] # Play the first match it finds
                else:
                    return f"I couldn't find {requested_song} in your music folder."

            # 4. Create the full file path and play it
            file_path = os.path.join(music_folder, song_to_play)
            
            # Note: os.startfile is for Windows. It opens your default media player.
            os.startfile(file_path)
            
            # Clean up the file name so the bot says it nicely (removes .mp3)
            spoken_name = song_to_play.replace(".mp3", "").replace(".wav", "")
            return f"Playing {spoken_name}"

        except FileNotFoundError:
            return "I couldn't find your music folder. Please check the folder path in the code."

    else:
        return "Sorry, I didn't understand that."