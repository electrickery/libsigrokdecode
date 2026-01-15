##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2014 Daniel Elstner <daniel.kitta@gmail.com>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

'''
The TMS7000 is an 8-bit microprocessor family. This decoder is for the MC-mode.

In addition to the 8-bit data bus, this decoder requires the input signals
/EN (enable), RD/WR (read not write) and AS (address strobe) to do its work. An explicit
clock signal is not required. However, the TMS7000 CPU clock may be used as
sampling clock, if applicable.

Notes on the TMS7000 opcode format and descriptions of both documented and
"undocumented" opcodes are available here:

Details:

'''

from .pd import Decoder
