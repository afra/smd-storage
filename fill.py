#!/usr/bin/env python3

import sys,os,argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('template', type=argparse.FileType('r'), help='The svg template file')
parser.add_argument('-s', '--section', type=str, nargs='+', help='The section of the value list to process')
args = parser.parse_args()

sections = args.section or []
values = []
read = False
for line in sys.stdin:
	if read:
		if line[0] is '#': #next section
			read = False
		else:
			values.append(line.strip())
	if not read:
		if line[1:-1] in sections: #strip '#' and newline character
			read = True

values = values + list(map(str, range(len(values), 133)))

print('Read {} values'.format(len(values)), file=sys.stderr)

content = ''
for line in args.template:
	content += line

for value in values:
	line1, _, line2 = value.partition('\\')
	content = content.replace('LBL1', line1, 1)
	content = content.replace('LBL2', line2, 1) #args.section, 1)

print(content)
