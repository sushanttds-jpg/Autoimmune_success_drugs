import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

# Data for medicines for autoimmune diseases with effectiveness rates (%)
medicines = [
    {"name": "Methotrexate", "success_rate": 75, "category": "DMARDs"},
    {"name": "Hydroxychloroquine", "success_rate": 65, "category": "Antimalarials"},
    {"name": "Sulfasalazine", "success_rate": 60, "category": "DMARDs"},
    {"name": "Infliximab (TNF inhibitor)", "success_rate": 85, "category": "Biologics"},
    {"name": "Etanercept (TNF inhibitor)", "success_rate": 80, "category": "Biologics"},
    {"name": "Adalimumab (TNF inhibitor)", "success_rate": 82, "category": "Biologics"},
    {"name": "Rituximab (B-cell inhibitor)", "success_rate": 88, "category": "Biologics"},
    {"name": "Abatacept (T-cell modulator)", "success_rate": 78, "category": "Biologics"},
    {"name": "Tocilizumab (IL-6 inhibitor)", "success_rate": 86, "category": "Biologics"},
    {"name": "Anakinra (IL-1 inhibitor)", "success_rate": 72, "category": "Biologics"},
    {"name": "Baricitinib (JAK inhibitor)", "success_rate": 84, "category": "JAK Inhibitors"},
    {"name": "Tofacitinib (JAK inhibitor)", "success_rate": 83, "category": "JAK Inhibitors"},
    {"name": "Upadacitinib (JAK inhibitor)", "success_rate": 85, "category": "JAK Inhibitors"},
    {"name": "Prednisolone (Corticosteroid)", "success_rate": 70, "category": "Corticosteroids"},
    {"name": "Azathioprine", "success_rate": 58, "category": "Immunosuppressants"},
    {"name": "Mycophenolate Mofetil", "success_rate": 68, "category": "Immunosuppressants"},
    {"name": "Leflunomide", "success_rate": 72, "category": "DMARDs"},
    {"name": "Certolizumab Pegol", "success_rate": 81, "category": "Biologics"},
    {"name": "Golimumab", "success_rate": 79, "category": "Biologics"},
    {"name": "Belimumab (B-LyS inhibitor)", "success_rate": 76, "category": "Biologics"},
]


medicine_names = [med["name"] for med in medicines]
success_rates = [med["success_rate"] for med in medicines]

category_data = defaultdict(list)
for med in medicines:
    category_data[med["category"]].append(med["success_rate"])

plt.style.use('bmh')
fig = plt.figure(figsize=(16, 12))
fig.canvas.manager.set_window_title("Autoimmune Medicine Analysis Image")
standard_colors = ['steelblue', 'darkorange', 'forestgreen', 'firebrick', 'mediumpurple', 'sienna']

# 1. Bar Chart - Success Rate by Medicine
ax1 = plt.subplot(2, 3, 1)
ax1.barh(medicine_names, success_rates, color='steelblue')
ax1.set_xlabel("Success Rate (%)")
ax1.set_title("Medicine Success Rates")
ax1.set_xlim(50, 95)

# 2. Line Graph - Success Rate Trend
ax2 = plt.subplot(2, 3, 2)
sorted_meds = sorted(medicines, key=lambda x: x["success_rate"])
sorted_names = [m["name"] for m in sorted_meds]
sorted_rates = [m["success_rate"] for m in sorted_meds]

ax2.plot(range(len(sorted_names)), sorted_rates, marker='o', color='firebrick', linewidth=2)
ax2.set_xticks(range(0, len(sorted_names), 2))
ax2.set_xticklabels([sorted_names[i] for i in range(0, len(sorted_names), 2)], rotation=45, ha='right')
ax2.set_ylabel("Success Rate (%)")
ax2.set_title("Success Rate Trend (Sorted)")

# 3. Pie Chart - Category Distribution
ax3 = plt.subplot(2, 3, 3)
categories = list(category_data.keys())
category_counts = [len(category_data[cat]) for cat in categories]
ax3.pie(category_counts, labels=categories, autopct='%1.1f%%', colors=standard_colors, startangle=90)
ax3.set_title("Distribution by Category")

# 4. Box Plot - Distribution by Category
ax4 = plt.subplot(2, 3, 4)
box_data = [category_data[cat] for cat in categories]
ax4.boxplot(box_data, tick_labels=categories, patch_artist=True, boxprops=dict(facecolor='lightgray'))
ax4.set_ylabel("Success Rate (%)")
ax4.set_title("Success Rate by Category")
plt.setp(ax4.xaxis.get_majorticklabels(), rotation=45, ha='right')

# 5. Scatter Plot - Success Rate
ax5 = plt.subplot(2, 3, 5)
ax5.scatter(range(len(medicines)), success_rates, s=100, color='darkorange', alpha=0.7, edgecolors='black')
ax5.set_xlabel("Medicine Index")
ax5.set_ylabel("Success Rate (%)")
ax5.set_title("Success Rate Distribution")

# 6. Bar Chart - Average Success Rate
ax6 = plt.subplot(2, 3, 6)
avg_rates = [np.mean(category_data[cat]) for cat in categories]
ax6.bar(categories, avg_rates, color='forestgreen')
ax6.set_ylabel("Average Success Rate (%)")
ax6.set_title("Average Rate by Category")
plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45, ha='right')
ax6.set_ylim(55, 90)

plt.tight_layout(h_pad=4)
plt.show()