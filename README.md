# Exam4 – Rank 05 Python (rank05.42exam.net)

Solutions in `solutions/`, tests in `tests/` (run `./run_tests.sh`, stdlib `unittest` only).

Points où le sujet est ambigu (choix faits) :
- `py_prism_detector` : les codes D2/D2- suivent les **vecteurs** `(dx,dy)` du sujet (x = colonne, y = ligne vers le bas), pas la prose ("up-right"/"down-left"), qui les contredit. Résultats triés par ligne, puis colonne, puis ordre des directions du sujet.
- `py_room_scheduler` : **version examen** — retourne `{"rooms_needed": n, "room_assignments": {0: salle0, 1: salle1, ...}}` (une clé par salle, même pour 1 seule salle ; `{}` si vide). `py_room_scheduler_site_format.py` = version du site (`total_rooms`/`schedule`). Algorithme commun : tri par heure de début (stable), chaque réunion va dans la première salle libre (`fin <= début`, réunions qui se touchent OK).
- `py_word_ladder` : `end` doit être dans `sentence` (sinon 0, cf. 2e exemple).
- `py_room_scheduler_chunks.py` : PLAN B pour l'exo 4, à n'utiliser que si la moulinette refuse `py_room_scheduler.py`. Reproduit à la lettre les exemples de l'énoncé de l'exam (blocs consécutifs de `ceil(n/k)` réunions triées), mais ce n'est pas un planning sans chevauchement.
