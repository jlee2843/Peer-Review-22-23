from pipeline.pipeline_runner import PipelineRunner

config = {
    'data_path': 'data/peer_review_data.csv',
    'causal': {
        'treatment': 'peer_reviewed',
        'outcome': 'citation_count',
        'covariates': ['semantic_score', 'author_experience']
    },
    'nlp_text_column': 'review_comments'
}

if __name__ == "__main__":
    results = PipelineRunner(config).run()
    print(results)
