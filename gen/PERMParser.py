# Generated from /Users/bytedance/PycharmProjects/PERM/PERMParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,232,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,1,0,3,0,45,8,0,1,0,1,0,1,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,1,1,5,1,58,8,1,10,1,12,1,61,9,1,1,1,5,1,64,8,1,10,1,12,1,
        67,9,1,1,1,5,1,70,8,1,10,1,12,1,73,9,1,1,1,1,1,1,2,1,2,1,2,3,2,80,
        8,2,1,2,1,2,5,2,84,8,2,10,2,12,2,87,9,2,1,2,3,2,90,8,2,1,2,1,2,3,
        2,94,8,2,1,2,3,2,97,8,2,1,3,1,3,3,3,101,8,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,117,8,5,1,6,1,6,1,6,3,6,
        122,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,
        137,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,
        1,7,1,7,5,7,155,8,7,10,7,12,7,158,9,7,1,8,1,8,1,9,1,9,1,9,1,10,1,
        10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,5,12,174,8,12,10,12,12,12,
        177,9,12,3,12,179,8,12,1,12,1,12,1,13,1,13,1,13,1,13,5,13,187,8,
        13,10,13,12,13,190,9,13,3,13,192,8,13,1,13,1,13,1,14,1,14,1,15,1,
        15,1,15,1,15,1,15,3,15,203,8,15,1,16,1,16,1,17,1,17,1,17,3,17,210,
        8,17,1,18,1,18,3,18,214,8,18,1,19,1,19,1,20,3,20,219,8,20,1,20,1,
        20,3,20,223,8,20,1,20,1,20,3,20,227,8,20,1,20,3,20,230,8,20,1,20,
        0,1,14,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,0,6,2,0,35,36,38,38,3,0,32,32,34,34,37,37,1,0,35,36,1,0,26,31,
        1,0,12,15,1,0,1,2,248,0,42,1,0,0,0,2,48,1,0,0,0,4,76,1,0,0,0,6,98,
        1,0,0,0,8,104,1,0,0,0,10,116,1,0,0,0,12,121,1,0,0,0,14,136,1,0,0,
        0,16,159,1,0,0,0,18,161,1,0,0,0,20,164,1,0,0,0,22,167,1,0,0,0,24,
        169,1,0,0,0,26,182,1,0,0,0,28,195,1,0,0,0,30,202,1,0,0,0,32,204,
        1,0,0,0,34,209,1,0,0,0,36,213,1,0,0,0,38,215,1,0,0,0,40,229,1,0,
        0,0,42,44,5,8,0,0,43,45,5,50,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,
        46,1,0,0,0,46,47,3,2,1,0,47,1,1,0,0,0,48,52,5,20,0,0,49,51,5,50,
        0,0,50,49,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,55,
        1,0,0,0,54,52,1,0,0,0,55,65,3,12,6,0,56,58,5,50,0,0,57,56,1,0,0,
        0,58,61,1,0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,
        1,0,0,0,62,64,3,12,6,0,63,59,1,0,0,0,64,67,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,71,1,0,0,0,67,65,1,0,0,0,68,70,5,50,0,0,69,68,1,
        0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,74,1,0,0,0,73,
        71,1,0,0,0,74,75,5,21,0,0,75,3,1,0,0,0,76,77,5,9,0,0,77,85,3,6,3,
        0,78,80,5,50,0,0,79,78,1,0,0,0,79,80,1,0,0,0,80,81,1,0,0,0,81,82,
        5,10,0,0,82,84,3,6,3,0,83,79,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,
        85,86,1,0,0,0,86,96,1,0,0,0,87,85,1,0,0,0,88,90,5,50,0,0,89,88,1,
        0,0,0,89,90,1,0,0,0,90,91,1,0,0,0,91,93,5,11,0,0,92,94,5,50,0,0,
        93,92,1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,97,3,2,1,0,96,89,1,
        0,0,0,96,97,1,0,0,0,97,5,1,0,0,0,98,100,3,8,4,0,99,101,5,50,0,0,
        100,99,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,103,3,2,1,0,103,
        7,1,0,0,0,104,105,5,22,0,0,105,106,3,14,7,0,106,107,5,23,0,0,107,
        9,1,0,0,0,108,109,3,30,15,0,109,110,5,25,0,0,110,111,3,20,10,0,111,
        117,1,0,0,0,112,113,3,30,15,0,113,114,5,25,0,0,114,115,3,14,7,0,
        115,117,1,0,0,0,116,108,1,0,0,0,116,112,1,0,0,0,117,11,1,0,0,0,118,
        122,3,14,7,0,119,122,3,4,2,0,120,122,3,10,5,0,121,118,1,0,0,0,121,
        119,1,0,0,0,121,120,1,0,0,0,122,13,1,0,0,0,123,124,6,7,-1,0,124,
        137,3,18,9,0,125,126,5,22,0,0,126,127,3,14,7,0,127,128,5,23,0,0,
        128,137,1,0,0,0,129,137,3,30,15,0,130,131,5,7,0,0,131,137,3,14,7,
        8,132,133,7,0,0,0,133,137,3,14,7,5,134,137,3,34,17,0,135,137,3,36,
        18,0,136,123,1,0,0,0,136,125,1,0,0,0,136,129,1,0,0,0,136,130,1,0,
        0,0,136,132,1,0,0,0,136,134,1,0,0,0,136,135,1,0,0,0,137,156,1,0,
        0,0,138,139,10,9,0,0,139,140,3,16,8,0,140,141,3,14,7,10,141,155,
        1,0,0,0,142,143,10,7,0,0,143,144,5,6,0,0,144,155,3,14,7,8,145,146,
        10,6,0,0,146,147,5,5,0,0,147,155,3,14,7,7,148,149,10,4,0,0,149,150,
        7,1,0,0,150,155,3,14,7,5,151,152,10,3,0,0,152,153,7,2,0,0,153,155,
        3,14,7,4,154,138,1,0,0,0,154,142,1,0,0,0,154,145,1,0,0,0,154,148,
        1,0,0,0,154,151,1,0,0,0,155,158,1,0,0,0,156,154,1,0,0,0,156,157,
        1,0,0,0,157,15,1,0,0,0,158,156,1,0,0,0,159,160,7,3,0,0,160,17,1,
        0,0,0,161,162,3,28,14,0,162,163,3,26,13,0,163,19,1,0,0,0,164,165,
        3,22,11,0,165,166,3,24,12,0,166,21,1,0,0,0,167,168,7,4,0,0,168,23,
        1,0,0,0,169,178,5,22,0,0,170,175,3,14,7,0,171,172,5,41,0,0,172,174,
        3,14,7,0,173,171,1,0,0,0,174,177,1,0,0,0,175,173,1,0,0,0,175,176,
        1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,178,170,1,0,0,0,178,179,
        1,0,0,0,179,180,1,0,0,0,180,181,5,23,0,0,181,25,1,0,0,0,182,191,
        5,22,0,0,183,188,3,14,7,0,184,185,5,41,0,0,185,187,3,14,7,0,186,
        184,1,0,0,0,187,190,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,
        192,1,0,0,0,190,188,1,0,0,0,191,183,1,0,0,0,191,192,1,0,0,0,192,
        193,1,0,0,0,193,194,5,23,0,0,194,27,1,0,0,0,195,196,3,32,16,0,196,
        29,1,0,0,0,197,198,3,32,16,0,198,199,5,42,0,0,199,200,3,32,16,0,
        200,203,1,0,0,0,201,203,3,32,16,0,202,197,1,0,0,0,202,201,1,0,0,
        0,203,31,1,0,0,0,204,205,5,47,0,0,205,33,1,0,0,0,206,210,3,40,20,
        0,207,210,5,49,0,0,208,210,3,38,19,0,209,206,1,0,0,0,209,207,1,0,
        0,0,209,208,1,0,0,0,210,35,1,0,0,0,211,214,5,3,0,0,212,214,5,4,0,
        0,213,211,1,0,0,0,213,212,1,0,0,0,214,37,1,0,0,0,215,216,7,5,0,0,
        216,39,1,0,0,0,217,219,5,36,0,0,218,217,1,0,0,0,218,219,1,0,0,0,
        219,220,1,0,0,0,220,230,5,43,0,0,221,223,5,36,0,0,222,221,1,0,0,
        0,222,223,1,0,0,0,223,224,1,0,0,0,224,230,5,45,0,0,225,227,5,36,
        0,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,230,5,44,
        0,0,229,218,1,0,0,0,229,222,1,0,0,0,229,226,1,0,0,0,230,41,1,0,0,
        0,27,44,52,59,65,71,79,85,89,93,96,100,116,121,136,154,156,175,178,
        188,191,202,209,213,218,222,226,229
    ]

