
from app import app
from flask import render_template, redirect, request
from models.game import *
from models.player import *
from models.players import *

@app.route('/game')
def index():
    return render_template('play_game.html', players=players)

@app.route("/game/<player1>/<player2>")
# def run_game(player_choice1, player_choice2):

def play(player1, player2):

    player_one = Player("Player_1", player1)
    player_two = Player("Player_2", player2)

    play(player_one, player_two)

    # if player1 == "Rock" and player2 == "Scissors":
    #     return f"Player1 is the winner by playing {player1}"

    # if player1 == "Scissors" and player2 == "Paper":
    #     return f"Player1 is the winner by playing {player1}"

    # if player1 == "Paper" and player2 == "Rock":
    #     return f"Player1 is the winner by playing {player1}"

    # if player1 == "Rock" and player2 == "Paper":
    #     return f"Player2 is the winner by playing {player2}"

    # if player1 == "Scissors" and player2 == "Rock":
    #     return f"Player2 is the winner by playing  {player2}"

    # if player1 == "Paper" and player2 == "Scissors":
    #     return f"Player2 is the winner by playing {player2}"

    # if player1 == player2:
    #     return "It was a draw"
        # return None <--crashes
    # return render_template("/game/results.html")

@app.route("/game", methods=["POST"])
def play_new_game():
    name1 = request.form["name1"]
    choice1 = request.form["choice1"]
    name2 = request.form["name2"]
    choice2 = request.form["choice2"]
    new_player1 = Player(name1, choice1)
    new_player2 = Player(name2, choice2)
    play(new_player1, new_player2)
    return redirect('/game')

@app.route("/game/new_game")
def new_game_form():
    return render_template('new_game.html')

@app.route("/game/players")
def list_of_players():
    return render_template("players.html", players=players)

@app.route("/game/results")
def results_list():
    return render_template("results.html", players=players)

    # name = request.form['name']
    # choice = request.form['choice']
    # player_one = Player(name, choice)
    # player_two = Player(name, choice)



    # return redirect("/game")

    # player1 = Player("Player1", player_choice1)
    # player2 = Player("Player2", player_choice2)
    # winner = play(player1, player2)
    # print(winner)


    # player1 = players[]

    # choice1 = player_choice1
    # choice2 = player_choice2
    
    # for player1, player2 in players:
    #     if player1.choice == player_choice1 and player2.choice == player_choice2:
    #         return play(player1, player2)
    #     return "Please try again"

    # for player2 in players:
    #     if player2.choice == player_choice2:
    #         return player2
    #     return "Please try again"

    # play(player1, player2)
            
        # elif player.choice == player_choice2:
        #     return "pass2"
        # return "Please try again"
    # player1 = player
    # return redirect("/game")
    # return render_template("play_game.html")



    
    # event_to_delete = events[int(index)]
    # delete_old_event(event_to_delete)
    # return redirect("/events")