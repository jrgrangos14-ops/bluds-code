from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        d1 = int(request.form.get("d1", 0))
        d2 = int(request.form.get("d2", 0))
        result = "Shot Enemy 1!" if d1 < d2 else "Shot Enemy 2!"
    return f'''
    <h2>Mini Onboarding Game</h2>
    <form method="POST">
      Enemy 1 Distance: <input type="number" name="d1" required><br>
      Enemy 2 Distance: <input type="number" name="d2" required><br>
      <button type="submit">Shoot Closest</button>
    </form>
    <p>{result}</p>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
