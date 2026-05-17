MazeSolver2 : Algorithmes de Recherche Informée et Non-Informée
Ce projet implémente et compare différents algorithmes de recherche pour résoudre des labyrinthes complexes de type grille. L'objectif est d'analyser les performances des algorithmes en termes de coût du chemin, de temps d'exécution et de nombre de nœuds explorés.

🚀 Fonctionnalités
Génération de Labyrinthes : Création de grilles avec obstacles.

Algorithmes implémentés :

Recherche non-informée : BFS (Breadth-First Search) et DFS (Depth-First Search).

Recherche informée : Algorithme A* utilisant la distance de Manhattan comme heuristique.

Visualisation : Comparaison graphique des résultats via Matplotlib (Courbes, diagrammes circulaires et radar).

Analyse Comparative : Évaluation de l'efficacité de chaque méthode.

🛠️ Technologies Utilisées
Langage : Python 3.13

Environnement : Kali Linux (WSL) / VS Code

Bibliothèques :

Matplotlib : Pour la génération des graphiques de performance.

Collections (deque) : Pour la gestion des structures de données (files/piles).

Time : Pour la mesure précise du temps d'exécution.

📂 Structure du Projet
Bash
.
├── main.py              # Point d'entrée de l'application
├── algorithms.py        # Implémentation de BFS, DFS et A*
├── config_maze.py       # Configuration et génération du labyrinthe
├── visualization.py     # Logique de rendu des graphiques
├── Dockerfile           # Configuration pour la conteneurisation
└── README.md            # Documentation du projet
📈 Résultats et Analyse
D'après les tests effectués (visibles dans le rapport), l'algorithme A* s'est révélé être le plus performant pour ce type de problème, offrant le meilleur compromis entre la rapidité et l'optimalité du chemin grâce à l'utilisation de l'heuristique de Manhattan.
