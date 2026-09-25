# Evaluation report

Answer concisely in your own words. Refer to concrete evidence from the project
and its tools.

## 1. Initial assessment

What was incomplete, incorrectly configured, or failing when you first examined
the repository? Explain how you discovered each item.

I used quality analysis tools to identify the issues.
Pytest flagged three failed tests in metrics.py: the click-through rate returned 0.05 instead of 5.0, the campaign tag count was incorrect (returning 2 instead of 3), and the call to normalize_campaign_name(None) caused an error.
I also discovered that mypy was missing from the development dependencies, preventing me from using it initially; the .gitignore file was also missing.

## 2. Toolchain evidence

What did the quality chain tools contribute to
your investigation? Give relevant examples and distinguish the kinds of problems they can detect. 

Pytest allowed me to detect issues with function behavior, as some tests were failing.
Ruff checked the code's formatting and style. After formatting the code, the command `ruff format --check .` confirmed that all eight files were already correctly formatted, and `ruff check .` passed successfully.
Mypy checked the types in the Python code; execution completed without reporting any issues.

## 3. Corrections

Describe the implementation and configuration corrections you made. For each
important correction, connect the original problem, the evidence, and the
resulting behavior.

For `click_through_rate`, I modified the calculation so the result is a percentage—meaning the expected output was 5.0 rather than 0.05—so I multiplied by 100. For `count_campaign_tags`, I removed the subtraction of 1 so the function now returns the actual count; for `normalize_campaign_name`, I added handling for cases where `None` is passed, ensuring an empty string is returned instead of raising an error.
I also added `mypy` as a development dependency. Following these fixes, `pytest`, `Ruff`, and `mypy` reported no issues.

## 4. Reproducibility and local configuration

Explain how the completed repository lets another developer reconstruct,
configure, run, and verify the project safely.
The project uses uv; dependencies are defined in pyproject.toml and recorded in uv.lock. Another developer can use uv sync to recreate the environment.
The application uses CAMPAIGN_ACCESS_TOKEN from a local .env file. The .env file is included in .gitignore, so the local token is not committed to Git.
The README explains how to install dependencies, configure the .env file, run the application, and perform quality checks.

## 5. Git workflow

Explain how your branches and commits divide the work into reviewable changes.
Mention how the completed work was integrated.

I used commits to separate the changes. One commit contains fixes related to metrics and development quality tools. Another commit adds a rule to ignore the local environment configuration.
Before the final submission, all completed work is merged into the main branch.

## 6. Limits of verification

Why does a completely passing quality toolchain provide useful evidence but not
proof that the program contains no defects?

Passing all quality checks is useful, but it does not guarantee the absence of bugs in the program.
Pytest verifies only the cases included in the tests; Ruff checks formatting and code quality rules, while mypy checks types; however, none of them can detect every possible logical or runtime issue. Problems can still occur in scenarios not covered by the tests.

## 7. Bonus question

Document the investigation trail for the bonus question:

1. How did you decide which project tool was responsible for this type of
   policy?
2. What documentation or repository evidence did you consult?
3. Which rule or rule family did you identify, and what behavior does it check?
4. What configuration did you change, and how did you verify that every existing
   rule remained enabled?
5. What new diagnostic appeared after the configuration change?


