"""
Author: Sarcoma
Language: Python
Github: https://github.com/sarcoma
"""


def main():
    print('\n'.join([(lambda i: 'cats' if i % 3 == 0 else (lambda i: 'bats' if i % 5 == 0 else (lambda i: 'spiders' if i % 15 == 0 else str(i))(i))(i))(i) for i in range(1, 101)]))


if __name__ == '__main__':
    main()
