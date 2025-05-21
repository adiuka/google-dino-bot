# google-dino-bot

Welcome to the google dino bot! Upon executing the program, should open your desired browser, and start playing the dino game to the best of it's abilities. It is not perfect though... Uses pyautogui to achieve this. Uses the dino website to play. [Link](https://elgoog.im/t-rex/)

Currently, I am having issues at around 1000 - 1800 points. THe game speed increases so much, I am unable to make the dino jump faster. 

Things to improve on:
1. I tried using numpy arrays, to check a whole row of pixels if there is an obstacle. That could optimise the script so that even when the speed increases, my dino would be able to make it. That is something I would like to implement somehow.
2. I want to rework the timing mechanism. For now it counts the frequency of the jumps. What could be more interesting is how frequently obstacles are detected, which could increase detection range. Could slow it down, but like I said, as of now the script cannot keep up.

Otherwise enjoy!

![hippo](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmxkbzZ6djR5aDNnaGhzdGRuZzF3dnAwM2Z6Zjh0NW03YzJoZWpseiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SNy3XfJ7p9FCOeISVu/giphy.gif)
