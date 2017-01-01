class DotDict(dict):
    """
    Simple dictionary wrapper that overrides the dot operator with dictionary getter and setter
    so that instance['value'] is equivalent to instance.value

    """
    def __init__(self, data_dict=None, *args, **kwargs):
        super(dict, self).__init__()
        self._user_defined_attrs = set()

        if data_dict:
            for k, v in data_dict.items():
                self._user_defined_attrs.add(k)
                if not isinstance(v, DotDict):
                    self[k] = DotDict.ToDotDict(v)
                else:
                    self[k] = v
        elif kwargs:
            for k, v in kwargs.items():
                self._user_defined_attrs.add(k)
                if not isinstance(v, DotDict):
                    self[k] = DotDict.ToDotDict(v)
                else:
                    self[k] = v

    def __setattr__(self, k, v):
        if k[0] == '_' or k in self.__dict__:
            return super(DotDict, self).__setattr__(k, v)
        else:
            self._user_defined_attrs.add(k)
            self[k] = v

    def __getattr__(self, k):
        if k[0] == '_':
            raise AttributeError(k)

        try:
            return self[k]
        except KeyError as err:
            return None

    @staticmethod
    def ToDotDict(data):
        """
        Recursively transforms a dict to a dotted dictionary

        """
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, dict):
                    data[k] = DotDict(v)
                    DotDict.ToDotDict(data[k])
                elif isinstance(v, list):
                    data[k] = [DotDict.ToDotDict(i) for i in v]
        elif isinstance(data, list):
            return [DotDict.ToDotDict(i) for i in data]
        else:
            return data

        return DotDict(data)


