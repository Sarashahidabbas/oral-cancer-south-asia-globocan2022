"""Oral cancer outcomes across South Asia, GLOBOCAN 2022.
Run from the repository folder: python analysis.py
Needs: pandas, matplotlib
"""
import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("results", exist_ok=True)
os.makedirs("figures", exist_ok=True)

DATA = "data/globocan2022_south_asia_oral_cancer.csv"

df = pd.read_csv(DATA)
df = df.rename(columns={
    "New_cases_both_sexes": "New_cases",
    "Deaths_both_sexes": "Deaths",
    "Five_year_prevalence_both_sexes": "Five_year_prevalence",
})

# Main outcome: deaths per new case
df["Mortality_to_incidence_ratio"] = (df["Deaths"] / df["New_cases"]).round(3)
# Supporting outcome: five-year prevalent patients per new case
df["Prevalence_per_new_case"] = (df["Five_year_prevalence"] / df["New_cases"]).round(2)
# Share of the four-country total
df["Share_of_cases_pct"] = (100 * df["New_cases"] / df["New_cases"].sum()).round(1)
df["Share_of_deaths_pct"] = (100 * df["Deaths"] / df["Deaths"].sum()).round(1)

df = df.sort_values("Mortality_to_incidence_ratio", ascending=False).reset_index(drop=True)
cols = ["Country", "New_cases", "Deaths", "Five_year_prevalence",
        "Mortality_to_incidence_ratio", "Prevalence_per_new_case",
        "Share_of_cases_pct", "Share_of_deaths_pct"]
df[cols].to_csv("results/results_table.csv", index=False)
print(df[cols].to_string(index=False))

# Figure 1: mortality-to-incidence ratio
fig, ax = plt.subplots(figsize=(7, 4))
d = df.sort_values("Mortality_to_incidence_ratio")
bars = ax.barh(d["Country"], d["Mortality_to_incidence_ratio"], color="#1f4e79")
for b, v in zip(bars, d["Mortality_to_incidence_ratio"]):
    ax.text(v + 0.01, b.get_y() + b.get_height() / 2, f"{v:.2f}", va="center")
ax.set_xlim(0, 0.8)
ax.set_xlabel("Deaths per new case")
ax.set_title("Oral cancer mortality-to-incidence ratio, 2022")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("figures/fig1_mortality_incidence_ratio.png", dpi=200)
plt.close()

# Figure 2: five-year prevalent patients per new case
fig, ax = plt.subplots(figsize=(7, 4))
d = df.sort_values("Prevalence_per_new_case")
bars = ax.barh(d["Country"], d["Prevalence_per_new_case"], color="#5d8aa8")
for b, v in zip(bars, d["Prevalence_per_new_case"]):
    ax.text(v + 0.03, b.get_y() + b.get_height() / 2, f"{v:.2f}", va="center")
ax.set_xlim(0, 3.5)
ax.set_xlabel("Five-year prevalent patients per new case")
ax.set_title("Oral cancer five-year prevalence per new case, 2022")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("figures/fig2_prevalence_per_new_case.png", dpi=200)
plt.close()

# Figure 3: share of regional cases and deaths
fig, ax = plt.subplots(figsize=(7, 4))
d = df.sort_values("Share_of_cases_pct", ascending=False)
x = range(len(d))
w = 0.38
ax.bar([i - w / 2 for i in x], d["Share_of_cases_pct"], w, label="New cases", color="#1f4e79")
ax.bar([i + w / 2 for i in x], d["Share_of_deaths_pct"], w, label="Deaths", color="#b03a2e")
ax.set_xticks(list(x))
ax.set_xticklabels(d["Country"])
ax.set_ylabel("Share of four-country total (%)")
ax.set_title("Share of regional oral cancer cases and deaths, 2022")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("figures/fig3_share_of_cases_and_deaths.png", dpi=200)
plt.close()

# Illustrative scenario: deaths if each country matched the best ratio in the group
best = df["Mortality_to_incidence_ratio"].min()
best_country = df.loc[df["Mortality_to_incidence_ratio"].idxmin(), "Country"]
sc = df[df["Country"] != best_country][["Country", "New_cases", "Deaths"]].copy()
sc["Deaths_at_best_ratio"] = (sc["New_cases"] * best).round(0).astype(int)
sc["Deaths_above_best_ratio"] = sc["Deaths"] - sc["Deaths_at_best_ratio"]
sc = sc.sort_values("Deaths_above_best_ratio", ascending=False)
sc.to_csv("results/scenario_deaths_above_best_ratio.csv", index=False)
print("\nBest ratio:", best_country, round(best, 3))
print(sc.to_string(index=False))
print("Total deaths above best ratio:", sc["Deaths_above_best_ratio"].sum())

# Figure 4: deaths above the best ratio
fig, ax = plt.subplots(figsize=(7, 4))
d = sc.sort_values("Deaths_above_best_ratio")
bars = ax.barh(d["Country"], d["Deaths_above_best_ratio"], color="#b03a2e")
for b, v in zip(bars, d["Deaths_above_best_ratio"]):
    ax.text(v + 200, b.get_y() + b.get_height() / 2, f"{v:,}", va="center")
ax.set_xlim(0, d["Deaths_above_best_ratio"].max() * 1.18)
ax.set_xlabel(f"Deaths above the {best_country} ratio (illustrative)")
ax.set_title("Deaths above the best regional ratio, 2022")
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("figures/fig4_deaths_above_best_ratio.png", dpi=200)
plt.close()
