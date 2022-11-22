# -*- coding: utf-8 -*-

class ReqPack(object):
    """"web request parse pack"""

    def __init__(self):
        pass

    @staticmethod
    def check_params_require(params: dict, requires: list):
        """
        check request params integrality
        :param params: the request params dict
        :param requires: the require param key list
        :return: the miss key
        """
        miss_list = []
        for item in requires:
            assert isinstance(item, str)
            if params.get(item) is None:
                miss_list.append(item)
        if len(miss_list) == 0:
            return
        miss_str = ','.join(miss_list)
        return miss_str


if __name__ == '__main__':
    req_pack = ReqPack()
    rsp = req_pack.check_params_require({'name': 'shawn', 'age': 18}, ['gender'])
    print(rsp)
