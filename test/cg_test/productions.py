from app.syntax_nonterminal import Nonterminal
from app.syntax_production import Production
from app.lex_tokens import TokenType as T
from .nonterminals import NonterminalType as N
import unittest


productionList = [
    Production("prog ->  'CGPROGRAM' cg_prog 'ENDCG'",
               'p1',
               N.prog,
               ('CGPROGRAM', N.cg_prog, 'ENDCG', )),
    Production("cg_prog ->  cg_stms",
               'p2',
               N.cg_prog,
               (N.cg_stms, )),
    Production("cg_stms ->  cg_stm cg_stms",
               'p3',
               N.cg_stms,
               (N.cg_stm, N.cg_stms, )),
    Production("cg_stms -> ",
               'p4',
               N.cg_stms,
               ()),
    Production("cg_stm ->  preprocessing_stm",
               'p5',
               N.cg_stm,
               (N.preprocessing_stm, )),
    Production("cg_stm ->  function_definition",
               'p6',
               N.cg_stm,
               (N.function_definition, )),
    Production("cg_stm ->  dec",
               'p7',
               N.cg_stm,
               (N.dec, )),
    Production("function_definition ->  dec_specifier declarator compound_stm",
               'p8',
               N.function_definition,
               (N.dec_specifier, N.declarator, N.compound_stm, )),
    Production("preprocessing_stm ->  pp_if_stm",
               'p9',
               N.preprocessing_stm,
               (N.pp_if_stm, )),
    Production("preprocessing_stm ->  pp_cmd",
               'p10',
               N.preprocessing_stm,
               (N.pp_cmd, )),
    Production("pp_if_stm ->  # 'if' ID",
               'p11',
               N.pp_if_stm,
               (T.Pound, 'if', T.ID, )),
    Production("pp_if_stm ->  # 'ifdef' ID",
               'p12',
               N.pp_if_stm,
               (T.Pound, 'ifdef', T.ID, )),
    Production("pp_if_stm ->  # 'ifndef' ID",
               'p13',
               N.pp_if_stm,
               (T.Pound, 'ifndef', T.ID, )),
    Production("pp_if_stm ->  # 'elif' ID",
               'p14',
               N.pp_if_stm,
               (T.Pound, 'elif', T.ID, )),
    Production("pp_if_stm ->  # 'else'",
               'p15',
               N.pp_if_stm,
               (T.Pound, 'else', )),
    Production("pp_if_stm ->  # 'endif'",
               'p16',
               N.pp_if_stm,
               (T.Pound, 'endif', )),
    Production("pp_cmd ->  # 'include' String",
               'p17',
               N.pp_cmd,
               (T.Pound, 'include', T.String, )),
    Production("pp_cmd ->  # 'pragma' ids Enter",
               'p18',
               N.pp_cmd,
               (T.Pound, 'pragma', N.ids, T.Enter, )),
    Production("ids ->  ID ids",
               'p19',
               N.ids,
               (T.ID, N.ids, )),
    Production("ids -> ",
               'p20',
               N.ids,
               ()),
    Production("primary_exp ->  ID",
               'p21',
               N.primary_exp,
               (T.ID, )),
    Production("primary_exp ->  String",
               'p22',
               N.primary_exp,
               (T.String, )),
    Production("primary_exp ->  Number",
               'p23',
               N.primary_exp,
               (T.Number, )),
    Production("primary_exp ->  ( exp )",
               'p24',
               N.primary_exp,
               (T.LParen, N.exp, T.RParen, )),
    Production("postfix_exp ->  primary_exp",
               'p25',
               N.postfix_exp,
               (N.primary_exp, )),
    Production("postfix_exp ->  postfix_exp [ exp ]",
               'p26',
               N.postfix_exp,
               (N.postfix_exp, T.LBrack, N.exp, T.RBrack, )),
    Production("postfix_exp ->  postfix_exp ( )",
               'p27',
               N.postfix_exp,
               (N.postfix_exp, T.LParen, T.RParen, )),
    Production("postfix_exp ->  postfix_exp ( argument_exp_list )",
               'p28',
               N.postfix_exp,
               (N.postfix_exp, T.LParen, N.argument_exp_list, T.RParen, )),
    Production("postfix_exp ->  postfix_exp . ID",
               'p29',
               N.postfix_exp,
               (N.postfix_exp, T.Dot, T.ID, )),
    Production("postfix_exp ->  postfix_exp ++",
               'p30',
               N.postfix_exp,
               (N.postfix_exp, T.Increment, )),
    Production("postfix_exp ->  postfix_exp --",
               'p31',
               N.postfix_exp,
               (N.postfix_exp, T.Decrement, )),
    Production("argument_exp_list ->  assignment_exp",
               'p32',
               N.argument_exp_list,
               (N.assignment_exp, )),
    Production("argument_exp_list ->  argument_exp_list , assignment_exp",
               'p33',
               N.argument_exp_list,
               (N.argument_exp_list, T.Comma, N.assignment_exp, )),
    Production("unary_exp ->  postfix_exp",
               'p34',
               N.unary_exp,
               (N.postfix_exp, )),
    Production("unary_exp ->  ++ unary_exp",
               'p35',
               N.unary_exp,
               (T.Increment, N.unary_exp, )),
    Production("unary_exp ->  -- unary_exp",
               'p36',
               N.unary_exp,
               (T.Decrement, N.unary_exp, )),
    Production("unary_exp ->  unary_op unary_exp",
               'p37',
               N.unary_exp,
               (N.unary_op, N.unary_exp, )),
    Production("unary_op ->  +",
               'p38',
               N.unary_op,
               (T.Plus, )),
    Production("unary_op ->  -",
               'p39',
               N.unary_op,
               (T.Minus, )),
    Production("unary_op ->  !",
               'p40',
               N.unary_op,
               (T.NOT, )),
    Production("unary_op ->  ~",
               'p41',
               N.unary_op,
               (T.Tilde, )),
    Production("binary_exp ->  unary_exp",
               'p42',
               N.binary_exp,
               (N.unary_exp, )),
    Production("binary_exp ->  binary_exp binary_op unary_exp",
               'p43',
               N.binary_exp,
               (N.binary_exp, N.binary_op, N.unary_exp, )),
    Production("binary_op ->  *",
               'p44',
               N.binary_op,
               (T.Times, )),
    Production("binary_op ->  /",
               'p45',
               N.binary_op,
               (T.Divide, )),
    Production("binary_op ->  %",
               'p46',
               N.binary_op,
               (T.Percent, )),
    Production("binary_op ->  +",
               'p47',
               N.binary_op,
               (T.Plus, )),
    Production("binary_op ->  -",
               'p48',
               N.binary_op,
               (T.Minus, )),
    Production("binary_op ->  <<",
               'p49',
               N.binary_op,
               (T.LeftShift, )),
    Production("binary_op ->  >>",
               'p50',
               N.binary_op,
               (T.RightShift, )),
    Production("binary_op ->  <",
               'p51',
               N.binary_op,
               (T.LT, )),
    Production("binary_op ->  >",
               'p52',
               N.binary_op,
               (T.GT, )),
    Production("binary_op ->  <=",
               'p53',
               N.binary_op,
               (T.LE, )),
    Production("binary_op ->  >=",
               'p54',
               N.binary_op,
               (T.GE, )),
    Production("binary_op ->  ==",
               'p55',
               N.binary_op,
               (T.EQ, )),
    Production("binary_op ->  !=",
               'p56',
               N.binary_op,
               (T.NEQ, )),
    Production("binary_op ->  &",
               'p57',
               N.binary_op,
               (T.Ampersand, )),
    Production("binary_op ->  ^",
               'p58',
               N.binary_op,
               (T.Caret, )),
    Production("binary_op ->  |",
               'p59',
               N.binary_op,
               (T.VerticalBar, )),
    Production("binary_op ->  &&",
               'p60',
               N.binary_op,
               (T.AND, )),
    Production("binary_op ->  ||",
               'p61',
               N.binary_op,
               (T.OR, )),
    Production("conditional_exp ->  binary_exp",
               'p62',
               N.conditional_exp,
               (N.binary_exp, )),
    Production("conditional_exp ->  binary_exp ? exp : conditional_exp",
               'p63',
               N.conditional_exp,
               (N.binary_exp, T.Question, N.exp, T.Colon, N.conditional_exp, )),
    Production("assignment_exp ->  conditional_exp",
               'p64',
               N.assignment_exp,
               (N.conditional_exp, )),
    Production("assignment_exp ->  unary_exp assignment_op assignment_exp",
               'p65',
               N.assignment_exp,
               (N.unary_exp, N.assignment_op, N.assignment_exp, )),
    Production("assignment_op ->  =",
               'p66',
               N.assignment_op,
               (T.Assign, )),
    Production("exp ->  assignment_exp",
               'p67',
               N.exp,
               (N.assignment_exp, )),
    Production("exp ->  exp , assignment_exp",
               'p68',
               N.exp,
               (N.exp, T.Comma, N.assignment_exp, )),
    Production("dec ->  struct_specifier ;",
               'p69',
               N.dec,
               (N.struct_specifier, T.Semicolon, )),
    Production("dec ->  dec_specifier init_dec_list ;",
               'p70',
               N.dec,
               (N.dec_specifier, N.init_dec_list, T.Semicolon, )),
    Production("dec_specifier ->  type_specifier",
               'p71',
               N.dec_specifier,
               (N.type_specifier, )),
    Production("dec_specifier ->  type_qualifier type_specifier",
               'p72',
               N.dec_specifier,
               (N.type_qualifier, N.type_specifier, )),
    Production("type_specifier ->  'void'",
               'p73',
               N.type_specifier,
               ('void', )),
    Production("type_specifier ->  'char'",
               'p74',
               N.type_specifier,
               ('char', )),
    Production("type_specifier ->  'short'",
               'p75',
               N.type_specifier,
               ('short', )),
    Production("type_specifier ->  'int'",
               'p76',
               N.type_specifier,
               ('int', )),
    Production("type_specifier ->  'long'",
               'p77',
               N.type_specifier,
               ('long', )),
    Production("type_specifier ->  'float'",
               'p78',
               N.type_specifier,
               ('float', )),
    Production("type_specifier ->  'double'",
               'p79',
               N.type_specifier,
               ('double', )),
    Production("type_specifier ->  'sampler2D'",
               'p80',
               N.type_specifier,
               ('sampler2D', )),
    Production("type_specifier ->  'float2'",
               'p81',
               N.type_specifier,
               ('float2', )),
    Production("type_specifier ->  'float3'",
               'p82',
               N.type_specifier,
               ('float3', )),
    Production("type_specifier ->  'float4'",
               'p83',
               N.type_specifier,
               ('float4', )),
    Production("type_specifier ->  'half2'",
               'p84',
               N.type_specifier,
               ('half2', )),
    Production("type_specifier ->  'half3'",
               'p85',
               N.type_specifier,
               ('half3', )),
    Production("type_specifier ->  'half4'",
               'p86',
               N.type_specifier,
               ('half4', )),
    Production("type_specifier ->  'fixed2'",
               'p87',
               N.type_specifier,
               ('fixed2', )),
    Production("type_specifier ->  'fixed3'",
               'p88',
               N.type_specifier,
               ('fixed3', )),
    Production("type_specifier ->  'fixed4'",
               'p89',
               N.type_specifier,
               ('fixed4', )),
    Production("type_specifier ->  typedef_name",
               'p90',
               N.type_specifier,
               (N.typedef_name, )),
    Production("type_qualifier ->  'uniform'",
               'p91',
               N.type_qualifier,
               ('uniform', )),
    Production("typedef_name ->  ID",
               'p92',
               N.typedef_name,
               (T.ID, )),
    Production("struct_specifier ->  'struct' ID",
               'p93',
               N.struct_specifier,
               ('struct', T.ID, )),
    Production("struct_specifier ->  'struct' ID { struct_dec_list }",
               'p94',
               N.struct_specifier,
               ('struct', T.ID, T.LBrace, N.struct_dec_list, T.RBrace, )),
    Production("struct_dec_list ->  struct_dec",
               'p95',
               N.struct_dec_list,
               (N.struct_dec, )),
    Production("struct_dec_list ->  struct_dec_list struct_dec",
               'p96',
               N.struct_dec_list,
               (N.struct_dec_list, N.struct_dec, )),
    Production("struct_dec ->  type_specifier struct_declarator_list ;",
               'p97',
               N.struct_dec,
               (N.type_specifier, N.struct_declarator_list, T.Semicolon, )),
    Production("struct_declarator_list ->  struct_declarator",
               'p98',
               N.struct_declarator_list,
               (N.struct_declarator, )),
    Production("struct_declarator_list ->  struct_declarator_list , struct_declarator",
               'p99',
               N.struct_declarator_list,
               (N.struct_declarator_list, T.Comma, N.struct_declarator, )),
    Production("struct_declarator ->  declarator",
               'p100',
               N.struct_declarator,
               (N.declarator, )),
    Production("struct_declarator ->  declarator : ID",
               'p101',
               N.struct_declarator,
               (N.declarator, T.Colon, T.ID, )),
    Production("declarator ->  ID",
               'p102',
               N.declarator,
               (T.ID, )),
    Production("declarator ->  ( declarator )",
               'p103',
               N.declarator,
               (T.LParen, N.declarator, T.RParen, )),
    Production("declarator ->  declarator ( parameter_list )",
               'p104',
               N.declarator,
               (N.declarator, T.LParen, N.parameter_list, T.RParen, )),
    Production("parameter_list ->  parameter_dec",
               'p105',
               N.parameter_list,
               (N.parameter_dec, )),
    Production("parameter_list ->  parameter_list , parameter_dec",
               'p106',
               N.parameter_list,
               (N.parameter_list, T.Comma, N.parameter_dec, )),
    Production("parameter_dec ->  type_specifier declarator",
               'p107',
               N.parameter_dec,
               (N.type_specifier, N.declarator, )),
    Production("init_dec_list ->  ID",
               'p108',
               N.init_dec_list,
               (T.ID, )),
    Production("stm ->  exp_stm",
               'p109',
               N.stm,
               (N.exp_stm, )),
    Production("stm ->  compound_stm",
               'p110',
               N.stm,
               (N.compound_stm, )),
    Production("stm ->  selection_stm",
               'p111',
               N.stm,
               (N.selection_stm, )),
    Production("stm ->  iteration_stm",
               'p112',
               N.stm,
               (N.iteration_stm, )),
    Production("stm ->  jump_stm",
               'p113',
               N.stm,
               (N.jump_stm, )),
    Production("exp_stm ->  exp ;",
               'p114',
               N.exp_stm,
               (N.exp, T.Semicolon, )),
    Production("exp_stm ->  ;",
               'p115',
               N.exp_stm,
               (T.Semicolon, )),
    Production("compound_stm ->  { block_item_list }",
               'p116',
               N.compound_stm,
               (T.LBrace, N.block_item_list, T.RBrace, )),
    Production("compound_stm ->  { }",
               'p117',
               N.compound_stm,
               (T.LBrace, T.RBrace, )),
    Production("block_item_list ->  block_item",
               'p118',
               N.block_item_list,
               (N.block_item, )),
    Production("block_item_list ->  block_item_list block_item",
               'p119',
               N.block_item_list,
               (N.block_item_list, N.block_item, )),
    Production("block_item ->  dec",
               'p120',
               N.block_item,
               (N.dec, )),
    Production("block_item ->  stm",
               'p121',
               N.block_item,
               (N.stm, )),
    Production("selection_stm ->  'if' ( exp ) stm",
               'p122',
               N.selection_stm,
               ('if', T.LParen, N.exp, T.RParen, N.stm, )),
    Production("selection_stm ->  'if' ( exp ) stm 'else' stm",
               'p123',
               N.selection_stm,
               ('if', T.LParen, N.exp, T.RParen, N.stm, 'else', N.stm, )),
    Production("iteration_stm ->  'while' ( exp ) stm",
               'p124',
               N.iteration_stm,
               ('while', T.LParen, N.exp, T.RParen, N.stm, )),
    Production("iteration_stm ->  'do' stm 'while' ( exp ) ;",
               'p125',
               N.iteration_stm,
               ('do', N.stm, 'while', T.LParen, N.exp, T.RParen, T.Semicolon, )),
    Production("iteration_stm ->  'for' ( exp ; exp ; exp ) stm",
               'p126',
               N.iteration_stm,
               ('for', T.LParen, N.exp, T.Semicolon, N.exp, T.Semicolon, N.exp, T.RParen, N.stm, )),
    Production("jump_stm ->  'goto' ID",
               'p127',
               N.jump_stm,
               ('goto', T.ID, )),
    Production("jump_stm ->  'continue'",
               'p128',
               N.jump_stm,
               ('continue', )),
    Production("jump_stm ->  'break'",
               'p129',
               N.jump_stm,
               ('break', )),
    Production("jump_stm ->  'return' exp ;",
               'p130',
               N.jump_stm,
               ('return', N.exp, T.Semicolon, )),
]



