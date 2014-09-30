from tabloid import FormattedTable
from colorama import Back


table = FormattedTable(fill_symbol=' ', header_background=Back.RED, padding=1)

table.add_column('Name')
table.add_column('Value', max_width=10)
table.add_column('Comment')

table.add_row(['spam', 'ham', 'This line will be carry. '*10])
table.add_row(['foo', 'bar'*10, 'This line will be carry. '*10])
table.add_row(['egg', 'egg'*10, 'Blah blah blah ...'])

print('\n')
print('\n'.join(table.get_table()))
print('\n')
