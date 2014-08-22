from itertools import cycle
from tabloid import FormattedTable
from colorama import Back, Style, Fore


class Colorfull:
    uniq_colors = cycle((Fore.YELLOW, Fore.MAGENTA, Fore.CYAN))
    nodes = {}

    @classmethod
    def node(cls, node, row):
        if node in cls.nodes:
            return cls.nodes[node]
        else:
            if row[2] == 'sleep':
                style = Style.BRIGHT + next(cls.uniq_colors)
            else:
                style = next(cls.uniq_colors)
            cls.nodes[node] = '{}{}{}'.format(style,
                                              node,
                                              Style.RESET_ALL)
            return cls.nodes[node]

    @classmethod
    def status(cls, status, _):
        return {'up': '{}{}{}'.format(Fore.GREEN, status, Style.RESET_ALL),
                'down': '{}{}{}'.format(Fore.RED, Style.DIM, status, Style.RESET_ALL),
                'sleep': '{}{}{}'.format(Fore.WHITE, status, Style.RESET_ALL)}.get(status.strip(), status)


table = FormattedTable(fill_symbol=' ', header_background=Back.BLUE, padding=2)
table.add_column('Name')
table.add_column('Node', Colorfull.node)
table.add_column('Status', Colorfull.status)
table.add_column('Uptime')

table.add_row(['Twilight', 'ferm', 'up', '2 days'])
table.add_row(['Applejack', 'forest', 'sleep', '0 days'])
table.add_row(['Rainbow Dash', 'ferm', 'down', '2 days'])
table.add_row(['Rarity', 'shop', 'up', '5 days'])
table.add_row(['Fluttershy', 'shop', 'up', '3 days'])
table.add_row(['Pinkie Pi', 'ferm', 'down', '1 days'])


print('\n')
print('\n'.join(table.get_table()))
print('\n')

