"""
evaluate.py
Evaluation metrics, statistical reporting, and visual plotting for regression models.
Computes R2, RMSE, MAE, generates Actual vs Predicted, Residual Plots,
Correlation Heatmaps, and Feature Importance charts.
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import r2_score, root_mean_squared_error, mean_absolute_error

# Configure visual style
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.sans-serif': 'Arial', 'font.size': 11})

def calculate_metrics(y_true, y_pred):
    """Compute R2 Score, RMSE, and MAE."""
    r2 = r2_score(y_true, y_pred)
    rmse = root_mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    return {'R2': r2, 'RMSE': rmse, 'MAE': mae}

def plot_correlation_heatmap(df, feature_cols, target_col='popularity', save_path='outputs/correlation_matrix.png'):
    """Plot correlation heatmap of audio features with track popularity."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cols = [target_col] + [c for c in feature_cols if c != target_col]
    corr = df[cols].corr()

    plt.figure(figsize=(11, 8.5))
    mask = np.triu(np.ones_like(corr, dtype=bool))
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        cbar_kws={'label': 'Pearson Correlation Coefficient'}
    )
    plt.title("Audio Features & Track Popularity Correlation Matrix", fontsize=14, weight='bold', pad=15)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved correlation heatmap to {save_path}")

def plot_actual_vs_predicted(y_test, predictions_dict, save_path='outputs/actual_vs_predicted.png'):
    """Plot Actual vs Predicted Popularity scores across multiple models."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    models = list(predictions_dict.keys())
    n_models = len(models)
    
    fig, axes = plt.subplots(1, n_models, figsize=(5 * n_models, 4.5), sharey=True)
    if n_models == 1:
        axes = [axes]
        
    for ax, (model_name, y_pred) in zip(axes, predictions_dict.items()):
        # Sample for cleaner visualization if test set is large
        sample_indices = np.random.RandomState(42).choice(len(y_test), size=min(1500, len(y_test)), replace=False)
        y_test_samp = np.array(y_test)[sample_indices]
        y_pred_samp = np.array(y_pred)[sample_indices]
        
        ax.scatter(y_test_samp, y_pred_samp, alpha=0.35, color='#1DB954', edgecolors='none', s=25)
        ax.plot([0, 100], [0, 100], 'r--', lw=2, label='Ideal Fit (y=x)')
        r2 = r2_score(y_test, y_pred)
        rmse = root_mean_squared_error(y_test, y_pred)
        
        ax.set_title(f"{model_name}\n$R^2$ = {r2:.3f} | RMSE = {rmse:.2f}", fontsize=11, weight='bold')
        ax.set_xlabel("Actual Popularity (0-100)")
        ax.set_xlim(-5, 105)
        ax.set_ylim(-5, 105)
        ax.legend(loc='upper left', frameon=True)

    axes[0].set_ylabel("Predicted Popularity (0-100)")
    fig.suptitle("Actual vs. Predicted Popularity Comparison", fontsize=15, weight='bold', y=1.03)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved actual vs predicted plot to {save_path}")

def plot_residual_analysis(y_test, predictions_dict, save_path='outputs/residual_plots.png'):
    """Plot Residuals vs Fitted values and residual distribution histograms."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    models = list(predictions_dict.keys())
    n_models = len(models)

    fig, axes = plt.subplots(2, n_models, figsize=(4.5 * n_models, 8))
    if n_models == 1:
        axes = np.array([[axes[0]], [axes[1]]])

    for i, (model_name, y_pred) in enumerate(predictions_dict.items()):
        residuals = np.array(y_test) - np.array(y_pred)
        
        # Row 1: Residuals vs Fitted
        sample_indices = np.random.RandomState(42).choice(len(y_test), size=min(1500, len(y_test)), replace=False)
        axes[0, i].scatter(
            np.array(y_pred)[sample_indices],
            residuals[sample_indices],
            alpha=0.35,
            color='#2b5c8f',
            s=22
        )
        axes[0, i].axhline(0, color='red', linestyle='--', lw=2)
        axes[0, i].set_title(f"{model_name}\nResiduals vs Fitted", fontsize=11, weight='bold')
        axes[0, i].set_xlabel("Fitted (Predicted) Popularity")
        axes[0, i].set_ylabel("Residuals ($y - \\hat{y}$)" if i == 0 else "")
        
        # Row 2: Residual Distribution
        sns.histplot(residuals, kde=True, ax=axes[1, i], color='#e74c3c', bins=35)
        axes[1, i].axvline(0, color='black', linestyle=':', lw=1.5)
        axes[1, i].set_title(f"Residual Distribution\nMean: {np.mean(residuals):.2f}, Std: {np.std(residuals):.2f}", fontsize=10)
        axes[1, i].set_xlabel("Residual Value")
        axes[1, i].set_ylabel("Count" if i == 0 else "")

    fig.suptitle("Comprehensive Residual Analysis Across Models", fontsize=15, weight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Saved residual plots to {save_path}")

def plot_feature_importance_or_coefficients(model, feature_names, model_name, save_path='outputs/feature_importance.png'):
    """Plot regression coefficients or tree feature importances."""
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.figure(figsize=(9, 5.5))

    if hasattr(model, 'coef_'):
        values = model.coef_
        metric_name = "Standardized Coefficient (Weights)"
        title = f"{model_name} - Feature Coefficients"
        colors = ['#2ecc71' if v > 0 else '#e74c3c' for v in values]
    elif hasattr(model, 'feature_importances_'):
        values = model.feature_importances_
        metric_name = "Gini Feature Importance"
        title = f"{model_name} - Feature Importances"
        colors = '#3498db'
    else:
        return

    feat_df = pd.DataFrame({'Feature': feature_names, 'Value': values})
    feat_df = feat_df.sort_values(by='Value', key=abs, ascending=True)

    plt.barh(feat_df['Feature'], feat_df['Value'], color=colors if isinstance(colors, list) else colors, edgecolor='black', alpha=0.85)
    plt.axvline(0, color='gray', linestyle='--', lw=1)
    plt.title(title, fontsize=13, weight='bold')
    plt.xlabel(metric_name)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()
    print(f"Saved feature importance chart to {save_path}")
