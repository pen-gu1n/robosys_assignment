# robosys_assignment

## determinantコマンド
![test](https://github.com/pen-gu1n/robosys_assignment/actions/workflows/det_test.yml/badge.svg)
- 入力された正方行列の行列式を計算するコマンド
- 2×2 3×3　対応

## インストール方法
以下のコマンドを実行し、リポジトリをクローンしてディレクトリに移動してください。

- `$ git clone https://github.com/pen-gu1n/robosys_assignment.git`
- `$ cd robosys_assignment`

## 使い方
- 左上のaから順番に入力

$$
\begin{pmatrix}
a & b \\
c & d \end{pmatrix}
$$

- 引数は数字＋スペース
- `$ ./determinant a b c d`


## 必要なソフトウェア
- Python
  - テスト済みバージョン: 3.10〜3.14

## テスト環境
- Ubuntu 24.04 LTS

## ライセンス
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- © 2026 Kenjiro Era
