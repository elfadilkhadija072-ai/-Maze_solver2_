# main.py
import pandas as pd

from config_maze import generate_maze, initialize_path, width, height, start, goal
from algorithms import bfs, dfs, a_star, gbfs, heuristic
from visualization import (
    plot_step_metrics,
    plot_radar_chart,
    plot_boxplots,
    plot_pie_charts,
    plot_performance_comparison
)

# Génération du labyrinthe (une seule fois, partagé par tous)
path = []
path = initialize_path(path, width, height)
maze = generate_maze(width, height, path, start, goal)

# Dictionnaire des algorithmes
algorithms = {
    'BFS':  lambda s, g: bfs(s, g, maze),
    'DFS':  lambda s, g: dfs(s, g, maze),
    'A*':   lambda s, g: a_star(s, g, maze, heuristic),
    'GBFS': lambda s, g: gbfs(s, g, maze, heuristic),
}

def run_experiments(algorithms, runs=10):
    results = []
    for name, algo in algorithms.items():
        for _ in range(runs):
            path_found, metrics = algo(start, goal)
            results.append({
                'Algorithm':   name,
                'Time':        metrics['time'][-1],
                'Memory':      metrics['memory'][-1],
                'Path Length': len(path_found),
                'Step Times':  metrics['time'],
                'Step Memory': metrics['memory'],
            })
    return pd.DataFrame(results)

if __name__ == "__main__":
    df = run_experiments(algorithms, runs=10)

    stats = df.groupby('Algorithm').agg({
        'Time':        ['mean', 'std'],
        'Memory':      ['mean', 'std'],
        'Path Length': ['mean', 'std'],
    })
    print(stats)

    plot_step_metrics(df)
    plot_radar_chart(df)
    plot_boxplots(df)
    plot_pie_charts(stats)
    plot_performance_comparison(stats)