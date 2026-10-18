#!/bin/sh
cd "$(dirname "$0")/tests" && python3 -m unittest discover -p 'test_*.py' "$@"
