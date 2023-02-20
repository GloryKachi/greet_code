if __name__ == '__main__':
    arg = [1, 2, 3]


    def list_invert(param):
        if type(param) == list:
            param[0] = 100
            print(param)


    print(arg)
    list_invert(arg)

