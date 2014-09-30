from tabloid import FormattedTable
from colorama import Back, Fore, Style


table = FormattedTable(fill_symbol=' ', header_background=Back.RED, padding=1, width=120)

table.add_column('Name')
table.add_column('Value', max_width=20)
table.add_column('Comment', lambda row, _: '{}{}{}'.format(Fore.GREEN, row, Style.RESET_ALL))

table.add_row(['spam', 'ham', 'This line will be carry. ' * 20])
table.add_row(['foo', 'bar ' * 10, 'This line will be carry. ' * 10])
table.add_row(['egg', 'egg ' * 10, 'Blah blah blah ...'])

print('\n')
print('\n'.join(table.get_table()))
print('\n')
