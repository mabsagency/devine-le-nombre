# 🎲 Devine le Nombre

Un jeu web interactif et responsive où vous devez deviner un nombre entre 1 et 100.

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
- **Thème sombre/clair** : Adaptation automatique
- **Accessibilité** : Support clavier et navigation intuitive

### 🚀 Fonctionnalités Techniques
- **Validation côté client** : JavaScript pour une expérience fluide
- **API REST** : Endpoints pour réinitialisation et statistiques
- **Gestion d'erreurs** : Pages d'erreur personnalisées (404, 500)
- **Performance** : Code optimisé et chargement rapide
- **Sécurité** : Validation des entrées et protection CSRF

## 🛠️ Installation

### Prérequis
- Python 3.7+
- pip

### Installation rapide
```bash
# Cloner le repository
git clone <repository-url>
cd devine_le_nombre

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install flask

# Lancer l'application
python app.py
```

### Accès
Ouvrez votre navigateur à l'adresse : `http://127.0.0.1:5000`

## 🎯 Comment jouer

1. **Commencer** : Un nombre entre 1 et 100 est généré aléatoirement
2. **Deviner** : Entrez votre estimation dans le champ
3. **Valider** : Cliquez sur "Tester" ou appuyez sur Entrée
4. **Indices** : Suivez les indications pour affiner votre recherche
5. **Victoire** : Félicitations quand vous trouvez le nombre !
6. **Rejouer** : Cliquez sur "Nouveau Jeu" pour recommencer

## ⌨️ Raccourcis clavier

- **Entrée** : Valider la saisie
- **Ctrl/Cmd + Entrée** : Soumettre rapidement
- **Échap** : Effacer le champ de saisie

## 📱 Support mobile

- **Touch optimisé** : Boutons adaptés aux écrans tactiles
- **Responsive** : Interface qui s'adapte à toutes les tailles d'écran
- **Performance** : Chargement rapide même sur mobile

## 🏗️ Architecture

```
devine_le_nombre/
├── app.py                 # Application Flask principale
├── templates/
│   ├── index.html        # Page principale du jeu
│   ├── 404.html          # Page d'erreur 404
│   └── 500.html          # Page d'erreur 500
└── static/
    ├── style.css         # Styles CSS modernes
    └── script.js         # JavaScript interactif
```

## 🔧 API Endpoints

- `GET /` : Page principale du jeu
- `POST /` : Soumettre une estimation
- `POST /reset` : Réinitialiser la partie
- `GET /stats` : Obtenir les statistiques actuelles

## 🚀 Déploiement

### Variables d'environnement
```bash
export SECRET_KEY="votre-cle-secrete"
export PORT=5000
```

### Production
Pour un déploiement en production, utilisez un serveur WSGI comme Gunicorn :

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- Signaler des bugs
- Proposer des améliorations
- Soumettre des pull requests

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.

## 🙏 Remerciements

- **Flask** : Framework web Python
- **Font Awesome** : Icônes vectorielles
- **Google Fonts** : Police Poppins
- **Animate.css** : Animations CSS

---

**Amusez-vous bien en devinant le nombre ! 🎲✨**