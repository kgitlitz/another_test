

class cl_result:

    def __init__(self):
        self.result = 7

    def show_result(self):
        print(self.result)

    def get_result(self):
        return self.result

if __name__ == "__main__":
    some_object = cl_result()

    some_object.show_result()