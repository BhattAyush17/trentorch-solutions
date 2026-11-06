import numpy as np


def kmeans_empty_cluster_update(
    points: np.ndarray,
    assignments: np.ndarray,
    old_centroids: np.ndarray,
    k: int,
) -> np.ndarray:

    points = np.asarray(points, dtype=float)
    assignments = np.asarray(assignments, dtype=int)
    old_centroids = np.asarray(old_centroids, dtype=float)

    new_centroids = old_centroids.copy()

    for cluster_id in range(k):
        cluster_points = points[assignments == cluster_id]

        if len(cluster_points) > 0:
            new_centroids[cluster_id] = np.mean(
                cluster_points, axis=0
            )

    return new_centroids
