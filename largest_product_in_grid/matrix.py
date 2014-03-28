class Matrix():
    def __init__(self, rows, columns):
        self._rows = [MatrixRow(columns) for x in xrange(rows)]
        self._num_columns = columns

    def assert_valid_row_idx(self, idx):
        if idx < 0 or idx >= self.num_rows():
            raise ValueError("Index out of range")

    def __getitem__(self, idx):
        self.assert_valid_row_idx(idx)
        return self._rows[idx]

    def row(self, idx):
        self.assert_valid_row_idx(idx)
        return self._rows[idx]

    def column(self, idx):
        if idx < 0 or idx >= self._num_columns:
            raise ValueError("Index out of range %s" % idx)
        return [self[x][idx] for x in xrange(self.num_rows())]

    def num_rows(self):
        return len(self._rows)

    def num_columns(self):
        return self._num_columns

    def transpose(self):
        result = Matrix(self.num_columns(), self.num_rows())
        for i in xrange(self.num_rows()):
            for j in xrange(len(self[i])):
                result[j][i] = self[i][j]
        return result


class MatrixRow():
    def __init__(self, size):
        self._columns = [0 for x in range(0, size)]

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            (start, stop, step) = idx.indices(len(self._columns))
            return [self._columns[x] for x in range(start, stop, step)]
        else:
            self._assert_valid_idx(idx)
            return self._columns[idx]

    def _assert_valid_idx(self, idx):
        if idx < 0 or idx >= len(self._columns):
            raise ValueError("Index out of range %s " % idx)

    def __setitem__(self, key, value):
        self._assert_valid_idx(key)
        self._columns[key] = value

    def __iter__(self):
        return self._columns.__iter__()

    def __len__(self):
        return len(self._columns)
