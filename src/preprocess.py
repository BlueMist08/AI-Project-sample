"""
preprocess.py
Data preprocessing module for Hit Song Popularity Prediction.
Handles loading, deduplication, missing value imputation,
feature selection, scaling, and train-test splitting.
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

AUDIO_FEATURES = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'duration_ms',
    'key',
    'mode',
    'time_signature'
]

def load_data(filepath='data/dataset.csv'):
    """Load the raw dataset from a relative file path."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Dataset not found at {filepath}. Please ensure data/dataset.csv exists."
        )
    df = pd.read_csv(filepath)
    return df

def clean_data(df):
    """
    Clean dataset:
    - Drop redundant index columns like 'Unnamed: 0'
    - Drop duplicate tracks by 'track_id'
    - Drop missing values
    - Convert boolean 'explicit' to integer 0/1
    """
    cleaned_df = df.copy()
    if 'Unnamed: 0' in cleaned_df.columns:
        cleaned_df = cleaned_df.drop(columns=['Unnamed: 0'])
    
    # Drop rows with null values
    cleaned_df = cleaned_df.dropna().reset_index(drop=True)
    
    # Drop duplicate track records
    if 'track_id' in cleaned_df.columns:
        cleaned_df = cleaned_df.drop_duplicates(subset=['track_id']).reset_index(drop=True)
    
    if 'explicit' in cleaned_df.columns:
        cleaned_df['explicit'] = cleaned_df['explicit'].astype(int)
        
    return cleaned_df

def prepare_audio_features(df, test_size=0.2, random_state=42, scale=True):
    """
    Extract core audio features and target popularity score.
    Performs train-test split and standardizes continuous features.
    """
    X = df[AUDIO_FEATURES].copy()
    y = df['popularity'].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    scaler = None
    if scale:
        scaler = StandardScaler()
        X_train_scaled = pd.DataFrame(
            scaler.fit_transform(X_train),
            columns=AUDIO_FEATURES,
            index=X_train.index
        )
        X_test_scaled = pd.DataFrame(
            scaler.transform(X_test),
            columns=AUDIO_FEATURES,
            index=X_test.index
        )
        return X_train_scaled, X_test_scaled, y_train, y_test, scaler, AUDIO_FEATURES

    return X_train, X_test, y_train, y_test, None, AUDIO_FEATURES

def prepare_enhanced_features(df, test_size=0.2, random_state=42):
    """
    Prepare enhanced features by combining audio features with
    track genre mean popularity (target-encoded on training set to prevent data leakage)
    and explicit flag.
    """
    features = AUDIO_FEATURES + ['explicit']
    X = df[features + ['track_genre']].copy()
    y = df['popularity'].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    # Compute genre mean target encoding strictly on train split to prevent data leakage
    train_genre_means = y_train.groupby(X_train['track_genre']).mean()
    global_mean = y_train.mean()

    X_train['genre_popularity_enc'] = X_train['track_genre'].map(train_genre_means).fillna(global_mean)
    X_test['genre_popularity_enc'] = X_test['track_genre'].map(train_genre_means).fillna(global_mean)

    final_cols = AUDIO_FEATURES + ['explicit', 'genre_popularity_enc']
    X_train = X_train[final_cols]
    X_test = X_test[final_cols]

    scaler = StandardScaler()
    X_train_scaled = pd.DataFrame(
        scaler.fit_transform(X_train),
        columns=final_cols,
        index=X_train.index
    )
    X_test_scaled = pd.DataFrame(
        scaler.transform(X_test),
        columns=final_cols,
        index=X_test.index
    )

    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, final_cols
