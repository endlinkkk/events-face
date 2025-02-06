DC = docker compose
STORAGE = docker-compose.yaml
ENV = --env-file .env

.PHONY: infra app lint

lint:
	uv run ruff format .
	uv run ruff check --fix .

app:
	uv run uvicorn --factory app.application.main:create_app --timeout-graceful-shutdown 2 --host 0.0.0.0 --port 8001 --reload

infra:
	${DC} -f ${STORAGE} ${ENV} up --build -d

