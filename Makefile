build:
	python setup.py build_ext --inplace

install:
	python setup.py build_ext --inplace
	python setup.py install

sdist:
	python setup.py sdist

clean:
	rm -rf *.pyc *.so build/ bh_sne.cpp
	rm -rf tsne/*.pyc tsne/*.so tsne/build/ tsne/bh_sne.cpp
