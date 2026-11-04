# Capstone: what predicts a struggling student?

Use a public student dataset to explore limits, beat a simple baseline with honest cross-validation, report uncertainty with a bootstrap, check fairness across groups, and write a two-page memo a head teacher could use.

[العربية](README.ar.md)

## What you will be able to do

- Run real free tools from a laptop or Codespaces
- Finish five milestones, each with checks you can self-verify
- Leave with a portfolio piece: a report, demo or tool tagged v1.0
- **Darsi never runs your code** — it reads your link and check file, then an advisory review

## Install once

### Windows

1. Install Python 3.12: open PowerShell and run winget install Python.Python.3.12
2. Install Git: winget install Git.Git
3. Install VS Code from https://code.visualstudio.com (free)
4. On GitHub, open https://github.com/darsi-org/data-science-capstone and press Use this template, then Clone your copy
5. In the project folder run:
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   python check.py

### Mac

1. Install Homebrew from https://brew.sh if you don't have it
2. brew install python@3.12 git
3. Install VS Code from https://code.visualstudio.com
4. On GitHub open https://github.com/darsi-org/data-science-capstone → Use this template → clone your copy
5. In the project folder run:
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python check.py

### Codespaces / Colab

No computer of your own? Use GitHub Codespaces: open your copy → Code → Codespaces → Create codespace. Everything installs there. Or open a notebook in Google Colab, run the first cell that clones your repo, then run python check.py. Both work from a borrowed laptop; a phone browser is enough to read results.

## Start

Press **Use this template** on https://github.com/darsi-org/data-science-capstone, clone your copy, then follow milestone 1.

## Milestones

### m1: Explore the data and its limits (3 hours)

## Why this matters
Before any model, you need to know who is in the data and who is missing. A Portuguese 2008 dataset is not Egyptian students today.

## Tools for this milestone
- **ucimlrepo** — downloads the UCI Student Performance set. Get it: pip install -r requirements.txt
- **Jupyter / Colab** — runs the explore notebook in a browser. Get it: https://colab.research.google.com or Codespaces

## Do this
1. Clone your copy of https://github.com/darsi-org/data-science-capstone and set up the venv as in the setup tab.
2. Run: python fetch_data.py. It saves data/students.csv (649 Portuguese secondary students).
3. Open notebooks/01_explore.ipynb in VS Code or Colab. Make five charts: G3 distribution, absences, study time vs G3, plus two of your choice. Save them in figures/.
4. Write LIMITS.md: where and when the data was collected, who is missing, and why it is not about Egyptian students.
5. Add a Colab or notebook link in README.md. Run python check.py --milestone m1.

## You know you're done when
- figures/ has five PNGs
- LIMITS.md is written
- m1 passes and the notebook link opens

