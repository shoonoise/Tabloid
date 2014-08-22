import shutil
from colorama import Style, Back


class FormattedTable:
    def __init__(self, width=None, padding=1, fill_symbol=' ', header_background=Back.GREEN):
        self._terminal_width = width or shutil.get_terminal_size()[0]
        self._header_background = header_background
        self._padding = padding
        self._fill_symbol = fill_symbol
        self._table = []

    def _fill_up_string(self, string, width):
        indent = self._fill_symbol * self._padding
        fill = self._fill_symbol * (width - (len(string) + self._padding))
        return '{}{}{}'.format(indent, string, fill)

    def _align_head(self):
        header = ''
        tile = self._terminal_width
        for column in self._table:
            width = column['width'] + self._padding
            title = column['title']
            if width < tile:
                tile -= width
            else:
                width = tile - self._padding * len(self._table)
                column['width'] = width
            header += self._fill_up_string(title, width)
        return header + self._fill_symbol * self._padding

    def _align_cell(self, elem, column_number):
        column_width = self._table[column_number]['width']
        needed_with = column_width + self._padding
        if needed_with >= len(elem):
            return self._fill_up_string(elem, needed_with)
        else:
            sliced_line = [elem[x:x+column_width] for x in range(0, len(elem), column_width)]
            head = self._fill_up_string(''.join(sliced_line[:1]), 0)

            padding = sum([column['width'] + self._padding for column in self._table[:column_number]])
            tail = '\n'.join([(self._fill_symbol * self._padding) +
                              (self._fill_symbol * padding) +
                              elem for elem in sliced_line[1:]])
            return '{}\n{}'.format(head, tail)

    def _format_row(self, row):
        formatted_row = ''
        for column_number, line in enumerate(row):
            format_function = self._table[column_number]['formatter']
            if format_function is None:
                format_function = lambda x, y: x
            formatted_row += format_function(self._align_cell(line, column_number), row)
        return formatted_row

    def _get_rows(self):
        for row in zip(*[column['lines'] for column in self._table]):
            yield self._format_row(row)

    def add_column(self, name, formatter=None):
        self._table.append({'title': name,
                            'width': len(name),
                            'formatter': formatter,
                            'lines': []})

    def add_row(self, row):
        for column_number, line in enumerate(row):
            line = str(line)
            self._table[column_number]['lines'].append(line)
            if self._table[column_number]['width'] < len(line):
                self._table[column_number]['width'] = len(line)

    def get_table(self):
        header = '{}{}{}'.format(self._header_background,
                                 self._align_head(),
                                 Style.RESET_ALL)
        body = '\n'.join(self._get_rows())
        return header, body
