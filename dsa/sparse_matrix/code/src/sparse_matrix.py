class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=0, numCols=0):
        if matrixFilePath:
            self.numRows, self.numCols, self.elements = self._read_matrix_from_file(matrixFilePath)
        else:
            self.numRows = numRows
            self.numCols = numCols
            self.elements = {}

    def _read_matrix_from_file(self, filePath):
        elements = {}
        with open(filePath, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("Input file is empty")
            rows = int(lines[0].strip().split('=')[1])
            cols = int(lines[1].strip().split('=')[1])
            for line in lines[2:]:
                line = line.strip()
                if line:
                    if not line.startswith('(') or not line.endswith(')'):
                        raise ValueError("Input file has wrong format")
                    row, col, value = map(int, line[1:-1].split(','))
                    elements[(row, col)] = value
        return rows, cols, elements

    def getElement(self, currRow, currCol):
        return self.elements.get((currRow, currCol), 0)

    def setElement(self, currRow, currCol, value):
        if value != 0:
            self.elements[(currRow, currCol)] = value
        elif (currRow, currCol) in self.elements:
            del self.elements[(currRow, currCol)]

    def __add__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for addition")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for key in self.elements:
            result.setElement(*key, self.getElement(*key) + other.getElement(*key))
        for key in other.elements:
            if key not in self.elements:
                result.setElement(*key, other.getElement(*key))
        return result

    def __sub__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrices dimensions do not match for subtraction")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for key in self.elements:
            result.setElement(*key, self.getElement(*key) - other.getElement(*key))
        for key in other.elements:
            if key not in self.elements:
                result.setElement(*key, -other.getElement(*key))
        return result

    def __mul__(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrices dimensions do not match for multiplication")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (i, k), v in self.elements.items():
            for j in range(other.numCols):
                result.setElement(i, j, result.getElement(i, j) + v * other.getElement(k, j))
        return result

    def to_file(self, filePath):
        with open(filePath, 'w') as file:
            file.write(f"rows={self.numRows}\n")
            file.write(f"cols={self.numCols}\n")
            for (row, col), value in sorted(self.elements.items()):
                file.write(f"({row}, {col}, {value})\n")

def main():
    import sys
    if len(sys.argv) < 5:
        print("Usage: python sparse_matrix.py <operation> <matrix1.txt> <matrix2.txt> <output.txt>")
        return

    operation = sys.argv[1]
    matrix1Path = sys.argv[2]
    matrix2Path = sys.argv[3]
    outputPath = sys.argv[4]

    matrix1 = SparseMatrix(matrixFilePath=matrix1Path)
    matrix2 = SparseMatrix(matrixFilePath=matrix2Path)

    if operation == "add":
        result = matrix1 + matrix2
    elif operation == "subtract":
        result = matrix1 - matrix2
    elif operation == "multiply":
        result = matrix1 * matrix2
    else:
        print("Invalid operation. Use 'add', 'subtract', or 'multiply'.")
        return

    result.to_file(outputPath)
    print(f"Operation {operation} completed. Result written to {outputPath}")

if __name__ == "__main__":
    main()

