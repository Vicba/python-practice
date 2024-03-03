# Adapter Pattern

1. What is it?

   The Adapter Pattern is like a language translator for your code. Imagine you have a friend who speaks only French, but you have a message in English. An adapter helps you understand each other by translating the message.

2. What is its purpose?

   The purpose of the Adapter Pattern is to make different classes work together smoothly. It acts as a bridge between two incompatible interfaces, allowing them to cooperate without changing their code.

3. When to use this?

   Use the Adapter Pattern when you have two pieces of code that can't talk directly because they have different interfaces (like speaking different languages). If you want them to work together without modifying their original code, an adapter helps them understand each other.

4. Small Code example

   Let's say you have a music player that plays music in MP3 format, but you find an awesome new music source that provides music in a different format, like WAV. Instead of changing your music player's code, you create an adapter that translates the new music format into something your player understands.

```python
# Existing MP3 Player
class MP3Player:
    def play_mp3(self, file):
        print(f"Playing MP3 file: {file}")

# New Music Source in WAV format
class WAVPlayer:
    def play_wav(self, file):
        print(f"Playing WAV file: {file}")

# Adapter to make WAVPlayer work with MP3Player
class WAVAdapter:
    def __init__(self, wav_player):
        self.wav_player = wav_player

    def play_mp3(self, file):
        # Convert MP3 play request into WAV format
        print(f"Converting MP3 to WAV and playing: {file}")
        self.wav_player.play_wav(file)

# Using the adapted WAVPlayer with the MP3Player
mp3_player = MP3Player()
wav_player = WAVPlayer()
adapter = WAVAdapter(wav_player)

# Now you can play WAV files with the MP3 player using the adapter
adapter.play_mp3("awesome_song.wav")
```

In this example, the WAVAdapter allows the MP3 player to understand and play WAV files from the new music source without changing the original MP3 player code.
