#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import SLCT

input_dir  = '../logs/SVTFS/' # The input directory of log file
output_dir = 'SLCT_SVTFS_CFGDB_TASK_result/' # The output directory of parsing results
log_file   = 'svtfs_cfgdb_taskmgrsvc.log' # The input log file name
log_format = '<Date>T<Time>Z <Level> .* \[:\] <Component> <Content>' # SVTFS hive controller log format
support    = 10  # The minimum support threshold
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = SLCT.LogParser(log_format=log_format, indir=input_dir, outdir=output_dir,
                        support=support, rex=regex)

parser.parse(log_file)
