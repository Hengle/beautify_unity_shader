import unittest

r''' 定制SymbolType，实现如下目标：
1. TokenType.ID，用.的写法来表示Enum，
2. 支持iter
3. 支持in
'''
class SymbolTypeMeta(type):

    def __new__(metacls, clsName, bases, attrs):
        members = []
        for k in filter(lambda name: name[0:2] != '__' and not callable(attrs[name]), sorted(attrs)):
            members.append(attrs[k])

        attrs['__members__'] = members
        newCls = super().__new__(metacls, clsName, bases, attrs)

        if clsName != 'SymbolType':
            baseMembers = SymbolType.__members__
            for k in filter(lambda name: name[0:2] != '__' and not callable(attrs[name]), sorted(attrs)):
                baseMembers.append(attrs[k])

            # like: SymbolType.TokenType
            setattr(SymbolType, clsName, newCls)

        return newCls

    def __len__(cls):
        return len(cls.__members__)

    def __iter__(cls):
        return iter(cls.__members__)

    def __contains__(cls, item):
        return item in cls.__members__

    def add(cls, member):
        cls.__members__.append(member)
        cls.__members__.sort()

        # SymbolType should not use this menthod
        SymbolType.__members__.append(member)
        SymbolType.__members__.sort()



class SymbolType(metaclass=SymbolTypeMeta):

    pass


class Test(unittest.TestCase):

    def test(self):

        class TokenType(SymbolType):

            # 变量
            ID = 'ID'
            String = 'String'
            # 标点
            Times = 'Times'
            EQ = 'EQ'
            # Debug
            NULL = 'NULL'


        class NonterminalType(SymbolType):

            S = 'S'
            E = 'E'

        for ty in TokenType:
            print(ty)

        print('-------')

        TokenType.add('__End')

        for ty in TokenType:
            print(ty)

        print('-------')

        for ty in SymbolType:
            print(ty)

        self.assertIn(TokenType.ID, TokenType)
        self.assertNotIn(TokenType.ID, NonterminalType)