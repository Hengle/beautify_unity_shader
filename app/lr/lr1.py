from ..syntax_production import Production
from ..symbol_type import SymbolType
from .base_types import ObjectSet, Item
from .base_algorithms import calcClosure, goto, calcFirstDict
import sys
import unittest


# BeginningNonterminal = '__Begin'
# EndingTerminal = '__End'


def construct(productionList, stateListOutputFile=None, edgesOutputFile=None, isDebug=False):
    # 初始化symbolType
    TokenType = SymbolType.TokenType
    NonterminalType = SymbolType.NonterminalType

    # # 加入S -> XX $
    # NonterminalType.add(BeginningNonterminal)
    # TokenType.add(EndingTerminal)

    # firstNonterminalType = productionList[0].left
    # beginningProduction = Production(
    #     '%s -> %s %s' % (BeginningNonterminal,
    #                      firstNonterminalType, EndingTerminal),
    #     'p0',
    #     BeginningNonterminal,
    #     (firstNonterminalType, EndingTerminal),
    # )
    # productionList.insert(0, beginningProduction)

    # 根据productionList获取firstDict和nullableDict
    firstDict, nullableDict = calcFirstDict(productionList, TokenType)

    # 初始的ItemSet
    beginningItemSet = ObjectSet()
    beginningItemSet.add(Item(productionList[0], 0, '*')) 
    beginningState = calcClosure(productionList, firstDict, nullableDict, beginningItemSet)

    # 初始的StateSet
    stateSet = ObjectSet()
    stateSet.add(beginningState)
    stateList = []
    stateList.append(beginningState)
    # preStateIndex查看state之间的关系，state1 -> state2
    preStateIndex = []
    preStateIndex.append((0,0)) # 0 -> 0

    # 初始化edges
    edges = {}
    stateIndex = 0
    debug_IterationCount = 0
    while (stateIndex < len(stateList)):
        state = stateList[stateIndex]
        edges[stateIndex] = {}

        #for debug
        debug_IterationCount += 1
        if isDebug:
            print('Iteration Count = %s, now state = \n\t %s' % (debug_IterationCount, state))

        # 放置Reduce
        for item in state:
            if item.getNextSymbolType() is None:
                productionNo = item.production.name[1:]
                st = item.getLookAheadST()
                _addEdge(edges, stateIndex, st, 'r' + productionNo)

        # 放置Shift
        for ty in SymbolType:
   
            newState = goto(productionList, firstDict, nullableDict, state, ty)
            if len(newState) == 0:
                continue

            # 放置Accept
            if ty == TokenType.EndingTerminal:
                _addEdge(edges, stateIndex, ty, 'a')
                continue

            if not stateSet.has(newState):
                stateSet.add(newState)
                stateList.append(newState)
                # update preStateIndex
                preStateIndex.append((stateIndex, ty))

            _addEdge(edges, stateIndex, ty, 's%s' % stateSet.getSerialNumber(newState))

        stateIndex = stateIndex + 1

    if stateListOutputFile:
        _printStateList(stateList, preStateIndex, stateListOutputFile)
    if edgesOutputFile:
        _printEdges(edges, edgesOutputFile)

    return edges


def _addEdge(edges, key1, key2, action):
    oldValue = edges[key1].get(key2)
    if oldValue is None:
        edges[key1][key2] = action
    elif isinstance(oldValue, str):
        if oldValue != action:
            edges[key1][key2] = [oldValue, action]
    elif isinstance(oldValue, list) and action not in edges[key1][key2]:
        edges[key1][key2].append(action)
    else:
        print('should not go here!')


_cellOffset = 0
def _printCell(text):
    global _cellOffset
    if text == '\n':
        print('')
        _cellOffset = 0
        
        return

    if _cellOffset > 0:
        text = ' ' + text
    for i in range(len(text), 15-_cellOffset):
        text = text + ' '
    mayShortedLen = 15 - len(text)
    _cellOffset -= mayShortedLen
    if _cellOffset < 0:
        _cellOffset = 0

    print(text, end='')


def _printProductionList(productionList):
    print('-------ProductionList-----------')
    for p in productionList:
        print(p)
    print('--------------------------------')


def _printStateList(stateList, preStateIndex, file=None):
    if file is not None:
        oldStdout = sys.stdout
        sys.stdout = file
    else:
        print('-----------StateList------------')
    
    for i, state in enumerate(stateList):
        print(i, '<-', preStateIndex[i], state)

    if file is not None:
        sys.stdout = oldStdout
    else:
        print('--------------------------------')


def _printEdges(edges, file=None):
    if file is not None:
        oldStdout = sys.stdout
        sys.stdout = file
    else:
        print('------------Edges---------------')

    _printCell('')
    for ty in SymbolType:
        _printCell(ty)
    _printCell('\n')

    for i, _ in enumerate(edges):
        _printCell(str(i))
        for ty in SymbolType:
            actionStr = str(edges[i][ty] if edges[i].get(ty) else '')
            _printCell(actionStr)
        _printCell('\n')

    print('unsolved conflicts:')
    for i, _ in enumerate(edges):
        for ty in SymbolType:
            if  isinstance(edges[i].get(ty), list):
                print('%s x %s : %s' % (i, ty, edges[i].get(ty)))

    if file is not None:
        sys.stdout = oldStdout
    else:
        print('--------------------------------')



class Test(unittest.TestCase):

    def test(self):
        from test.lr1_test.productions import productionList
        _printProductionList(productionList)
        edges = construct(productionList)
        _printEdges(edges)



    def DDtestFirstDict(self):        
        # 加入S -> XX $
        firstNonterminalType = productionList[0].left
        beginningProduction = Production(
            '%s -> %s %s' % (BeginningNonterminal,
                             firstNonterminalType, EndingTerminal),
            'p0',
            BeginningNonterminal,
            (firstNonterminalType, EndingTerminal),
        )
        productionList.insert(0, beginningProduction)
        beginningItemSet = ObjectSet()
        beginningItemSet.add(Item(beginningProduction, 0, EndingTerminal))

        # 初始化symbolType
        from test.lr1_test.tokens import TokenType
        from test.lr1_test.nonterminals import NonterminalType
        SymbolType = [ty for ty in TokenType] + [ty for ty in NonterminalType]

        # 根据productionList获取firstDict和nullableDict
        firstDict, nullableDict = calcFirstDict(productionList, TokenType)
        for st in firstDict:
            print(st)
            for st2 in firstDict[st]:
                print('\t', st2)

        print(nullableDict)