## If something goes wrong
- **ucimlrepo download fails** → Check your internet; retry. The dataset id is 320.
- **Notebook kernel missing** → Select the .venv interpreter in VS Code, or use Colab
- **check.py wants five figures** → Save exactly into figures/*.png from the notebook

## What you should understand
You can describe a dataset's shape and say clearly who it does not represent.

**Hand in:** The notebook link, five charts, LIMITS.md, and darsi-check.json that passes m1.

### m2: A baseline, then three models (4 hours)

## Why this matters
A fancy model that barely beats 'predict the average' is not progress. A seeded split and cross-validation keep you honest.

## Tools for this milestone
- **scikit-learn** — kNN, linear regression, decision tree, cross-validation. Get it: in requirements.txt

## Do this
1. Split once: 80% train, 20% test, random_state fixed. Do not look at the test set yet.
2. Baseline: predict the training mean of G3 for everyone. Record MAE in results/cv.json.
3. Train k-nearest neighbours, linear regression and a decision tree with 5-fold CV on the training part only. Log each CV MAE.
4. Set test_used to false in results/cv.json. Run python check.py --milestone m2.

## You know you're done when
- results/cv.json has seed, baseline_mae and test_used false
- m2 passes

## If something goes wrong
- **Scores look perfect (MAE near 0)** → You probably evaluated on the training set; use cross_val_score on train only
- **Different numbers every run** → Set random_state everywhere and save it as seed in cv.json

## What you should understand
You can compare models against a dumb baseline with a seeded split, without peeking at the test set.

**Hand in:** results/cv.json, your metrics table, and darsi-check.json that passes m2.

### m3: How sure are you? The bootstrap (3 hours)

## Why this matters
One MAE hides how much it could move. A bootstrap interval shows whether your model really beat the baseline.

## Tools for this milestone
- **numpy / pandas** — resample predictions 1,000 times. Get it: in requirements.txt

## Do this
1. Evaluate your chosen model once on the test set. Save test MAE.
2. Bootstrap: resample the test predictions 1,000 times with replacement. Take the 2.5th and 97.5th percentiles as a 95% interval.
3. Do the same for the baseline. Write one sentence on whether the intervals overlap. Save results/test.json.
4. Run python check.py --milestone m3.

## You know you're done when
- results/test.json has ci95 and baseline_ci95
- m3 passes

## If something goes wrong
- **Interval is a single number** → Store both ends, e.g. [low, high]
- **Bootstrap takes forever** → 1,000 resamples of the test vector is enough; don't retrain inside the loop

## What you should understand
You can report uncertainty, not just a point score, and say whether two models truly differ.

**Hand in:** results/test.json, one sentence on overlap, and darsi-check.json that passes m3.

### m4: Is it fair? Errors by group (3 hours)

## Why this matters
An average can hide a group the model fails. Schools should see that before they trust a score.

## Tools for this milestone
- **pandas groupby** — MAE per school, urban/rural, sex. Get it: built into your stack

## Do this
1. Compute test MAE separately by school, by urban/rural address, and by sex. Save before numbers in results/groups.json.
2. Find the biggest gap and suggest why (fewer examples? different grading?).
3. Try one fix (reweight the smaller group, or drop a proxy feature) and save after numbers.
4. Run python check.py --milestone m4.

## You know you're done when
- results/groups.json has before and after
- m4 passes

## If something goes wrong
- **A group has zero rows** → Merge rare levels or report 'n too small' instead of a fake MAE
- **Fix makes average worse and gap worse** → Say so honestly; not every fix helps. Try a different one.

## What you should understand
You can measure error gaps across groups and try one concrete fix without hiding the trade-off.

**Hand in:** results/groups.json, a short note on the gap, and darsi-check.json that passes m4.

### m5: A memo a school could use (3 hours)

## Why this matters
The skill is not the notebook; it is advice a head teacher can act on without being misled.

## Tools for this milestone
- **GitHub Actions** — re-runs notebooks top to bottom. Get it: workflow in the starter
- **GitHub Release** — a fixed version of your memo and code. Get it: tag v1.0

## Do this
1. Write MEMO.md (English or Arabic, two pages max): question, data limits, best model vs baseline with interval, fairness gaps, three recommendations, and what a school should NOT do.
2. Say what local data, with consent, would be needed to do this properly in Egypt.
3. Push so Actions runs the notebooks. Tag release v1.0. Run python check.py --milestone m5.
4. Explain the whole project in your own words on Darsi.

## You know you're done when
- MEMO.md says what not to do
- v1.0 exists and m5 passes

## If something goes wrong
- **Actions fails on missing data file** → Commit data/students.csv or re-run fetch in the workflow
- **MEMO is longer than two pages** → Cut charts; link the notebook instead

## What you should understand
You can turn a modelling project into careful advice that names limits and refuses harmful uses.

**Hand in:** MEMO.md, a green Actions run, v1.0, darsi-check.json that passes m5, and your explanation.

## The check

Run `python check.py` or `python check.py --milestone m2`. It only reads files, writes `darsi-check.json`, and prints English and Arabic. It uploads nothing.

## Review on Darsi

Send your repository link and `darsi-check.json` with each milestone on Darsi. Darsi reads your latest Actions run and release from GitHub's public API, adds an advisory AI review, then your teacher or the Darsi team reviews it. **Darsi never runs your code.**

## Licence

MIT — see [LICENSE](LICENSE).
