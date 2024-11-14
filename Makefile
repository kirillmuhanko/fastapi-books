# Makefile for setting up a Python environment and running tasks

# Variables
VENV_DIR = venv
REQ_FILE = requirements.txt
PYTHON = $(VENV_DIR)/Scripts/python
PIP = $(VENV_DIR)/Scripts/pip
ALEMBIC = $(VENV_DIR)/Scripts/alembic

# Create Virtual Environment
create_venv:
	python -m venv $(VENV_DIR)

# Install Requirements
install_requirements: create_venv
	$(PIP) install -r $(REQ_FILE)

# Alembic Upgrade Head
alembic_upgrade: install_requirements
	$(PYTHON) -m alembic upgrade head

# Default task
setup: create_venv install_requirements alembic_upgrade
