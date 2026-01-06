from flask import Flask, render_template_string, request, session, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# Configuration pour Vercel
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Templates intégrés pour Vercel
INDEX_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#667eea">
    <meta name="description" content="Jeu de devinette de nombre - Devine le nombre entre 1 et 100">
    <title>Devine le Nombre - Jeu Interactif</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎲</text></svg>">
    <style>
        /* CSS intégré pour Vercel */
        * { margin: 0; padding: 0; box-sizing: border-box; }
        html { scroll-behavior: smooth; }
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-attachment: fixed;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #333;
            overflow-x: hidden;
        }
        .container { width: 100%; max-width: 500px; padding: 0 20px; }
        .card {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.2);
            animation: fadeInUp 0.8s ease-out;
            position: relative;
            overflow: hidden;
        }
        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .header {
            text-align: center;
            margin-bottom: 1.5rem;
            position: relative;
        }
        .header i {
            font-size: 3rem;
            color: #667eea;
            margin-bottom: 1rem;
            display: block;
            animation: bounce 2s infinite;
        }
        @keyframes bounce {
            0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-10px); }
            60% { transform: translateY(-5px); }
        }
        h1 {
            font-size: 2rem;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 1rem;
        }
        .stats {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1rem;
        }
        .stat {
            text-align: center;
        }
        .stat-number {
            display: block;
            font-size: 1.8rem;
            font-weight: 700;
            color: #667eea;
            line-height: 1;
        }
        .stat-label {
            font-size: 0.9rem;
            color: #7f8c8d;
            font-weight: 500;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .subtitle {
            font-size: 1.1rem;
            color: #7f8c8d;
            text-align: center;
            margin-bottom: 2rem;
            font-weight: 400;
        }
        .guess-form {
            margin-bottom: 2rem;
        }
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 1rem;
        }
        input {
            flex: 1;
            padding: 1rem;
            border: 2px solid #e1e8ed;
            border-radius: 12px;
            font-size: 1.1rem;
            font-family: 'Poppins', sans-serif;
            transition: all 0.3s ease;
            outline: none;
            background: rgba(255, 255, 255, 0.9);
        }
        input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            transform: translateY(-2px);
        }
        input:hover { border-color: #556cd6; }
        input::placeholder { color: #bdc3c7; }
        .btn-primary, .btn-secondary {
            padding: 1rem 1.5rem;
            border: none;
            border-radius: 12px;
            font-size: 1.1rem;
            font-weight: 600;
            font-family: 'Poppins', sans-serif;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
            position: relative;
            overflow: hidden;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }
        .btn-primary:active { transform: translateY(0); }
        .btn-primary::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }
        .btn-primary:hover::before { left: 100%; }
        .btn-secondary {
            background: rgba(127, 140, 141, 0.1);
            color: #7f8c8d;
            border: 2px solid rgba(127, 140, 141, 0.2);
            width: 100%;
            justify-content: center;
            margin-top: 1rem;
        }
        .btn-secondary:hover {
            background: rgba(127, 140, 141, 0.2);
            border-color: #7f8c8d;
            color: #34495e;
        }
        .message {
            padding: 1.5rem;
            border-radius: 12px;
            font-weight: 500;
            text-align: center;
            min-height: 4rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            transition: all 0.3s ease;
            margin-bottom: 2rem;
            background: rgba(255, 255, 255, 0.8);
            border: 1px solid rgba(0, 0, 0, 0.05);
        }
        .message-content {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 1.1rem;
        }
        .message-content.welcome {
            color: #7f8c8d;
        }
        .message-content.welcome i { color: #667eea; }
        .game-history {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 1rem;
        }
        .game-history h3 {
            font-size: 1.2rem;
            color: #2c3e50;
            margin-bottom: 1rem;
            text-align: center;
            font-weight: 600;
        }
        .history-list {
            max-height: 200px;
            overflow-y: auto;
            scrollbar-width: thin;
            scrollbar-color: #667eea rgba(255, 255, 255, 0.3);
        }
        .history-list::-webkit-scrollbar { width: 6px; }
        .history-list::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.3);
            border-radius: 3px;
        }
        .history-list::-webkit-scrollbar-thumb {
            background: #667eea;
            border-radius: 3px;
        }
        .history-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.8rem;
            margin-bottom: 0.5rem;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.9);
            border-left: 4px solid;
            animation: slideIn 0.3s ease-out;
        }
        @keyframes slideIn {
            from { opacity: 0; transform: translateX(-20px); }
            to { opacity: 1; transform: translateX(0); }
        }
        .history-item.correct {
            border-left-color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
        }
        .history-item.high {
            border-left-color: #e74c3c;
            background: rgba(231, 76, 60, 0.1);
        }
        .history-item.low {
            border-left-color: #f39c12;
            background: rgba(243, 156, 18, 0.1);
        }
        .guess-number {
            font-weight: 600;
            font-size: 1.1rem;
        }
        .guess-result {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 0.9rem;
        }
        .footer {
            text-align: center;
            margin-top: 2rem;
            color: rgba(255, 255, 255, 0.8);
            font-size: 0.9rem;
        }
        .footer i { color: #e74c3c; }
        /* Responsive */
        @media (max-width: 768px) {
            .card { padding: 2rem 1.5rem; margin: 10px; }
            h1 { font-size: 1.8rem; }
            .header i { font-size: 2.5rem; }
            .subtitle { font-size: 1rem; }
            .stats { gap: 1.5rem; }
            .stat-number { font-size: 1.5rem; }
            .input-group { flex-direction: column; }
            .btn-primary { justify-content: center; }
            input { font-size: 1rem; }
            .message { padding: 1rem; min-height: 3rem; }
            .game-history { padding: 1rem; }
        }
        @media (max-width: 480px) {
            body { padding: 10px; }
            .card { padding: 1.5rem 1rem; }
            h1 { font-size: 1.6rem; }
            .header i { font-size: 2rem; }
            .stats { gap: 1rem; }
            .stat-number { font-size: 1.3rem; }
            .btn-primary, .btn-secondary { padding: 0.9rem 1.2rem; font-size: 1rem; }
        }
        /* Animations */
        .loading { opacity: 0.6; pointer-events: none; }
        .loading::after {
            content: '';
            display: inline-block;
            width: 16px;
            height: 16px;
            border: 2px solid #ffffff;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 1s ease-in-out infinite;
            margin-left: 8px;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
        .success { animation: successPulse 0.6s ease-out; }
        @keyframes successPulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .error { animation: shake 0.5s ease-in-out; }
        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-5px); }
            75% { transform: translateX(5px); }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="card">
            <div class="header">
                <i class="fas fa-dice-six"></i>
                <h1>Devine le Nombre</h1>
                <div class="stats">
                    <div class="stat">
                        <span class="stat-number" id="current-tries">{{ session.get('tries', 0) }}</span>
                        <span class="stat-label">Essais</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number" id="best-score">{{ session.get('best_score', '-') }}</span>
                        <span class="stat-label">Record</span>
                    </div>
                </div>
            </div>

            <p class="subtitle">Choisis un nombre entre 1 et 100</p>

            <form method="POST" class="guess-form" id="guess-form">
                <div class="input-group">
                    <input type="number" name="guess" id="guess" required min="1" max="100" placeholder="Entre 1 et 100" autocomplete="off">
                    <button type="submit" class="btn-primary" id="submit-btn">
                        <i class="fas fa-search"></i>
                        <span class="btn-text">Tester</span>
                    </button>
                </div>
                <button type="button" class="btn-secondary" id="reset-btn">
                    <i class="fas fa-redo"></i>
                    <span>Nouveau Jeu</span>
                </button>
            </form>

            <div class="message" id="message">
                {% if message %}
                    <div class="message-content">{{ message }}</div>
                {% else %}
                    <div class="message-content welcome">
                        <i class="fas fa-gamepad"></i>
                        <span>Prêt à jouer ?</span>
                    </div>
                {% endif %}
            </div>

            <div class="game-history" id="game-history">
                <h3>Derniers essais</h3>
                <div class="history-list" id="history-list">
                    {% if session.get('history') %}
                        {% for guess in session.history %}
                            <div class="history-item {{ 'correct' if guess.correct else ('high' if guess.high else 'low') }}">
                                <span class="guess-number">{{ guess.number }}</span>
                                <span class="guess-result">
                                    {% if guess.correct %}
                                        <i class="fas fa-check"></i> Correct
                                    {% elif guess.high %}
                                        <i class="fas fa-arrow-up"></i> Trop grand
                                    {% else %}
                                        <i class="fas fa-arrow-down"></i> Trop petit
                                    {% endif %}
                                </span>
                            </div>
                        {% endfor %}
                    {% endif %}
                </div>
            </div>
        </div>

        <div class="footer">
            <p>Fait avec <i class="fas fa-heart"></i> en Python Flask</p>
        </div>
    </div>

    <script>
        // JavaScript intégré pour Vercel
        document.addEventListener('DOMContentLoaded', function() {
            const guessForm = document.getElementById('guess-form');
            const guessInput = document.getElementById('guess');
            const submitBtn = document.getElementById('submit-btn');
            const resetBtn = document.getElementById('reset-btn');
            const messageDiv = document.getElementById('message');

            // Validation input
            guessInput.addEventListener('input', function() {
                const value = parseInt(this.value);
                const isValid = value >= 1 && value <= 100 && !isNaN(value);

                if (this.value === '') {
                    this.classList.remove('error');
                    submitBtn.disabled = false;
                } else if (!isValid) {
                    this.classList.add('error');
                    submitBtn.disabled = true;
                } else {
                    this.classList.remove('error');
                    submitBtn.disabled = false;
                }
            });

            // Enter key
            guessInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter' && !submitBtn.disabled) {
                    guessForm.dispatchEvent(new Event('submit'));
                }
            });

            // Form submission
            guessForm.addEventListener('submit', function(e) {
                const value = parseInt(guessInput.value);
                if (value < 1 || value > 100 || isNaN(value)) {
                    e.preventDefault();
                    showError('Veuillez entrer un nombre entre 1 et 100');
                    guessInput.focus();
                    return;
                }

                submitBtn.classList.add('loading');
                submitBtn.innerHTML = '<i class="fas fa-spinner"></i><span class="btn-text">Vérification...</span>';
                submitBtn.disabled = true;
            });

            // Reset button
            resetBtn.addEventListener('click', function() {
                if (confirm('Voulez-vous vraiment commencer une nouvelle partie ?')) {
                    fetch('/reset', { method: 'POST' })
                        .then(() => { location.reload(); })
                        .catch(() => { location.reload(); });
                }
            });

            function showError(message) {
                messageDiv.innerHTML = `<div class="message-content error">${message}</div>`;
                messageDiv.classList.add('error');
                setTimeout(() => { messageDiv.classList.remove('error'); }, 500);
            }

            // Auto-focus
            guessInput.focus();

            // Touch optimization
            if ('ontouchstart' in window) {
                guessInput.addEventListener('focus', function() {
                    this.setAttribute('readonly', 'readonly');
                    setTimeout(() => {
                        this.removeAttribute('readonly');
                        this.focus();
                    }, 100);
                });
            }

            // Keyboard shortcuts
            document.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    guessInput.value = '';
                    guessInput.focus();
                }
                if ((e.ctrlKey || e.metaKey) && e.key === 'Enter' && !submitBtn.disabled) {
                    guessForm.dispatchEvent(new Event('submit'));
                }
            });

            // Button animations
            submitBtn.addEventListener('mousedown', function() { this.style.transform = 'scale(0.98)'; });
            submitBtn.addEventListener('mouseup', function() { this.style.transform = ''; });
            submitBtn.addEventListener('mouseleave', function() { this.style.transform = ''; });
        });
    </script>
