install: 
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

local:
	.venv/bin/python main.py
