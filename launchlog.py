
# coding: utf-8

from collections import defaultdict, namedtuple

Column = namedtuple('Column', ['name', 'start', 'end'])
def group_by(file, field='year', success=None):
    columns = []
    
    headers = file.readline()[:-1]
    sizes = file.readline()[:-1]

    last = -1
    for idx, c in enumerate(sizes[1:]):
        if c == "#":
            start = last + 1
            end = idx - 1
            columns.append(Column(headers[start:end].strip(), start, end))
            last = idx

    aggregate = defaultdict(lambda: 0)
    success_translation = {True: "S", False: "F"}
    for line in file:
        date = get_value(line, find_column(columns, 'Launch Date (UTC)'))
        if date: 
            year, month, *rest = date.split(' ')

            if success is not None:
                _success = get_value(line, find_column(columns, 'Suc'))
                if success_translation[success] != _success:
                    continue

            aggregate_value = year if field == 'year' else month
        aggregate[aggregate_value] += 1
        
    return dict(aggregate)

def find_column(columns, name):
    return [c for c in columns if c.name==name][0]

def get_value(row, column):
    return row[column.start:column.end].strip()

print(group_by(open('launchlog.txt')))

