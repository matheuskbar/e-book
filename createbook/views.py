from ebooklib import epub
from django.shortcuts import render
from django.shortcuts import redirect, render
from .forms import FormEbook
from .models import Ebook

def index(request):
    ebook = Ebook.objects.all()
    return render(request, 'createbook/index.html', context={'ebook':ebook})


def create(request):
    if request.method == 'POST':
        form = FormEbook(request.POST)
        if form.is_valid():
            book = epub.EpubBook()

            # set metadata
            book.set_identifier('id123456')
            book.set_title(request.POST["titulo"])
            book.set_language('pt-br')

            book.add_author(request.POST["autor"])
            book.add_author(
                'Danko Bananko', file_as='Gospodin Danko Bananko', role='ill', uid='coauthor')

            # create chapter
            c1 = epub.EpubHtml(
                title=request.POST['capitulo'], file_name='cap1.xhtml', lang='hr')
            c1.content = u'<h1>Cap�tulo 1</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis facilisis sapien, et scelerisque ante. Mauris ut semper justo. Sed sed tortor et nunc tempor tempus. Vestibulum quis massa sit amet justo dictum varius nec sed purus. Integer in sagittis turpis. Morbi pulvinar tempor sapien luctus pulvinar. Pellentesque et sapien nec metus tincidunt efficitur in vel nulla. Suspendisse pellentesque a nulla vitae pretium. Duis neque augue, feugiat at odio ut, finibus porta arcu. Cras tempus nisi eget lectus elementum posuere quis mollis ex.</p>'

            c2 = epub.EpubHtml(
                title=request.POST['capitulo'], file_name='cap2.xhtml', lang='hr')
            c2.content = u'<h1>Cap�tulo 2</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis facilisis sapien, et scelerisque ante. Mauris ut semper justo. Sed sed tortor et nunc tempor tempus. Vestibulum quis massa sit amet justo dictum varius nec sed purus. Integer in sagittis turpis. Morbi pulvinar tempor sapien luctus pulvinar. Pellentesque et sapien nec metus tincidunt efficitur in vel nulla. Suspendisse pellentesque a nulla vitae pretium. Duis neque augue, feugiat at odio ut, finibus porta arcu. Cras tempus nisi eget lectus elementum posuere quis mollis ex.</p>'

            c3 = epub.EpubHtml(
                title=request.POST['capitulo'], file_name='cap3.xhtml', lang='hr')
            c3.content = u'<h1>Cap�tulo 3</h1><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus iaculis facilisis sapien, et scelerisque ante. Mauris ut semper justo. Sed sed tortor et nunc tempor tempus. Vestibulum quis massa sit amet justo dictum varius nec sed purus. Integer in sagittis turpis. Morbi pulvinar tempor sapien luctus pulvinar. Pellentesque et sapien nec metus tincidunt efficitur in vel nulla. Suspendisse pellentesque a nulla vitae pretium. Duis neque augue, feugiat at odio ut, finibus porta arcu. Cras tempus nisi eget lectus elementum posuere quis mollis ex.</p>'

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
            nav_css = epub.EpubItem(
                uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

            # add CSS file
            book.add_item(nav_css)

            # basic spine
            book.spine = ['nav', c1, c2, c3]

            # write to the file
            epub.write_epub('test.epub', book, {})

            print('='*30)
            print(request.POST.values())
            print()
            print()
            print()
            print()
            form.save()
            return redirect('index')
            
        return render(request, 'createbook/form.html', context={
            'form':form
        })
    form = FormEbook()
    return render(request, 'createbook/form.html', context={'form':form})


