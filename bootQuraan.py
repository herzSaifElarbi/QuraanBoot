import telebot
from telebot import types, util, TeleBot
import requests
import time
from datetime import timedelta

surah = 1 #suarah li rana fiha
f = open(f"./tafseer/{surah}.txt", "r", encoding="utf-8")

def save_quran_verse(verse_number):
    url = f'https://api.alquran.cloud/v1/ayah/{verse_number}/ar'

    response = requests.get(url)

    if response.status_code == 200:
        if response.headers['Content-Type'] == 'application/json':
            data = response.json()

            # Extract the verse text from the JSON response
            ayah = data['data']['text']  # Store verse text in 'ayah' variable
            numberInSurah = data['data']['numberInSurah']
            # Send the verse text to the chat
            try:
                return ayah, numberInSurah
            except Exception as e:
                print(f'Error sending message: {e}')

        else:
            print('Unexpected content type:', response.headers['Content-Type'])
    else:
        print('Error:', response.status_code)

# Replace with your actual Telegram bot token
BOT_TOKEN = ""
# Target chat ID (replace with the actual chat ID)

# Update with the correct chat ID

chat_id = None  #id lazem dir

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Handle other message types if needed (optional)
    pass

#start = random.randint(1, 6236)
start = 1#wechmen aya 3la 7sab el Quraan complet

verse_number = 1 # لي مايديباسيش الليميت جاي كيما ال "اي"تم

ayah = ""#var fih ayat bach ytkatbo

tafseer_ayah = ""#tafsir ayat

numberInSurah = 0 #رقم الاية لي رانا فيها

number_of_ayah_to_put = 6#قداش اية نهزو

if __name__ == "__main__":
    print("Bot is running...")
    while(True):
        tafseer_ayah = ""
        
        ayah = ""
        
        verse_number = 1
        
        while verse_number < number_of_ayah_to_put:
            # Generate a random verse number between 1 and 6236
            #verse_number = random.randint(1, 6236)
            ayahTemp, numberInSurah= save_quran_verse(start)
            
            if(numberInSurah == 1 and start != 1):
                ayah += "\n\n\n"
                surah += 1
                f.close()
                f = open(f"./tafseer/{surah}.txt", "r", encoding="utf-8")
                tafseer_ayah += "\n\n\n"#
                
            tafseer_ayahTemp = f.readline()            
            tafseer_ayah += tafseer_ayahTemp#
            tafseer_ayah += f"({numberInSurah})\n"#
            
            
            ayah += ayahTemp
            ayah += f"({numberInSurah})"
            verse_number +=1
            start +=1

        bot.send_message(chat_id, ayah)
        bot.send_message(chat_id, tafseer_ayah)


        if(start == 6236):
            start = 1
            surah = 1

        #sleep_duration = timedelta(seconds=60)  # Change hours to seconds
        #time.sleep(sleep_duration.total_seconds())

        sleep_duration = timedelta(hours=24)
        time.sleep(sleep_duration.total_seconds())  # Sleep for 24 hours
        
f.close()
