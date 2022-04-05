install: # устанавливает poetry
	poetry install

brain-games: # запуск brain-games
	poetry run brain-games

build: # собирает пакет
	poetry build

publish: # отладка публикации
	poetry publish -r foo  --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games        
