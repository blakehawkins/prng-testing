#! /usr/bin/python
import sys, os, re
import numpy as np

STATE_STATIC_SEEDS = 0
STATE_SAMPLES_A    = 1
STATE_SAMPLES_B    = 2

static_seed_a = 0
static_seed_b = 0
public_seed   = 0
uniq_seeds    = [0, 0]
samples       = [[], []]
cross_correl  = []

state = STATE_STATIC_SEEDS

def correlate(samples_a, samples_b):
    samples_a = (samples_a - np.mean(samples_a) / (np.std(samples_a) * len(samples_a)))
    samples_b = (samples_b - np.mean(samples_b) / np.std(samples_b))
    return np.correlate(samples_a, samples_b, 'full')

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

            # cross-correlate
            cross_correl = correlate(map(int, samples[0]), map(int, samples[1]))
            print cross_correl

            state = STATE_SAMPLES_A