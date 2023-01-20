class User():
    '''创建User类'''
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
    def describe_user(self):
        full_name = self.first_name + ' ' + self.last_name
        # print(full_name)
        return full_name

    def greet_user(self):
        print(self.first_name + ' ' + self.last_name + '，欢迎你的的到来！')