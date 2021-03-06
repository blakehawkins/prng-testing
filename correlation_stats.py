#! /usr/bin/python
import sys, os, re
import numpy as np

STATE_STATIC_SEEDS = 0
STATE_SAMPLES_A    = 1
STATE_SAMPLES_B    = 2


HISTOGRAM_BINS = 20

graphs_generated = 0

static_seed_a = 0
static_seed_b = 0
public_seed   = 0
uniq_seeds    = [0, 0]
samples       = [[], []]
cross_correl  = []
correls       = []

state = STATE_STATIC_SEEDS



def correlate(samples_a, samples_b):
    c0 = np.correlate(samples_a, samples_b, 'full')
    return c0 / float(len(samples_a))

for line in sys.stdin:
    line = line.strip()
    
    # filter blank lines
    if len(line) == 0:
        state = STATE_STATIC_SEEDS
    else:
        if state is STATE_STATIC_SEEDS:
            static_seed_a, static_seed_b = re.search(r'[^\[]+\[([0-9]+), ([0-9]+)\]', line).groups()
            state = STATE_SAMPLES_A
        elif state is STATE_SAMPLES_A:
            public_seed, temp_samples = re.search(r'\[([0-9]+)\t\^\t[0-9]+\]\t(.*)', line).groups()
            samples[0] = temp_samples.split('\t')
            uniq_seeds[0] = int(public_seed)^int(static_seed_a)
            state = STATE_SAMPLES_B
        elif state is STATE_SAMPLES_B:
            public_seed, temp_samples = re.search(r'\[([0-9]+)\t\^\t[0-9]+\]\t(.*)', line).groups()
            samples[1] = temp_samples.split('\t')
            uniq_seeds[1] = int(public_seed)^int(static_seed_b)

            # get float versions of samples
            s0 = map(np.float64, samples[0])
            s1 = map(np.float64, samples[1])

            # scale samples down to [0.0, 2.0]
            s0 /= (0.5 * max(s0))
            s1 /= (0.5 * max(s1))

            # subtract 1 to make [-1.0, 1.0]
            s0 -= 1.0
            s1 -= 1.0

            xs = np.arange(0, len(s0), 1)
            xc = np.arange(0, 2 * len(s0) - 1, 1)
            xc -= (len(s0) / 2)

            # cross-correlate
            cross_correl = correlate(s0, s1)

            mx = max(abs(cross_correl))

            correls.append(mx)

            state = STATE_SAMPLES_A

print ("Maximum cross-correlation:\t" + str(max(correls)))
print ("Average peak cross-correlation:\t" + str(np.average(correls)))
print ("Histogram of peak cross-correlations:")

linsp = np.linspace(min(correls), max(correls), HISTOGRAM_BINS)

hist = np.histogram(correls, linsp)[0]

for z in xrange(len(hist)):
    print '\tbin[' + str(linsp[z]) + ']\t' + ('x' * int(hist[z]))