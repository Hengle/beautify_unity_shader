import re
from . import error_message
from .lex_token import Token
from .lex_tokens import TokenType


def LexicalError(text):
    error_message.error('find a lexical error. The pending text : ' + text)
    return Token(TokenType.LexicalError, text)


def PragmaSpecialDealer(text):
    # 特殊处理（pragma一直吃到回车），要么特殊处理preprocess命令，要么近似为stm处理但是特殊捕获Enter
    # 假如是pragma，则将下一个Enter捕获为Enter，而非SpaceLike。
    def enableEnterOnce(d):
        d['EnableEnterOnce'] = True
        return d
    SpaceDealer(modifyEnv=enableEnterOnce)
    return Token(TokenType.ID, text, text)




def SpaceDealer(text = '', env = {'EnableEnterOnce': False}, modifyEnv=None):
    if modifyEnv:
        modifyEnv(env)
        return

    if env['EnableEnterOnce'] and '\n' in text:
        env['EnableEnterOnce'] = False
        return Token(TokenType.Enter, text)
    return Token(TokenType.SpaceLike, text)


floatPattern = '[-+]?([\d]*[\.]?[\d]+)[fF]?'
numberPattern = '%s(e%s)?' % (floatPattern, floatPattern)

rules = [
    # priority 1 行注释
    {'pattern': re.compile(r"//.*"),
     'action': lambda text: Token(TokenType.Comment, text)},
    # 块注释
    {'pattern': re.compile(r"/\*(.|\n)*?\*/"),
     'action': lambda text: Token(TokenType.Comment, text)},
    # 字符串
    {'pattern': re.compile(r'\"[^\"]*\"'),
     'action': lambda text: Token(TokenType.String, text, text)},
    # 保留字
    {'pattern': re.compile(r'\b(Color|Vector|Range|Int|Float|2D|Cube|3D)\b'),
     'action': lambda text: Token(TokenType.ReservedWord, text, text)},
    {'pattern': re.compile(r'\b(Lighting|Cull|ZTest|ZWrite|Blend)\b'),
     'action': lambda text: Token(TokenType.ReservedWord, text, text)},
    # priority 2 ID，ID的前后一定要是\b
    {'pattern': re.compile(r"\bpragma\b"),
     'action': PragmaSpecialDealer},
    {'pattern': re.compile(r"\b[a-zA-Z_]\w*\b"),
     'action': lambda text: Token(TokenType.ID, text, text)},
    {'pattern': re.compile(numberPattern),
     'action': lambda text: Token(TokenType.Number, text, text)},
    # 标点符号
    {'pattern': re.compile(r"->"),
     'action': lambda text: Token(TokenType.RightArrow, text)},
    {'pattern': re.compile(r"\*="),
     'action': lambda text: Token(TokenType.AddAssign, text)},
    {'pattern': re.compile(r"/="),
     'action': lambda text: Token(TokenType.SubAssign, text)},
    {'pattern': re.compile(r"%="),
     'action': lambda text: Token(TokenType.MulAssign, text)},
    {'pattern': re.compile(r"\+="),
     'action': lambda text: Token(TokenType.DivAssign, text)},
    {'pattern': re.compile(r"-="),
     'action': lambda text: Token(TokenType.ModAssign, text)},
    {'pattern': re.compile(r"<<="),
     'action': lambda text: Token(TokenType.LeftShiftAssign, text)},
    {'pattern': re.compile(r">>="),
     'action': lambda text: Token(TokenType.RightShiftAssign, text)},
    {'pattern': re.compile(r"%="),
     'action': lambda text: Token(TokenType.ModAssign, text)},
    {'pattern': re.compile(r"&="),
     'action': lambda text: Token(TokenType.AndAssign, text)},
    {'pattern': re.compile(r"\^="),
     'action': lambda text: Token(TokenType.XorAssign, text)},
    {'pattern': re.compile(r"\|="),
     'action': lambda text: Token(TokenType.OrAssign, text)},
    {'pattern': re.compile(r"=="),
     'action': lambda text: Token(TokenType.EQ, text)},
    {'pattern': re.compile(r"!="),
     'action': lambda text: Token(TokenType.NEQ, text)},
    {'pattern': re.compile(r"<="),
     'action': lambda text: Token(TokenType.LE, text)},
    {'pattern': re.compile(r">="),
     'action': lambda text: Token(TokenType.GE, text)},
    {'pattern': re.compile(r"&&"),
     'action': lambda text: Token(TokenType.AND, text)},
    {'pattern': re.compile(r"\|\|"),
     'action': lambda text: Token(TokenType.OR, text)},
    {'pattern': re.compile(r"<<"),
     'action': lambda text: Token(TokenType.LeftShift, text)},
    {'pattern': re.compile(r">>"),
     'action': lambda text: Token(TokenType.RightShift, text)},
    {'pattern': re.compile(r"\+\+"),
     'action': lambda text: Token(TokenType.Increment, text)},
    {'pattern': re.compile(r"--"),
     'action': lambda text: Token(TokenType.Decrement, text)},
    # 单
    {'pattern': re.compile(r","),
     'action': lambda text: Token(TokenType.Comma, text)},
    {'pattern': re.compile(r":"),
     'action': lambda text: Token(TokenType.Colon, text)},
    {'pattern': re.compile(r";"),
     'action': lambda text: Token(TokenType.Semicolon, text)},
    {'pattern': re.compile(r"\("),
     'action': lambda text: Token(TokenType.LParen, text)},
    {'pattern': re.compile(r"\)"),
     'action': lambda text: Token(TokenType.RParen, text)},
    {'pattern': re.compile(r"\["),
     'action': lambda text: Token(TokenType.LBrack, text)},
    {'pattern': re.compile(r"\]"),
     'action': lambda text: Token(TokenType.RBrack, text)},
    {'pattern': re.compile(r"{"),
     'action': lambda text: Token(TokenType.LBrace, text)},
    {'pattern': re.compile(r"}"),
     'action': lambda text: Token(TokenType.RBrace, text)},
    {'pattern': re.compile(r"\."),
     'action': lambda text: Token(TokenType.Dot, text)},
    {'pattern': re.compile(r"\+"),
     'action': lambda text: Token(TokenType.Plus, text)},
    {'pattern': re.compile(r"-"),
     'action': lambda text: Token(TokenType.Minus, text)},
    {'pattern': re.compile(r"\*"),
     'action': lambda text: Token(TokenType.Times, text)},
    {'pattern': re.compile(r"/"),
     'action': lambda text: Token(TokenType.Divide, text)},
    {'pattern': re.compile(r"~"),
     'action': lambda text: Token(TokenType.Tilde, text)},
    {'pattern': re.compile(r"%"),
     'action': lambda text: Token(TokenType.Percent, text)},
    {'pattern': re.compile(r"&"),
     'action': lambda text: Token(TokenType.Ampersand, text)},
    {'pattern': re.compile(r"\^"),
     'action': lambda text: Token(TokenType.Caret, text)},
    {'pattern': re.compile(r"\|"),
     'action': lambda text: Token(TokenType.VerticalBar, text)},
    {'pattern': re.compile(r"="),
     'action': lambda text: Token(TokenType.Assign, text)},
    {'pattern': re.compile(r"#"),
     'action': lambda text: Token(TokenType.Pound, text)},
    {'pattern': re.compile(r"\?"),
     'action': lambda text: Token(TokenType.Question, text)},
    {'pattern': re.compile(r"!"),
     'action': lambda text: Token(TokenType.NOT, text)},
    {'pattern': re.compile(r"<"),
     'action': lambda text: Token(TokenType.LT, text)},
    {'pattern': re.compile(r">"),
     'action': lambda text: Token(TokenType.GT, text)},
    # { 'pattern' : re.compile(r"tab1"),
    #   'action' : lambda text: Token(TokenType.tab2, text)},
    # priority 3
    # switchable Enter
    {'pattern': re.compile(r"\s+", re.DOTALL),
     'action': SpaceDealer},
     # 'action': lambda text: Token(TokenType.SpaceLike, text)},
    {'pattern': re.compile(r".*"),
     'action': LexicalError},
    {'pattern': re.compile(r".", re.DOTALL),
     'action': lambda text: Token(TokenType.Any, text)},
]
