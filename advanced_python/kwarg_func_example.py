"""
Khi bạn muốn truyền vào số lượng tham số không cố định, có thể là một có thể là nhiều tham số.
Tuy kwargs được khuyên dùng ở mức tối thiểu nhưng theo kinh nghiệm của mình ở những dự án lớn, các function thường được truyền vào số lượng lớn tham số sẽ sử dụng kwargs.
"""


def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Example usage of the function with keyword arguments
print_details(name="Alice", age=30, city="New York")
