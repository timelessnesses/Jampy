run:
	python BotJam.py
beauty:
	isort .
	black .
	flake8 .  --exit-zero