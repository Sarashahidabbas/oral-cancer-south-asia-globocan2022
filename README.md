# Oral Cancer Outcomes Across South Asia

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Data](https://img.shields.io/badge/Data-GLOBOCAN%202022-1f4e79)
![Licence](https://img.shields.io/badge/Licence-MIT-green)

![Mortality ratio by country](figures/fig1_mortality_incidence_ratio.png)

## Getting Started

```sh
git clone https://github.com/Sarashahidabbas/oral-cancer-south-asia-globocan2022.git
cd oral-cancer-south-asia-globocan2022
pip install -r requirements.txt
python analysis.py                                      # tables to results/, figures to figures/
jupyter notebook oral_cancer_south_asia_analysis.ipynb  # full walkthrough with outputs
```

The result, in deaths per new case of lip and oral cavity cancer (2022):

```
Pakistan      0.64
Bangladesh    0.59
India         0.56
Sri Lanka     0.47
```

Pakistan recorded 64 deaths per 100 new cases. Sri Lanka recorded 47.

## Table of Contents

- [Introduction](#introduction)
- [Data](#data)
- [Methods](#methods)
- [Results](#results)
- [Interpretation](#interpretation)
- [Limitations](#limitations)
- [Repository structure](#repository-structure)
- [Getting help](#getting-help)
- [Citing](#citing)

## Introduction

Oral cancer shows early. Chewing tobacco and betel quid raise the risk across South Asia. Outcomes still differ by country. This project compares Pakistan, India, Bangladesh and Sri Lanka with public GLOBOCAN 2022 estimates and sizes the gap in deaths.

Main question: How does the mortality-to-incidence ratio for lip and oral cavity cancer differ across the four countries in 2022?

Supporting questions:
1. Which country holds the largest share of regional cases and deaths?
2. Do countries with a higher mortality ratio show fewer five-year prevalent patients per new case?

## Data

Source: GLOBOCAN 2022, International Agency for Research on Cancer (IARC), https://gco.iarc.who.int

| Item | Detail |
|---|---|
| Cancer site | Lip, oral cavity |
| Population | All ages |
| Variables | New cases, deaths, five-year prevalence |
| File | `data/globocan2022_south_asia_oral_cancer.csv` |
| Provenance | Typed by hand from the IARC country fact sheets. Each row holds its fact sheet URL |

Check every number against the fact sheet before you cite this work.

## Methods

### Indicators

Three indicators, calculated per country:

- Mortality-to-incidence ratio: deaths divided by new cases. The main outcome, used as a proxy for survival and access to care.
- Prevalence per new case: five-year prevalence divided by new cases. A second view of how many patients live after diagnosis.
- Share of the four-country total, for cases and deaths.

### Scenario

A scenario applies Sri Lanka's ratio (the lowest) to the new cases of the other three countries and compares the result with observed deaths. The scenario sizes the gap and makes no claim about avoidable deaths.

### Tools

Python, pandas, matplotlib.

## Results

### Country table

| Country | New cases | Deaths | Mortality ratio | Prevalence per new case | Share of cases | Share of deaths |
|---|---|---|---|---|---|---|
| Pakistan | 15,915 | 10,181 | 0.64 | 2.28 | 8.9% | 10.1% |
| Bangladesh | 16,083 | 9,447 | 0.59 | 2.50 | 9.0% | 9.4% |
| India | 143,759 | 79,979 | 0.56 | 2.57 | 80.6% | 79.3% |
| Sri Lanka | 2,556 | 1,198 | 0.47 | 2.93 | 1.4% | 1.2% |

### Findings

- Pakistan's ratio is 36% higher than Sri Lanka's.
- Prevalence per new case runs in the opposite order. Sri Lanka keeps 2.93 patients alive per new case and Pakistan 2.28.
- India holds 80.6% of cases and 79.3% of deaths.
- Pakistan and Bangladesh carry a larger share of deaths than of cases.
- At Sri Lanka's ratio, India, Pakistan and Bangladesh would record 17,177 fewer deaths (12,556 in India, 2,717 in Pakistan, 1,904 in Bangladesh). This figure is illustrative.

### Figures

![Prevalence per new case](figures/fig2_prevalence_per_new_case.png)
![Share of cases and deaths](figures/fig3_share_of_cases_and_deaths.png)
![Deaths above the best ratio](figures/fig4_deaths_above_best_ratio.png)

## Interpretation

A high ratio points to late diagnosis, limited access to surgery and radiotherapy, weak follow-up, or incomplete registration. This analysis does not test which one applies. Two measures agree on the ranking. Four countries are too few for statistical testing.

The next question: what separates Sri Lanka's path from diagnosis to treatment from the paths in Pakistan and Bangladesh? Start with early detection programmes and treatment access.

## Limitations

1. Country-level data. The results say nothing about individual patients.
2. The ratio approximates survival. Deaths and new cases in one year do not follow the same patients.
3. GLOBOCAN values are modelled estimates. Countries with thin registry coverage carry more uncertainty.
4. Values were typed by hand from fact sheets.
5. No age standardisation. Age structure differs by country.
6. One year, four countries. No trend and no causal claim.
7. The scenario treats Sri Lanka as a fair benchmark. Case mix and registry quality differ.

## Repository structure

```
.
├── README.md
├── analysis.py
├── oral_cancer_south_asia_analysis.ipynb
├── requirements.txt
├── data/
│   └── globocan2022_south_asia_oral_cancer.csv
├── results/
│   ├── results_table.csv
│   └── scenario_deaths_above_best_ratio.csv
└── figures/
    ├── fig1_mortality_incidence_ratio.png
    ├── fig2_prevalence_per_new_case.png
    ├── fig3_share_of_cases_and_deaths.png
    └── fig4_deaths_above_best_ratio.png
```

## Getting help

Open an issue on this repository for questions, errors in the data, or suggestions. Include the file name and the row.

## Citing

Data: Ferlay J, Ervik M, Lam F, et al. Global Cancer Observatory: Cancer Today. Lyon, France: International Agency for Research on Cancer, 2024. https://gco.iarc.who.int

This repository: Sara. Oral cancer outcomes across South Asia, GLOBOCAN 2022. GitHub, https://github.com/Sarashahidabbas/oral-cancer-south-asia-globocan2022

## Licence

Code: MIT. The data belong to IARC and follow their terms of use.
