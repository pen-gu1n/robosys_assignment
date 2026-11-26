# SPDX-FileCopyrightText: 2026 kenjiro era
# SPDX-License-Identifier: BSD-3-Clause

def det_3x3(nums):
	a, b, c, d, e, f, g, h, i = nums
	x = (float(a) * float(e) * float(i)) + (float(b) * float(f) * float(g)) + (float(c) * float(d) * float(h))
	y = (float(c) * float(e) * float(g)) + (float(b) * float(d) * float(i)) + (float(a) * float(f) * float(h))
	return x - y
