# Student Performance Analysis

An exploratory data analysis of a student performance dataset (10,000 rows) using Python, pandas, and matplotlib. The notebook looks for patterns that separate students who got placed from those who didn't, and pulls out a few standalone stats about the dataset.

## Dataset

`student_dataset_10000_rows.csv` — 10,000 student records with the following columns:

| Column | Description |
|---|---|
| `study_hours` | Hours spent studying |
| `attendance` | Attendance percentage |
| `sleep_hours` | Hours of sleep |
| `internet_usage` | Internet usage (hours) |
| `assignments_completed` | Number of assignments completed |
| `previous_score` | Score from a previous exam/term |
| `exam_score` | Final exam score |
| `placement_status` | Whether the student was `Placed` or `Not Placed` |

## What the Notebook Does

1. **Load and inspect the data** — reads the CSV with `pandas` and checks its structure with `.info()`.
2. **Placement counts** — bar chart of how many students were `Placed` vs `Not Placed`.
3. **Placed vs. not placed comparison** — splits the data into placed and non-placed groups and compares their average:
   - Study hours
   - Sleep hours
   - Internet usage
   - Assignments completed
   - Previous score
4. **Standalone stats**:
   - Most and least hours slept by any student
   - Number of students who scored a perfect 100 on the exam
   - Number of students who scored 50 or below on the exam

## Built With

- **Python 3**
- **[pandas](https://pandas.pydata.org/)** — data loading and manipulation
- **[matplotlib](https://matplotlib.org/)** — bar chart visualizations

## Getting Started

### Prerequisites
```bash
pip install pandas matplotlib jupyter
```

### Running the notebook
```bash
git clone https://github.com/Mtahaseifi/data-analysis.git
cd data-analysis
jupyter notebook students_performance_analysis.ipynb
```

Make sure `student_dataset_10000_rows.csv` is in the same folder as the notebook.

## Roadmap

- [ ] Add a correlation analysis between numeric features and exam score
- [ ] Add a written summary/conclusion of findings at the end of the notebook
- [ ] Try a simple classification model to predict `placement_status`

## Author

**Mohammad Taha Seifi**
[GitHub](https://github.com/Mtahaseifi)