class PERMParser ( Parser ):

    grammarFileName = "PERMParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'{'", "'}'", "'('", "')'", "'\\u000C'", "'='", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'*'", "<INVALID>", 
                     "'/'", "'+'", "'-'", "'%'", "'~'", "':'", "';'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "ALLOW", "DENY", "OR", 
                      "AND", "NOT", "PROGRAM", "IF", "ELSEIF", "ELSE", "REQUEST", 
                      "POLICY", "EFFECT", "MATCHER", "FOR", "FROM", "TO", 
                      "STEP", "LR_BRACE", "RR_BRACE", "LR_BRACKET", "RR_BRACKET", 
                      "BLANK", "OpAssign", "EQ", "NEQ", "LT", "LTE", "GT", 
                      "GTE", "STAR", "MUL", "DIV", "ADD", "SUB", "MOD", 
                      "TILDE", "Colon", "Semicolon", "COMMA", "DOT", "INTEGER", 
                      "DOT_STARTING_FLOAT", "FLOAT", "DIGIT", "IDENTIFIER", 
                      "CHINESE_IDENTIFIER", "STRING", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_suite = 1
    RULE_ifStmt = 2
    RULE_conditionStmt = 3
    RULE_condition = 4
    RULE_assignStmt = 5
    RULE_block = 6
    RULE_expr = 7
    RULE_comparisonOperator = 8
    RULE_function = 9
    RULE_primitive = 10
    RULE_primitive_name = 11
    RULE_primitive_arguments = 12
    RULE_function_arguments = 13
    RULE_function_name = 14
    RULE_compound_identifier = 15
    RULE_identifier = 16
    RULE_literal = 17
    RULE_policyAction = 18
    RULE_boolean = 19
    RULE_number = 20

    ruleNames =  [ "program", "suite", "ifStmt", "conditionStmt", "condition", 
                   "assignStmt", "block", "expr", "comparisonOperator", 
                   "function", "primitive", "primitive_name", "primitive_arguments", 
                   "function_arguments", "function_name", "compound_identifier", 
                   "identifier", "literal", "policyAction", "boolean", "number" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    ALLOW=3
    DENY=4
    OR=5
    AND=6
    NOT=7
    PROGRAM=8
    IF=9
    ELSEIF=10
    ELSE=11
    REQUEST=12
    POLICY=13
    EFFECT=14
    MATCHER=15
    FOR=16
    FROM=17
    TO=18
    STEP=19
    LR_BRACE=20
    RR_BRACE=21
    LR_BRACKET=22
    RR_BRACKET=23
    BLANK=24
    OpAssign=25
    EQ=26
    NEQ=27
    LT=28
    LTE=29
    GT=30
    GTE=31
    STAR=32
    MUL=33
    DIV=34
    ADD=35
    SUB=36
    MOD=37
    TILDE=38
    Colon=39
    Semicolon=40
    COMMA=41
    DOT=42
    INTEGER=43
    DOT_STARTING_FLOAT=44
    FLOAT=45
    DIGIT=46
    IDENTIFIER=47
    CHINESE_IDENTIFIER=48
    STRING=49
    NEWLINE=50
    WS=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(PERMParser.PROGRAM, 0)

        def suite(self):
            return self.getTypedRuleContext(PERMParser.SuiteContext,0)


        def NEWLINE(self):
            return self.getToken(PERMParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = PERMParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(PERMParser.PROGRAM)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 43
                self.match(PERMParser.NEWLINE)


            self.state = 46
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuiteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACE(self):
            return self.getToken(PERMParser.LR_BRACE, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.BlockContext)
            else:
                return self.getTypedRuleContext(PERMParser.BlockContext,i)


        def RR_BRACE(self):
            return self.getToken(PERMParser.RR_BRACE, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PERMParser.NEWLINE)
            else:
                return self.getToken(PERMParser.NEWLINE, i)

        def getRuleIndex(self):
            return PERMParser.RULE_suite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuite" ):
                listener.enterSuite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuite" ):
                listener.exitSuite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSuite" ):
                return visitor.visitSuite(self)
            else:
                return visitor.visitChildren(self)




    def suite(self):

        localctx = PERMParser.SuiteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_suite)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(PERMParser.LR_BRACE)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 49
                self.match(PERMParser.NEWLINE)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 55
            self.block()
            self.state = 65
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 59
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==50:
                        self.state = 56
                        self.match(PERMParser.NEWLINE)
                        self.state = 61
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 62
                    self.block() 
                self.state = 67
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 68
                self.match(PERMParser.NEWLINE)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
            self.match(PERMParser.RR_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.else_ = None # SuiteContext

        def IF(self):
            return self.getToken(PERMParser.IF, 0)

        def conditionStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.ConditionStmtContext)
            else:
                return self.getTypedRuleContext(PERMParser.ConditionStmtContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(PERMParser.ELSEIF)
            else:
                return self.getToken(PERMParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(PERMParser.ELSE, 0)

        def suite(self):
            return self.getTypedRuleContext(PERMParser.SuiteContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PERMParser.NEWLINE)
            else:
                return self.getToken(PERMParser.NEWLINE, i)

        def getRuleIndex(self):
            return PERMParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = PERMParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(PERMParser.IF)
            self.state = 77
            self.conditionStmt()
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 79
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==50:
                        self.state = 78
                        self.match(PERMParser.NEWLINE)


                    self.state = 81
                    self.match(PERMParser.ELSEIF)
                    self.state = 82
                    self.conditionStmt() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 88
                    self.match(PERMParser.NEWLINE)


                self.state = 91
                self.match(PERMParser.ELSE)
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==50:
                    self.state = 92
                    self.match(PERMParser.NEWLINE)


                self.state = 95
                localctx.else_ = self.suite()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(PERMParser.ConditionContext,0)


        def suite(self):
            return self.getTypedRuleContext(PERMParser.SuiteContext,0)


        def NEWLINE(self):
            return self.getToken(PERMParser.NEWLINE, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_conditionStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionStmt" ):
                listener.enterConditionStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionStmt" ):
                listener.exitConditionStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionStmt" ):
                return visitor.visitConditionStmt(self)
            else:
                return visitor.visitChildren(self)




    def conditionStmt(self):

        localctx = PERMParser.ConditionStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_conditionStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.condition()
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==50:
                self.state = 99
                self.match(PERMParser.NEWLINE)


            self.state = 102
            self.suite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self):
            return self.getToken(PERMParser.LR_BRACKET, 0)

        def expr(self):
            return self.getTypedRuleContext(PERMParser.ExprContext,0)


        def RR_BRACKET(self):
            return self.getToken(PERMParser.RR_BRACKET, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = PERMParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(PERMParser.LR_BRACKET)
            self.state = 105
            self.expr(0)
            self.state = 106
            self.match(PERMParser.RR_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compound_identifier(self):
            return self.getTypedRuleContext(PERMParser.Compound_identifierContext,0)


        def OpAssign(self):
            return self.getToken(PERMParser.OpAssign, 0)

        def primitive(self):
            return self.getTypedRuleContext(PERMParser.PrimitiveContext,0)


        def expr(self):
            return self.getTypedRuleContext(PERMParser.ExprContext,0)


        def getRuleIndex(self):
            return PERMParser.RULE_assignStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStmt" ):
                listener.enterAssignStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStmt" ):
                listener.exitAssignStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStmt" ):
                return visitor.visitAssignStmt(self)
            else:
                return visitor.visitChildren(self)




    def assignStmt(self):

        localctx = PERMParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignStmt)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.compound_identifier()
                self.state = 109
                self.match(PERMParser.OpAssign)
                self.state = 110
                self.primitive()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.compound_identifier()
                self.state = 113
                self.match(PERMParser.OpAssign)
                self.state = 114
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_block

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StmtExprContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PERMParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtExpr" ):
                listener.enterStmtExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtExpr" ):
                listener.exitStmtExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtExpr" ):
                return visitor.visitStmtExpr(self)
            else:
                return visitor.visitChildren(self)


    class StmtIfContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ifStmt(self):
            return self.getTypedRuleContext(PERMParser.IfStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtIf" ):
                listener.enterStmtIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtIf" ):
                listener.exitStmtIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtIf" ):
                return visitor.visitStmtIf(self)
            else:
                return visitor.visitChildren(self)


    class StmtAssignContext(BlockContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.BlockContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignStmt(self):
            return self.getTypedRuleContext(PERMParser.AssignStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtAssign" ):
                listener.enterStmtAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtAssign" ):
                listener.exitStmtAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtAssign" ):
                return visitor.visitStmtAssign(self)
            else:
                return visitor.visitChildren(self)



    def block(self):

        localctx = PERMParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        try:
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = PERMParser.StmtExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = PERMParser.StmtIfContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                self.ifStmt()
                pass

            elif la_ == 3:
                localctx = PERMParser.StmtAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 120
                self.assignStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ExprArithmeticBinaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.ExprContext)
            else:
                return self.getTypedRuleContext(PERMParser.ExprContext,i)

        def STAR(self):
            return self.getToken(PERMParser.STAR, 0)
        def DIV(self):
            return self.getToken(PERMParser.DIV, 0)
        def MOD(self):
            return self.getToken(PERMParser.MOD, 0)
        def ADD(self):
            return self.getToken(PERMParser.ADD, 0)
        def SUB(self):
            return self.getToken(PERMParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArithmeticBinary" ):
                listener.enterExprArithmeticBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArithmeticBinary" ):
                listener.exitExprArithmeticBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArithmeticBinary" ):
                return visitor.visitExprArithmeticBinary(self)
            else:
                return visitor.visitChildren(self)


    class ExprComparisonContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def comparisonOperator(self):
            return self.getTypedRuleContext(PERMParser.ComparisonOperatorContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.ExprContext)
            else:
                return self.getTypedRuleContext(PERMParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprComparison" ):
                listener.enterExprComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprComparison" ):
                listener.exitExprComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprComparison" ):
                return visitor.visitExprComparison(self)
            else:
                return visitor.visitChildren(self)


    class ExprBracketContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(PERMParser.LR_BRACKET, 0)
        def expr(self):
            return self.getTypedRuleContext(PERMParser.ExprContext,0)

        def RR_BRACKET(self):
            return self.getToken(PERMParser.RR_BRACKET, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprBracket" ):
                listener.enterExprBracket(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprBracket" ):
                listener.exitExprBracket(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprBracket" ):
                return visitor.visitExprBracket(self)
            else:
                return visitor.visitChildren(self)


    class ExprIdentifierContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compound_identifier(self):
            return self.getTypedRuleContext(PERMParser.Compound_identifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprIdentifier" ):
                listener.enterExprIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprIdentifier" ):
                listener.exitExprIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprIdentifier" ):
                return visitor.visitExprIdentifier(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicalNotContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(PERMParser.NOT, 0)
        def expr(self):
            return self.getTypedRuleContext(PERMParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicalNot" ):
                listener.enterExprLogicalNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicalNot" ):
                listener.exitExprLogicalNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicalNot" ):
                return visitor.visitExprLogicalNot(self)
            else:
                return visitor.visitChildren(self)


    class ExprFuncContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function(self):
            return self.getTypedRuleContext(PERMParser.FunctionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprFunc" ):
                listener.enterExprFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprFunc" ):
                listener.exitExprFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprFunc" ):
                return visitor.visitExprFunc(self)
            else:
                return visitor.visitChildren(self)


    class ExprLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(PERMParser.LiteralContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLiteral" ):
                listener.enterExprLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLiteral" ):
                listener.exitExprLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLiteral" ):
                return visitor.visitExprLiteral(self)
            else:
                return visitor.visitChildren(self)


    class ExprLogicalBinaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.ExprContext)
            else:
                return self.getTypedRuleContext(PERMParser.ExprContext,i)

        def AND(self):
            return self.getToken(PERMParser.AND, 0)
        def OR(self):
            return self.getToken(PERMParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprLogicalBinary" ):
                listener.enterExprLogicalBinary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprLogicalBinary" ):
                listener.exitExprLogicalBinary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprLogicalBinary" ):
                return visitor.visitExprLogicalBinary(self)
            else:
                return visitor.visitChildren(self)


    class ExprPolicyActionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def policyAction(self):
            return self.getTypedRuleContext(PERMParser.PolicyActionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprPolicyAction" ):
                listener.enterExprPolicyAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprPolicyAction" ):
                listener.exitExprPolicyAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprPolicyAction" ):
                return visitor.visitExprPolicyAction(self)
            else:
                return visitor.visitChildren(self)


    class ExprArithmeticUnaryContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.valueExpr = None # ExprContext
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PERMParser.ExprContext,0)

        def ADD(self):
            return self.getToken(PERMParser.ADD, 0)
        def SUB(self):
            return self.getToken(PERMParser.SUB, 0)
        def TILDE(self):
            return self.getToken(PERMParser.TILDE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprArithmeticUnary" ):
                listener.enterExprArithmeticUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprArithmeticUnary" ):
                listener.exitExprArithmeticUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprArithmeticUnary" ):
                return visitor.visitExprArithmeticUnary(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PERMParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                localctx = PERMParser.ExprFuncContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 124
                self.function()
                pass

            elif la_ == 2:
                localctx = PERMParser.ExprBracketContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 125
                self.match(PERMParser.LR_BRACKET)
                self.state = 126
                self.expr(0)
                self.state = 127
                self.match(PERMParser.RR_BRACKET)
                pass

            elif la_ == 3:
                localctx = PERMParser.ExprIdentifierContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.compound_identifier()
                pass

            elif la_ == 4:
                localctx = PERMParser.ExprLogicalNotContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(PERMParser.NOT)
                self.state = 131
                self.expr(8)
                pass

            elif la_ == 5:
                localctx = PERMParser.ExprArithmeticUnaryContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 132
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 377957122048) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                localctx.valueExpr = self.expr(5)
                pass

            elif la_ == 6:
                localctx = PERMParser.ExprLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.literal()
                pass

            elif la_ == 7:
                localctx = PERMParser.ExprPolicyActionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.policyAction()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 154
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = PERMParser.ExprComparisonContext(self, PERMParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 138
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 139
                        self.comparisonOperator()
                        self.state = 140
                        localctx.right = self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = PERMParser.ExprLogicalBinaryContext(self, PERMParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 142
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 143
                        localctx.op = self.match(PERMParser.AND)
                        self.state = 144
                        localctx.right = self.expr(8)
                        pass

                    elif la_ == 3:
                        localctx = PERMParser.ExprLogicalBinaryContext(self, PERMParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 145
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 146
                        localctx.op = self.match(PERMParser.OR)
                        self.state = 147
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 4:
                        localctx = PERMParser.ExprArithmeticBinaryContext(self, PERMParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 148
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 149
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 158913789952) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = PERMParser.ExprArithmeticBinaryContext(self, PERMParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 151
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 152
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==35 or _la==36):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 153
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(PERMParser.EQ, 0)

        def NEQ(self):
            return self.getToken(PERMParser.NEQ, 0)

        def LT(self):
            return self.getToken(PERMParser.LT, 0)

        def LTE(self):
            return self.getToken(PERMParser.LTE, 0)

        def GT(self):
            return self.getToken(PERMParser.GT, 0)

        def GTE(self):
            return self.getToken(PERMParser.GTE, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = PERMParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_function

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionCallContext(FunctionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.FunctionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_name(self):
            return self.getTypedRuleContext(PERMParser.Function_nameContext,0)

        def function_arguments(self):
            return self.getTypedRuleContext(PERMParser.Function_argumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)



    def function(self):

        localctx = PERMParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function)
        try:
            localctx = PERMParser.FunctionCallContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.function_name()
            self.state = 162
            self.function_arguments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_primitive

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StmtPrimitiveContext(PrimitiveContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.PrimitiveContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def primitive_name(self):
            return self.getTypedRuleContext(PERMParser.Primitive_nameContext,0)

        def primitive_arguments(self):
            return self.getTypedRuleContext(PERMParser.Primitive_argumentsContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtPrimitive" ):
                listener.enterStmtPrimitive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtPrimitive" ):
                listener.exitStmtPrimitive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmtPrimitive" ):
                return visitor.visitStmtPrimitive(self)
            else:
                return visitor.visitChildren(self)



    def primitive(self):

        localctx = PERMParser.PrimitiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_primitive)
        try:
            localctx = PERMParser.StmtPrimitiveContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.primitive_name()
            self.state = 165
            self.primitive_arguments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REQUEST(self):
            return self.getToken(PERMParser.REQUEST, 0)

        def POLICY(self):
            return self.getToken(PERMParser.POLICY, 0)

        def EFFECT(self):
            return self.getToken(PERMParser.EFFECT, 0)

        def MATCHER(self):
            return self.getToken(PERMParser.MATCHER, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_primitive_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_name" ):
                listener.enterPrimitive_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_name" ):
                listener.exitPrimitive_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_name" ):
                return visitor.visitPrimitive_name(self)
            else:
                return visitor.visitChildren(self)




    def primitive_name(self):

        localctx = PERMParser.Primitive_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_primitive_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61440) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_primitive_arguments

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrimitiveArgumentsContext(Primitive_argumentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.Primitive_argumentsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(PERMParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(PERMParser.RR_BRACKET, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.ExprContext)
            else:
                return self.getTypedRuleContext(PERMParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PERMParser.COMMA)
            else:
                return self.getToken(PERMParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveArguments" ):
                listener.enterPrimitiveArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveArguments" ):
                listener.exitPrimitiveArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveArguments" ):
                return visitor.visitPrimitiveArguments(self)
            else:
                return visitor.visitChildren(self)



    def primitive_arguments(self):

        localctx = PERMParser.Primitive_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_primitive_arguments)
        self._la = 0 # Token type
        try:
            localctx = PERMParser.PrimitiveArgumentsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(PERMParser.LR_BRACKET)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 765638054248606) != 0):
                self.state = 170
                self.expr(0)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 171
                    self.match(PERMParser.COMMA)
                    self.state = 172
                    self.expr(0)
                    self.state = 177
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 180
            self.match(PERMParser.RR_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_function_arguments

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FunctionArgumentsContext(Function_argumentsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.Function_argumentsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LR_BRACKET(self):
            return self.getToken(PERMParser.LR_BRACKET, 0)
        def RR_BRACKET(self):
            return self.getToken(PERMParser.RR_BRACKET, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.ExprContext)
            else:
                return self.getTypedRuleContext(PERMParser.ExprContext,i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PERMParser.COMMA)
            else:
                return self.getToken(PERMParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionArguments" ):
                listener.enterFunctionArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionArguments" ):
                listener.exitFunctionArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionArguments" ):
                return visitor.visitFunctionArguments(self)
            else:
                return visitor.visitChildren(self)



    def function_arguments(self):

        localctx = PERMParser.Function_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_arguments)
        self._la = 0 # Token type
        try:
            localctx = PERMParser.FunctionArgumentsContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(PERMParser.LR_BRACKET)
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 765638054248606) != 0):
                self.state = 183
                self.expr(0)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==41:
                    self.state = 184
                    self.match(PERMParser.COMMA)
                    self.state = 185
                    self.expr(0)
                    self.state = 190
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 193
            self.match(PERMParser.RR_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(PERMParser.IdentifierContext,0)


        def getRuleIndex(self):
            return PERMParser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_name" ):
                return visitor.visitFunction_name(self)
            else:
                return visitor.visitChildren(self)




    def function_name(self):

        localctx = PERMParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_identifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PERMParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(PERMParser.IdentifierContext,i)


        def DOT(self):
            return self.getToken(PERMParser.DOT, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_compound_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompound_identifier" ):
                listener.enterCompound_identifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompound_identifier" ):
                listener.exitCompound_identifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_identifier" ):
                return visitor.visitCompound_identifier(self)
            else:
                return visitor.visitChildren(self)




    def compound_identifier(self):

        localctx = PERMParser.Compound_identifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_compound_identifier)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.identifier()
                self.state = 198
                self.match(PERMParser.DOT)
                self.state = 199
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PERMParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = PERMParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(PERMParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_literal

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class STRContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(PERMParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSTR" ):
                listener.enterSTR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSTR" ):
                listener.exitSTR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSTR" ):
                return visitor.visitSTR(self)
            else:
                return visitor.visitChildren(self)


    class NUMBERContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(PERMParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNUMBER" ):
                listener.enterNUMBER(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNUMBER" ):
                listener.exitNUMBER(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNUMBER" ):
                return visitor.visitNUMBER(self)
            else:
                return visitor.visitChildren(self)


    class BOOLContext(LiteralContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.LiteralContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean(self):
            return self.getTypedRuleContext(PERMParser.BooleanContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBOOL" ):
                listener.enterBOOL(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBOOL" ):
                listener.exitBOOL(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBOOL" ):
                return visitor.visitBOOL(self)
            else:
                return visitor.visitChildren(self)



    def literal(self):

        localctx = PERMParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_literal)
        try:
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 43, 44, 45]:
                localctx = PERMParser.NUMBERContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.number()
                pass
            elif token in [49]:
                localctx = PERMParser.STRContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(PERMParser.STRING)
                pass
            elif token in [1, 2]:
                localctx = PERMParser.BOOLContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.boolean()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PolicyActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_policyAction

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ActionAllowContext(PolicyActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.PolicyActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ALLOW(self):
            return self.getToken(PERMParser.ALLOW, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionAllow" ):
                listener.enterActionAllow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionAllow" ):
                listener.exitActionAllow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionAllow" ):
                return visitor.visitActionAllow(self)
            else:
                return visitor.visitChildren(self)


    class ActionDenyContext(PolicyActionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.PolicyActionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DENY(self):
            return self.getToken(PERMParser.DENY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionDeny" ):
                listener.enterActionDeny(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionDeny" ):
                listener.exitActionDeny(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionDeny" ):
                return visitor.visitActionDeny(self)
            else:
                return visitor.visitChildren(self)



    def policyAction(self):

        localctx = PERMParser.PolicyActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_policyAction)
        try:
            self.state = 213
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                localctx = PERMParser.ActionAllowContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.match(PERMParser.ALLOW)
                pass
            elif token in [4]:
                localctx = PERMParser.ActionDenyContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 212
                self.match(PERMParser.DENY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(PERMParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PERMParser.FALSE, 0)

        def getRuleIndex(self):
            return PERMParser.RULE_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean" ):
                listener.enterBoolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean" ):
                listener.exitBoolean(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean" ):
                return visitor.visitBoolean(self)
            else:
                return visitor.visitChildren(self)




    def boolean(self):

        localctx = PERMParser.BooleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_boolean)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PERMParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FLOATContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.NumberContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(PERMParser.FLOAT, 0)
        def SUB(self):
            return self.getToken(PERMParser.SUB, 0)
        def DOT_STARTING_FLOAT(self):
            return self.getToken(PERMParser.DOT_STARTING_FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFLOAT" ):
                listener.enterFLOAT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFLOAT" ):
                listener.exitFLOAT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFLOAT" ):
                return visitor.visitFLOAT(self)
            else:
                return visitor.visitChildren(self)


    class INTContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a PERMParser.NumberContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def INTEGER(self):
            return self.getToken(PERMParser.INTEGER, 0)
        def SUB(self):
            return self.getToken(PERMParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterINT" ):
                listener.enterINT(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitINT" ):
                listener.exitINT(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitINT" ):
                return visitor.visitINT(self)
            else:
                return visitor.visitChildren(self)



    def number(self):

        localctx = PERMParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                localctx = PERMParser.INTContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 217
                    localctx.op = self.match(PERMParser.SUB)


                self.state = 220
                self.match(PERMParser.INTEGER)
                pass

            elif la_ == 2:
                localctx = PERMParser.FLOATContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 222
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 221
                    localctx.op = self.match(PERMParser.SUB)


                self.state = 224
                self.match(PERMParser.FLOAT)
                pass

            elif la_ == 3:
                localctx = PERMParser.FLOATContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 225
                    localctx.op = self.match(PERMParser.SUB)


                self.state = 228
                self.match(PERMParser.DOT_STARTING_FLOAT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




