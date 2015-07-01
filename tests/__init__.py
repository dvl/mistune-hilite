# -*- coding: utf-8 -*-

import unittest

import mistune
import mistune_hilite

python = '''
```python
def test():
    pass
```
'''

javascript = '''
```javascript
function test() {
    console.log('Hi!');
}
```
'''


class TestMistuneHilite(unittest.TestCase):

    def setUp(self):
        pass

    def test_language_used(self):
        renderer = mistune_hilite.HiliteRenderer()
        md = mistune.Markdown(renderer=renderer)

        md(python)
        self.assertEqual(md.token['lang'], 'python')

        md(javascript)
        self.assertTrue(md.token['lang'], 'javascript')

    def test_linenos_option(self):
        renderer = mistune_hilite.HiliteRenderer(linenos=True)
        md = mistune.Markdown(renderer=renderer)
        html = md(python)

        self.assertTrue('class="linenos"' in html)

    def test_cssclass_option(self):
        renderer = mistune_hilite.HiliteRenderer(cssclass='foobar')
        md = mistune.Markdown(renderer=renderer)
        html = md(python)

        self.assertTrue('class="foobar"' in html)

    def test_noclass_option(self):
        renderer = mistune_hilite.HiliteRenderer(noclasses=True)
        md = mistune.Markdown(renderer=renderer)
        html = md(python)

        self.assertTrue('<span style="' in html)


if __name__ == '__main__':
    unittest.main()
