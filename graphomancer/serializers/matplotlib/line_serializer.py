from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from graphomancer.schemas.line_schema import LinePlotSchema, SeriesEntry, XAxisConfig, YAxisConfig, GridConfig
from typing import Optional, Union, List, Tuple
import numpy as np


class LinePlotMatplotlibSerializer:
    def __init__(self, fig: Figure, *, theme: str = "default", description: Optional[str] = None, source: Optional[str] = None):
        if not isinstance(fig, Figure):
            raise ValueError("Expected a matplotlib.figure.Figure object")
        
        self.fig = fig
        self.theme = theme
        self.description = description
        self.source = source

    def extract_series(self, ax) -> Tuple[List[Union[str, int]], List[SeriesEntry]]:
        x_ref = None
        series = []

        for line in ax.get_lines():
            if not isinstance(line, Line2D) or line.get_label().startswith('_'):
                continue  # Skip placeholder lines

            x = line.get_xdata()
            y = line.get_ydata()

            # Convert to Python-native types
            x = x.tolist() if isinstance(x, (np.ndarray, list)) else list(x)
            y = y.tolist() if isinstance(y, (np.ndarray, list)) else list(y)

            if x_ref is None:
                x_ref = x
            else:
                if len(x) != len(x_ref):
                    raise ValueError(f"Series '{line.get_label()}' x-length does not match reference x-axis")

            entry = SeriesEntry(
                label=line.get_label(),
                y=y,
                color=line.get_color() if hasattr(line, "get_color") else None,
                lineStyle=self._map_linestyle(line.get_linestyle()),
                area=False,         # Optional: logic can be added
                stacked=False,      # Optional: logic can be added
                step=None           # Optional: logic can be added
            )
            series.append(entry)

        if x_ref is None:
            raise ValueError("No valid line series found in the figure")

        return x_ref, series

    def _map_linestyle(self, linestyle: str) -> str:
        # Maps matplotlib line styles to Graphomancer styles
        if linestyle in ('-', 'solid'):
            return "solid"
        elif linestyle in ('--', 'dashed'):
            return "dashed"
        elif linestyle in (':', 'dotted'):
            return "dotted"
        elif linestyle in ('-.', 'dashdot'):
            return "dashed"
        return "solid"

    def serialize(self) -> LinePlotSchema:
        ax = self.fig.axes[0]  # For now, support only the first subplot
        x, series = self.extract_series(ax)

        return LinePlotSchema(
            type="line",
            title=ax.get_title() or None,
            description=self.description,
            source=self.source,
            theme=self.theme,
            x=x,
            series=series,
            xAxis=XAxisConfig(
                label=ax.get_xlabel(),
                type="category"
            ),
            yAxis=YAxisConfig(
                label=ax.get_ylabel(),
                type="value"
            ),
            grid=GridConfig(),  # Defaults, can be inferred later
            legend=True,
            tooltip=True
        )
