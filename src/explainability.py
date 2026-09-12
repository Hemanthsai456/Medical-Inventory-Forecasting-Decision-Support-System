from typing import Tuple, Any
import matplotlib.pyplot as plt
import pandas as pd
import shap


def get_feature_importance(
    model: Any, feature_names: pd.Index, top_n: int = 5
) -> pd.DataFrame:
    # Extract top N important features from a fitted tree model
    importance = getattr(model, "feature_importances_", None)
    if importance is None:
        raise ValueError(
            "Model does not have feature_importances_ attribute."
        )

    feat_imp = pd.DataFrame(
        {"Feature": feature_names, "Importance": importance}
    ).sort_values(by="Importance", ascending=False)

    return feat_imp.head(top_n)


def plot_feature_importance(
    feat_imp: pd.DataFrame, title: str = "Feature Importance"
) -> plt.Figure:
    # Plot horizontal bar chart of feature importances
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.barh(feat_imp["Feature"], feat_imp["Importance"])
    ax.set_title(title)
    ax.set_xlabel("Importance Score")
    ax.invert_yaxis()
    ax.grid(True, axis="x")
    plt.tight_layout()
    return fig


def compute_shap_values(
    model: Any, X: pd.DataFrame
) -> Tuple[shap.TreeExplainer, Any]:
    # Compute SHAP values using TreeExplainer on a tree-based model
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)
    return explainer, shap_values


def plot_shap_summary(
    shap_values: Any, X: pd.DataFrame, show: bool = True
) -> None:
    # Generate SHAP summary plot
    shap.summary_plot(shap_values, X, show=show)


def plot_shap_waterfall(
    explainer: shap.TreeExplainer,
    shap_values: Any,
    X: pd.DataFrame,
    index: int = 0,
    show: bool = True,
) -> None:
    # Generate SHAP waterfall plot for a single instance
    base_val = (
        explainer.expected_value[0]
        if isinstance(explainer.expected_value, (list, tuple))
        else explainer.expected_value
    )
    val = (
        shap_values[index]
        if hasattr(shap_values, "__getitem__")
        else shap_values
    )

    explanation = shap.Explanation(
        values=val,
        base_values=base_val,
        data=X.iloc[index],
        feature_names=X.columns,
    )
    shap.plots.waterfall(explanation, show=show)