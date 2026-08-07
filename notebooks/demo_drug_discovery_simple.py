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
    import csv,io,urllib.request as u
    import marimo as mo
    url="https://huggingface.co/datasets/dbn4/drug-discovery-demo/resolve/42d94e62750e792836a873a8fe062abd9e3a0923/data/drug_discovery_dummy.csv"
    txt=u.urlopen(url).read().decode("utf-8")
    mo.ui.table(list(csv.DictReader(io.StringIO(txt,newline=""))))
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""
 
    """)
    return


if __name__ == "__main__":
    app.run()
