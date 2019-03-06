#!/usr/bin/env python
import sys
sys.path.append('../')
from logparser import SLCT

input_dir  = '../logs/SVTFS/' # The input directory of log file
output_dir = 'SLCT_SVTFS_CFGDB_TASK_result/' # The output directory of parsing results
log_good = 'svtfs_cfgdb_task_good.log'
log_bad = 'svtfs_cfgdb_task_bad.log'
log_good_new = 'svtfs_cfgdb_task_another_good.log'
#log_file1k   = 'svtfs_1k-8k_task.log' # The input log file name
#log_file8k   = 'svtfs_8k-16k_task.log' # The input log file name
log_format = '<Date>T<Time>Z <Level> .* \[:\] <Component> <Content>' # SVTFS hive controller log format
support    = 2  # The minimum support threshold
regex      = []  # Regular expression list for optional preprocessing (default: [])

parser = SLCT.LogParser(log_format=log_format, indir=input_dir, outdir=output_dir,
                        support=support, rex=regex)

#parser.parse(log_file1k)
#parser.parse(log_file8k)
parser.parse(log_good)
parser.parse(log_bad)
parser.parse(log_good_new)
