# Capstone: what predicts a struggling student?


> **Darsi briefs are short on purpose.** The in-app lesson shows tight numbered clicks. This README keeps the full commands, error fixes, and background for each milestone — open the matching **Milestone N** section when you need detail.

Use a public student dataset to explore limits, beat a simple baseline with honest cross-validation, report uncertainty with a bootstrap, check fairness across groups, and write a two-page memo a head teacher could use.

[العربية](README.ar.md)

## What you will be able to do

- Run real free tools from a laptop or Codespaces
- Finish five milestones, each with checks you can self-verify
- Leave with a portfolio piece: a report, demo or tool tagged v1.0
- **Darsi never runs your code** — it reads your link and check file, then an advisory review

## Install once

### Windows

1. Install Python 3.12: open PowerShell and run `winget install Python.Python.3.12`
2. Install Git: `winget install Git.Git`
3. Install VS Code from https://code.visualstudio.com (free)
4. On GitHub, open https://github.com/darsi-org/data-science-capstone and press **Use this template** to make your own copy. Then clone your copy, not darsi-org's: `git clone https://github.com/<your-username>/data-science-capstone.git`
5. Open a new PowerShell, go into the folder with `cd data-science-capstone`, and run these lines one at a time:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   python check.py
   ```

   If PowerShell says running scripts is disabled on this system, you don't need to change any setting: use Command Prompt and run `.venv\Scripts\activate.bat` instead, or skip activating and start every command with `.venv\Scripts\python` (for example `.venv\Scripts\python -m pip install -r requirements.txt`, then `.venv\Scripts\python check.py`).

### Mac

1. Install Homebrew from https://brew.sh if you don't have it
2. Install Python and Git: `brew install python@3.12 git`
3. Install VS Code from https://code.visualstudio.com
4. On GitHub, open https://github.com/darsi-org/data-science-capstone, press **Use this template**, then clone your copy: `git clone https://github.com/<your-username>/data-science-capstone.git`
5. In Terminal, go into the folder with `cd data-science-capstone` and run:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py
   ```

### Codespaces / Colab

No computer of your own? Use GitHub Codespaces, from a borrowed laptop too: open your copy → **Code** → **Codespaces** → **Create codespace**. Python and Git are already there. In its terminal, run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check.py
```

Or use Google Colab for the notebook in notebooks/: open `https://colab.research.google.com/github/<your-username>/data-science-capstone/blob/main/notebooks/01_explore.ipynb` (your username in place of `<your-username>`), put your copy's address in the first cell and run it. That cell clones your copy and moves into it. Colab works on its own copy, so download what you made (figures/ and results/) and add it to your repository on GitHub (**Add file** → **Upload files**).

A phone browser is enough to read the results.

## Start

Press **Use this template** on https://github.com/darsi-org/data-science-capstone, clone your copy, then follow milestone 1.

## Milestones

### m1: Explore the data and its limits (3 hours)

#### Why this matters
Before any model, you need to know who is in the data and who is missing. Data collected in 2005–2006 at two Portuguese schools (published 2008) is not Egyptian students today.

#### Tools for this milestone
- **ucimlrepo** — downloads the UCI Student Performance set. Get it: pip install -r requirements.txt
- **Jupyter / Colab** — runs the explore notebook in a browser. Get it: https://colab.research.google.com or Codespaces