</body>
</html>
"""

ERROR_404_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page non trouvée - Devine le Nombre</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #333;
        }
        .error-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 3rem;
            text-align: center;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            max-width: 500px;
            width: 100%;
        }
        .error-icon { font-size: 4rem; color: #e74c3c; margin-bottom: 1rem; }
        h1 { font-size: 2.5rem; color: #2c3e50; margin-bottom: 1rem; }
        p { font-size: 1.1rem; color: #7f8c8d; margin-bottom: 2rem; }
        .btn-home {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .btn-home:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3); }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">🎲</div>
        <h1>404</h1>
        <p>Oups ! La page que vous cherchez n'existe pas.</p>
        <a href="/" class="btn-home">🎮 Retour à l'accueil</a>
    </div>
</body>
</html>
"""

ERROR_500_HTML = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erreur serveur - Devine le Nombre</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
            color: #333;
        }
        .error-container {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 3rem;
            text-align: center;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            max-width: 500px;
            width: 100%;
        }
        .error-icon { font-size: 4rem; color: #e74c3c; margin-bottom: 1rem; }
        h1 { font-size: 2.5rem; color: #2c3e50; margin-bottom: 1rem; }
        p { font-size: 1.1rem; color: #7f8c8d; margin-bottom: 2rem; }
        .error-details {
            background: rgba(231, 76, 60, 0.1);
            border: 1px solid rgba(231, 76, 60, 0.2);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
            font-size: 0.9rem;
            color: #c0392b;
        }
        .btn-home {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 12px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .btn-home:hover { transform: translateY(-2px); box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3); }
    </style>
</head>
<body>
    <div class="error-container">
        <div class="error-icon">🐛</div>
        <h1>500</h1>
        <p>Oups ! Une erreur inattendue s'est produite.</p>
        <div class="error-details">
            <strong>Que faire ?</strong><br>
            • Actualisez la page<br>
            • Vérifiez votre connexion internet<br>
            • Contactez le support si le problème persiste
        </div>
        <a href="/" class="btn-home">🏠 Retour à l'accueil</a>
    </div>
</body>
</html>
"""

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
        session["game_won"] = False

    if request.method == "POST":
        try:
            guess = int(request.form["guess"])

            # Validate input
            if guess < 1 or guess > 100:
                message = "Erreur: Le nombre doit être entre 1 et 100"
            elif session.get("game_won", False):
                message = "Félicitations ! Cliquez sur 'Nouveau Jeu' pour recommencer."
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
                    session["game_won"] = True

                    # Update best score
                    if session["best_score"] is None or session["tries"] < session["best_score"]:
                        session["best_score"] = session["tries"]

                # Add to history (keep last 10 guesses)
                session["history"].append(guess_data)
                if len(session["history"]) > 10:
                    session["history"] = session["history"][-10:]

        except (ValueError, TypeError):
            message = "Erreur: Veuillez entrer un nombre valide"

    # Render with embedded template
    return render_template_string(INDEX_HTML,
                                message=message,
                                session=session)

@app.route("/reset", methods=["POST"])
def reset_game():
    """Reset the current game session"""
    try:
        # Reset all game data for a new game
        session["number"] = random.randint(1, 100)
        session["tries"] = 0
        session["history"] = []
        session["game_won"] = False
        # Keep best_score
        return jsonify({"success": True, "message": "Nouvelle partie commencée"})
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
    return render_template_string(ERROR_404_HTML), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template_string(ERROR_500_HTML), 500

# Pour le développement local
if __name__ == "__main__":
    app.run(debug=True)