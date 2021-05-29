import re
from itertools import zip_longest, chain
from docutils import nodes

class cjkspacer(nodes.General, nodes.Element):
    pass

class CJKBoundary(object):
    CJK_RANGE_LIST = [r'\u2E80-\u9FFF', r'\uF900-\uFAFF', r'\uFF00-\uFF60\uFFE0-\uFFE6', r'\U00020000-\U0003FFFF']
    BEFORE_EXCEPTION_LIST = ['\s\n']
    AFTER_EXCEPTION_LIST  = ['\s\n']
    
    def __init__(self):
        cjk_pattern = ''.join(CJKBoundary.CJK_RANGE_LIST)
        b_except_pattern = ''.join(CJKBoundary.BEFORE_EXCEPTION_LIST + CJKBoundary.CJK_RANGE_LIST)
        a_except_pattern = ''.join(CJKBoundary.AFTER_EXCEPTION_LIST  + CJKBoundary.CJK_RANGE_LIST)
        self._border_pattern_pairs = (
            (re.compile('(?:[^{b_except}])$'.format(b_except=b_except_pattern)),
             re.compile('^(?:[{cjk}])'.format(cjk=cjk_pattern))),
            (re.compile('(?:[{cjk}])$'.format(cjk=cjk_pattern)),
             re.compile('^(?:[^{a_except}])'.format(a_except=a_except_pattern)))
        )
        self._pattern = re.compile('(?<![{b_except}])(?=[{cjk}])|(?<=[{cjk}])(?![{a_except}])'.format(
            cjk=cjk_pattern, b_except=b_except_pattern, a_except=a_except_pattern)
        )

    def split(self, txt):
        return self._pattern.split(txt)        

    def check_boundary(self, leading_txt, following_txt):
        return any((pat[0].search(leading_txt) and pat[1].match(following_txt))
                   for pat in self._border_pattern_pairs)

class CJKSpacerVisitor(nodes.GenericNodeVisitor):
    EXCLUDED_ELEMENTS = (
        nodes.FixedTextElement, nodes.Inline,
        nodes.Invisible, nodes.Bibliographic
    )

    def __init__(self, document, spacer):
        super(CJKSpacerVisitor, self).__init__(document)
        self._spacer = spacer
        self._cjk_boundary = CJKBoundary()
        self._spacer = cjkspacer()

    def default_visit(self, node):
        if not isinstance(node, nodes.TextElement):
            return
        if isinstance(node, CJKSpacerVisitor.EXCLUDED_ELEMENTS):
            return
        self._insert_cjkspacer(node)
        raise nodes.SkipChildren

    def unknown_visit(self, node):
        self.default_visit(node)

    def _insert_cjkspacer(self, node):
        target_inline_elems = (nodes.emphasis, nodes.strong)
        num_children = len(node.children)
        new_children = []
        for idx, child in enumerate(node.children):
            if not isinstance(child, nodes.Text):
                if isinstance(child, target_inline_elems):
                    self._insert_cjkspacer(child)
                new_children.append(child)
                continue
            new_txt = child.astext()
            new_child = list(chain.from_iterable(zip_longest((nodes.Text(sep)
                                                              for sep in self._cjk_boundary.split(new_txt) if sep),
                                                             [], fillvalue=self._spacer)))[:-1]
            if idx - 1 >= 0:
                prev_txt = node.children[idx - 1].astext()
                if prev_txt and self._cjk_boundary.check_boundary(prev_txt, new_txt):
                    new_child = [self._spacer] + new_child
            if idx + 1 < num_children:
                next_txt = node.children[idx + 1].astext()
                if next_txt and self._cjk_boundary.check_boundary(new_txt, next_txt):
                    new_child = new_child + [self._spacer]
            new_children += new_child
        node.children = new_children

def get_bool_value(config, builder_name):
    if not isinstance(config, (list, tuple)):
        return config
    return builder_name in config

def insert_cjkspacer(app, doctree, _docname):
    spacer = cjkspacer()
    visitor = CJKSpacerVisitor(doctree, spacer)
    doctree.walk(visitor)

def visit_cjkspacer_html(self, node):
    self.body.append('<span class="cjkspacer"></span>')

def depart_cjkspacer_html(self, node):
    pass

def setup(app):
    app.connect("doctree-resolved", insert_cjkspacer)
    app.add_node(cjkspacer,
                 html=(visit_cjkspacer_html, depart_cjkspacer_html))
    
    return {'parallel_read_safe': True, 'parallel_write_safe': True}

