"""
models.py
Regression models implementation for Hit Song Popularity Prediction.
Includes Multiple Linear Regression, Ridge, Lasso, and Decision Tree Regressors.
"""

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

def get_regression_models(alpha_ridge=10.0, alpha_lasso=0.05, max_depth_tree=8, random_state=42):
    """
    Returns a dictionary of regression models for training and benchmarking:
    - Multiple Linear Regression (baseline OLS)
    - Ridge Regression (L2 regularization)
    - Lasso Regression (L1 regularization)
    - Decision Tree Regressor (non-linear tree model)
    - Random Forest Regressor (ensemble model)
    """
    models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(alpha=alpha_ridge, random_state=random_state),
        'Lasso Regression': Lasso(alpha=alpha_lasso, random_state=random_state),
        'Decision Tree': DecisionTreeRegressor(
            max_depth=max_depth_tree,
            min_samples_leaf=20,
            random_state=random_state
        ),
        'Random Forest': RandomForestRegressor(
            n_estimators=35,
            max_depth=12,
            min_samples_leaf=10,
            random_state=random_state
        )
    }
    return models

def train_and_predict(model, X_train, y_train, X_test):
    """Fit model on train data and predict on test set."""
    model.fit(X_train, y_train)
    preds_train = model.predict(X_train)
    preds_test = model.predict(X_test)
    return preds_train, preds_test
