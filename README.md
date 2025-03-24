# parse_git_index.py

このPythonスクリプトは、`.git/index`ファイルを解析し、その内容を人間が読める形式で出力します。これは、`git ls-files --stage`コマンドと同様の機能を提供しますが、indexファイル単体で動作させることができます。

## 使い方

```bash
python parse_git_index.py <path/to/.git/index>
```

`<path/to/.git/index>` は、解析したい`.git/index`ファイルへのパスに置き換えてください。通常、これはGitリポジトリのルートディレクトリにある`.git/index`です。

## 出力

スクリプトは、以下の形式で各ファイルのエントリを出力します。

```
<file mode> <SHA-1 hash> <stage number>\t<file name>
```

* **file mode:** ファイルのモード（8進数表記）。
* **SHA-1 hash:** ファイル内容のSHA-1ハッシュ値。
* **stage number:** ステージ番号（常に0）。
* **file name:** ファイル名。

ヘッダー情報も表示されます。

```
==== header ===
signature = DIRC
version = <version number>
entries = <number of entries>
```


## エラー処理

スクリプトには以下のエラー処理が含まれています。

* `.git/index`ファイルが存在しない場合は、エラーメッセージを出力して終了します。
* `.git/index`ファイルが不正な形式である場合（例：signatureが"DIRC"でない、データが破損しているなど）、エラーメッセージを出力して終了します。

## 依存関係

このスクリプトは、Python 3.4以降で動作します。外部ライブラリへの依存関係はありません。標準ライブラリの`struct`、`os`、`sys`モジュールを使用しています。

## 例

```bash
python parse_git_index.py .git/index
```

## 制限事項

* このスクリプトは、`.git/index`ファイルのすべての機能をサポートしているわけではありません。特に、拡張版のインデックスフォーマットやresolve-undo情報などは処理しません。
* 非常に大きな`.git/index`ファイルを処理する場合、パフォーマンスの問題が発生する可能性があります.

