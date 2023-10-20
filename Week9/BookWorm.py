"""BookWorm"""

def bookwormer(test_count):
    """Do as <e>judge says"""
    all_test = []
    book_list = []
    count = 0
    for _ in range(test_count):
        min_per_book = float(input())
        book_amount = int(input())
        for _ in range(book_amount):
            book_list.append(float(input()))
        all_test.append([min_per_book, sorted(book_list)])
        book_list.clear()
    for things in all_test:
        count = 0
        for num in things[1]:
            if things[0] < num:
                break
            things[0] -= num
            count += 1
        print(count)

bookwormer(int(input()))
