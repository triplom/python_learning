# Data Visualization with Matplotlib
# Course 1 §7

import matplotlib

matplotlib.use(
    "Agg"
)  # non-interactive backend — saves files instead of opening windows
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save(name):
    path = os.path.join(OUTPUT_DIR, name)
    plt.savefig(path, dpi=100, bbox_inches="tight")
    plt.close()
    print(f"Saved: {path}")


# ═══════════════════════════════════════
#  LINE CHART
# ═══════════════════════════════════════
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2025 = [12000, 15000, 13500, 17000, 14500, 19000]
sales_2026 = [14000, 16500, 15000, 18500, 17000, 22000]

plt.figure(figsize=(10, 5))
plt.plot(months, sales_2025, marker="o", label="2025", color="steelblue", linewidth=2)
plt.plot(months, sales_2026, marker="s", label="2026", color="tomato", linewidth=2)
plt.title("Monthly Sales Comparison", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Revenue (R$)")
plt.legend()
plt.grid(True, alpha=0.4)
save("line_chart.png")

# ═══════════════════════════════════════
#  BAR CHART
# ═══════════════════════════════════════
products = ["Book", "Keyboard", "USB Hub", "Webcam", "Monitor"]
units_sold = [42, 18, 95, 30, 12]
colors = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B2"]

plt.figure(figsize=(10, 5))
bars = plt.bar(products, units_sold, color=colors, edgecolor="black", linewidth=0.5)

# Add value labels on bars
for bar, val in zip(bars, units_sold):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 1,
        str(val),
        ha="center",
        va="bottom",
        fontsize=10,
    )

plt.title("Units Sold per Product", fontsize=14)
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.ylim(0, max(units_sold) * 1.15)
save("bar_chart.png")

# ═══════════════════════════════════════
#  SCATTER PLOT
# ═══════════════════════════════════════
import random

random.seed(42)

study_hours = [random.uniform(1, 10) for _ in range(50)]
exam_scores = [min(100, h * 9 + random.gauss(0, 5)) for h in study_hours]

plt.figure(figsize=(8, 6))
plt.scatter(
    study_hours,
    exam_scores,
    alpha=0.6,
    color="mediumseagreen",
    edgecolors="darkgreen",
    s=60,
)
plt.title("Study Hours vs Exam Score", fontsize=14)
plt.xlabel("Study Hours per Day")
plt.ylabel("Exam Score")
plt.grid(True, alpha=0.3)

# Trend line (linear regression via numpy)
import numpy as np

m, b = np.polyfit(study_hours, exam_scores, 1)
x_line = np.linspace(1, 10, 100)
plt.plot(x_line, m * x_line + b, "r--", label=f"Trend (y={m:.1f}x+{b:.1f})")
plt.legend()
save("scatter.png")

# ═══════════════════════════════════════
#  BOXPLOT
# ═══════════════════════════════════════
data = {
    "Math": [72, 85, 91, 68, 95, 78, 83, 60, 88, 74],
    "Science": [80, 88, 76, 92, 65, 84, 70, 90, 78, 82],
    "History": [60, 72, 65, 80, 55, 70, 68, 75, 58, 77],
}

plt.figure(figsize=(9, 6))
bp = plt.boxplot(
    list(data.values()), labels=list(data.keys()), patch_artist=True, notch=False
)

colors = ["#AED6F1", "#A9DFBF", "#F9E79F"]
for patch, color in zip(bp["boxes"], colors):
    patch.set_facecolor(color)

plt.title("Score Distribution by Subject", fontsize=14)
plt.ylabel("Score")
plt.grid(True, axis="y", alpha=0.4)
save("boxplot.png")

# ═══════════════════════════════════════
#  SUBPLOTS
# ═══════════════════════════════════════
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle("Dashboard — Sales & Performance", fontsize=16)

# Top-left: line
axes[0, 0].plot(months, sales_2026, marker="o", color="steelblue")
axes[0, 0].set_title("Monthly Sales 2026")
axes[0, 0].set_ylabel("R$")
axes[0, 0].grid(True, alpha=0.3)

# Top-right: bar
axes[0, 1].bar(products, units_sold, color=colors)
axes[0, 1].set_title("Units Sold")
axes[0, 1].tick_params(axis="x", rotation=20)

# Bottom-left: pie
axes[1, 0].pie(units_sold, labels=products, autopct="%1.1f%%", startangle=90)
axes[1, 0].set_title("Market Share")

# Bottom-right: histogram
axes[1, 1].hist(exam_scores, bins=10, color="mediumseagreen", edgecolor="black")
axes[1, 1].set_title("Score Distribution")
axes[1, 1].set_xlabel("Score")

plt.tight_layout()
save("dashboard.png")

print("\nAll charts saved to outputs/")
print("LAB: Modify colors, data, and titles then re-run to see changes.")
