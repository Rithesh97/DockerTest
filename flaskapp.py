from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcom():
    return "Welcome"
    
if __name__=='__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True)
