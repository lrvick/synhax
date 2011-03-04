from django.db import models
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter

LEXER_DICT = tuple(sorted([(i[1][0],i[0]) for i in get_all_lexers()]))

class Snippet(models.Model):
    caption = models.CharField('Caption', max_length=255)
    author = models.CharField('Your Name/Handle', max_length=255, blank=True)
    email = models.EmailField('Your Email', max_length=255, blank=True)
    website = models.URLField('Your Website', max_length=255, blank=True)
    date = models.DateTimeField('Date Submitted',auto_now_add=True)
    code = models.TextField('Snippet')
    code_highlight = models.TextField('Highlighted Code', blank=True)
    lexer = models.CharField('Language', max_length=255, choices=LEXER_DICT, blank=True, null=True)
    url = models.SlugField('URL', max_length=255, blank=True)
    published models.BooleanField('Published', default=False)
    class Meta:
        ordering = ('-date',)
    def save(self, *args, **kwargs):
        self.code_highlight = highlight(self.code, get_lexer_by_name(lexer), HtmlFormatter())
