def html_converter(tag, text):
    tags = ['h1', 'h2', 'h3', 'h4', 'h4', 'h5', 'h6', 'p', 'ol', 'ul', 'li']
    if tag not in tags:
        print('This is not a HTML Tag')
        return ''
    generated = f'<{tag}>{text}</{tag}>'
    return generated


# h1 = html_converter('h1', 'This is a H1 tag')
# print(h1)