#!/bin/bash
# SPDX-FileCopyrightText: 2026 Kenjiro Era
# SPDX-License-Identifier: BSD-3-Clause

ng(){
	echo ${1}行目のテスト失敗
        res=1                          # 失敗の記録
}

res=0

# correct
output_2x2=$(./determinant 1 2 3 4)
[ "${output_2x2}" = "-2.0" ] || ng "$LINENO"

output_3x3=$(./determinant 1 2 3 4 5 6 7 8 9)
[ "${output_3x3}" = "0.0" ] || ng "$LINENO"


# error
./determinant 1 2 2			#数字の個数が足りていないとき
[ "$?" = 1 ] || ng "$LINENO"

./determinant			        #数字がないとき
[ "$?" = 1 ] || ng "$LINENO"


[ "${res}" = 0 ] && echo OK


exit $res
