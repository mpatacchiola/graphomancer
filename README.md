# 🧙‍♂️ Graphomancer

Graphomancer is a modular Python + JavaScript library for serializing visualizations into portable JSON schemas, making it easy to generate and share rich, interactive charts from Python (e.g. Matplotlib) into frontend environments (e.g. ECharts, Plotly).

---

## ✨ Features

- 📤 **Serialization of Matplotlib objects** into clean, typed JSON
- 🧱 **Typed Pydantic schemas** for chart configuration and rendering
- 🔁 **Frontend-agnostic JSON spec** (supports ECharts, Plotly, etc.)
- 🧩 **Modular structure** for easy extension to new chart types and engines
- 🧪 Designed for future integration into [Moloch.run](https://moloch.run) and compatible dashboards

---

## 📦 Repository Structure

```
graphomancer/
├── graphomancer/                      # Python source code
│   ├── __init__.py
│   ├── schemas/                       # Pydantic JSON schemas (e.g. line_schema.py)
│   ├── serializers/                   # Python serializers (e.g. matplotlib -> JSON)
│   │   └── matplotlib/
│   └── ...
├── js/                                # JavaScript rendering engine (JSON → Chart)
│   ├── src/
│   │   ├── index.js                   # JS entry point
│   │   └── renderers/
│   │       └── echarts.js            # JSON to EChart renderer
│   ├── package.json                   # JS project metadata and dependencies
│   ├── vite.config.js                 # Vite bundler config
│   └── README.md                      # JS-specific documentation
├── examples/                          # Usage examples for serialization
│   └── simple_matplotlib_serialization.py
├── tests/                             # Unit tests (to be added)
├── pyproject.toml                     # Python project configuration
├── .gitignore
└── README.md
````

---

## 🧪 Quickstart

### 1. Install in editable mode

```bash
git clone https://github.com/yourusername/graphomancer.git
cd graphomancer
pip install -e .
````

### 2. Create a plot and serialize it

```python
import matplotlib.pyplot as plt
from graphomancer.serializers.matplotlib.line_serializer import LinePlotMatplotlibSerializer

fig, ax = plt.subplots()
ax.plot([2000, 2001, 2002], [1.5, 1.8, 2.0], label="USA")
ax.plot([2000, 2001, 2002], [1.2, 1.4, 1.6], label="Germany")

serializer = LinePlotMatplotlibSerializer(fig, theme="dark", description="GDP over years", source="World Bank")
schema = serializer.serialize()

print(schema.model_dump_json(indent=2))
```

---

## 📚 Roadmap

* [x] Line plot schema and Matplotlib serializer
* [ ] Add support for bar, pie, and scatter plots
* [ ] Pandas dataframe to JSON
* [ ] JavaScript rendering engine (ECharts first)
* [ ] Live chart updates via WebSocket-compatible deltas
* [ ] Graphomancer as a plugin for [Moloch.run](https://moloch.run)
* [ ] Public docs and open-source release

---

## ⚙️ Requirements

* Python 3.8+
* [matplotlib](https://matplotlib.org/)
* [pydantic](https://docs.pydantic.dev/)
* numpy

---

## 🧙‍♂️ Why the name?

> Inspired by *Neuromancer* and the arcane magic of data visualization, **Graphomancer** is a conjurer of charts — turning raw Python plots into front-end ready artifacts.

---

## 📝 License

Currently private. License terms will be determined upon public release.

---

## 🤝 Contributing

Not yet open to contributions — but stay tuned as we stabilize the API and publish our first public spec.