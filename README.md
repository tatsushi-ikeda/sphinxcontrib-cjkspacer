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
    The `spacer_string` will be inserted between the CJK characters and the others when the format of the builder is `format`.

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

- `cjkspacer_cjk_characters`: (default: `r'\u2E80-\u9FFF\uF900-\uFAFF\uFF00-\uFF60\uFFE0-\uFFE6\U00020000-\U0003FFFF'`)

- `cjkspacer_before_exception`: (default: `r'\s\n({\['`)

- `cjkspacer_after_exception`: (default: `r'\s\n)}\],.'`)
    
    These three elements decide the boundaries between the CJK characters and the other characters.
    
    If regular expressions
    
    -  `f'[^{cjkspacer_before_exception}{cjkspacer_cjk_characters}][{cjkspacer_cjk_characters}']`

    or 

    -  `f'[{cjkspacer_cjk_characters}'][^{cjkspacer_after_exception}{cjkspacer_cjk_characters}]`
    
    match parts of texts, they are regarded as the boundaries.

## License

MIT License

