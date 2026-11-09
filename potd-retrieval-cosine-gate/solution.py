import numpy as np


def retrieval_cosine_gate(query: np.ndarray, documents: np.ndarray) -> np.ndarray:
    """
    query: array of shape (d,).
    documents: array of shape (n, d).

    Returns an array of shape (n,): cosine similarity between query and
    each document row. If either the query or a document has zero norm,
    that document's similarity is 0.
    """
    # TODO: compute dot(query, doc) / (||query|| * ||doc||) per document,
    # guarding against zero norms.
    query = np.asarray(query, dtype=float)
    documents = np.asarray(documents, dtype=float)

    query_norm = np.linalg.norm(query)
    document_norms = np.linalg.norm(documents, axis=1)

    dot_products = documents @ query

    denominators = query_norm * document_norms

    similarities = np.zeros(len(documents), dtype=float)

    valid = denominators > 0
    similarities[valid] = dot_products[valid] / denominators[valid]

    return similarities
    pass
