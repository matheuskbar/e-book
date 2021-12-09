from django.shortcuts import render
from ebooklib import epub


def index(request):
    book = epub.EpubBook()

    # set metadata
    book.set_identifier('id123456')
    book.set_title('Um teste de e-book python')
    book.set_language('pt-br')

    book.add_author('Matheus Kontarski')
    book.add_author('Danko Bananko', file_as='Gospodin Danko Bananko', role='ill', uid='coauthor')

    # create chapter
    c1 = epub.EpubHtml(title='Capítulo 1', file_name='cap1.xhtml', lang='hr')
    c1.content = u'<h1>Capítulo 1</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis facilisis sapien, et scelerisque ante. Mauris ut semper justo. Sed sed tortor et nunc tempor tempus. Vestibulum quis massa sit amet justo dictum varius nec sed purus. Integer in sagittis turpis. Morbi pulvinar tempor sapien luctus pulvinar. Pellentesque et sapien nec metus tincidunt efficitur in vel nulla. Suspendisse pellentesque a nulla vitae pretium. Duis neque augue, feugiat at odio ut, finibus porta arcu. Cras tempus nisi eget lectus elementum posuere quis mollis ex.</p>'

    c2 = epub.EpubHtml(title='Capítulo 2', file_name='cap2.xhtml', lang='hr')
    c2.content = u'<h1>Capítulo 2</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis facilisis sapien, et scelerisque ante. Mauris ut semper justo. Sed sed tortor et nunc tempor tempus. Vestibulum quis massa sit amet justo dictum varius nec sed purus. Integer in sagittis turpis. Morbi pulvinar tempor sapien luctus pulvinar. Pellentesque et sapien nec metus tincidunt efficitur in vel nulla. Suspendisse pellentesque a nulla vitae pretium. Duis neque augue, feugiat at odio ut, finibus porta arcu. Cras tempus nisi eget lectus elementum posuere quis mollis ex.</p>'

    c3 = epub.EpubHtml(title='Capítulo 3', file_name='cap3.xhtml', lang='hr')
    c3.content = u'<h1>Capítulo 3</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis facilisis sapien, et scelerisque ante. Mauris ut semper justo. Sed sed tortor et nunc tempor tempus. Vestibulum quis massa sit amet justo dictum varius nec sed purus. Integer in sagittis turpis. Morbi pulvinar tempor sapien luctus pulvinar. Pellentesque et sapien nec metus tincidunt efficitur in vel nulla. Suspendisse pellentesque a nulla vitae pretium. Duis neque augue, feugiat at odio ut, finibus porta arcu. Cras tempus nisi eget lectus elementum posuere quis mollis ex.</p>'

    # add chapter
    book.add_item(c1)
    book.add_item(c2)
    book.add_item(c3)

    # define Table Of Contents
    book.toc = (c1, c2, c3)


    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define CSS style
    style = 'body {background-color: red;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)

    # basic spine
    book.spine = ['nav', c1, c2, c3]

    # write to the file
    epub.write_epub('test.epub', book, {})
    return render(request, 'index.html')