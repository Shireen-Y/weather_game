# Make a weather/clothing game
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'

import time
weather = ['sunny', 'stormy', 'rainy', 'rainy and stormy']
print('Please choose from the following:')
time.sleep(0.5)
for key in weather:
    print(key)
    time.sleep(0.5)
weather_response = input('What is the weather like today? ')
if weather_response == (weather[0]):
    print('Do not forget to take your shorts!')
elif weather_response == (weather[1]):
    print('Take rain coat')
elif weather_response == (weather[2]):
    print('Do not forget to take your umbrella')
elif weather_response == (weather[3]):
    print('Just stay at home buddy :|')
else:
    print('Sorry I did not quite catch that')