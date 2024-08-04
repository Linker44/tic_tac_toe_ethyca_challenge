# NOUGHTS AND CROSSES (TIC TAC TOE) - Ethyca Technical Challenge

## IMPORTANT
- the backend rest api was created in 3 hours.
- the frontend application was created in 4 hours. its features are listed as follows:
    - show previous games
    - start a new game
    - play a game
- special features:
    - added a frontend application
    - added win conditions
- trade-offs:
    - to simplify game logic the user always starts as 'X' and the computer as 'O'
    - the frontend application was made with the intention to showcase the api. it has very limited features.

## How to run
 ### Backend
    1. go into the tictactoe directory (backend) and run `pip install requirements.txt` (you can create a venv before installing dependencies)
    2. run `python manage.py migrate`
    3. run `python manage.py runserver`
    4. the backend server runs on **localhost:8000**
 ### Frontend
    1. go into the frontend/tic-tac-toe directory and run `npm install`
    2. run `npm start`
    3. the frontend runs on **localhost:3000**

## REST API DOCS
    - list games `GET URL/` 
    - get game `GET URL/{game-uid}/`
    - create game `POST URL/`
    - make a move `POST URL/{game-uid}/move` data=position ex. {'x': 0, 'y': 0}
    - list moves `GET URL/{game-uid}/list_moves`
    - delete game `DELETE URL/{game-uid}/`

## FEEDBACK
The challenge was very fun to do. I appreciate the time limit being short, as it added a level of urgency and focus to the task. It encouraged me to think quickly and make decisions efficiently.