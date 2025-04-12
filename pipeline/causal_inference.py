from causalinference import CausalModel


class CausalInference:
    def __init__(self, df, treatment, outcome, covariates):
        self.df = df.dropna(subset=[treatment, outcome] + covariates)
        self.treatment = treatment
        self.outcome = outcome
        self.covariates = covariates

    def run_psm(self):
        model = CausalModel(
            Y=self.df[self.outcome].values,
            D=self.df[self.treatment].values,
            X=self.df[self.covariates].values
        )
        model.est_propensity()
        model.trim_s()
        model.stratify_s()
        model.est_via_matching()
        return model.estimates
