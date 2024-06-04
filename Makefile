all: console

clean:
		rm -rf test_dot.dot
tests:
		python3.12  test.py

s21_graph: console

console:
		python3.12 console.py
