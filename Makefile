.PHONY: build ## Build
build:
	docker build -t flask-tutorial:latest .

.PHONY: run ## Run
run:
	docker run -d -p 5000:5000 --name flasker flask-tutorial

.PHONY: start ## Start
start:
	docker start flasker

.PHONY: pylint ## Test
pylint:
	docker exec flasker pylint app.py

.PHONY: stop ## Stop
stop:
	docker stop flasker