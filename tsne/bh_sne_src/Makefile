#CXX = clang++
#CFLAGS = -march=haswell -ffast-math -O3 -Rpass=loop-vectorize -Rpass-missed=loop-vectorize  -Rpass-analysis=loop-vectorize
#CFLAGS = -march=haswell -ffast-math -O3

CXX = g++
CFLAGS = -ffast-math -O3

all: bh_tsne

bh_tsne: tsne.o sptree.o
	$(CXX) $(CFLAGS) tsne.o sptree.o -o bh_tsne

sptree.o: sptree.cpp sptree.h
	$(CXX) $(CFLAGS) -c sptree.cpp

tsne.o: tsne.cpp tsne.h sptree.h vptree.h
	$(CXX) $(CFLAGS) -c tsne.cpp

clean:
	rm -Rf *.o bh_tsne
