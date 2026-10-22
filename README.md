# Python Training for Risk Teams

Welcome! This repository holds the notebooks for the course. Materials are added here as the course progresses, so check back before each session.

## Course outline

| Session | Topic | Student | Coach (lectures) |
|---|---|---|---|
| 1 | Python Fundamentals | Available | Available |
| 2 | Data Extraction & Manipulation | Available | Available |
| 3 | Data Quality & Exploratory Analysis | Available | Available |
| 4 | Statistics for Risk Analysis | Coming soon | Coming soon |
| 5 | Machine Learning for Model Developers | Coming soon | Coming soon |

## How the materials work

Each session contains two kinds of notebook:

- **Lectures** (`_Lecture_`): the walkthrough we follow together in the session.
- **Practicals** (`_Practical_`, `_Project_`): hands-on exercises for you to complete.

Notebooks come in two versions:

| Version | When it is available | What it contains |
|---|---|---|
| **Student** (`_Student`) | Before the session | Exercises with empty `# Your turn` cells for you to complete |
| **Coach** (`_Coach`) | After the session | The same notebook with worked answers |

Please attempt the exercises yourself before looking at the Coach version. That is where most of the learning happens.

## Getting the materials

**Option 1: Download (no Git needed)**
Click the green **Code** button, then **Download ZIP**. Download again after each session to get the new files.

**Option 2: Clone with Git**

```bash
git clone https://github.com/masrazo/CBS---Python-Training-for-Risk-Teams_BLANK.git
```

Then run `git pull` before each session to get the latest files.

> **Tip:** Make a copy of a notebook before working in it (for example `01_07_Practical_..._MyAnswers.ipynb`). If you edit the original files, `git pull` may report conflicts when new versions are released.

## Setup

- Python 3.10 or later with Jupyter (Anaconda is the simplest option), or the course environment provided by your trainer.
- Packages used: `pandas`, `numpy`, `matplotlib`, `seaborn`, `sweetviz`. Install any missing ones with:

  ```bash
  pip install pandas numpy matplotlib seaborn sweetviz
  ```

- Open notebooks from inside their session folder so that imports such as `from config import session_datasets` work.

## Data

Most datasets are read directly from online links in the notebooks or from the `config.py` file in each session folder, so you do not need to download them separately. You will need an internet connection.

## Getting help

If something does not run, first restart the kernel and run all cells from the top. If it still fails, bring the error message to the next session or contact your trainer.
