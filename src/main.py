"""
main.py
Main entry point for Hit Song Popularity Prediction (Regression).
Executes end-to-end ML pipeline:
1. Data loading and preprocessing
2. Feature extraction and train-test split
3. Model training (Linear Regression, Ridge, Lasso, Decision Tree, Random Forest)
4. Evaluation: R2, RMSE, MAE, Residual Plots, and Feature Analysis
5. Generates all visual outputs in outputs/ and summary metrics CSV.
"""

import os
import sys
import pandas as pd
import numpy as np

# Ensure local imports work reliably
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocess import (
    load_data,
    clean_data,
    prepare_audio_features,
    prepare_enhanced_features,
    AUDIO_FEATURES
)
from src.models import get_regression_models, train_and_predict
from src.evaluate import (
    calculate_metrics,
    plot_correlation_heatmap,
    plot_actual_vs_predicted,
    plot_residual_analysis,
    plot_feature_importance_or_coefficients
)

def run_pipeline():
    print("=" * 75)
    print("AI101 PROJECT: HIT SONG POPULARITY PREDICTION (REGRESSION)")
    print("=" * 75)

    data_path = os.path.join("data", "dataset.csv")
    print(f"\n[1/5] Loading and cleaning dataset from: {data_path}")
    raw_df = load_data(data_path)
    print(f"      Raw dataset shape: {raw_df.shape}")

    df = clean_data(raw_df)
    print(f"      Cleaned dataset shape (after deduplication): {df.shape}")
    print(f"      Target: popularity (mean={df['popularity'].mean():.2f}, std={df['popularity'].std():.2f})")

    # Generate exploratory correlation heatmap
    print("\n[2/5] Generating Correlation Heatmap for audio features...")
    plot_correlation_heatmap(df, AUDIO_FEATURES, target_col='popularity', save_path='outputs/correlation_matrix.png')

    # Experiment 1: Pure Audio Features
    print("\n[3/5] EXPERIMENT 1: Pure Audio Features Baseline")
    print("      Features: danceability, energy, loudness, speechiness, acousticness,")
    print("                instrumentalness, liveness, valence, tempo, duration, key, mode")
    X_train, X_test, y_train, y_test, scaler, feature_cols = prepare_audio_features(df, test_size=0.2, random_state=42)
    print(f"      Train samples: {len(X_train)} | Test samples: {len(X_test)}")

    models = get_regression_models()
    results = []
    test_preds = {}

    for name, model in models.items():
        print(f"      Training {name}...")
        y_train_pred, y_test_pred = train_and_predict(model, X_train, y_train, X_test)
        test_preds[name] = y_test_pred

        train_m = calculate_metrics(y_train, y_train_pred)
        test_m = calculate_metrics(y_test, y_test_pred)

        results.append({
            'Model': name,
            'Feature Set': 'Audio Features',
            'Train R2': round(train_m['R2'], 4),
            'Test R2': round(test_m['R2'], 4),
            'Train RMSE': round(train_m['RMSE'], 3),
            'Test RMSE': round(test_m['RMSE'], 3),
            'Train MAE': round(train_m['MAE'], 3),
            'Test MAE': round(test_m['MAE'], 3)
        })

    # Visualizations for Experiment 1
    print("\n[4/5] Generating Diagnostic & Residual Visualizations...")
    # Select key models for multi-panel comparison plots
    selected_models_to_plot = {
        'Linear Regression': test_preds['Linear Regression'],
        'Ridge Regression': test_preds['Ridge Regression'],
        'Decision Tree': test_preds['Decision Tree'],
        'Random Forest': test_preds['Random Forest']
    }
    plot_actual_vs_predicted(y_test, selected_models_to_plot, save_path='outputs/actual_vs_predicted.png')
    plot_residual_analysis(y_test, selected_models_to_plot, save_path='outputs/residual_plots.png')

    # Feature Importance for Decision Tree & Linear Reg
    plot_feature_importance_or_coefficients(models['Linear Regression'], feature_cols, 'Linear Regression', save_path='outputs/linear_reg_coefficients.png')
    plot_feature_importance_or_coefficients(models['Decision Tree'], feature_cols, 'Decision Tree Regressor', save_path='outputs/feature_importance.png')

    # Experiment 2: Enhanced Features (Audio + Genre Context + Explicit)
    print("\n[5/5] EXPERIMENT 2: Enhanced Model (Audio Features + Genre Context + Explicit)")
    X_train_enh, X_test_enh, y_train_enh, y_test_enh, _, enh_cols = prepare_enhanced_features(df, test_size=0.2, random_state=42)
    
    rf_enh = models['Random Forest']
    _, y_test_enh_pred = train_and_predict(rf_enh, X_train_enh, y_train_enh, X_test_enh)
    enh_m = calculate_metrics(y_test_enh, y_test_enh_pred)
    
    results.append({
        'Model': 'Random Forest (Enhanced)',
        'Feature Set': 'Audio + Genre + Explicit',
        'Train R2': round(calculate_metrics(y_train_enh, rf_enh.predict(X_train_enh))['R2'], 4),
        'Test R2': round(enh_m['R2'], 4),
        'Train RMSE': round(calculate_metrics(y_train_enh, rf_enh.predict(X_train_enh))['RMSE'], 3),
        'Test RMSE': round(enh_m['RMSE'], 3),
        'Train MAE': round(calculate_metrics(y_train_enh, rf_enh.predict(X_train_enh))['MAE'], 3),
        'Test MAE': round(enh_m['MAE'], 3)
    })

    # Summary table output
    results_df = pd.DataFrame(results)
    csv_path = os.path.join("outputs", "metrics_summary.csv")
    os.makedirs("outputs", exist_ok=True)
    results_df.to_csv(csv_path, index=False)
    
    print("\n" + "=" * 75)
    print("BENCHMARK RESULTS SUMMARY:")
    print("=" * 75)
    print(results_df.to_string(index=False))
    print(f"\n[OK] Summary metrics saved to: {csv_path}")
    print("[OK] All visual figures saved to outputs/ directory:")
    print("     - outputs/correlation_matrix.png")
    print("     - outputs/actual_vs_predicted.png")
    print("     - outputs/residual_plots.png")
    print("     - outputs/feature_importance.png")
    print("     - outputs/linear_reg_coefficients.png")
    print("=" * 75)
    print("Pipeline execution completed successfully!")

if __name__ == '__main__':
    run_pipeline()
