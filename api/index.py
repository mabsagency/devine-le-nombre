from flask import Flask, render_template, request, session, jsonify
import random
import os

app = Flask(__name__,
            static_folder='../static',
            template_folder='../templates')

# Configuration pour Vercel
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
app.config['SESSION_TYPE'] = 'filesystem'

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    # Initialize session variables if not exist
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["tries"] = 0
        session["history"] = []
        if "best_score" not in session:
            session["best_score"] = None

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])

            # Validate input
            if guess < 1 or guess > 100:
                message = "Erreur: Le nombre doit être entre 1 et 100"
            else:
                session["tries"] += 1

                # Track guess in history
                guess_data = {
                    "number": guess,
                    "correct": False,
                    "high": False,
                    "low": False
                }

                if guess < session["number"]:
                    message = "Trop petit 📉"
                    guess_data["low"] = True
                elif guess > session["number"]:
                    message = "Trop grand 📈"
                    guess_data["high"] = True
                else:
                    message = f"Bravo 🎉 Trouvé en {session['tries']} essais !"
                    guess_data["correct"] = True

                    # Update best score
                    if session["best_score"] is None or session["tries"] < session["best_score"]:
                        session["best_score"] = session["tries"]

                    # Reset for new game after success
                    session.pop("number", None)
                    session.pop("tries", None)

                # Add to history (keep last 10 guesses)
                session["history"].append(guess_data)
                if len(session["history"]) > 10:
                    session["history"] = session["history"][-10:]

        except (ValueError, TypeError):
            message = "Erreur: Veuillez entrer un nombre valide"

    return render_template("index.html", message=message)

@app.route("/reset", methods=["POST"])
def reset_game():
    """Reset the current game session"""
    try:
        # Clear game-specific session data
        session.pop("number", None)
        session.pop("tries", None)
        session.pop("history", None)
        # Keep best_score
        return jsonify({"success": True, "message": "Partie réinitialisée"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@app.route("/stats")
def get_stats():
    """Get current game statistics"""
    stats = {
        "current_tries": session.get("tries", 0),
        "best_score": session.get("best_score"),
        "has_active_game": "number" in session,
        "history_count": len(session.get("history", []))
    }
    return jsonify(stats)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500

# Pour Vercel, on exporte l'app
def handler(event, context):
    """Handler pour Vercel serverless functions"""
    from werkzeug.middleware.dispatcher import DispatcherMiddleware
    from werkzeug.serving import WSGIRequestHandler

    # Retourner l'app Flask pour Vercel
    return app

# Pour le développement local
if __name__ == "__main__":
    app.run(debug=True)