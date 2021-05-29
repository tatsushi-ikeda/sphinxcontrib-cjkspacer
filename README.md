[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# sphinxcontrib-cjkspacer
A Sphinx extension, which inserts spacer elements between the CJK characters and the other characters.

Some of the word processors, e.g., Microsoft® Word and TeX (at least in the case of pTeX), adjust the distances between the words CJK characters and other characters automatically.
Unfortunately, however, HTML with CSS does not have this function as of CSS3 (See the `text-spacing` property discussed in some old versions of W3C Working Draft, e.g., [1 September 2011](https://www.w3.org/TR/2011/WD-css3-text-20110901/), [19 January 2012](https://www.w3.org/TR/2012/WD-css3-text-20120119/)).
This Sphinx extension provides an alternative function to adjust such distances.

## Install

```
pip install git+https://github.com/tatsushi-ikeda/sphinxcontrib-linkattr.git@master
```

## Usage

Add `sphinxcontrib.cjkspacer` in the `extensions` list in `conf.py`.

```Python
extensions += ['sphinxcontrib.cjkspacer']
```

## Configuration

## License

MIT License

