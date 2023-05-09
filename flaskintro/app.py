from flask import Flask
from flask import render_template

app = Flask(__name__)

#Using a decorator to bind root URL to a function, i.e. navigating to root page, will execute the 
#following function, which will load the hello.html page
@app.route("/")
def hello_world(name=None):

    #Perform some SQL

    return render_template('index.html', name='Emlily')


#Checks if scripts is executed directly from command line
if __name__ == "__main__":
    app.run(debug=True)


