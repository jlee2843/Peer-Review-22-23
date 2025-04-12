import pandas as pd

from pipeline.network_analysis import NetworkAnalysis


def test_network_centrality():
    df = pd.DataFrame({
        'source': ['A', 'B', 'C'],
        'target': ['B', 'C', 'A']
    })
    analysis = NetworkAnalysis(df, 'source', 'target')
    centrality = analysis.calculate_centrality()
    assert 'degree_centrality' in centrality
