import tabloid
from colorama import Back, Style, Fore
from pygments import highlight
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer


def colorize_code(code, _):
    """
    Return highlighted code
    """
    return highlight(code, PythonLexer(), Terminal256Formatter()).strip('\n')


table = tabloid.FormattedTable(header_background=Back.BLUE, fill_symbol=" ")
table.add_column("#", lambda x, _: Fore.GREEN + x + Style.RESET_ALL)
table.add_column("Code", colorize_code)
table.add_column("Symbols", colorize_code)

code_example = (
    """  def _format_row(self, row):
        for multiline_cells in zip_longest(*[self._get_sliced_elements(elem, column_number)
                                             for column_number, elem in enumerate(row)], fillvalue=self._fill_symbol):
            formatted_row = ''
            for column_number, line in enumerate(multiline_cells):
                format_function = self._table[column_number]['formatter']
                needed_with = self._table[column_number]['width'] + self._padding
                if format_function is None:
                    format_function = lambda x, _: x
                formatted_row += format_function(self._fill_up_string(line, needed_with), row)
            yield formatted_row""")


code_example_2 = (
    """    def _get_sliced_elements(self, elem, column_number):
        column_width = self._table[column_number]['width']
        if len(elem) < column_width + self._padding:
            return [elem]
        return [elem[x:x+column_width] for x in range(0, len(elem), column_width)]"""
)

for n, line in enumerate(code_example.split('\n')):
    table.add_row([n, line, len(line)])
table.add_row(['-', '', ''])
for n, line in enumerate(code_example_2.split('\n')):
    table.add_row([n, line, len(line)])

print("\n", "\n".join(table.get_table()))
