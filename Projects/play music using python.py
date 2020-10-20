from pygame import mixer

file = 'music.mp3'

mixer.init()
mixer.music.load(file)
mixer.music.play()
