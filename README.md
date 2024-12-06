# aide_decisions

Livrable data visualisation


Aide à la décision pour la prise de positions sur le marché des cryptomonnaies


L'objectif est de créer une aide à la décision pour donner une vision globale, capter des signaux de trading et une prévision à court terme. Le projet se porte sur le cours de trois cryptomonnaies : le Bitcoin, l'Ethereum et le Binance Coin. Le Bitcoin est le premier réseau de blockchain et domine le marché, l'Ethereum est l'alternative au Bitcoin la plus populaire et le Binance Coin a été créé par le courtier Binance.




Sources des données

La première API utilisée est celle de CoinGecko pour importer les données OHLC (Open High Low Close) avec un intervalle de temps de 30 minutes.
La deuxième API utilisée est yfinance pour importer également des données OHLC en ajoutant le volume et pour des périodes hebdomadaire et mensuelle.




Les indicateurs

L'historique des prix permet de comprendre la tendance de long terme grâce aux bougies d'une semaine et d'un mois.

L'historique des volumes est la quantité de monnaie échangée sur une période hebdomadaire et mensuelle. Si le volume est élevé et accompagné d'une tendance haussière, il indique un fort intérêt du côté des acheteurs et inversement.

Les bandes de Bollinger indiquent les périodes de forte volatilité avec les bandes supérieure et inférieure fortement divergentes et inversement pour une volatilité faible, les bandes convergent.

L'indice de force relative (RSI) permet de savoir si le prix se trouve dans une zone de surachat ou de survente. Dans ces cas, il envoie un signal d'inversion de tendance.

La moyenne mobile exponentielle des gains et pertes : si la ligne de l'EMA up est supérieure à celle de l'EMA down, alors la tendance est haussière. Par la suite, si les lignes se croisent, on s'attend à un renversement de tendance.
La prévision utilise une méthode de lissage exponentiel simple pour projeter le prix sur des périodes à venir.

Le tableau de conseil de position est composé de trois éléments : le prix cible (prix le plus haut de la prévision), le prix d'entrée (prix le plus bas de la prévision) et le prix stop (prix d'entrée en retirant 5% de perte du capital).


    
Problèmes rencontrés

- L'API Binance qui empêche la connexion venant d'un serveur localisé aux États-Unis (changement pour yfinance).
- Décalage temporel de l'API CoinGecko, ne donnant pas les dernières périodes en temps réel (version gratuite).
- Problème de performance pour la partie long terme (retrait des graphiques de la période journalière).
- Affichage dynamique des lignes, le cours en premier suivi de la prévision.


  
Axes d'améliorations

- Mettre les commentaires et toutes les variables en anglais (respect de la nomenclature). - Changer l'API CoinGecko pour l'API yfinance pour une meilleure performance.
- Utilisation de fonctions pour le calcul des prévisions.
- Améliorer les modèles de prévision.
