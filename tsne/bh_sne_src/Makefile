#CXX = clang++
#CFLAGS = -march=haswell -ffast-math -O3 -Rpass=loop-vectorize -Rpass-missed=loop-vectorize  -Rpass-analysis=loop-vectorize
#CFLAGS = -march=haswell -ffast-math -O3

CXX = g++
CFLAGS = -ffast-math -O3

all: bh_tsne bh_tsne_3d

bh_tsne: tsne.o sptree.o
	$(CXX) $(CFLAGS) tsne.o sptree.o -o bh_tsne

bh_tsne_3d: tsne_3d.o sptree.o
	$(CXX) $(CFLAGS) tsne_3d.o sptree.o -o bh_tsne_3d

sptree.o: sptree.cpp sptree.h
	$(CXX) $(CFLAGS) -c sptree.cpp

tsne.o: tsne.cpp tsne.h sptree.h vptree.h
	$(CXX) $(CFLAGS) -c tsne.cpp

tsne_3d.o: tsne.cpp tsne.h sptree.h vptree.h
	$(CXX) $(CFLAGS) -DTSNE3D -c tsne.cpp

clean:
	rm -Rf *.o bh_tsne bh_tsne_3d
