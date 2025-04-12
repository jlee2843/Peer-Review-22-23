import pandas as pd

from pipeline.predictive_modeling import PredictiveModeling


def test_model_training():
    df = pd.DataFrame({
        'feature1': [0.1, 0.2, 0.3, 0.4],
        'feature2': [1, 0, 1, 0],
        'target': [1, 0, 1, 0]
    })
    model = PredictiveModeling(df, ['feature1', 'feature2'], 'target')
    report = model.train_model()
    assert 'accuracy' in report
