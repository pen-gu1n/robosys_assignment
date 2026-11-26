# SPDX-FileCopyrightText: 2026 kenjiro era
# SPDX-License-Identifier: BSD-3-Clause

def det3x3(a,b,c,d,e,f,g,h,i):
	x = 0.0
	y = 0.0
	z = 0.0

	x = (float(a) * float(e) * float(i)) + (float(b) * float(f) * float(g)) + (float(c) * float(d) * float(h))
	y = (float(c) * float(e) * float(g)) + (float(b) * float(d) * float(h)) + (float(a) * float(f) * float(i))
	z = x - y
	return z
