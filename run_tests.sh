#!/bin/sh
cd "$(dirname "$0")/tests" && python3 official_examples.py | grep -E "BAD|examples:" ; python3 -m unittest discover -v -p 'test_*.py' 2>&1 | tail -${1:-6}
