from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Union


class SeriesEntry(BaseModel):
    label: str
    y: List[Optional[float]]
    color: Optional[str] = None
    lineStyle: Optional[Literal["solid", "dashed", "dotted"]] = "solid"
    area: Optional[bool] = False
    stacked: Optional[bool] = False
    step: Optional[Literal["start", "middle", "end"]] = None


class XAxisConfig(BaseModel):
    label: Optional[str] = None
    type: Literal["category", "value"] = "category"


class YAxisConfig(BaseModel):
    label: Optional[str] = None
    type: Literal["value", "log"] = "value"


class GridConfig(BaseModel):
    left: Union[str, int] = "10%"
    right: Union[str, int] = "10%"
    top: Union[str, int] = "15%"
    bottom: Union[str, int] = "10%"
    containLabel: bool = True


class LinePlotSchema(BaseModel):
    # Required
    type: Literal["line"] = "line"
    x: List[Union[str, int]]
    series: List[SeriesEntry]

    # Optional config
    title: Optional[str] = None
    theme: Literal["default", "light", "dark"] = "default"
    xAxis: Optional[XAxisConfig] = XAxisConfig()
    yAxis: Optional[YAxisConfig] = YAxisConfig()
    legend: Optional[bool] = True
    tooltip: Optional[bool] = True
    grid: Optional[GridConfig] = GridConfig()

    class Config:
        extra = "forbid"
        schema_extra = {
            "example": {
                "type": "line",
                "title": "GDP Comparison",
                "theme": "dark",
                "x": [2000, 2001, 2002, 2003],
                "series": [
                    {
                        "label": "USA",
                        "y": [10.5, 10.9, 11.2, 11.7],
                        "color": "#4f46e5",
                        "lineStyle": "solid",
                        "area": False,
                        "stacked": False
                    },
                    {
                        "label": "Germany",
                        "y": [8.3, 8.6, 8.9, None],
                        "color": "#16a34a",
                        "lineStyle": "dashed",
                        "area": True,
                        "stacked": False
                    }
                ],
                "xAxis": {"label": "Year", "type": "category"},
                "yAxis": {"label": "Trillions USD", "type": "value"},
                "legend": True,
                "tooltip": True,
                "grid": {
                    "left": "10%",
                    "right": "10%",
                    "top": "15%",
                    "bottom": "10%",
                    "containLabel": True
                }
            }
        }
