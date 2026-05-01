from utils.constants import COLORS


def clean_layout(fig):
    fig.update_layout(
        height=380,
        margin=dict(l=10, r=10, t=50, b=20),
        plot_bgcolor="rgba(15, 23, 42, 0.0)",
        paper_bgcolor="rgba(15, 23, 42, 0.0)",
        font=dict(color=COLORS["text"], size=13),
        hoverlabel=dict(
            bgcolor="#0F172A",
            font_color=COLORS["text"],
            bordercolor=COLORS["blue"]
        ),
        legend=dict(
            bgcolor="rgba(0,0,0,0)",
            orientation="h",
            y=1.1
        )
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.16)",
        zeroline=False
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="rgba(148, 163, 184, 0.16)",
        zeroline=False
    )

    return fig