#!/bin/bash

# Script de déploiement pour Devine le Nombre
# Utilisation: ./deploy.sh [local|vercel]

set -e

echo "🎲 Devine le Nombre - Script de déploiement"
echo "=========================================="

MODE=${1:-local}

if [ "$MODE" = "local" ]; then
    echo "🚀 Déploiement en mode local..."

    # Vérifier si Python est installé
    if ! command -v python &> /dev/null; then
        echo "❌ Python n'est pas installé. Veuillez installer Python 3.7+"
        exit 1
    fi

    # Créer l'environnement virtuel s'il n'existe pas
    if [ ! -d "venv" ]; then
        echo "📦 Création de l'environnement virtuel..."
        python -m venv venv
    fi

    # Activer l'environnement virtuel
    echo "🔧 Activation de l'environnement virtuel..."
    source venv/bin/activate  # Pour Linux/Mac
    # Sur Windows, utiliser: venv\Scripts\activate

    # Installer les dépendances
    echo "📥 Installation des dépendances..."
    pip install -r requirements.txt

    # Lancer l'application
    echo "🎮 Démarrage de l'application..."
    echo "📱 Accessible sur: http://127.0.0.1:5000"
    python app.py

elif [ "$MODE" = "vercel" ]; then
    echo "🚀 Déploiement sur Vercel..."

    # Vérifier si Vercel CLI est installé
    if ! command -v vercel &> /dev/null; then
        echo "❌ Vercel CLI n'est pas installé."
        echo "📥 Installation: npm install -g vercel"
        exit 1
    fi

    # Vérifier si connecté à Vercel
    if ! vercel whoami &> /dev/null; then
        echo "🔑 Connexion à Vercel..."
        vercel login
    fi

    # Déployer
    echo "📤 Déploiement sur Vercel..."
    vercel --prod

    echo "✅ Déploiement terminé !"
    echo "🌐 Votre application est maintenant en ligne."

else
    echo "❌ Mode inconnu: $MODE"
    echo "📖 Utilisation: ./deploy.sh [local|vercel]"
    echo "   local  - Déploiement local (par défaut)"
    echo "   vercel - Déploiement sur Vercel"
    exit 1
fi