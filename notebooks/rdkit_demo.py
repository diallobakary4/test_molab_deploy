import marimo

__generated_with = "0.23.9"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    from rdkit import Chem
    from rdkit.Chem import Descriptors

    return Chem, Descriptors, mo


@app.cell
def _(Chem, Descriptors, mo):
    mol = Chem.MolFromSmiles("CCO")
    mo.md(f"""
    # RDKit in marimo + Molab

    SMILES: `CCO`

    Molecular weight: `{Descriptors.MolWt(mol):.2f}`
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
