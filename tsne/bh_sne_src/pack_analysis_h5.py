#!/usr/bin/env python

import sys
from struct import pack

import cellranger.analysis as cr_analysis
import cellranger.constants as cr_constants

def pack_data(in_h5, out_dat):
    ana = cr_analysis.SingleGenomeAnalysis.load_h5(in_h5)
    samples, _ = ana.get_pca()
    (sample_count, sample_dim) = samples.shape
    perplexity = min(cr_constants.TSNE_DEFAULT_PERPLEXITY, max(1, -1 + float((sample_count-1))/3))
    theta = 0.5 # TODO tweak for speed?
    no_dims = 2
    max_iter = 1000
    with open(out_dat, 'wb') as data_file:
        # Write the bh_tsne header
        data_file.write(pack('iiddii', sample_count, sample_dim, theta, perplexity, no_dims, max_iter))
        # Then write the data
        for sample in samples:
            data_file.write(pack('{}d'.format(len(sample)), *sample))

def main():
    in_h5 = sys.argv[1]
    out_dat = sys.argv[2]
    pack_data(in_h5, out_dat)

if __name__ == '__main__':
    main()
