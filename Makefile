.PHONY: install_dev
install_dev:
	python -m pip install -r requirement.txt
	pip install pre-commit

.PHONY: start_docker_compose
start_docker_compose:
	cd tests && docker compose up

.PHONY: tests
tests:
	pytest --cov --cov-report term-missign