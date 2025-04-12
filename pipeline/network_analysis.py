import networkx as nx


class NetworkAnalysis:
    def __init__(self, df, source_col, target_col):
        self.graph = nx.from_pandas_edgelist(df, source=source_col, target=target_col)

    def calculate_centrality(self):
        return {
            'degree_centrality': nx.degree_centrality(self.graph),
            'betweenness_centrality': nx.betweenness_centrality(self.graph)
        }

    def detect_communities(self):
        return list(nx.community.greedy_modularity_communities(self.graph))
