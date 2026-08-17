# Titanic Data Analysis

An exploratory data analysis of the classic Titanic passenger dataset using Python, pandas, and matplotlib. The notebook looks at who survived, how survival broke down by sex, and pulls out a few other stats about the passengers.

## Dataset

`titanic.csv` — Titanic passenger records, including (at least) these columns:

| Column | Description |
|---|---|
| `Sex` | Passenger's sex |
| `Survived` | Survival status (0 = dead, 1 = survived) |
| `Age` | Passenger's age |
| `Fare` | Ticket fare paid |

## What the Notebook Does

1. **Load and inspect the data** — reads `titanic.csv` with `pandas`.
2. **Sex distribution** — bar chart of passenger counts by sex.
3. **Overall survival** — pie chart of how many passengers survived vs. died.
4. **Survival by sex** — separate pie charts breaking down survival for males and for females.
5. **Age stats** — oldest passenger, youngest passenger, and average age; also looks up the record for the youngest passenger (age 0.42).
6. **Age vs. fare** — scatter plot exploring the relationship between passenger age and ticket fare.
7. **High fares** — pulls out all passengers who paid a fare of 500 or more.

## Built With

- **Python 3**
- **[pandas](https://pandas.pydata.org/)** — data loading and manipulation
- **[matplotlib](https://matplotlib.org/)** — bar, pie, and scatter plot visualizations

## Getting Started

### Prerequisites
```bash
pip install pandas matplotlib jupyter
```

### Running the notebook
```bash
git clone https://github.com/Mtahaseifi/data-analysis.git
cd data-analysis
jupyter notebook titanic_analysis.ipynb
```

Make sure `titanic.csv` is in the same folder as the notebook.

## Roadmap

- [ ] Handle missing `Age` values explicitly instead of relying on `dropna()` only for the scatter plot
- [ ] Add survival breakdown by passenger class (`Pclass`) if available in the dataset
- [ ] Add a written summary/conclusion of findings at the end of the notebook

## Author

**Mohammad Taha Seifi**
[GitHub](https://github.com/Mtahaseifi)
