import json

# https://github.com/0x192/universal-android-debloater/blob/main/resources/assets/uad_lists.json
with open('uad_lists.json', 'r') as f:
    uad = json.load(f)

with open('onphone.txt', 'r') as f:
    my_packages = f.read().splitlines()

with_doc = list()
for package in uad:
    if package['id'] in my_packages:
        with_doc.append((package['id'], package['description'], package['removal']))

print('''
 <table border=1>
  <tr>
    <th>id</th>
    <th>desc</th>
    <th>removal</th>
  </tr>
''')

for p in sorted(with_doc, key=lambda x: x[2]):
    color = ''
    if p[2] == 'Unsafe':
        color = 'magenta'
    elif p[2] == 'Recommended':
        color = 'lightgreen'

    print(f"""
  <tr bgcolor='{color}'>
    <td>{p[0]}</td>
    <td>{p[1]}</td>
    <td>{p[2]}</td>
  </tr>
    """)

print('</table>')

