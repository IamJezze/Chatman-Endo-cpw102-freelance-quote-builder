# Test Cases

Run both cases separately. Calculate expected labor cost and total before each run.

From the repository folder, run:

```text
python 03_execution/freelance_quote_builder.py
```

For each case, paste the terminal input and output as evidence. Mark Pass or Fail and briefly explain why. A passing run has correct amounts, a cleaned client name, the `PROJECT ESTIMATE` heading, labeled costs, and dollars with two decimal places.

## Case 1: Ordinary values

Enter:

- Client name: `Alex Taylor`
- Estimated hours: `4`
- Hourly rate: `30`
- Direct expenses: `15`

**Expected labor cost and total:**

**Evidence (paste your terminal run):**

```text

```

**Pass / Fail and why:**

## Case 2: Partial hours and text cleanup

Enter:

- Client name: `  aLEX tAYLOR  ` (include two spaces before and after the name)
- Estimated hours: `2.5`
- Hourly rate: `30`
- Direct expenses: `0`

The displayed name should be `Alex Taylor` without surrounding spaces.

**Expected labor cost and total:**

**Evidence (paste your terminal run):**

```text

```

**Pass / Fail and why:**

If a case fails, fix the program and add evidence of the rerun below that case.
