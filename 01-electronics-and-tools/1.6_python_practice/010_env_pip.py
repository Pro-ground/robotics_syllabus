# Problem 10 — virtual environments and pip
# Write a single file, e.g. 010_env_pip.py. Only the stdlib — no external packages.
#
#
# What you will need
#
# Packages: none inside this worksheet. You will install requests only as
# a practice install, then delete the environment.
#
# Ideas to have in place before you start:
# - A virtual environment is a folder with its own Python and its own
#   installed packages, so a project does not depend on whatever happens
#   to be on the rest of the machine.
# - pip is the tool that installs packages into the environment you have
#   activated.
# - You run Python tools as python -m pip ... so you use the pip that
#   belongs to that same Python.
#
# Commands and names to look up (this is a lab, not a guessing game):
# - python -m venv
# - the activate script inside the environment folder (bin/activate on
#   Linux and macOS, Scripts\\activate on Windows)
# - deactivate
# - python -m pip list, python -m pip install, python -m pip show
# - importlib.metadata.version or the package's own version attribute,
#   if you print a version from a script
#
# You do not need: to write the graded sensor functions from the other
# files, or to commit the environment folder.
#
# This exercise is about learning to work with Python environments and
# installing packages, not about writing a complex program.
#
# Spec
#
# This is a **lab exercise**. You need to complete the following steps in your
# terminal, not write a program. Write your observations and answers below.
#
# Steps
#
# 1. **Create a virtual environment.**
#    Create a new virtual environment in a folder called `env_lab` inside
#    this exercise's directory.
#
#    What command do you run? Write it below:
#
#    YOUR_COMMAND_HERE:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# 2. **Activate it.**
#    Activate the environment and confirm it is active. On Linux/Mac you
#    would type `source env_lab/bin/activate`. On Windows you would type
#    `env_lab\Scripts\activate`.
#
#    What prompt or environment variable shows that the environment is active?
#    Record it below:
#
#    OBSERVATION:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# 3. **Confirm the environment is isolated.**
#    Run `python -m pip list` and note which packages are available.
#    Then deactivate the environment and run the same command. Note the
#    difference.
#
#    List two packages that appear in the global environment but NOT in
#    the virtual environment (or vice versa, depending on what you find):
#
#    1. ─────────────────────────────────────────────────────────────────────────
#    2. ─────────────────────────────────────────────────────────────────────────
#
#
#
# 4. **Install a package.**
#    Activate the environment and install the `requests` package (a popular
#    HTTP library, included here only as an example).
#
#    What command do you run? Write it below:
#
#    YOUR_COMMAND_HERE:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# 5. **Verify installation.**
#    Run `python -m pip show requests` and record the version number you get:
#
#    VERSION:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# 6. **Use the installed package.**
#    Write a short Python script (in a new file called `010_test_import.py`)
#    that imports requests and prints the library's version string.
#    Run it from inside the virtual environment.
#
#    Paste your script below:
#
#    YOUR_SCRIPT_HERE:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# 7. **Deactivate and verify.**
#    Deactivate the environment and run the same script again.
#    What happens? Record it below:
#
#    OBSERVATION:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# 8. **Debris cleanup.**
#    Delete the `env_lab` folder. Why is it normal to delete it rather
#    than committing it to Git?
#
#    ANSWER:
#    ────────────────────────────────────────────────────────────────────────────
#
#
#
# How you know you are done
#
# You have filled in every blank above with your own observations, and you
# can explain to someone else why virtual environments exist and what pip
# does. If you cannot explain it in your own words, go back and redo the
# steps.
#
# You do not need assertions here. The evidence of completion is the filled
#-in answers and the ability to recreate the steps from memory.
#
# If you want a minimal check you can run:
#
#    python 010_env_pip.py
#
# and see the text you wrote. This file is a lab worksheet, not a program
# with auto-grading. The learning is in the doing, not in passing assertions.
#
# print("lab complete — check your answers above")
#