class Test(unittest.TestCase):

    def test(self):
        for production in productionList:
            print(production)


def _init():

    for p in productionList:
        # Production <--> Nonterminal
        name1 = p.left
        name2 = name1 + p.name

        cls1 = Nonterminal.getClass(name1)
        if cls1 is None:
            print('error: lack of nonterminal class. production = %s' % p)
        cls1.leadingProductions.append(p)
        cls2 = Nonterminal.getClass(name2) or Nonterminal.getClass(name1)
        cls2.production = p
        p.LeftNonterminalClass = cls2

        # add 'Shader' into TokenType
        stTuple = ()
        for elm in p.right:
            if elm not in T and elm not in N:
                newSt = '-%s-' % elm
                T.add(newSt)
                stTuple += (newSt,)
            else:
                stTuple += (elm,)
        p.right = stTuple


    # 加入S -> XX $
    BeginningNonterminal = '__Begin'
    EndingTerminal = '__End'

    N.add(BeginningNonterminal)
    T.add(EndingTerminal)

    firstNonterminalType = productionList[0].left
    beginningProduction = Production(
        '%s -> %s %s' % (BeginningNonterminal,
                         firstNonterminalType, EndingTerminal),
        'p0',
        BeginningNonterminal,
        (firstNonterminalType, EndingTerminal),
    )
    productionList.insert(0, beginningProduction)


_init()
