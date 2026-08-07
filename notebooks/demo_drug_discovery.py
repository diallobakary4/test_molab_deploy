# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.23.3",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    url="https://huggingface.co/datasets/dbn4/drug-discovery-demo/resolve/42d94e62750e792836a873a8fe062abd9e3a0923/data/drug_discovery_dummy.csv"
    df=mo.sql(f"SELECT * FROM read_csv('{url}') LIMIT 1000")
    mo.ui.table(df)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
