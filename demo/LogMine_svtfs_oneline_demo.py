#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import LogMine

input_dir  = '../logs/SVTFS/' # The input directory of log file
output_dir = 'LogMine_SVTFS_OL_result/' # The output directory of parsing results
log_file   = 'svtfs_one_line.log' # The input log file name
log_format = '<Date>T<Time>Z <Level> .* \[:\] <Component> <Content>' # SVTFS hive controller log format
levels     = 5 # The levels of hierarchy of patterns
max_dist   = 0.001 # The maximum distance between any log message in a cluster and the cluster representative
k          = 1 # The message distance weight (default: 1)
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = LogMine.LogParser(input_dir, output_dir, log_format, rex=regex, levels=levels, max_dist=max_dist, k=k)
parser.parse(log_file)
