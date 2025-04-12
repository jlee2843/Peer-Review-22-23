import xgboost as xgb
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


class PredictiveModeling:
    def __init__(self, df, features, target):
        self.X = df[features]
        self.y = df[target]

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size=0.3)
        model = xgb.XGBClassifier()
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        return classification_report(y_test, preds, output_dict=True)
