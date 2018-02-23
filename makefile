.DEFAULT_GOAL := all

all:
	cd examples; make all
	@echo
	cd projects/collatz; make all

clean:
	cd examples; make clean
	@echo
	cd projects/collatz; make clean

config:
	git config -l

docker:
	docker run -it -v $(PWD):/usr/cs373 -w /usr/cs373 gpdowning/python

init:
	touch  README
	git init
	git add README
	git commit -m 'first commit'
	git remote add origin git@github.com:gpdowning/cs373.git
	git push -u origin master

pull:
	make clean
	@echo
	git pull
	git status

push:
	make clean
	@echo
	git add .gitignore
	git add .travis.yml
	git add examples
	git add makefile
	git add notes
	git add projects/collatz
	git commit -m "another commit"
	git push
	git status

run:
	cd examples; make run
	@echo
	cd projects/collatz; make run

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

sync:
	@rsync -r -t -u -v --delete            \
    --include "Docker.txt"                 \
    --include "Dockerfile"                 \
    --include "Hello.py"                   \
    --include "Assertions.py"              \
    --include "UnitTests1.py"              \
    --include "UnitTests2.py"              \
    --include "UnitTests3.py"              \
    --include "Coverage1.py"               \
    --include "Coverage2.py"               \
    --include "Coverage3.py"               \
    --include "IsPrime.py"                 \
    --include "IsPrimeT.py"                \
    --include "Exceptions.py"              \
    --include "StrCmp.py"                  \
    --include "StrCmpT.py"                 \
    --include "Types.py"                   \
    --include "Operators.py"               \
    --include "Factorial.py"               \
    --include "FactorialT.py"              \
    --include "Reduce.py"                  \
    --include "ReduceT.py"                 \
    --include "Iteration.py"               \
    --include "RangeIterator.py"           \
    --include "RangeIteratorT.py"          \
    --include "Yield.py"                   \
    --include "Range.py"                   \
    --include "Comprehensions.py"          \
    --include "Map.py"                     \
    --exclude "*"                          \
    ../../examples/python/ examples
	@rsync -r -t -u -v --delete            \
    --include "Hello.js"                   \
    --include "Assertions.js"              \
    --include "UnitTests1.js"              \
    --include "UnitTests2.js"              \
    --include "UnitTests3.js"              \
    --include "Coverage1.js"               \
    --include "Coverage2.js"               \
    --include "Coverage3.js"               \
    --include "Exceptions.js"              \
    --include "StrCmp.js"                  \
    --include "StrCmpT.js"                 \
    --include "Types.js"                   \
    --include "Factorial.js"               \
    --include "FactorialT.js"              \
    --include "Reduce.js"                  \
    --include "ReduceT.js"                 \
    --include "Iteration.js"               \
    --include "RangeIterator.js"           \
    --include "RangeIteratorT.js"          \
    --include "Yield.js"                   \
    --include "Range.js"                   \
    --exclude "*"                          \
    ../../examples/javascript/ examples
	@rsync -r -t -u -v --delete            \
    --include "Collatz.py"                 \
    --include "RunCollatz.py"              \
    --include "RunCollatz.in"              \
    --include "RunCollatz.out"             \
    --include "TestCollatz.py"             \
    --exclude "*"                          \
    ../../projects/python/collatz/ projects/collatz

travis:
	cd examples; make travis
	@echo
	cd projects/collatz; make travis
