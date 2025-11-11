.PHONY: help migrate upgrade downgrade seed db-reset

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

migrate: ## Generate a new migration (usage: make migrate msg="migration message")
	@cd apps/backend && alembic revision --autogenerate -m "$(msg)"

upgrade: ## Apply all pending migrations
	@cd apps/backend && alembic upgrade head

downgrade: ## Rollback one migration
	@cd apps/backend && alembic downgrade -1

seed: ## Seed the database with sample data
	@cd apps/backend && python -m scripts.seed

db-reset: ## Reset database (downgrade all, upgrade all, seed)
	@cd apps/backend && alembic downgrade base && alembic upgrade head && python -m scripts.seed
