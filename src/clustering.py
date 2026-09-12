from typing import List, Tuple, Dict, Optional, Any
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def prepare_clustering_data(
    stock_df: pd.DataFrame,
    feature_cols: Optional[List[str]] = None,
) -> pd.DataFrame:
    # Extract specified numerical features for clustering
    if feature_cols is None:
        feature_cols = ["OStk", "PurTot", "SaleTot", "QohValue"]

    present_cols = [c for c in feature_cols if c in stock_df.columns]
    return stock_df[present_cols].copy()


def scale_clustering_data(
    cluster_df: pd.DataFrame,
) -> Tuple[np.ndarray, StandardScaler]:
    # Fit StandardScaler and transform clustering features
    scaler = StandardScaler()
    cluster_scaled = scaler.fit_transform(cluster_df)
    return cluster_scaled, scaler


def compute_elbow_inertia(
    cluster_scaled: np.ndarray, k_range: range = range(1, 10)
) -> Tuple[List[int], List[float]]:
    # Compute inertia across a range of k values for the Elbow Method
    inertia = []
    k_list = list(k_range)
    for k in k_list:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(cluster_scaled)
        inertia.append(kmeans.inertia_)
    return k_list, inertia


def plot_elbow_method(
    k_list: List[int],
    inertia: List[float],
    title: str = "Elbow Method",
) -> plt.Figure:
    # Plot Elbow Method curve for selecting k
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(k_list, inertia, marker="o")
    ax.set_xlabel("Number of Clusters (k)")
    ax.set_ylabel("Inertia")
    ax.set_title(title)
    ax.grid(True)
    plt.tight_layout()
    return fig


def fit_kmeans_clusters(
    cluster_df: pd.DataFrame,
    cluster_scaled: np.ndarray,
    n_clusters: int = 4,
    random_state: int = 5,
    cluster_labels_map: Optional[Dict[int, str]] = None,
) -> Tuple[pd.DataFrame, KMeans, float]:
    # Fit K-Means clustering, assign labels, map cluster names, and compute silhouette score
    if cluster_labels_map is None:
        cluster_labels_map = {
            0: "Low Demand",
            1: "Fast Moving",
            2: "High Value",
            3: "Bulk/Moderate Demand",
        }

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(cluster_scaled)

    df_result = cluster_df.copy()
    df_result["Cluster"] = clusters
    df_result["Cluster_Label"] = df_result["Cluster"].map(cluster_labels_map)

    score = silhouette_score(cluster_scaled, clusters)

    return df_result, kmeans, score


def plot_cluster_scatter(
    cluster_df: pd.DataFrame,
    x_col: str = "SaleTot",
    y_col: str = "QohValue",
    hue_col: str = "Cluster_Label",
    title: str = "Product Clusters by Sales and Inventory Value",
) -> plt.Figure:

    # Scatter plot of clustered products
    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(
        data=cluster_df,
        x=x_col,
        y=y_col,
        hue=hue_col,
        palette="tab10",
        s=60,
        ax=ax,
    )
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend(title="Cluster Type")
    ax.grid(True)
    plt.tight_layout()
    return fig