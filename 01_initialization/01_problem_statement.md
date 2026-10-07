# Problem Statement

## Freelance Quote Builder

A freelance graphic designer creates logos, flyers, and business cards for local small businesses. They currently calculate project costs by hand and want a simple terminal tool to prepare an estimate for one project at a time.

The designer will enter the client's name, estimated work hours, hourly rate, and direct expenses such as materials. Some jobs take partial hours, such as 2.5 hours. Labor cost is the hours multiplied by the hourly rate; adding direct expenses gives the total estimate.

The designer wants a readable result headed `PROJECT ESTIMATE`, showing the client's name, labor cost, direct expenses, and total estimate. Each amount should have a dollar sign and two decimal places, such as `$75.00`. Names sometimes arrive with extra spaces or mixed capitalization, so an entry like `  aLEX tAYLOR  ` should appear as `Alex Taylor`.

## Example terminal run

```text
Client name:   aLEX tAYLOR  
Estimated work hours: 7.5
Hourly rate: 40
Direct expenses: 25

PROJECT ESTIMATE
Client: Alex Taylor
Labor cost: $300.00
Direct expenses: $25.00
Total estimate: $325.00
```

The client input includes surrounding spaces. Your prompts and layout may differ.

## Technical expectations

Organize the program with `main()` and call it to start the interaction. Write at least one calculation function that accepts parameter(s) and returns a number. Use `.strip()` and `.title()` for the name cleanup. Choose readable variable names and use comments. 

## Assumptions

Assume valid, nonnegative numeric input without dollar signs or commas. Expenses may be zero. Input validation is not required; invalid numeric input may cause a crash. 

No conditionals, loops, exception handling, libraries, file storage, or automated tests should be used. 
