import statsmodels.api as sm


class MetaAnalysis:
    def __init__(self, effect_sizes, variances):
        self.effect_sizes = effect_sizes
        self.variances = variances

    def run_meta_analysis(self):
        return sm.stats.meta_analysis(self.effect_sizes, self.variances, method='random')
