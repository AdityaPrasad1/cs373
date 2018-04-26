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
    --include "RangeT.py"                  \
    --include "Comprehensions.py"          \
    --include "Map.py"                     \
    --include "MapT.py"                    \
    --include "Iterables.py"               \
    --include "Functions.py"               \
    --include "FunctionKeywords.py"        \
    --include "FunctionDefaults.py"        \
    --include "FunctionUnpacking.py"       \
    --include "FunctionTuple.py"           \
    --include "FunctionDict.py"            \
    --include "Select.py"                  \
    --include "SelectT.py"                 \
    --include "Project.py"                 \
    --include "ProjectT.py"                \
    --include "RegExps.py"                 \
    --include "CrossJoin.py"               \
    --include "CrossJoinT.py"              \
    --include "ThetaJoin.py"               \
    --include "ThetaJoinT.py"              \
    --include "NaturalJoin.py"             \
    --include "NaturalJoinT.py"            \
    --include "Decorators.py"              \
    --include "SingletonPattern.py"        \
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
    --include "Operators.js"               \
    --include "Factorial.js"               \
    --include "FactorialT.js"              \
    --include "Reduce.js"                  \
    --include "ReduceT.js"                 \
    --include "Iteration.js"               \
    --include "RangeIterator.js"           \
    --include "RangeIteratorT.js"          \
    --include "Yield.js"                   \
    --include "Range.js"                   \
    --include "RangeT.js"                  \
    --include "Map.js"                     \
    --include "MapT.js"                    \
    --include "Functions.js"               \
    --include "FunctionDefaults.js"        \
    --include "FunctionUnpacking.js"       \
    --exclude "*"                          \
    ../../examples/javascript/ examples
	@rsync -r -t -u -v --delete            \
    --include "ShowDatabases.sql"          \
    --include "ShowDatabases.out"          \
    --include "ShowEngines.sql"            \
    --include "ShowEngines.out"            \
    --include "CreateDatabase.sql"         \
    --include "CreateDatabase.out"         \
    --include "CreateTables.sql"           \
    --include "CreateTables.out"           \
    --include "Insert.sql"                 \
    --include "Insert.out"                 \
    --include "Select.sql"                 \
    --include "Select.out"                 \
    --include "SelectT.sql"                \
    --include "SelectT.out"                \
    --include "Like.sql"                   \
    --include "Like.out"                   \
    --include "LikeT.sql"                  \
    --include "LikeT.out"                  \
    --include "Join.sql"                   \
    --include "Join.out"                   \
    --include "JoinT.sql"                  \
    --include "JoinT.out"                  \
    --include "Joins.sql"                  \
    --include "Joins.out"                  \
    --exclude "*"                          \
    ../../examples/sql/ examples
	@rsync -r -t -u -v --delete            \
    --include "StrategyPattern1.java"      \
    --include "StrategyPattern2.java"      \
    --include "StrategyPattern3.java"      \
    --include "StrategyPattern4.java"      \
    --include "StrategyPattern5.java"      \
    --include "StrategyPattern6.java"      \
    --include "MethodOverriding2.java"     \
    --include "DynamicBinding.java"        \
    --include "StrategyPattern7.java"      \
    --include "Reflection.java"            \
    --include "StrategyPattern8.java"      \
    --exclude "*"                          \
    ../../examples/java/ examples
	@rsync -r -t -u -v --delete            \
    --include "SAC.uml"                    \
    --include "SAC.png"                    \
    --include "StrategyPattern1.uml"       \
    --include "StrategyPattern1.png"       \
    --include "StrategyPattern2.uml"       \
    --include "StrategyPattern2.png"       \
    --include "StrategyPattern3.uml"       \
    --include "StrategyPattern3.png"       \
    --include "StrategyPattern4.uml"       \
    --include "StrategyPattern4.png"       \
    --include "StrategyPattern5.uml"       \
    --include "StrategyPattern5.png"       \
    --include "StrategyPattern6.uml"       \
    --include "StrategyPattern6.png"       \
    --include "StrategyPattern7.uml"       \
    --include "StrategyPattern7.png"       \
    --include "StrategyPattern8.uml"       \
    --include "StrategyPattern8.png"       \
    --exclude "*"                          \
    ../../examples/uml/ examples
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
