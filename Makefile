build:
	python setup.py build_ext

install:
	python setup.py build_ext
	python setup.py install -e .

wheel:
	python setup.py bdist_wheel

clean:
	rm -rf *.pyc *.so build/ bh_sne.cpp
	rm -rf tsne/*.pyc tsne/*.so tsne/bh_sne.cpp
	rm -rf build dist
