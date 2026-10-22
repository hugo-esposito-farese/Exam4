# Exam5 – Rank 06 Python (rank06.42exam.net)

8 solutions rank06 (un fichier par sujet, nom exact du site) + `bridge_finder.py` (sujet donné à part, hors site). Tests : `./run_tests.sh` (stdlib `unittest` uniquement).

- `tests/test_00_official_examples.py` rejoue mot pour mot les exemples du site (`tests/rank06_examples.json`).
- Chaque exo a aussi des tests aléatoires contre une implémentation naïve, plus les cas limites et les gros volumes.

Point ambigu :
- `cache_keeper` : l'exemple 2 du site (`put(1); put(2); put(3); get(2)` → `-1`) contredit la LRU de l'énoncé (c'est la clé 1 qui est évincée, donc `get(2)` vaut `2`). La solution suit l'énoncé (vraie LRU) ; il manque sans doute un `get(1)` dans cet exemple.
