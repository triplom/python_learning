# Matplotlib Cheatsheet

## Setup

```python
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")   # non-interactive (saves files); remove for interactive
```

## Line Chart

```python
plt.figure(figsize=(10, 5))
plt.plot(x, y, marker="o", color="steelblue", linewidth=2, label="Series 1")
plt.plot(x, y2, marker="s", color="tomato", linestyle="--", label="Series 2")
plt.title("Title", fontsize=14)
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.legend()
plt.grid(True, alpha=0.4)
plt.tight_layout()
plt.savefig("chart.png", dpi=100)
plt.show()     # interactive only
plt.close()
```

## Bar Chart

```python
bars = plt.bar(categories, values, color="steelblue", edgecolor="black")

# Labels on bars
for bar, val in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(val), ha="center", va="bottom")

# Horizontal bar
plt.barh(categories, values)
```

## Scatter Plot

```python
plt.scatter(x, y, alpha=0.6, color="green", edgecolors="darkgreen",
            s=60, label="Data points")

# Trend line
import numpy as np
m, b = np.polyfit(x, y, 1)
plt.plot(x_line, m*x_line + b, "r--", label="Trend")
```

## Boxplot

```python
plt.boxplot(
    [data1, data2, data3],
    labels=["A", "B", "C"],
    patch_artist=True,
    notch=False,
)
```

## Histogram

```python
plt.hist(data, bins=20, color="steelblue", edgecolor="black", alpha=0.7)
```

## Pie Chart

```python
plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
```

## Subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Dashboard", fontsize=16)

axes[0, 0].plot(x, y)        # top-left
axes[0, 1].bar(cats, vals)   # top-right
axes[1, 0].scatter(x, y)     # bottom-left
axes[1, 1].hist(data)        # bottom-right

plt.tight_layout()
```

## Styles & Colors

```python
plt.style.use("ggplot")       # seaborn, fivethirtyeight, bmh, dark_background
plt.rcParams["figure.dpi"] = 120

# Named colors: "steelblue", "tomato", "mediumseagreen", "coral"
# Hex colors: "#4C72B0"
# Colormaps: plt.cm.viridis, plt.cm.Blues
```

## Common Parameters

| Parameter | Values |
|-----------|--------|
| `linestyle` | `"-"` `"--"` `":"` `"-."` |
| `marker` | `"o"` `"s"` `"^"` `"D"` `"x"` `"+"` |
| `color` | name, hex, RGB tuple |
| `alpha` | 0.0 (transparent) – 1.0 (opaque) |
| `linewidth` | float |
| `fontsize` | int |
