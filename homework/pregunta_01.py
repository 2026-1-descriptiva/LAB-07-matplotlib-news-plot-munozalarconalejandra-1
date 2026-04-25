"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    os.makedirs("files/plots", exist_ok=True)

    df = pd.read_csv("files/input/news.csv", index_col=0)

    colors = {
        "Television": "#76FA4E",
        "Newspaper": "gray",
        "Internet": "#1f77b4",
        "Radio": "#ff7f0e",
    }

    plt.figure(figsize=(6.4, 4.8))

    for col in df.columns:
        plt.plot(df.index, df[col], color=colors[col], linewidth=3 if col == "Internet" else 2)

        first_year = df.index[0]
        last_year = df.index[-1]

        plt.scatter(first_year, df[col][first_year], color=colors[col])
        plt.text(
            first_year - 0.2,
            df[col][first_year],
            col + " " + str(df[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        plt.scatter(last_year, df[col][last_year], color=colors[col])
        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.title("How people get their news", fontsize=16)
    plt.text(
        df.index[0] + 0.5,
        df.max().max() + 2,
        "An increasing proportion cite the internet as their primary news source",
        fontsize=8,
    )

    plt.xticks(df.index)
    plt.yticks([])
    plt.xlim(df.index[0] - 0.5, df.index[-1] + 0.5)
    plt.ylim(df.min().min() - 5, df.max().max() + 5)

    for spine in ["top", "right", "left"]:
        plt.gca().spines[spine].set_visible(False)

    plt.tight_layout()
    plt.savefig("files/plots/news.png")
    plt.close()