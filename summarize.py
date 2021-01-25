from decouple import config
import openai
import lyricsgenius

openai.api_key = config('OPENAI_API_KEY')
GENIUS_ACCESS_TOKEN = config('GENIUS_ACCESS_TOKEN')

genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
print("What's the song name?")
song_input = input()
print("Who's the artist?")
artist_input = input()
song = genius.search_song(song_input, artist_input)

lyrics = song.lyrics
sentence_list = lyrics.split("\n")

for sentence in sentence_list:

    response = openai.Completion.create(
    engine="davinci",
    prompt="My second grader asked me what this passage means with Dave Chappelle comedic tone:\n\"\"\"\n" + sentence,
    temperature=0.5,
    max_tokens=len(lyrics.split()),
    top_p=1,
    frequency_penalty=0.2,
    stop=["\n"]
    )
    print(response.choices[0]["text"])