# SPDX-FileCopyrightText: 2026 kenjiro era
# SPDX-License-Identifier: BSD-3-Clause

def det_2x2(nums):
	a, b, c, d = nums 	#リストを１つずつ分けて渡す
	return (float(a) * float(d)) - (float(b) * float(c))
