import sys
import importlib.metadata


try:
    import matplotlib.pyplot as plt  # type: ignore
    import numpy as np
    import pandas as pd  # type: ignore

except ImportError:
    print("Error: Missing dependencies.")
    print("To install with pip, run:")
    print("pip install -r requirements.txt")
    print("\nTo install with Poetry, run:")
    print("poetry install")
    print("poetry run python loading.py")
    print("\nTo install Poetry, run:")
    print("curl -sSL https://install.python-poetry.org | python3 -")
    sys.exit(1)


def check_dependencies() -> None:
    """Display the installed versions of the required packages."""
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    missing: bool = False

    packages_info = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "python-dotenv": "dotenv ready",
    }

    for package, message in packages_info.items():
        try:
            version = importlib.metadata.version(package)
            print(f"[OK] {package} ({version}) - {message}")
        except importlib.metadata.PackageNotFoundError:
            missing = True
            print(f"[MISSING] {package} - {message}")

    if missing:
        print("\nMissing dependencies detected.")
        print("\nInstall with pip:")
        print("pip install -r requirements.txt")
        print("\nOr install with Poetry:")
        print("poetry install")
        sys.exit(1)


def compare_packages() -> None:
    """Show the difference between pip and Poetry dependency management."""
    print("\nDependency management:")
    print("[pip] Uses requirements.txt to list project dependencies.")
    print("[Poetry] Uses pyproject.toml to manage dependencies and env.")
    print("[pip] Install with: pip install -r requirements.txt")
    print("[Poetry] Install with: poetry install")
    print("[Poetry] Run with: poetry run python loading.py")


def generate_matrix_data(size: int = 1000) -> pd.DataFrame:
    rng = np.random.default_rng(42)

    signal = rng.normal(loc=50.0, scale=15.0, size=size)
    noise = rng.normal(loc=0.0, scale=5.0, size=size)
    anomaly = rng.random(size) < 0.05

    values = signal + noise
    values[anomaly] += rng.normal(loc=30.0, scale=10.0, size=anomaly.sum())

    status = np.where(anomaly, "ANOMALY", "NORMAL")

    return pd.DataFrame({
        "signal": signal,
        "noise": noise,
        "value": values,
        "status": status
    })


def analyze_and_plot() -> None:

    print("\nAnalyzing Matrix data...")

    df = generate_matrix_data()

    if df.empty:
        print("Error: No data found in the Matrix.")
        sys.exit(1)

    print(f"Processing {len(df)} data points...")

    mean_value = df["value"].mean()
    maximum_value = df["value"].max()
    minimum_value = df["value"].min()
    anomalies = (df["status"] == "ANOMALY").sum()

    print(f"Average signal value: {mean_value:.2f}")
    print(f"Minimum signal value: {minimum_value:.2f}")
    print(f"Maximum signal value: {maximum_value:.2f}")
    print(f"Detected anomalies: {anomalies}")

    print("Generating visualization...")
    plt.figure(figsize=(10, 6), facecolor="black")
    normal = df[df["status"] == "NORMAL"]
    anomaly = df[df["status"] == "ANOMALY"]

    ax = plt.gca()
    ax.set_facecolor("black")
    for spine in ax.spines.values():
        spine.set_color("#002200")
    ax.xaxis.label.set_color("green")
    ax.yaxis.label.set_color("green")
    ax.tick_params(
        axis="both",
        colors="green"
    )

    plt.scatter(
        normal.index,
        normal["value"],
        alpha=0.5,
        label="Normal"
    )

    plt.scatter(
        anomaly.index,
        anomaly["value"],
        color="#ff0000",
        alpha=0.8,
        label="Anomaly"
    )

    plt.axhline(
        mean_value,
        color="green",
        linestyle="--",
        label=f"Average ({mean_value:.2f})"
    )

    plt.title("Matrix Simulated Data Analysis", color="#00ff00")
    plt.xlabel("Data Point", color="#00ff00")
    plt.ylabel("Matrix Signal Value", color="#00ff00")
    plt.grid(True, linestyle="--", color="#333333", alpha=0.7)
    plt.legend(
        facecolor="black",
        edgecolor="#00ff00",
        labelcolor="white"
    )

    plt.tight_layout()
    plt.savefig("matrix_analysis.png", facecolor="black")
    plt.close()

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_dependencies()
    compare_packages()
    analyze_and_plot()
