class Footer:
    def __init__(self, name, number):
        self.name = name
        self.number = number

footers = []

def add_footer():
    n = input("enter name: ")
    nb = input("enter number: ")
    footer = Footer(n, nb)
    print(f"footer name {footer.name}, footer number {footer.number}")
add_footer()
