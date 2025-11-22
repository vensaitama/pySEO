def html_generator(tag, text):
    """
    This is a HTML tags generator.
    """
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'li']
    if tag not in tags:
        print('Sorry, this is not HTML Tag')
        return ''
    generated_tags = f'<{tag}>{text}</{tag}>'
    return generated_tags

h1 = html_generator('hh1', 'This is a html H1 Tag')
print(h1)