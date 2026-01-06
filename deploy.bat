@echo off
REM Script de déploiement pour Devine le Nombre (Windows)
REM Utilisation: deploy.bat [local|vercel]

echo 🎲 Devine le Nombre - Script de déploiement
echo ==========================================

if "%1"=="" (
    set MODE=local
) else (
    set MODE=%1
)

if "%MODE%"=="local" (
    echo 🚀 Déploiement en mode local...

    REM Vérifier si Python est installé
    python --version >nul 2>&1
    if errorlevel 1 (
        echo ❌ Python n'est pas installé. Veuillez installer Python 3.7+
        pause
        exit /b 1
    )

    REM Créer l'environnement virtuel s'il n'existe pas
    if not exist "venv" (
        echo 📦 Création de l'environnement virtuel...
        python -m venv venv
    )

    REM Activer l'environnement virtuel
    echo 🔧 Activation de l'environnement virtuel...
    call venv\Scripts\activate.bat

    REM Installer les dépendances
    echo 📥 Installation des dépendances...
    pip install -r requirements.txt

    REM Lancer l'application
    echo 🎮 Démarrage de l'application...
    echo 📱 Accessible sur: http://127.0.0.1:5000
    python app.py

) else if "%MODE%"=="vercel" (
    echo 🚀 Déploiement sur Vercel...

    REM Vérifier si Vercel CLI est installé
    vercel --version >nul 2>&1
    if errorlevel 1 (
        echo ❌ Vercel CLI n'est pas installé.
        echo 📥 Installation: npm install -g vercel
        pause
        exit /b 1
    )

    REM Vérifier si connecté à Vercel
    vercel whoami >nul 2>&1
    if errorlevel 1 (
        echo 🔑 Connexion à Vercel...
        vercel login
    )

    REM Déployer
    echo 📤 Déploiement sur Vercel...
    vercel --prod

    echo ✅ Déploiement terminé !
    echo 🌐 Votre application est maintenant en ligne.

) else (
    echo ❌ Mode inconnu: %MODE%
    echo 📖 Utilisation: deploy.bat [local|vercel]
    echo    local  - Déploiement local (par défaut)
    echo    vercel - Déploiement sur Vercel
    pause
    exit /b 1
)