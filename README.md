# CPW 102 Freelance Quote Builder Project

This project is organized into phases. Complete each phase in order.

Each folder represents a phase of the engineering design process:

```text
01_initialization
02_planning
03_execution
04_testing
05_shipping
```

---

# Before You Start

You will create your own GitHub repository from the course template, clone it to your computer, create a branch, and then complete the project from that branch.

## Key Terms

**Repository**

A project stored in GitHub. It contains your files, folders, and version history.

**Template repository**

A starter repository you can use to create your own copy of the project.

**Clone**

Downloading a GitHub repository to your computer so you can work on it locally.

**Branch**

A separate line of development inside a repository. You will do your work on a branch instead of directly on `main`.

**Commit**

A saved checkpoint of your changes.

**Push**

Sending your local commits from your computer to GitHub.

**Pull Request (PR)**

A request to merge changes from one branch into another. You will create a pull request from `development` into `main` when you are finished.

---

# 1. Create Your Repository from the Template

1. Open the assignment repository in GitHub.
2. Near the top of the page, click **Use this template**.
3. Click **Create a new repository**.
4. Choose your GitHub account as the owner.

For **Repository name**, use:

```text
lastname-cpw102-freelance-quote-builder
```

If you are working with more than one person, include each group member's last name:

```text
lastname-lastname-cpw102-freelance-quote-builder
```

Example:

```text
smith-jones-cpw102-freelance-quote-builder
```

5. Set the repository visibility to **Public**.
6. Click **Create repository**.

You should now be viewing your own copy of the project.

---

# 2. Add Group Members

If you are working alone, skip this section.

If you are working with a group:

1. Open your repository on GitHub.
2. Click the **Settings** tab.
3. In the left sidebar, click **Collaborators**.
4. Click **Add people**.
5. Search for your group member's GitHub username.
6. Send the invitation.

Each group member should accept the invitation before beginning work.

---

# 3. Clone the Repository with GitHub Desktop

You need a copy of the repository on your computer before you can edit it.

1. Open your repository on GitHub.
2. Click the green **Code** button.
3. Click **Open with GitHub Desktop**.
4. GitHub Desktop should open.
5. Choose where you want the project saved on your computer.
6. Click **Clone**.

You now have a local copy of the repository.

---

# 4. Create a Branch

Create a branch **before editing any project files**.

In GitHub Desktop:

1. Look near the top of the window for **Current branch**.
2. Click **Current branch**.
3. Click **New branch**.
4. Name the branch:

```text
development
```

5. Click **Create branch**.
6. If GitHub Desktop asks whether you want to publish the branch, click **Publish branch**.

Your current branch should now be `development`.

Do not complete the assignment directly on `main`.

---

# 5. Open the Project in Visual Studio Code

In GitHub Desktop:

1. Make sure **Current branch** shows `development`.
2. Click **Repository** in the menu bar.
3. Click **Open in Visual Studio Code**.

Visual Studio Code should open the project folder.

You are now ready to begin the assignment.

---

# 6. Start with `01_initialization`

In Visual Studio Code:

1. Find the **Explorer** panel on the left side.
2. Expand `01_initialization`.
3. Open [the problem statement](01_initialization/01_problem_statement.md).
4. Read it carefully before completing any other documents.

The problem statement describes the situation you are being asked to solve. Your job is to use that information to determine what the program needs to do.

Do not begin writing Python code yet.

## Complete the Phases

1. **Initialization:** Read the problem statement.
2. **Planning:** Complete [Product Requirements](02_planning/01_product_requirements.md) and [Engineering Design](02_planning/02_engineering_design.md), including your pseudocode.
3. **Execution:** Implement your design in `03_execution/freelance_quote_builder.py`. The starter file is intentionally empty.
4. **Testing:** Complete [Test Cases](04_testing/01_testing_cases.md). Calculate expected results before running your program.
5. **Shipping:** Follow [Submission Instructions](05_shipping/01_submission_instructions.md) and submit your pull request URL in Canvas.

## Learning Goals

Functions and variables. Practice input, numeric conversion, arithmetic, formatted output, `.strip()`, `.title()`, multiple parameters, return values, local scope, and a `main()` function that organizes the interaction. Use pseudocode and readable code to explain your approach.

See the problem statement for the input assumptions and limits of this lab.
