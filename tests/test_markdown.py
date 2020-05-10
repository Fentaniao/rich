# coding=utf-8

from _markdown import MARKDOWN

from render import render

from rich.console import Console
from rich.markdown import Markdown


def test_markdown_render():
    markdown = Markdown(MARKDOWN)
    rendered_markdown = render(markdown)
    expected = "╔══════════════════════════════════════════════════════════════════════════════════════════════════╗\n║                                             \x1b[1mHeading\x1b[0m                                              ║\n╚══════════════════════════════════════════════════════════════════════════════════════════════════╝\n\n\n                                            \x1b[1;4mSub-heading\x1b[0m                                             \n\n\n                                              \x1b[1mHeading\x1b[0m                                               \n\n\n                                             \x1b[1;2mH4 Heading\x1b[0m                                             \n\n\n                                             \x1b[4mH5 Heading\x1b[0m                                             \n\n\n                                             \x1b[3mH6 Heading\x1b[0m                                             \n\nParagraphs are separated by a blank line.                                                           \n\nTwo spaces at the end of a line                                                                     \nproduces a line break.                                                                              \n\nText attributes \x1b[3mitalic\x1b[0m, \x1b[1mbold\x1b[0m, \x1b[38;5;15;40mmonospace\x1b[0m.                                                            \n\nHorizontal rule:                                                                                    \n\n\x1b[2m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\x1b[0m\nBullet list:                                                                                        \n\n\x1b[1;33m • \x1b[0mapples                                                                                           \n\x1b[1;33m • \x1b[0moranges                                                                                          \n\x1b[1;33m • \x1b[0mpears                                                                                            \n\nNumbered list:                                                                                      \n\n\x1b[1;33m 1 \x1b[0mlather                                                                                           \n\x1b[1;33m 2 \x1b[0mrinse                                                                                            \n\x1b[1;33m 3 \x1b[0mrepeat                                                                                           \n\nAn \x1b]8;id=3607223980;http://example.com\x1b\\\x1b[38;5;12mexample\x1b[0m\x1b]8;;\x1b\\.                                                                                         \n\n\x1b[35m▌ \x1b[0m\x1b[35mMarkdown uses email-style > characters for blockquoting.\x1b[0m\x1b[35m                                        \x1b[0m\n\x1b[35m▌ \x1b[0m\x1b[35mLorem ipsum\x1b[0m\x1b[35m                                                                                     \x1b[0m\n\n🌆 \x1b]8;id=1358623393;https://github.com/willmcgugan/rich/raw/master/imgs/progress.gif\x1b\\progress\x1b]8;;\x1b\\                                                                                         \n\n\x1b[38;2;248;248;242;48;2;39;40;34ma=1                                                                                                 \x1b[0m\n\n\x1b[38;2;249;38;114;48;2;39;40;34mimport\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m \x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34mthis\x1b[0m\x1b[38;2;248;248;242;48;2;39;40;34m                                                                                         \x1b[0m\n\n\x1b[38;2;248;248;242;48;2;39;40;34mfoobar                                                                                              \x1b[0m\n"
    assert rendered_markdown == expected


if __name__ == "__main__":
    markdown = Markdown(MARKDOWN)
    rendered = render(markdown)
    print(rendered)
    print(repr(rendered))
