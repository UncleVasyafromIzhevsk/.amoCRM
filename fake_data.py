from yattag import Doc
from faker import Faker


fake = Faker('ru')
doc, tag, text = Doc().tagtext()

          
doc.asis('<!DOCTYPE html>')
doc.asis('<html lang="ru">')
with tag('head'):
    doc.asis('<meta charset="UTF-8">')
    doc.asis('<link href="static/styles.css" rel="stylesheet">')
    with tag('title'):
        text(' ')
with tag('body'):
    # Верхний блок
    with tag('h1'):
        text('Название')
    with tag('table', klass='table'):
        with tag('tr'):
            for r in ['id', 'имя', 'email', 'время создания']:
                with tag('th'):
                    text(r)
        for i in range(100):
            users = [
                fake.random_int(),
                fake.name(),
                fake.email(),
                fake.date() + ":" + fake.time(),
            ]
            print(users)
            with tag('tr'):
                for user in users:
                    with tag('td'):
                        text(user)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    data = doc.getvalue()
    f.write(data)
