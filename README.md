[![CI](https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/actions/workflows/main.yml/badge.svg)](https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/actions/workflows/main.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sphinxcontrib-cjkspacer
A Sphinx extension, which inserts spacer elements between the Chinese Japanese Korean (CJK) characters and the other characters.

Some of the word processors, e.g., Microsoft® Word and TeX (at least in the case of pTeX), adjust the distances between the CJK characters and the others automatically (c.f. [Requirements for Japanese Text Layout#spacing between characters](https://www.w3.org/TR/jlreq/#spacing_between_characters)).
Unfortunately, however, HTML with CSS does not have this function as of CSS3 (See the `text-spacing` property discussed in some old versions of W3C® Working Draft, e.g., [1 September 2011](https://www.w3.org/TR/2011/WD-css3-text-20110901/) and [19 January 2012](https://www.w3.org/TR/2012/WD-css3-text-20120119/)).
This Sphinx extension provides an alternative function to adjust such distances.

### Note

This extension is inspired by [sphinxcontrib-trimblank](https://github.com/amedama41/sphinxcontrib-trimblank).
The combination betweeen `sphinxcontrib-trimblank` and `sphinxcontrib-cjkspacer` should work well for the `html` builders:
`sphinxcontrib-trimblank` removes redundant spaces caused by the limitation of the reStructuredText syntax, and then `sphinxcontrib-cjkspacer` adjusts distances among characters (See [demo](https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/)).

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
[tests/](https://github.com/tatsushi-ikeda/sphinxcontrib-cjkspacer/tree/master/tests): ([demo](https://tatsushi-ikeda.github.io/sphinxcontrib-cjkspacer/))

- In `conf.py`

    ```Python
    extensions += ['sphinxcontrib.trimblank', 'sphinxcontrib.cjkspacer']
    html_css_files = ['custom.css']
    ```
    
- In `_static/custom.css`

    ```CSS
    .cjkspacer {
        padding-right: 0.13em;
    }
    ```

## Configuration

- `cjkspacer_spacer`: (default: `{'html':'<span class="cjkspacer"></span>'}`)
  
    A dictionary which has `format`:`spacer_string` pairs.
    The value of `spacer_string` will be inserted between the CJK characters and the others when the format of the builder is `format`.

    By using the default value, you can use `.cjkspacer` class in your custom css. 
    For example,
    ```css
    .cjkspacer {
        padding-right: 0.13em;
    }
    ```
    
    If the use of the thin space character is sufficient, this can be achieved by
    ```Python
    cjkspacer_spacer_str = {'html': '&thinsp;'}
    ```
    This however causes selectable spaces in the text.

- `cjkspacer_cjk_characters`

- `cjkspacer_before_exception`

- `cjkspacer_after_exception`
    
    These three elements decide the boundaries between the CJK characters and the other characters.
    
    If regular expressions
    
    -  `f'[^{cjkspacer_before_exception}{cjkspacer_cjk_characters}][{cjkspacer_cjk_characters}']`

    or 

    -  `f'[{cjkspacer_cjk_characters}'][^{cjkspacer_after_exception}{cjkspacer_cjk_characters}]`
    
    match parts of texts, they are regarded as the boundaries.
    
### Default values of `cjkspacer_cjk_characters`, `cjkspacer_before_exception`, and `cjkspacer_after_exception`

In the default configuration, we employ relatively simple rules.

If a CJK character is *preceded* by a **space** (`\s`), **newline** (`\n`), or **opening parenthesis** (`({\[`), we do not insert a spacer *before* the CJK character.

If a CJK character is *followed* by a **space** (`\s`), **newline** (`\n`), **closing parenthesis** (`[)}\]]`), or **punctuation** (`,.:;!?`), we do not insert a spacer *after* the CJK character.

The following Unicode blocks are adopted as the CJK characters in the default value of `cjkspacer_cjk_characters`:

- CJK characters

    | from         | to           | Example | Unicode block name                               |
    |:------------:|:------------:|:-------:|:------------------------------------------------:|
    | `\u2E80`     | `\u2EFF`     | ⺀      | CJK Radicals Supplement                          |
    | `\u2F00`     | `\u2FDF`     | ⼀      | Kangxi Radicals                                  |
    | `\u2FF0`     | `\u2FFF`     | ⿰      | Ideographic Description Characters               |
    | `\u3000`     | `\u303F`     | 々      | CJK Symbols and Punctuation                      |
    | `\u3040`     | `\u309F`     | あ      | Hiragana                                         |
    | `\u30A0`     | `\u30FF`     | ア      | Katakana                                         |
    | `\u3100`     | `\u312F`     | ㄅ      | Bopomofo                                         |
    | `\u3130`     | `\u318F`     | ㄱ      | Hangul Compatibility Jamo                        |
    | `\u3190`     | `\u319F`     | ㆐      | Kanbun                                           |
    | `\u31A0`     | `\u31BF`     | ㆠ      | Bopomofo Extended                                |
    | `\u31C0`     | `\u31EF`     | ㇀      | CJK Strokes                                      |
    | `\u31F0`     | `\u31FF`     | ㇰ      | Katakana Phonetic Extensions                     |
    | `\u3200`     | `\u32FF`     | ㉑      | Enclosed CJK Letters and Months                  |
    | `\u3300`     | `\u33FF`     | ㎏      | CJK Compatibility                                |
    | `\u3400`     | `\u4DBF`     | 㐀      | CJK Unified Ideographs Extension A               |
    | `\u4DC0`     | `\u4DFF`     | ䷀       | Yijing Hexagram Symbols                          |
    | `\u4E00`     | `\u9FFF`     | 一      | CJK Unified Ideographs                           |
    | `\uF900`     | `\uFAFF`     | 豈      | CJK Compatibility Ideographs                     |
    | `\uFF00`     | `\uFF60`     | ！      | Halfwidth and Fullwidth Forms (Full width Forms) |
    | `\uFFE0`     | `\uFFE6`     | ￠      | Halfwidth and Fullwidth Forms (Full width Forms) |
    | `\U00020000` | `\U0002A6DF` | 𠀀      | CJK Unified Ideographs Extension B               |
    | `\U0002A700` | `\U0002B73F` | 𪜀      | CJK Unified Ideographs Extension C               |
    | `\U0002B740` | `\U0002B81F` | 𫝀      | CJK Unified Ideographs Extension D               |
    | `\U0002B820` | `\U0002CEAF` | 𫠠      | CJK Unified Ideographs Extension E               |
    | `\U0002CEB0` | `\U0002EBEF` | 𬺰      | CJK Unified Ideographs Extension F               |
    | `\U0002F800` | `\U0002FA1F` | 丽      | CJK Compatibility Ideographs Supplement          |
    | `\U00030000` | `\U0003134F` | 𰀀      | CJK Unified Ideographs Extension G               |

The following block is also included into `cjkspacer_cjk_characters` for consistency with *Enclosed CJK Letters and Months*.

- Treated as CJK characters

    | from      | to        | Example | Unicode block name                               |
    |:---------:|:---------:|:-------:|:------------------------------------------------:|
    | `\u2460`  | `\u24FF`  | ①      | Enclosed Alphanumerics                           |

The following characters are eliminated from `cjkspacer_cjk_characters` since they are spaces, punctuation, and parentheses. 
Instead, they are included into `cjkspacer_before_exception` and `cjkspacer_after_exception`.

- Exceptions among *CJK symbols and punctuation* (`\u3000-\u303F`)

    | Unicode  | Character | Name                               |
    |:--------:|:---------:|:----------------------------------:|
    | `\u3000` | 　        | Ideographicl Space                 |
    | `\u3001` | 、        | Ideographic Comma                  |
    | `\u3002` | 。        | Ideographic Full Stop              |
    | `\u3008` | 〈        | Left Angle Bracket                 |
    | `\u3009` | 〉        | Right Angle Bracket                |
    | `\u300A` | 《        | Left Double Angle Bracket          |
    | `\u300B` | 》        | Right Double Angle Bracket         |
    | `\u300C` | 「        | Left Corner Bracket                |
    | `\u300D` | 」        | Right Corner Bracket               |
    | `\u300E` | 『        | Left White Corner Bracket          |
    | `\u300F` | 』        | Right White Corner Bracket         |
    | `\u3010` | 【        | Left Black Lenticular Bracket      |
    | `\u3011` | 】        | Right Black Lenticular Bracket     |
    | `\u3014` | 〔        | Left Tortoise Shell Bracket        |
    | `\u3015` | 〕        | Right Tortoise Shell Bracket       |
    | `\u3016` | 〖        | Left White Lenticular Bracket      |
    | `\u3017` | 〗        | Right White Lenticular Bracket     |
    | `\u3018` | 〘        | Left White Turtoise Shell Bracket  |
    | `\u3019` | 〙        | Right White Turtoise Shell Bracket |
    | `\u301A` | 〚        | Left White Square Bracket          |
    | `\u301B` | 〛        | Right White Square Bracket         |

- Exceptions among *Halfwidth and Fullwidth Forms* (`\uFF00-\uFF60`, `\uFFE0-\uFFE6`)

    | Unicode  | Character | Name                              |
    |:--------:|:---------:|:---------------------------------:|
    | `\uFF01` | ！        | Fullwidth Exclamation Mark        |
    | `\uFF02` | ＂        | Fullwidth Quotation Mark          |
    | `\uFF07` | ＇        | Fullwidth Apostrophe              |
    | `\uFF08` | （        | Fullwidth Left Parenthesis        |
    | `\uFF09` | ）        | Fullwidth RIght Parenthesis       |
    | `\uFF0C` | ，        | Fullwidth Comma                   |
    | `\uFF0E` | ．        | Fullwidth Full Stop               |
    | `\uFF0F` | ／        | Fullwidth Solidus                 |
    | `\uFF1A` | ：        | Fullwidth Colon                   |
    | `\uFF1B` | ；        | Fullwidth Semicolon               |
    | `\uFF1F` | ？        | Fullwidth Question Mark           |
    | `\uFF3B` | ［        | Fullwidth Left Square Bracket     |
    | `\uFF3C` | ＼        | Fullwidth Reverse Solidus         |
    | `\uFF3D` | ］        | Fullwidth Right Square Bracket    |
    | `\uFF5B` | ｛        | Fullwidth Left Curly Bracket      |
    | `\uFF5C` | ｜        | Fullwidth Vertical Line           |
    | `\uFF5D` | ｝        | Fullwidth Right Curly Bracket     |
    | `\uFF5F` | ｟        | Fullwidth Left White Parenthesis  |
    | `\uFF60` | ｠        | Fullwidth Right White Parenthesis |


Thus, we set the following as the default configuration.

```Python
cjkspacer_cjk_characters   = r'\u2460-\u24FF\u2E80-\u2FFF\u3003-\u3007\u3012\u3013\u301C-\u9FFF\uF900-\uFAFF\uFF00\uFF03-\uFF06\uFF0A\uFF0B\uFF0D\uFF10-\uFF19\uFF1C\uFF1D\uFF1E\uFF20-\uFF3A\uFF3E-\uFF5A\uFF5E\uFFE0-\uFFE6\U00020000-\U0002A6DF\U0002A700-\U0002EBEF\U0002F800-\U0002FA1F\U00030000-\U0003134F'
cjkspacer_before_exception = r'\s\n({\[\u3000\u3001\u3002\u3008-\u3011\u3014-\u301B\uFF01\uFF02\uFF07\uFF08\uFF09\uFF0C\uFF0E\uFF0F\uFF1A\uFF1B\uFF1F\uFF3B\uFF3C\uFF3D\uFF5B\uFF5C\uFF5D\uFF5F\uFF60'
cjkspacer_after_exception  = r'\s\n)}\],.:;!?\u3000\u3001\u3002\u3008-\u3011\u3014-\u301B\uFF01\uFF02\uFF07\uFF08\uFF09\uFF0C\uFF0E\uFF0F\uFF1A\uFF1B\uFF1F\uFF3B\uFF3C\uFF3D\uFF5B\uFF5C\uFF5D\uFF5F\uFF60'
```

## License

MIT License

