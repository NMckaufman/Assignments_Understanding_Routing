from flask import Flask
routing= Flask(__name__)

#Create a root route ("/") that responds with "Hello World!"
@routing.route('/')

def Hello_World():
    return 'Hello World!'

#Create a route that responds with "Dojo!"
@routing.route('/dojo')
def Dojo():
    return 'Dojo'

#Create a route that responds with "Hi" and whatever name is in the URL after /say/

#NINJA BONUS: Ensure the names provided in the 3rd task are strings
@routing.route('/say/<name>')
def hi(name):
    return 'Hi, '+ name

#Create a route that responds with the given word repeated as many times as specified in the URL
@routing.route('/repeat/<int:num>/<string:potato>')
def multiply (num,potato):
    return num * potato


if __name__=="__main__":

    routing.run(debug=True)