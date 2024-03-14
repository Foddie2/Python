from pygame import mixer
from gtts import gTTS

def main():
   tts = gTTS('I love coding in Python and Javascript I also love frameworks like vue and NuxtJS')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   main()