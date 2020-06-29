import os

from datetime import datetime
from flask import Flask, render_template, request, session, redirect, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from helpers import login_required


app = Flask(__name__)
app.config["SECRET_KEY"] = 'secret'
socketio = SocketIO(app)

channel_list = []

users = []

channel_msg = {}

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    if request.method == "GET":
        alias = session['username']
    
    if request.method == "POST":
        new_channel = request.form.get("channel_name")
        # check if new channel already exists
        if new_channel in channel_list:
            return "ERROR channel name already being used"
        # add new channel to array room_list
        channel_list.append(new_channel)
        alias = session['username']
    return render_template("index.html", channel_list=channel_list, alias=alias)

@app.route("/load_channels")
def load():
    return jsonify({"channel_list": channel_list})

# in socket, first append channel_list, then send new channel to interface to update
@socketio.on("new channel")
def channelList(data):
    selection = data
    if selection in channel_list:
        emit("error")
    else:
        channel_list.append(data)
        channel_msg[selection] = []
        emit("channel list", selection, broadcast=True)

@app.route("/channel/<channel_name>", methods=["GET", "POST"])
def channel(channel_name):
    if request.method == "GET":
        session["current_channel"] = channel_name
        past_messages = channel_msg[channel_name]
        return render_template('channel.html', past_messages=past_messages, channel_name=channel_name)

#shove msges into appropriate arrays within channel_msg dict
#need to put in: channel name, alias, time, and actual msg
@socketio.on("new message")
def newMessage(msg):
    message = msg
    channel_name = session["current_channel"]
    alias = session["username"]
    time = datetime.now().strftime("%m-%d-%Y %I:%M %p")
    msg_dict = {"alias": alias, "message": message, "time": time}
    channel_msg[channel_name].append(msg_dict)
    #cap msgs stored
    if len(channel_msg[channel_name]) > 50:
        del channel_msg[channel_name][0]
    emit("emit message", msg_dict, broadcast=True)
#channel_msg{"channel_name": [array of msg_dicts]}
@app.route("/load_messages")
def load_messages():
    channel_name = session["current_channel"]
    return jsonify({"channel_msg": channel_msg[channel_name]})

@app.route("/alias", methods=["POST", "GET"])
def alias():
    session.clear()
    if request.method == "GET":
        return render_template('alias.html')
    else:
        alias = request.form.get("alias")
        # check if alias is in use
        alias_check = alias.lower()
        if alias_check in users:
            return "ERROR ALIAS ALREADY IN USE"
        else:
            users.append(alias_check)
        session['username'] = alias
        print(session)
        for i in users:
            print(i)
        return redirect('/')

@app.route("/logout")
def logout():
    alias = session['username']
    alias_check = alias.lower()
    users.remove(alias_check)
    session.clear()
    return redirect("/alias")


if __name__ == '__main__':
    socketio.run(app)