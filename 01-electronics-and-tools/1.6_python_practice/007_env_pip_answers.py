# Problem 7 — virtual environments and pip
#
# This file is the worked answer for 007_env_pip.py. That file is a lab:
# you run commands in a terminal. The lines below are the usual answers
# on Ubuntu. Your version numbers will differ.
#
# 1. Create a virtual environment
#    python3 -m venv env_lab
#
# 2. Activate it
#    source env_lab/bin/activate
#    The prompt usually starts with (env_lab). The environment variable
#    VIRTUAL_ENV points at the env_lab folder.
#
# 3. Confirm the environment is isolated
#    python -m pip list
#    deactivate
#    python -m pip list
#    The global list is often longer. Two packages that may appear only
#    outside env_lab depend on what is already installed on the machine.
#
# 4. Install a package
#    source env_lab/bin/activate
#    python -m pip install requests
#
# 5. Verify installation
#    python -m pip show requests
#    VERSION is whatever pip printed, for example 2.32.3
#
# 6. Use the installed package
#    # 007_test_import.py
#    import requests
#    print(requests.__version__)
#
# 7. Deactivate and verify
#    deactivate
#    python 007_test_import.py
#    This usually fails with ModuleNotFoundError: No module named 'requests'
#    because that Python no longer has the environment's packages.
#
# 8. Debris cleanup
#    rm -rf env_lab
#    The environment folder is a machine-local install. Recreate it from
#    a requirements list instead of storing it in Git.
