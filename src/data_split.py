from typing import Tuple
import numpy as np
import pandas as pd


from sklearn.model_selection import train_test_split

def train_test_split_stratified(
    df: pd.DataFrame,
    target_column_name: str
) -> Tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
  """
  Performs stratified train-test split on a pandas DataFrame.

  Args:
      df: The pandas DataFrame containing features and target variable.
      target_column_name: The name of the column containing the target variable.

  Returns:
      A tuple containing four elements:
          - X_train: Features for the training set.
          - y_train: Target variable for the training set.
          - X_test: Features for the test set.
          - y_test: Target variable for the test set.
  """
  random_seed = 43 
  X = df.drop(columns=[target_column_name])
  y = df[target_column_name]

  X_train, X_test, y_train, y_test = train_test_split(
      X, y, train_size=0.8, stratify=y, random_state=random_seed)

  return X_train, y_train, X_test, y_test




def transform_churn_data_into_features_and_target(
    churn_data: pd.DataFrame
) -> pd.DataFrame:
    """
    Slices and transposes data into a (features, target)
    format that we can use to train Supervised ML models
    """    
    features = churn_data.columns[:-1]
    targets = churn_data.columns[-1]
    np.random.seed(42)

    # concatenate results
    features = churn_data[features]
    targets = churn_data[targets]

    features.reset_index(inplace=True, drop=True)
    targets.reset_index(inplace=True, drop=True)

    return features, targets