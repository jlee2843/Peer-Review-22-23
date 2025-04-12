import numpy as np

from pipeline.meta_analysis import MetaAnalysis


def test_meta_analysis_output():
    effect_sizes = np.array([0.2, 0.5, 0.3])
    variances = np.array([0.04, 0.01, 0.02])
    analysis = MetaAnalysis(effect_sizes, variances)
    result = analysis.run_meta_analysis()
    assert hasattr(result, 'summary_frame')
