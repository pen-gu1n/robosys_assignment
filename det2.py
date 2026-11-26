# SPDX-FileCopyrightText: 2026 kenjiro era
# SPDX-License-Identifier: BSD-3-Clause

def det_2x2(a, b, c, d)
	x = 0.0
	x = (float(a) * float(d)) - (float(b) * float(c))
	return x
