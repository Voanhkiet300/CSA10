print("abc")


def hello():
    print(__name__, "Hello, World!")


# nếu chạy file gốc thì __name__ tên là __main__ còn chạy bên file khác thì nó có tên của file gốc
if __name__ == "__main__":
    hello()