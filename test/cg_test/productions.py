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
    Production("prog ->  'CGINCLUDE' cg_prog 'ENDCG'",
               'p2',
               N.prog,
               ('CGINCLUDE', N.cg_prog, 'ENDCG', )),
    Production("cg_prog ->  cg_stms",
               'p3',
               N.cg_prog,
               (N.cg_stms, )),
    Production("cg_stms ->  cg_stm cg_stms",
               'p4',
               N.cg_stms,
               (N.cg_stm, N.cg_stms, )),
    Production("cg_stms -> ",
               'p5',
               N.cg_stms,
               ()),
    Production("cg_stm ->  preprocessing_stm",
               'p6',
               N.cg_stm,
               (N.preprocessing_stm, )),
    Production("cg_stm ->  function_definition",
               'p7',
               N.cg_stm,
               (N.function_definition, )),
    Production("cg_stm ->  dec",
               'p8',
               N.cg_stm,
               (N.dec, )),
    Production("function_definition ->  dec_specifier declarator compound_stm",
               'p9',
               N.function_definition,
               (N.dec_specifier, N.declarator, N.compound_stm, )),
    Production("function_definition ->  dec_specifier declarator : ID compound_stm",
               'p10',
               N.function_definition,
               (N.dec_specifier, N.declarator, T.Colon, T.ID, N.compound_stm, )),
    Production("preprocessing_stm ->  pp_if_stm",
               'p11',
               N.preprocessing_stm,
               (N.pp_if_stm, )),
    Production("preprocessing_stm ->  pp_cmd",
               'p12',
               N.preprocessing_stm,
               (N.pp_cmd, )),
    Production("pp_if_stm ->  # 'if' ID",
               'p13',
               N.pp_if_stm,
               (T.Pound, 'if', T.ID, )),
    Production("pp_if_stm ->  # 'ifdef' ID",
               'p14',
               N.pp_if_stm,
               (T.Pound, 'ifdef', T.ID, )),
    Production("pp_if_stm ->  # 'ifndef' ID",
               'p15',
               N.pp_if_stm,
               (T.Pound, 'ifndef', T.ID, )),
    Production("pp_if_stm ->  # 'elif' ID",
               'p16',
               N.pp_if_stm,
               (T.Pound, 'elif', T.ID, )),
    Production("pp_if_stm ->  # 'else'",
               'p17',
               N.pp_if_stm,
               (T.Pound, 'else', )),
    Production("pp_if_stm ->  # 'endif'",
               'p18',
               N.pp_if_stm,
               (T.Pound, 'endif', )),
    Production("pp_cmd ->  # 'include' String",
               'p19',
               N.pp_cmd,
               (T.Pound, 'include', T.String, )),
    Production("pp_cmd ->  # 'pragma' ids_or_numbers Enter",
               'p20',
               N.pp_cmd,
               (T.Pound, 'pragma', N.ids_or_numbers, T.Enter, )),
    Production("ids_or_numbers ->  ID ids_or_numbers",
               'p21',
               N.ids_or_numbers,
               (T.ID, N.ids_or_numbers, )),
    Production("ids_or_numbers ->  Number ids_or_numbers",
               'p22',
               N.ids_or_numbers,
               (T.Number, N.ids_or_numbers, )),
    Production("ids_or_numbers -> ",
               'p23',
               N.ids_or_numbers,
               ()),
    Production("primary_exp ->  ID",
               'p24',
               N.primary_exp,
               (T.ID, )),
    Production("primary_exp ->  String",
               'p25',
               N.primary_exp,
               (T.String, )),
    Production("primary_exp ->  Number",
               'p26',
               N.primary_exp,
               (T.Number, )),
    Production("primary_exp ->  ( exp )",
               'p27',
               N.primary_exp,
               (T.LParen, N.exp, T.RParen, )),
    Production("postfix_exp ->  primary_exp",
               'p28',
               N.postfix_exp,
               (N.primary_exp, )),
    Production("postfix_exp ->  postfix_exp [ exp ]",
               'p29',
               N.postfix_exp,
               (N.postfix_exp, T.LBrack, N.exp, T.RBrack, )),
    Production("postfix_exp ->  postfix_exp ( )",
               'p30',
               N.postfix_exp,
               (N.postfix_exp, T.LParen, T.RParen, )),
    Production("postfix_exp ->  postfix_exp ( argument_exp_list )",
               'p31',
               N.postfix_exp,
               (N.postfix_exp, T.LParen, N.argument_exp_list, T.RParen, )),
    Production("postfix_exp ->  postfix_exp . ID",
               'p32',
               N.postfix_exp,
               (N.postfix_exp, T.Dot, T.ID, )),
    Production("postfix_exp ->  postfix_exp ++",
               'p33',
               N.postfix_exp,
               (N.postfix_exp, T.Increment, )),
    Production("postfix_exp ->  postfix_exp --",
               'p34',
               N.postfix_exp,
               (N.postfix_exp, T.Decrement, )),
    Production("argument_exp_list ->  assignment_exp",
               'p35',
               N.argument_exp_list,
               (N.assignment_exp, )),
    Production("argument_exp_list ->  argument_exp_list , assignment_exp",
               'p36',
               N.argument_exp_list,
               (N.argument_exp_list, T.Comma, N.assignment_exp, )),
    Production("unary_exp ->  postfix_exp",
               'p37',
               N.unary_exp,
               (N.postfix_exp, )),
    Production("unary_exp ->  ++ unary_exp",
               'p38',
               N.unary_exp,
               (T.Increment, N.unary_exp, )),
    Production("unary_exp ->  -- unary_exp",
               'p39',
               N.unary_exp,
               (T.Decrement, N.unary_exp, )),
    Production("unary_exp ->  unary_op unary_exp",
               'p40',
               N.unary_exp,
               (N.unary_op, N.unary_exp, )),
    Production("unary_op ->  +",
               'p41',
               N.unary_op,
               (T.Plus, )),
    Production("unary_op ->  -",
               'p42',
               N.unary_op,
               (T.Minus, )),
    Production("unary_op ->  !",
               'p43',
               N.unary_op,
               (T.NOT, )),
    Production("unary_op ->  ~",
               'p44',
               N.unary_op,
               (T.Tilde, )),
    Production("binary_exp ->  unary_exp",
               'p45',
               N.binary_exp,
               (N.unary_exp, )),
    Production("binary_exp ->  binary_exp binary_op unary_exp",
               'p46',
               N.binary_exp,
               (N.binary_exp, N.binary_op, N.unary_exp, )),
    Production("binary_op ->  *",
               'p47',
               N.binary_op,
               (T.Times, )),
    Production("binary_op ->  /",
               'p48',
               N.binary_op,
               (T.Divide, )),
    Production("binary_op ->  %",
               'p49',
               N.binary_op,
               (T.Percent, )),
    Production("binary_op ->  +",
               'p50',
               N.binary_op,
               (T.Plus, )),
    Production("binary_op ->  -",
               'p51',
               N.binary_op,
               (T.Minus, )),
    Production("binary_op ->  <<",
               'p52',
               N.binary_op,
               (T.LeftShift, )),
    Production("binary_op ->  >>",
               'p53',
               N.binary_op,
               (T.RightShift, )),
    Production("binary_op ->  <",
               'p54',
               N.binary_op,
               (T.LT, )),
    Production("binary_op ->  >",
               'p55',
               N.binary_op,
               (T.GT, )),
    Production("binary_op ->  <=",
               'p56',
               N.binary_op,
               (T.LE, )),
    Production("binary_op ->  >=",
               'p57',
               N.binary_op,
               (T.GE, )),
    Production("binary_op ->  ==",
               'p58',
               N.binary_op,
               (T.EQ, )),
    Production("binary_op ->  !=",
               'p59',
               N.binary_op,
               (T.NEQ, )),
    Production("binary_op ->  &",
               'p60',
               N.binary_op,
               (T.Ampersand, )),
    Production("binary_op ->  ^",
               'p61',
               N.binary_op,
               (T.Caret, )),
    Production("binary_op ->  |",
               'p62',
               N.binary_op,
               (T.VerticalBar, )),
    Production("binary_op ->  &&",
               'p63',
               N.binary_op,
               (T.AND, )),
    Production("binary_op ->  ||",
               'p64',
               N.binary_op,
               (T.OR, )),
    Production("conditional_exp ->  binary_exp",
               'p65',
               N.conditional_exp,
               (N.binary_exp, )),
    Production("conditional_exp ->  binary_exp ? exp : conditional_exp",
               'p66',
               N.conditional_exp,
               (N.binary_exp, T.Question, N.exp, T.Colon, N.conditional_exp, )),
    Production("assignment_exp ->  conditional_exp",
               'p67',
               N.assignment_exp,
               (N.conditional_exp, )),
    Production("assignment_exp ->  unary_exp assignment_op assignment_exp",
               'p68',
               N.assignment_exp,
               (N.unary_exp, N.assignment_op, N.assignment_exp, )),
    Production("assignment_op ->  =",
               'p69',
               N.assignment_op,
               (T.Assign, )),
    Production("assignment_op ->  *=",
               'p70',
               N.assignment_op,
               (T.AddAssign, )),
    Production("assignment_op ->  /=",
               'p71',
               N.assignment_op,
               (T.SubAssign, )),
    Production("assignment_op ->  %=",
               'p72',
               N.assignment_op,
               (T.MulAssign, )),
    Production("assignment_op ->  +=",
               'p73',
               N.assignment_op,
               (T.DivAssign, )),
    Production("assignment_op ->  -=",
               'p74',
               N.assignment_op,
               (T.ModAssign, )),
    Production("assignment_op ->  <<=",
               'p75',
               N.assignment_op,
               (T.LeftShiftAssign, )),
    Production("assignment_op ->  >>=",
               'p76',
               N.assignment_op,
               (T.RightShiftAssign, )),
    Production("assignment_op ->  &=",
               'p77',
               N.assignment_op,
               (T.AndAssign, )),
    Production("assignment_op ->  ^=",
               'p78',
               N.assignment_op,
               (T.XorAssign, )),
    Production("assignment_op ->  |=",
               'p79',
               N.assignment_op,
               (T.OrAssign, )),
    Production("exp ->  assignment_exp",
               'p80',
               N.exp,
               (N.assignment_exp, )),
    Production("exp ->  exp , assignment_exp",
               'p81',
               N.exp,
               (N.exp, T.Comma, N.assignment_exp, )),
    Production("dec ->  struct_specifier ;",
               'p82',
               N.dec,
               (N.struct_specifier, T.Semicolon, )),
    Production("dec ->  dec_specifier init_dec_list ;",
               'p83',
               N.dec,
               (N.dec_specifier, N.init_dec_list, T.Semicolon, )),
    Production("dec_specifier ->  type_specifier",
               'p84',
               N.dec_specifier,
               (N.type_specifier, )),
    Production("dec_specifier ->  type_qualifier type_specifier",
               'p85',
               N.dec_specifier,
               (N.type_qualifier, N.type_specifier, )),
    Production("type_specifier ->  'void'",
               'p86',
               N.type_specifier,
               ('void', )),
    Production("type_specifier ->  'char'",
               'p87',
               N.type_specifier,
               ('char', )),
    Production("type_specifier ->  'short'",
               'p88',
               N.type_specifier,
               ('short', )),
    Production("type_specifier ->  'int'",
               'p89',
               N.type_specifier,
               ('int', )),
    Production("type_specifier ->  'long'",
               'p90',
               N.type_specifier,
               ('long', )),
    Production("type_specifier ->  'float'",
               'p91',
               N.type_specifier,
               ('float', )),
    Production("type_specifier ->  'double'",
               'p92',
               N.type_specifier,
               ('double', )),
    Production("type_specifier ->  'sampler2D'",
               'p93',
               N.type_specifier,
               ('sampler2D', )),
    Production("type_specifier ->  'float2'",
               'p94',
               N.type_specifier,
               ('float2', )),
    Production("type_specifier ->  'float3'",
               'p95',
               N.type_specifier,
               ('float3', )),
    Production("type_specifier ->  'float4'",
               'p96',
               N.type_specifier,
               ('float4', )),
    Production("type_specifier ->  'half2'",
               'p97',
               N.type_specifier,
               ('half2', )),
    Production("type_specifier ->  'half3'",
               'p98',
               N.type_specifier,
               ('half3', )),
    Production("type_specifier ->  'half4'",
               'p99',
               N.type_specifier,
               ('half4', )),
    Production("type_specifier ->  'fixed2'",
               'p100',
               N.type_specifier,
               ('fixed2', )),
    Production("type_specifier ->  'fixed3'",
               'p101',
               N.type_specifier,
               ('fixed3', )),
    Production("type_specifier ->  'fixed4'",
               'p102',
               N.type_specifier,
               ('fixed4', )),
    Production("type_specifier ->  typedef_name",
               'p103',
               N.type_specifier,
               (N.typedef_name, )),
    Production("type_qualifier ->  'uniform'",
               'p104',
               N.type_qualifier,
               ('uniform', )),
    Production("type_qualifier ->  'inout'",
               'p105',
               N.type_qualifier,
               ('inout', )),
    Production("typedef_name ->  ID",
               'p106',
               N.typedef_name,
               (T.ID, )),
    Production("struct_specifier ->  'struct' ID",
               'p107',
               N.struct_specifier,
               ('struct', T.ID, )),
    Production("struct_specifier ->  'struct' ID { struct_dec_list }",
               'p108',
               N.struct_specifier,
               ('struct', T.ID, T.LBrace, N.struct_dec_list, T.RBrace, )),
    Production("struct_dec_list ->  struct_dec",
               'p109',
               N.struct_dec_list,
               (N.struct_dec, )),
    Production("struct_dec_list ->  struct_dec_list struct_dec",
               'p110',
               N.struct_dec_list,
               (N.struct_dec_list, N.struct_dec, )),
    Production("struct_dec ->  type_specifier struct_declarator_list ;",
               'p111',
               N.struct_dec,
               (N.type_specifier, N.struct_declarator_list, T.Semicolon, )),
    Production("struct_declarator_list ->  struct_declarator",
               'p112',
               N.struct_declarator_list,
               (N.struct_declarator, )),
    Production("struct_declarator_list ->  struct_declarator_list , struct_declarator",
               'p113',
               N.struct_declarator_list,
               (N.struct_declarator_list, T.Comma, N.struct_declarator, )),
    Production("struct_declarator ->  declarator",
               'p114',
               N.struct_declarator,
               (N.declarator, )),
    Production("struct_declarator ->  declarator : ID",
               'p115',
               N.struct_declarator,
               (N.declarator, T.Colon, T.ID, )),
    Production("declarator ->  ID",
               'p116',
               N.declarator,
               (T.ID, )),
    Production("declarator ->  declarator [ exp ]",
               'p117',
               N.declarator,
               (N.declarator, T.LBrack, N.exp, T.RBrack, )),
    Production("declarator ->  declarator ( parameter_list )",
               'p118',
               N.declarator,
               (N.declarator, T.LParen, N.parameter_list, T.RParen, )),
    Production("parameter_list ->  parameter_dec",
               'p119',
               N.parameter_list,
               (N.parameter_dec, )),
    Production("parameter_list ->  parameter_list , parameter_dec",
               'p120',
               N.parameter_list,
               (N.parameter_list, T.Comma, N.parameter_dec, )),
    Production("parameter_dec ->  dec_specifier declarator",
               'p121',
               N.parameter_dec,
               (N.dec_specifier, N.declarator, )),
    Production("init_dec_list ->  init_dec",
               'p122',
               N.init_dec_list,
               (N.init_dec, )),
    Production("init_dec_list ->  init_dec_list , init_dec",
               'p123',
               N.init_dec_list,
               (N.init_dec_list, T.Comma, N.init_dec, )),
    Production("init_dec ->  declarator",
               'p124',
               N.init_dec,
               (N.declarator, )),
    Production("init_dec ->  declarator = assignment_exp",
               'p125',
               N.init_dec,
               (N.declarator, T.Assign, N.assignment_exp, )),
    Production("stm ->  exp_stm",
               'p126',
               N.stm,
               (N.exp_stm, )),
    Production("stm ->  compound_stm",
               'p127',
               N.stm,
               (N.compound_stm, )),
    Production("stm ->  selection_stm",
               'p128',
               N.stm,
               (N.selection_stm, )),
    Production("stm ->  iteration_stm",
               'p129',
               N.stm,
               (N.iteration_stm, )),
    Production("stm ->  jump_stm",
               'p130',
               N.stm,
               (N.jump_stm, )),
    Production("exp_stm ->  exp ;",
               'p131',
               N.exp_stm,
               (N.exp, T.Semicolon, )),
    Production("exp_stm ->  ;",
               'p132',
               N.exp_stm,
               (T.Semicolon, )),
    Production("compound_stm ->  { block_item_list }",
               'p133',
               N.compound_stm,
               (T.LBrace, N.block_item_list, T.RBrace, )),
    Production("compound_stm ->  { }",
               'p134',
               N.compound_stm,
               (T.LBrace, T.RBrace, )),
    Production("block_item_list ->  block_item",
               'p135',
               N.block_item_list,
               (N.block_item, )),
    Production("block_item_list ->  block_item_list block_item",
               'p136',
               N.block_item_list,
               (N.block_item_list, N.block_item, )),
    Production("block_item ->  dec",
               'p137',
               N.block_item,
               (N.dec, )),
    Production("block_item ->  stm",
               'p138',
               N.block_item,
               (N.stm, )),
    Production("selection_stm ->  'if' ( exp ) stm",
               'p139',
               N.selection_stm,
               ('if', T.LParen, N.exp, T.RParen, N.stm, )),
    Production("selection_stm ->  'if' ( exp ) stm 'else' stm",
               'p140',
               N.selection_stm,
               ('if', T.LParen, N.exp, T.RParen, N.stm, 'else', N.stm, )),
    Production("iteration_stm ->  'while' ( exp ) stm",
               'p141',
               N.iteration_stm,
               ('while', T.LParen, N.exp, T.RParen, N.stm, )),
    Production("iteration_stm ->  'do' stm 'while' ( exp ) ;",
               'p142',
               N.iteration_stm,
               ('do', N.stm, 'while', T.LParen, N.exp, T.RParen, T.Semicolon, )),
    Production("iteration_stm ->  'for' ( exp ; exp ; exp ) stm",
               'p143',
               N.iteration_stm,
               ('for', T.LParen, N.exp, T.Semicolon, N.exp, T.Semicolon, N.exp, T.RParen, N.stm, )),
    Production("jump_stm ->  'goto' ID",
               'p144',
               N.jump_stm,
               ('goto', T.ID, )),
    Production("jump_stm ->  'continue'",
               'p145',
               N.jump_stm,
               ('continue', )),
    Production("jump_stm ->  'break'",
               'p146',
               N.jump_stm,
               ('break', )),
    Production("jump_stm ->  'return' exp ;",
               'p147',
               N.jump_stm,
               ('return', N.exp, T.Semicolon, )),
]














class Test(unittest.TestCase):

    def test(self):
        for production in productionList:
            print(production)


    def DtestTokenType(self):
        for ty in T:
            print(ty)


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


_init()
