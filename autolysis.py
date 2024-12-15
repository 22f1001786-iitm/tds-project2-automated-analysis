# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "tenacity",
# ]
# ///

import os
import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import httpx
from tenacity import retry, stop_after_attempt, wait_fixed

# LLM API interaction
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def query_llm(prompt):
    """Send a prompt to the LLM and return its response."""
    token = os.getenv("AIPROXY_TOKEN")
    if not token:
        print("Error: AIPROXY_TOKEN environment variable not set.")
        sys.exit(1)
    
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"model": "gpt-4o-mini", "messages": [{"role": "user", "content": prompt}]}

    response = httpx.post("https://aiproxy.sanand.workers.dev/v1/chat/completions", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Data analysis functions
def analyze_data(file_path):
    """Perform a basic analysis on the dataset."""
    df = pd.read_csv(file_path)
    description = df.describe(include='all').transpose()
    missing_values = df.isnull().sum()
    correlation_matrix = df.corr(numeric_only=True)
    return df, description, missing_values, correlation_matrix

# Visualization
def visualize_correlation(correlation_matrix, output_path):
    """Generate and save a correlation heatmap."""
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Matrix Heatmap")
    plt.savefig(output_path)
    plt.close()

# Narrative generation
def generate_narrative(description, missing_values, insights):
    """Generate a narrative using the LLM."""
    prompt = f"""
    I analyzed a dataset with the following summary statistics:
    {description.to_string()}

    Missing values were found in the following columns:
    {missing_values.to_string()}

    Based on the analysis, here are the key insights:
    {insights}

    Write a detailed story summarizing this analysis, including implications.
    """
    return query_llm(prompt)

# Main script
def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py dataset.csv")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_dir = os.path.splitext(file_path)[0]

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Analyze the data
        df, description, missing_values, correlation_matrix = analyze_data(file_path)

        # Visualize correlation matrix
        correlation_output = os.path.join(output_dir, "correlation.png")
        visualize_correlation(correlation_matrix, correlation_output)

        # Generate insights
        sample_data = df.head().to_string()
        insights = query_llm(f"Analyze the following dataset:\n{sample_data}")
        narrative = generate_narrative(description, missing_values, insights)

        # Write narrative to README.md
        with open(os.path.join(output_dir, "README.md"), "w") as f:
            f.write(narrative)

        print(f"Analysis complete. Outputs saved in {output_dir}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
