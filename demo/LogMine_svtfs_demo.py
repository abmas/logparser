#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import LogMine

input_dir  = '../logs/SVTFS/' # The input directory of log file
output_dir = 'LogMine_SVTFS_result/' # The output directory of parsing results
log_file   = 'svtfs_pp3.log' # The input log file name
log_format = '<Date> <Time> <Level> <Component> <Content>' # SVTFS log format
levels     = 2 # The levels of hierarchy of patterns
max_dist   = 0.001 # The maximum distance between any log message in a cluster and the cluster representative
k          = 1 # The message distance weight (default: 1)
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = LogMine.LogParser(input_dir, output_dir, log_format, rex=regex, levels=levels, max_dist=max_dist, k=k)
parser.parse(log_file)
