import picamera
from picamera import Color
from time import sleep
import RPi.GPIO as GPIO
import pygame

import phototweet
import photoMerge as merge

from gpiozero import Button
button = Button(2)


pygame.init()
black = 0,0,0
white = 255,255,255
infoObject = pygame.display.Info()
newWidth = infoObject.current_w
newHeight = infoObject.current_h - 100
windowSize = width, height = newWidth, newHeight
screen = pygame.display.set_mode(windowSize)
myfont = pygame.font.Font(None, 600)
labelPOS = (newWidth / 2, newHeight / 3)

message = 'Tweeting another photo!'
finalPhotoName = 'imgmerge.jpg'

with picamera.PiCamera() as camera:
      camera.rotation = 180
      camera.resolution = (1280, 1024)
      camera.start_preview(fullscreen=False, window = (150, 110, 1680, 1050))
      camera.annotate_text_size = 45
      camera.annotate_background = Color('white')
      camera.annotate_foreground = Color('green')
      camera.annotate_text = 'Daugherty SA&E Summit 2019'
      screen.fill(black)
      camera.preview.alpha = 228
      #GPIO.wait_for_edge(17, GPIO.FALLING)
      while(True):
          button.wait_for_press()
          shot = 0
          while shot < 2:
                #GPIO.output(GREEN_LED,True)
                for x in range (3, 0 , -1):
                     label = myfont.render(str(x),1,white)
                     screen.blit(label, labelPOS)
                     sleep(1)
                     pygame.display.flip()
                     screen.fill(black)
                #GPIO.output(GREEN_LED,False)
                sleep(1)
                pygame.display.flip()
                photoName = 'img(%d).jpg' % shot
                if(shot > 0):
                    camera.annotate_text = ''
                camera.capture(photoName)
                shot += 1
                screen.fill(black)
          merge.smash()
          phototweet.postTweets(finalPhotoName, message)
      camera.stop_preview()
      pygame.display.quit()
      pygame.quit()
