export:
	python query.py | sed -e s/.*[0-9]m// > test.org
