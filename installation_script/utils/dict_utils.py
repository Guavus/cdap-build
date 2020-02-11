class DictUtil(object):
        def __init__(self):
            pass

        def check_dict(self,dict_yml):
            if isinstance(dict_yml, dict):
                return True
            else:
                return False

        def get_key_value(self,dict_yml):
            arr_val = []
            for key, value in dict_yml.items():
                arr_recur = []
                if self.check_dict(value):
                    self.get_key_value(value)
#                    for i, j in value.items():
#                        arr_recur.append(i)
#                        arr_recur.append(j)
#                        arr_val.append(arr_recur)
                else:
                    arr_recur.append(key)
                    arr_recur.append(value)
                    arr_val.append(arr_recur)
            print arr_val
            return arr_val




