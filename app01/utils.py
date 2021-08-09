
class MyResponse():
    def __init__(self):
        self.status = 200
        self.msg = '成功'

    @property
    def get_dict(self):
        return self.__dict__


if __name__ == '__main__':
    res = MyResponse()
    res.data = {'data':'hello'}
    print(res.get_dict) # {'status': 200, 'msg': '成功', 'data': {'data': 'hello'}}