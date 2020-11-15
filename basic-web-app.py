from flask import Flask

app = Flask(__name__)

# route
@app.route('/')
# route function
def home():  
  return 'hey!'

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=3000, debug=True)
  
   
