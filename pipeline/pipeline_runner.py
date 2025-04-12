from pipeline.advanced_nlp import AdvancedNLP
from pipeline.causal_inference import CausalInference
from pipeline.data_manager import DataManager


class PipelineRunner:
    def __init__(self, config):
        self.config = config

    def run(self):
        df = DataManager(self.config['data_path']).load_data()

        # Run Causal Inference
        causal = CausalInference(df, **self.config['causal'])
        causal_results = causal.run_psm()

        # Run NLP
        nlp = AdvancedNLP()
        nlp_results = nlp.analyze_sentiments(df[self.config['nlp_text_column']].dropna().tolist())

        return {'causal': causal_results, 'nlp': nlp_results}
