

shell:
	@uv run python

run:
	@uv run --env-file .env python hello.py 