# 🎲 Devine le Nombre

Un jeu web interactif et responsive où vous devez deviner un nombre entre 1 et 100.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/your-username/devine-le-nombre)

## ✨ Fonctionnalités

### 🎮 Gameplay
- **Devinez le nombre** : Entrez un nombre entre 1 et 100
- **Indices intelligents** : "Trop petit 📉" ou "Trop grand 📈"
- **Compteur d'essais** : Suivez vos tentatives
- **Historique des essais** : Visualisez vos dernières tentatives

### 📊 Statistiques
- **Meilleur score** : Suivi de votre record personnel
- **Essais actuels** : Nombre de tentatives pour la partie en cours
- **Historique détaillé** : Liste des derniers essais avec indicateurs visuels

### 🎨 Interface
- **Design moderne** : Interface avec effets de verre (glassmorphism)
- **Responsive** : Optimisé pour mobile, tablette et desktop
- **Animations fluides** : Transitions et animations CSS modernes
- **Accessibilité** : Support clavier et navigation intuitive

## 🚀 Déploiement sur Vercel

### Méthode 1: One-Click Deploy (Recommandé)

1. **Cliquez sur le bouton "Deploy with Vercel"** ci-dessus
2. **Connectez-vous** à votre compte Vercel (ou créez-en un gratuitement)
3. **Importez le repository** GitHub (ou utilisez le déploiement direct)
4. **Vercel configure automatiquement** tout pour vous !

### Méthode 2: Via Vercel CLI

```bash
# Installer Vercel CLI
npm install -g vercel

# Se connecter
vercel login

# Déployer en développement
vercel

# Déployer en production
vercel --prod
```

### Méthode 3: Manuel

1. **Créez un repository GitHub** avec ce code
2. **Connectez-vous à Vercel**
3. **Importez votre repository**
4. **Vercel détecte automatiquement** la configuration Python/Flask

## 🛠️ Installation Locale

### Prérequis
- Python 3.7+
- pip

### Installation
```bash
# Cloner le repository
git clone <repository-url>
cd devine_le_nombre

# Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python app.py
```

**Accès local :** `http://127.0.0.1:5000`

## 🎯 Comment Jouer

1. **Entrez un nombre** entre 1 et 100
2. **Cliquez "Tester"** ou appuyez sur Entrée
3. **Suivez les indices** : 📉 Trop petit / 📈 Trop grand
4. **Gagnez** et battez votre record !
5. **Rejouez** avec "Nouveau Jeu"

## 🏗️ Architecture pour Vercel

```
devine_le_nombre/
├── api/index.py          # ⚡ Point d'entrée Vercel (serverless)
├── vercel.json           # ⚙️ Configuration Vercel
├── requirements.txt      # 📦 Dépendances Python
├── app.py                # 🏠 Application locale
├── templates/            # 🎨 Templates HTML
├── static/               # 🎨 CSS & JavaScript
└── README.md            # 📖 Documentation
```

## 🔧 Configuration Vercel

Le projet est pré-configuré avec :

- **Serverless Functions** : `api/index.py`
- **Routes automatiques** : Toutes les routes gérées
- **Python 3.9** : Runtime optimisé
- **Static Files** : Servis automatiquement

## 🌟 Avantages Vercel

- ⚡ **Déploiement instantané**
- 🌍 **CDN global** pour rapidité
- 🔒 **HTTPS automatique**
- 📊 **Analytics intégrés**
- 🎯 **Scaling automatique**
- 💰 **Gratuit** pour ce type d'application

## 🎮 Testez l'Application

**Version démo :** [devine-le-nombre.vercel.app](https://devine-le-nombre.vercel.app)

## 🤝 Contribution

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez (`git commit -m 'Add some AmazingFeature'`)
4. Pushez (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📄 Licence

Sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Prêt à deviner ? 🎲✨**

[![Powered by Vercel](https://www.datocms-assets.com/31049/1618983297-powered-by-vercel.svg)](https://vercel.com)