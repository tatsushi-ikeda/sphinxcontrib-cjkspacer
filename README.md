[![CI](https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/actions/workflows/main.yml/badge.svg)](https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sphinxcontrib-cjkspacer
A [Sphinx](https://www.sphinx-doc.org/en/master/) extension, which inserts spacer elements between the Chinese Japanese Korean (CJK) characters and the other characters.

Some of the word processors, e.g., Microsoft® Word and TeX (at least in the case of pTeX), adjust the distances (spaces) between the CJK characters and the others automatically (c.f. [Requirements for Japanese Text Layout#spacing between characters](https://www.w3.org/TR/jlreq/#spacing_between_characters)).
Unfortunately, however, HTML with CSS does not have this function as of CSS3 (See the `text-spacing` property discussed in some old versions of W3C® Working Draft, e.g., [1 September 2011](https://www.w3.org/TR/2011/WD-css3-text-20110901/) and [19 January 2012](https://www.w3.org/TR/2012/WD-css3-text-20120119/)).
This Sphinx extension provides an alternative function to adjust such distances.

### Description for Japanese
> 異なる種類の文字種間の空き量(スペース)を調整する機能を持たないフォーマットに、日本語を含むCJK文字とその他の文字種の間での空き量調整機能を与える[Sphinx](https://www.sphinx-doc.org/ja/master/)拡張です。
> この拡張と[sphinxcontrib-trimblank](https://github.com/amedama41/sphinxcontrib-trimblank)などを併用することで、HTML出力において、数字／英語と日本語の間への手動でのスペース挿入・除去を行うよりも自然な仕上がりを実現することを目指しています([日本語によるデモ](https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/))。
> 
> ただし、現状では[組版処理の要件(日本語版)](https://www.w3.org/TR/2009/NOTE-jlreq-20090604/ja/)に記載されているような高度な調整は行っておらず、2種の判断基準による1種類の空き量しか導入していません。
> CSS3で延期された `text-spacing` が今後CSS4などで導入されればこの拡張は不要になることでしょう。

### Note

This extension is inspired by [sphinxcontrib-trimblank](https://github.com/amedama41/sphinxcontrib-trimblank).
The combination betweeen `sphinxcontrib-trimblank` and `sphinxcontrib-cjkspacer` should work well for the `html` builders:
`sphinxcontrib-trimblank` removes redundant spaces caused by the limitation of the reStructuredText syntax, and then `sphinxcontrib-cjkspacer` adjusts distances among characters (See [Japanese demo](https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/)).

## Install

```
pip install sphinxcontrib-cjkspacer
```

## Usage

Add `sphinxcontrib.cjkspacer` in the `extensions` list in `conf.py`.

```Python
extensions += ['sphinxcontrib.cjkspacer']
```

## Example
[tests/](https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/tree/master/tests): ([Japanese demo](https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/))

- In `conf.py`

    ```Python
    extensions += ['sphinxcontrib.trimblank', 'sphinxcontrib.cjkspacer']
    html_css_files = ['custom.css']
    ```
    
- In `_static/custom.css`

    ```CSS
    .cjkspacer:after {
        content: '\0020';
        font-size: 50%;
    }
    ```

## Configuration

- `cjkspacer_spacer`: (default: `{'html':'<span class="cjkspacer"></span>'}`)
  
    A dictionary which has `format`:`spacer_string` pairs.
    The value of `spacer_string` will be inserted between the CJK characters and the others when the format of the builder is `format`.

    By using the default value, you can use `.cjkspacer` class in your custom css as follows:
        
    The width of this type of space should be 1/4 of the width of the CJK characters, at least in the cases of Japanese language (shibu aki "四分アキ", see `cl-19 ideographic characters`:`cl-27 Western characters` and `cl-27`:`cl-19` in [Table 1 Spacing between characters](https://www.w3.org/TR/jlreq/tables/table_ja2.pdf)). 
    Hence, with the ordinary (half-width) space character `U+0020`, 
    ```CSS
    .cjkspacer:after {
        content: '\0020';
        font-size: 50%;
    }
    ```
    may be the most preferable solution.
    The use of the full-width space `U+3000`,
    ```CSS
    .cjkspacer:after {
        content: '\3000';
        font-size: 25%;
    }
    ```
    may be closer to the definition we need.
    In most cases, however, we cannot specify such a small `font-size` value.
    Of course you can use other space characters, like the thin space character `U+2009`.
    If you need, you can specify the width numerically as the following example:
    ```CSS
    .cjkspacer {
        padding-right: 0.15em;
    }
    ```
    Note that the width of `U+0020` depends on the font you use. For example,
    
    | font-family         | width of `U+0020` (eye measurement) |
    |:-------------------:|:-----------------------------------:|
    | Lucida Sans Unicode | 0.31em                              |
    | Verdana             | 0.34em                              |
    | sans-serif          | 0.33em                              |
    | Segoe UI            | 0.28em                              |
    | Helvetica           | 0.28em                              |
    | Arial               | 0.33em                              |

    Finally, if you cannot edit css files, the following example may be a possible solution (in `conf.py`)
    ```Python
    cjkspacer_spacer_str = {'html': '&thinsp;'}
    ```
    This however causes selectable spaces in the text.

- `cjkspacer_cjk_characters`

- `cjkspacer_before_exceptions`

- `cjkspacer_after_exceptions`
    
    These three elements decide the boundaries between the CJK characters and the other characters.
    
    If regular expressions
    
    -  `f'(?<![{cjkspacer_before_exceptions}{cjkspacer_cjk_characters}])(?=[{cjkspacer_cjk_characters}'])`

    or 

    -  `f'(?<=[{cjkspacer_cjk_characters}])(?![{cjkspacer_after_exceptions}{cjkspacer_cjk_characters}])'`
    
    match parts of texts, they are regarded as the boundaries.
    
### Default values of `cjkspacer_cjk_characters`, `cjkspacer_before_exceptions`, and `cjkspacer_after_exceptions`

In the default configuration, we employ relatively simple rules.

If a CJK character is *preceded* by a **space** (` \t\f\v`), **newline** (`\n\r`), or **opening parenthesis** (`({[`), we do not insert a spacer *before* the CJK character.

If a CJK character is *followed* by a **space** (` \t\f\v`), **newline** (`\n\r`), **closing parenthesis** (`)}]`), or **punctuation** (`,.:;!?`), we do not insert a spacer *after* the CJK character.

Here, we do not use `r'\s'` instead of `' \t\f\v'`, because `r'\s'` also matches *Ideographicl Space* (`U+3000`, 　).

The following Unicode blocks are adopted as the CJK characters in the default value of `cjkspacer_cjk_characters`:

- CJK characters

    | from      | to        | Example | Unicode block name                               |
    |:---------:|:---------:|:-------:|:------------------------------------------------:|
    | `U+2E80`  | `U+2EFF`  | ⺀      | CJK Radicals Supplement                          |
    | `U+2F00`  | `U+2FDF`  | ⼀      | Kangxi Radicals                                  |
    | `U+2FF0`  | `U+2FFF`  | ⿰      | Ideographic Description Characters               |
    | `U+3000`  | `U+303F`  | 々      | CJK Symbols and Punctuation                      |
    | `U+3040`  | `U+309F`  | あ      | Hiragana                                         |
    | `U+30A0`  | `U+30FF`  | ア      | Katakana                                         |
    | `U+3100`  | `U+312F`  | ㄅ      | Bopomofo                                         |
    | `U+3130`  | `U+318F`  | ㄱ      | Hangul Compatibility Jamo                        |
    | `U+3190`  | `U+319F`  | ㆐      | Kanbun                                           |
    | `U+31A0`  | `U+31BF`  | ㆠ      | Bopomofo Extended                                |
    | `U+31C0`  | `U+31EF`  | ㇀      | CJK Strokes                                      |
    | `U+31F0`  | `U+31FF`  | ㇰ      | Katakana Phonetic Extensions                     |
    | `U+3200`  | `U+32FF`  | ㉑      | Enclosed CJK Letters and Months                  |
    | `U+3300`  | `U+33FF`  | ㎏      | CJK Compatibility                                |
    | `U+3400`  | `U+4DBF`  | 㐀      | CJK Unified Ideographs Extension A               |
    | `U+4DC0`  | `U+4DFF`  | ䷀       | Yijing Hexagram Symbols                          |
    | `U+4E00`  | `U+9FFF`  | 一      | CJK Unified Ideographs                           |
    | `U+F900`  | `U+FAFF`  | 豈      | CJK Compatibility Ideographs                     |
    | `U+FF00`  | `U+FF60`  | ！      | Halfwidth and Fullwidth Forms (Full width Forms) |
    | `U+FFE0`  | `U+FFE6`  | ￠      | Halfwidth and Fullwidth Forms (Full width Forms) |
    | `U+20000` | `U+2A6DF` | 𠀀      | CJK Unified Ideographs Extension B               |
    | `U+2A700` | `U+2B73F` | 𪜀      | CJK Unified Ideographs Extension C               |
    | `U+2B740` | `U+2B81F` | 𫝀      | CJK Unified Ideographs Extension D               |
    | `U+2B820` | `U+2CEAF` | 𫠠      | CJK Unified Ideographs Extension E               |
    | `U+2CEB0` | `U+2EBEF` | 𬺰      | CJK Unified Ideographs Extension F               |
    | `U+2F800` | `U+2FA1F` | 丽      | CJK Compatibility Ideographs Supplement          |
    | `U+30000` | `U+3134F` | 𰀀      | CJK Unified Ideographs Extension G               |

The following block is also included into `cjkspacer_cjk_characters` for consistency with *Enclosed CJK Letters and Months*.

- Treated as CJK characters

    | from      | to        | Example | Unicode block name                               |
    |:---------:|:---------:|:-------:|:------------------------------------------------:|
    | `U+2460`  | `U+24FF`  | ①      | Enclosed Alphanumerics                           |

The following characters are eliminated from `cjkspacer_cjk_characters` since they are spaces, punctuation, and parentheses. 
Instead, they are included into `cjkspacer_before_exceptions` and `cjkspacer_after_exceptions`.

- Exceptions among *CJK symbols and punctuation* (`U+3000-U+303F`)

    | Unicode  | Character | Name                               |
    |:--------:|:---------:|:----------------------------------:|
    | `U+3000` | 　        | Ideographicl Space                 |
    | `U+3001` | 、        | Ideographic Comma                  |
    | `U+3002` | 。        | Ideographic Full Stop              |
    | `U+3008` | 〈        | Left Angle Bracket                 |
    | `U+3009` | 〉        | Right Angle Bracket                |
    | `U+300A` | 《        | Left Double Angle Bracket          |
    | `U+300B` | 》        | Right Double Angle Bracket         |
    | `U+300C` | 「        | Left Corner Bracket                |
    | `U+300D` | 」        | Right Corner Bracket               |
    | `U+300E` | 『        | Left White Corner Bracket          |
    | `U+300F` | 』        | Right White Corner Bracket         |
    | `U+3010` | 【        | Left Black Lenticular Bracket      |
    | `U+3011` | 】        | Right Black Lenticular Bracket     |
    | `U+3014` | 〔        | Left Tortoise Shell Bracket        |
    | `U+3015` | 〕        | Right Tortoise Shell Bracket       |
    | `U+3016` | 〖        | Left White Lenticular Bracket      |
    | `U+3017` | 〗        | Right White Lenticular Bracket     |
    | `U+3018` | 〘        | Left White Turtoise Shell Bracket  |
    | `U+3019` | 〙        | Right White Turtoise Shell Bracket |
    | `U+301A` | 〚        | Left White Square Bracket          |
    | `U+301B` | 〛        | Right White Square Bracket         |

- Exceptions among *Katakana* (`U+30A0-U+30FF`)

    | Unicode  | Character | Name                |
    |:--------:|:---------:|:-------------------:|
    | `U+30FB` | ・        | Katakana Middle Dot |

- Exceptions among *Halfwidth and Fullwidth Forms* (`U+FF00-U+FF60`, `U+FFE0-U+FFE6`)

    | Unicode  | Character | Name                              |
    |:--------:|:---------:|:---------------------------------:|
    | `U+FF01` | ！        | Fullwidth Exclamation Mark        |
    | `U+FF02` | ＂        | Fullwidth Quotation Mark          |
    | `U+FF07` | ＇        | Fullwidth Apostrophe              |
    | `U+FF08` | （        | Fullwidth Left Parenthesis        |
    | `U+FF09` | ）        | Fullwidth RIght Parenthesis       |
    | `U+FF0C` | ，        | Fullwidth Comma                   |
    | `U+FF0E` | ．        | Fullwidth Full Stop               |
    | `U+FF0F` | ／        | Fullwidth Solidus                 |
    | `U+FF1A` | ：        | Fullwidth Colon                   |
    | `U+FF1B` | ；        | Fullwidth Semicolon               |
    | `U+FF1F` | ？        | Fullwidth Question Mark           |
    | `U+FF3B` | ［        | Fullwidth Left Square Bracket     |
    | `U+FF3C` | ＼        | Fullwidth Reverse Solidus         |
    | `U+FF3D` | ］        | Fullwidth Right Square Bracket    |
    | `U+FF5B` | ｛        | Fullwidth Left Curly Bracket      |
    | `U+FF5C` | ｜        | Fullwidth Vertical Line           |
    | `U+FF5D` | ｝        | Fullwidth Right Curly Bracket     |
    | `U+FF5F` | ｟        | Fullwidth Left White Parenthesis  |
    | `U+FF60` | ｠        | Fullwidth Right White Parenthesis |

Thus, we set the following as the default configuration.

```Python
cjkspacer_cjk_characters = (
    r"\u2460-\u24FF\u2E80-\u2FFF\u3003-\u3007\u3012\u3013\u301C-\u30FA\u30FC-\u9FFF"
    r"\uF900-\uFAFF\uFF00\uFF03-\uFF06\uFF0A\uFF0B\uFF0D\uFF10-\uFF19\uFF1C\uFF1D"
    r"\uFF1E\uFF20-\uFF3A\uFF3E-\uFF5A\uFF5E\uFFE0-\uFFE6\U00020000-\U0002A6DF"
    r"\U0002A700-\U0002EBEF\U0002F800-\U0002FA1F\U00030000-\U0003134F"
)
cjkspacer_before_exceptions = (
    " \t\f\v\n\r"
    r"({\["
    r"\u3000\u3001\u3002\u3008-\u3011\u3014-\u301B\u30FB\uFF01\uFF02\uFF07\uFF08"
    r"\uFF09\uFF0C\uFF0E\uFF0F\uFF1A\uFF1B\uFF1F\uFF3B\uFF3C\uFF3D\uFF5B\uFF5C"
    r"\uFF5D\uFF5F\uFF60"
)
cjkspacer_after_exceptions = (
    " \t\f\v\n\r"
    r")}\],.:;!?"
    r"\u3000\u3001\u3002\u3008-\u3011\u3014-\u301B\u30FB\uFF01\uFF02\uFF07\uFF08"
    r"\uFF09\uFF0C\uFF0E\uFF0F\uFF1A\uFF1B\uFF1F\uFF3B\uFF3C\uFF3D\uFF5B\uFF5C"
    r"\uFF5D\uFF5F\uFF60"
)
```

## License

MIT License

