export:
	python src/query.py | sed -e s/.*[0-9]m// > docs/query.org