#### Do this
1. Set up your copy as in **Install once** (your copy, not darsi-org's).
2. Run `python fetch_data.py`. It saves data/students.csv (649 Portuguese secondary students). The notebook's first cell does this too when the file is missing.
3. Open notebooks/01_explore.ipynb in VS Code or Colab and run its first cell first: it moves to the top folder of the repository, so `plt.savefig("figures/<name>.png")` saves into the repository's figures/ folder, where check.py looks. Make five charts: G3 distribution (the notebook has it as an example), absences, study time vs G3, plus two of your choice.
4. Write LIMITS.md: where and when the data was collected, who is missing, and why it is not about Egyptian students.
5. Add a Colab or notebook link in README.md. Run python check.py --milestone m1.

#### You know you're done when
- figures/ has five PNGs
- LIMITS.md is written
- m1 passes and the notebook link opens

#### If something goes wrong
- **ucimlrepo download fails** → Check your internet; retry. The dataset id is 320.
- **Notebook kernel missing** → Select the .venv interpreter in VS Code, or use Colab
- **check.py wants five figures** → Run the notebook's first cell, then save with `plt.savefig("figures/<name>.png")`. The PNGs belong in figures/ at the top of the repository, not in notebooks/figures/

#### What you should understand
You can describe a dataset's shape and say clearly who it does not represent.

**Hand in:** The notebook link, five charts, LIMITS.md, and darsi-check.json that passes m1.

### m2: A baseline, then three models (4 hours)

#### Why this matters
A fancy model that barely beats 'predict the average' is not progress. A seeded split and cross-validation keep you honest.

#### Tools for this milestone
- **scikit-learn** — kNN, linear regression, decision tree, cross-validation. Get it: in requirements.txt

#### Do this
1. Split once: 80% train, 20% test, random_state fixed. Do not look at the test set yet.
2. Decide whether G1 and G2 (the term 1 and term 2 grades) are features. With them, your model is a term-2 check: G3 follows them closely, so it beats the baseline easily. Without them, it is an early warning, before any grades exist. Write your choice and why under your metrics table.
3. Baseline: predict the training mean of G3 for everyone. Record its MAE, cross-validated like the models, as baseline_mae in results/cv.json.
4. Train k-nearest neighbours, linear regression and a decision tree with 5-fold CV on the training part only. Log each CV MAE.
5. Set test_used to false in results/cv.json. Run python check.py --milestone m2.

#### Worked example: seeded 5-fold cross-validation
Run it from the top folder of your repository (in the notebook, after its first cell). This version leaves G1 and G2 out, an early warning. If you keep them, take them out of the drop list, but always drop G3: it is the answer.

```python
import json
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

SEED = 42
df = pd.read_csv("data/students.csv")
X = pd.get_dummies(df.drop(columns=["G1", "G2", "G3"]), drop_first=True)  # words become 0/1 columns
y = df["G3"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED)  # test: not yet

folds = KFold(n_splits=5, shuffle=True, random_state=SEED)
models = {
    "baseline": DummyRegressor(strategy="mean"),  # the training mean for everyone
    "knn": make_pipeline(StandardScaler(), KNeighborsRegressor(n_neighbors=10)),
    "linear": LinearRegression(),
    "tree": DecisionTreeRegressor(max_depth=4, random_state=SEED),
}
cv_mae = {}
for name, model in models.items():
    scores = cross_val_score(model, X_train, y_train, cv=folds, scoring="neg_mean_absolute_error")
    cv_mae[name] = round(float(-scores.mean()), 3)  # scikit-learn reports MAE as a negative number
print(cv_mae)
with open("results/cv.json", "w") as f:
    json.dump({"seed": SEED, "baseline_mae": cv_mae["baseline"], "cv_mae": cv_mae, "test_used": False}, f, indent=2)
```

`cross_val_score` cuts the training part into 5 folds, trains on 4 and scores the fifth, five times over; the test part is never used. kNN measures distances, so its pipeline scales every column first.

#### You know you're done when
- results/cv.json has seed, baseline_mae and test_used false
- Your metrics table says whether G1 and G2 are features, and why
- m2 passes

#### If something goes wrong
- **Scores look perfect (MAE near 0)** → You probably evaluated on the training set; use cross_val_score on train only
- **Different numbers every run** → Set random_state everywhere and save it as seed in cv.json

#### What you should understand
You can compare models against a dumb baseline with a seeded split, without peeking at the test set.

**Hand in:** results/cv.json, your metrics table with one sentence on G1 and G2, and darsi-check.json that passes m2.

### m3: How sure are you? The bootstrap (3 hours)

#### Why this matters
One MAE hides how much it could move. A bootstrap interval shows how much, and a paired interval of the difference shows whether your model really beat the baseline.

#### Tools for this milestone
- **numpy / pandas** — resample the test rows 1,000 times. Get it: in requirements.txt

#### Do this
1. Evaluate your chosen model once on the test set. Save test MAE.
2. Bootstrap: resample the test rows 1,000 times with replacement. Each time, compute your model's MAE and the baseline's MAE on the same rows, and record baseline MAE − model MAE. The 2.5th and 97.5th percentiles of each are 95% intervals: ci95 (your model), baseline_ci95 (the baseline) and diff_ci95 (the difference).
3. Read diff_ci95. If all of it is above 0, your model really beats the baseline. If it includes 0, this test set can't tell them apart: say so. Don't judge by whether ci95 and baseline_ci95 overlap: two separate intervals can overlap even when one model is reliably better. Write one sentence on what diff_ci95 says, and save results/test.json.
4. Run python check.py --milestone m3.

#### Worked example: a paired bootstrap
Run it after the m2 example, with the same SEED and split, so the test rows are the ones you never used.

```python
import numpy as np

best = models["linear"].fit(X_train, y_train)  # the model you chose in m2, trained on all of the training part
err_model = np.abs(y_test.to_numpy() - best.predict(X_test))
err_base = np.abs(y_test.to_numpy() - y_train.mean())

rng = np.random.default_rng(SEED)
rows = rng.integers(0, len(y_test), size=(1000, len(y_test)))  # 1,000 resamples of the test rows
model_mae = err_model[rows].mean(axis=1)  # each resample scores both on the SAME rows
base_mae = err_base[rows].mean(axis=1)
diff = base_mae - model_mae  # above 0: the model did better

def ci95(values):
    return [round(float(x), 3) for x in np.percentile(values, [2.5, 97.5])]

result = {"seed": SEED, "test_mae": round(float(err_model.mean()), 3), "baseline_test_mae": round(float(err_base.mean()), 3),
          "ci95": ci95(model_mae), "baseline_ci95": ci95(base_mae), "diff_ci95": ci95(diff)}
print(result)
with open("results/test.json", "w") as f:
    json.dump(result, f, indent=2)
```

Why pair them: a student who is easy to predict is easy for both, so the two MAEs rise and fall together from one resample to the next. Their difference moves less than the two intervals side by side suggest, which is why overlap is the wrong test.

#### You know you're done when
- results/test.json has ci95, baseline_ci95 and diff_ci95
- m3 passes

#### If something goes wrong
- **Interval is a single number** → Store both ends, e.g. [low, high]
- **Bootstrap takes forever** → 1,000 resamples of the test vector is enough; don't retrain inside the loop
- **ci95 and baseline_ci95 overlap, but diff_ci95 is all above 0** → That's normal. Trust diff_ci95: both were scored on the same students.

#### What you should understand
You can report uncertainty, not just a point score, and use a paired interval to say whether two models truly differ.

**Hand in:** results/test.json (with diff_ci95), one sentence on whether the difference interval is above 0, and darsi-check.json that passes m3.

### m4: Is it fair? Errors by group (3 hours)

#### Why this matters
An average can hide a group the model fails. Schools should see that before they trust a score.

#### Tools for this milestone
- **pandas groupby** — MAE per school, urban/rural, sex. Get it: built into your stack

#### Do this
1. Compute test MAE separately by school, by urban/rural address, and by sex. Save before numbers in results/groups.json.
2. Find the biggest gap and suggest why (fewer examples? different grading?).
3. Try one fix (reweight the smaller group, or drop a proxy feature) and save after numbers.
4. Run python check.py --milestone m4.

#### You know you're done when
- results/groups.json has before and after
- m4 passes

#### If something goes wrong
- **A group has zero rows** → Merge rare levels or report 'n too small' instead of a fake MAE
- **Fix makes average worse and gap worse** → Say so honestly; not every fix helps. Try a different one.

#### What you should understand
You can measure error gaps across groups and try one concrete fix without hiding the trade-off.

**Hand in:** results/groups.json, a short note on the gap, and darsi-check.json that passes m4.

### m5: A memo a school could use (3 hours)

#### Why this matters
The skill is not the notebook; it is advice a head teacher can act on without being misled.

#### Tools for this milestone
- **GitHub Actions** — re-runs notebooks top to bottom. Get it: workflow in the starter
- **GitHub Release** — a fixed version of your memo and code. Get it: tag v1.0

#### Do this
1. Write MEMO.md (English or Arabic, two pages max): question, data limits, best model vs baseline with the difference interval, fairness gaps, three recommendations, and what a school should NOT do.
2. Say what local data, with consent, would be needed to do this properly in Egypt.
3. Push so Actions runs the notebooks. Tag release v1.0. Run python check.py --milestone m5.
4. Explain the whole project in your own words on Darsi.

#### You know you're done when
- MEMO.md says what not to do
- v1.0 exists and m5 passes

#### If something goes wrong
- **Actions fails while fetching the data** → The notebook's first cell fetches it when data/students.csv is missing; if the UCI site is down, commit data/students.csv (its licence, CC BY 4.0, allows it)
- **MEMO is longer than two pages** → Cut charts; link the notebook instead

#### What you should understand
You can turn a modelling project into careful advice that names limits and refuses harmful uses.

**Hand in:** MEMO.md, a green Actions run, v1.0, darsi-check.json that passes m5, and your explanation.

## The check

Run `python check.py` or `python check.py --milestone m2`. It only reads files, writes `darsi-check.json`, and prints English and Arabic. It uploads nothing.

## Review on Darsi

Send your repository link and `darsi-check.json` with each milestone on Darsi. Darsi reads your latest Actions run and release from GitHub's public API, adds an advisory AI review, then your teacher or the Darsi team reviews it. **Darsi never runs your code.**

## Licence

MIT — see [LICENSE](LICENSE).
