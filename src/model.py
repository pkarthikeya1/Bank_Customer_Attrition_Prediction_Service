from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import make_pipeline, Pipeline
from sklearn.preprocessing import LabelEncoder, StandardScaler

import lightgbm as lgb


class CustomLabelEncode(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X,y=None):
        X_=X.copy()
        cat_cols = X_.select_dtypes(include='object').columns.to_list()
        le=LabelEncoder()   
        for i in X_[cat_cols]:
            X_[i]=le.fit_transform(X_[i])
        return X_



def get_pipeline(**hyperparams) -> Pipeline:
    
    # sklearn transform
    add_label_encoding = CustomLabelEncode()

    # sklearn pipeline
    return make_pipeline(
        add_label_encoding,
        lgb.LGBMClassifier(**hyperparams)
    )