

shell:
	@uv run python

run:
	@uv run --env-file .env python codechat.py 