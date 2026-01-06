# 🚀 Déploiement Vercel - Guide Rapide

## ✅ Problème Résolu

Le problème de la page 404 était dû au fait que Vercel ne trouvait pas les templates et fichiers statiques. **Solution : Intégration complète des templates et CSS dans le code Python.**

## 📋 Prérequis

1. **Compte Vercel** : [vercel.com](https://vercel.com)
2. **Repository GitHub** avec ce code
3. **Vercel CLI** (optionnel) : `npm install -g vercel`

## 🚀 Déploiement en 3 étapes

### Étape 1 : Préparer le code
```bash
# Votre code est déjà prêt ! ✅
# - api/index.py : Application Flask optimisée pour Vercel
# - vercel.json : Configuration automatique
# - requirements.txt : Dépendances Python
```

### Étape 2 : Déployer

#### Option A : One-Click (Recommandé)
1. Allez sur [vercel.com/new](https://vercel.com/new)
2. Connectez votre compte GitHub
3. Importez votre repository `devine-le-nombre`
4. Cliquez **"Deploy"** - C'est tout ! 🎉

#### Option B : Via Vercel CLI
```bash
# Installer Vercel CLI
npm install -g vercel

# Se connecter
vercel login

# Déployer
vercel --prod
```

### Étape 3 : Configurer (Optionnel)

Dans le dashboard Vercel, ajoutez la variable d'environnement :
- **Nom** : `SECRET_KEY`
- **Valeur** : `votre-cle-secrete-super-longue-et-complexe`

## 🌐 Accès à votre application

Après déploiement, Vercel vous donne une URL comme :
```
https://devine-le-nombre-[random].vercel.app
```

## 🔧 Fonctionnalités incluses

- ✅ **Application complète** intégrée
- ✅ **Templates HTML** intégrés
- ✅ **CSS et JavaScript** intégrés
- ✅ **Sessions Flask** optimisées pour serverless
- ✅ **Pages d'erreur** 404/500
- ✅ **API REST** pour reset/statistiques
- ✅ **Responsive design** mobile
- ✅ **Historique des parties**
- ✅ **Meilleurs scores**

## 🐛 Dépannage

### Si vous voyez encore une 404 :
1. Vérifiez que `api/index.py` existe
2. Vérifiez que `vercel.json` est à la racine
3. Redéployez : `vercel --prod`

### Si l'application ne charge pas :
1. Vérifiez les logs Vercel dans le dashboard
2. Assurez-vous que `requirements.txt` contient `Flask` et `Werkzeug`

### Pour les sessions :
- Les sessions utilisent des cookies sécurisés
- Elles persistent pendant la session utilisateur
- Les données sont stockées côté client

## 📊 Monitoring

Dans Vercel Dashboard, vous pouvez voir :
- **Analytics** : Visites et performance
- **Logs** : Erreurs et requêtes
- **Functions** : Utilisation serverless

## 🎯 Performance

- **Serverless** : Scaling automatique
- **CDN Global** : Chargement rapide partout
- **Cache intelligent** : Optimisation automatique
- **SSL gratuit** : HTTPS automatique

---

**🎲 Prêt à jouer ? Votre jeu est maintenant en ligne !**