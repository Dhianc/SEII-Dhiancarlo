import csv

html_output = ''
names = []

with open('/home/dhian/SEII-Dhiancarlo/Semana02/prog16/patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    #pula cabeçalho e primeira linha
    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f"{line[0]} {line[1]}")
        
for name in names:
    print(name)


html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)

with open('/home/dhian/SEII-Dhiancarlo/Semana02/prog16/patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    for item in csv_data:
        print(item)
        
html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

with open('/home/dhian/SEII-Dhiancarlo/Semana02/prog16/patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    #pula cabeçalho
    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")
        
html_output += f'<p>There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)