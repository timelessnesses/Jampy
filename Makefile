run:
	python BotJam.py
beauty:
	isort .
	black .
	flake8 . 
	mypy .
	pylint .
	pydocstyle .