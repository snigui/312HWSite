from flask import Flask, render_template
app = Flask('app')

@app.route('/game')
def game():
   return render_template('/TreasureHunter.html')

@app.route('/')
def main():
   return render_template('/main.html')   

app.run(host='0.0.0.0', port=8080)