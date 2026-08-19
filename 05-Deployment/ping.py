from flask import Flask

app = Flask('ping')

#add a decorator - a way to add extra functionality 
# This will allows us to turn it into a web service
# It will live in the ping address, methods - how to access this address ; use the GET method
# https://www.w3schools.com/tags/ref_httpmethods.asp


@app.route('/ping', methods=['GET'])

def ping():
    return "PONG"

#we run the app in the debug mode
# host is local host which 0.0.0.0
# refer https://docs.python.org/3/library/__main__.html

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    app.run(host= '127.0.0.1', debug=True, port=9696)           
            #replaced this address host='0.0.0.0' 