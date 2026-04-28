def print_matrix(matrix):
    """
    Допоміжна функція для форматованого виведення матриці на екран.
    """
    for row in matrix:
        # Використовуємо форматування для вирівнювання колонок (по 5 символів на число)
        print(" ".join(f"{val:5d}" for val in row))


def main():
    try:

        const_a = 3

        matrix_b = [
            [1, -5,   8,  12],
            [4,  2, -10,   3],
            [-7,  9,   0, -15]
        ]

        if not matrix_b or not matrix_b[0]:
            raise ValueError("Матриця порожня або не ініціалізована.")

        cols_count = len(matrix_b[0])
        for row in matrix_b:
            if len(row) != cols_count:
                raise ValueError(
                    "Матриця має бути правильною прямокутною (рядки різної довжини не допускаються).")

        rows = len(matrix_b)
        cols = len(matrix_b[0])

        print("Початкова матриця B:")
        print_matrix(matrix_b)
        print(f"Константа a = {const_a}\n")

        matrix_c = []
        for i in range(rows):
            new_row = []
            for j in range(cols):
                new_row.append(const_a * matrix_b[i][j])
            matrix_c.append(new_row)

        print("Результуюча матриця C = a * B:")
        print_matrix(matrix_c)
        print()

        sum_of_min_elements = 0

        for j in range(cols):

            min_in_col = matrix_c[0][j]

            for i in range(1, rows):
                if matrix_c[i][j] < min_in_col:
                    min_in_col = matrix_c[i][j]

            print(f"Найменший елемент у стовпці {j}: {min_in_col}")
            sum_of_min_elements += min_in_col

        print(
            f"\nСума найменших елементів кожного стовпця матриці C: {sum_of_min_elements}")

    except ValueError as ve:
        print(f"Помилка вхідних даних: {ve}")
    except Exception as e:
        print(f"Виникла непередбачена помилка: {e}")


if __name__ == "__main__":
    main()
