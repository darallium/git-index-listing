Japanese version is following below the english.
# parse_git_index.py

This Python script parses a `.git/index` file and prints its contents in a human-readable format. It provides similar functionality to the `git ls-files --stage` command.

## Usage

```bash
python parse_git_index.py <path/to/.git/index>
```

Replace `<path/to/.git/index>` with the path to the `.git/index` file you want to parse. This is typically `.git/index` in the root directory of your Git repository.

## Output

The script prints each file entry in the following format:

```
<file mode> <SHA-1 hash> <stage number>\t<file name>
```

* **file mode:** The file's mode (octal representation).
* **SHA-1 hash:** The SHA-1 hash of the file's contents.
* **stage number:** The stage number (always 0).
* **file name:** The file's name.

Header information is also displayed:

```
==== header ===
signature = DIRC
version = <version number>
entries = <number of entries>
```

## Dependencies

This script requires Python 3.4 or later. It has no external library dependencies.  It uses the standard library `struct`, `os`, and `sys` modules.


## Example

```bash
python parse_git_index.py .git/index
```

## Limitations

* This script does not support all features of the `.git/index` file.  In particular, it does not handle extended index formats or resolve-undo information.
* Performance issues may arise when processing extremely large `.git/index` files.

## License

This script is distributed under the MIT License. See the LICENSE file for details.


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

## 依存関係

このスクリプトは、Python 3.4以降で動作します。外部ライブラリへの依存関係はありません。標準ライブラリの`struct`、`os`、`sys`モジュールを使用しています。

## 例

```bash
python parse_git_index.py .git/index
```

## 制限事項

* このスクリプトは、`.git/index`ファイルのすべての機能をサポートしているわけではありません。特に、拡張版のインデックスフォーマットやresolve-undo情報などは処理しません。
* 非常に大きな`.git/index`ファイルを処理する場合、パフォーマンスの問題が発生する可能性があります.

