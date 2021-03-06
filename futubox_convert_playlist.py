#!/usr/bin/env python
#    futubox to XMLTV - copyright 2013 Francesco Santini <francesco.santini@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re
import sys

futuboxPrefix = 'futubox'

pat = r'#EXTINF:0,([0-9]+),'
replacement = r'#EXTINF:-1 tvg-id="' + futuboxPrefix + '\\1",'

inFileName = sys.argv[1]
outFileName = sys.argv[2]

inFile = open(inFileName, 'rb')
outFile = open(outFileName, 'wb')

for line in inFile:
  outFile.write(re.sub(pat, replacement, line))
  
inFile.close()
outFile.close()
