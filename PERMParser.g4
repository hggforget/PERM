parser grammar PERMParser;
options {
    tokenVocab=PERMLexer;
}

tigerProgram : KeywordMain KeywordLet declSegment KeywordIn KeywordBegin stmtList KeywordEnd;

declSegment: (typeDecl | varDecl | funcDecl)*;

typeDecl: KeywordType ID Equals type Semicolon;
type: typeId
    | KeywordArray LBracket IntLit RBracket KeywordOf typeId
    | ID;
typeId: KeywordInt | KeywordFloat;

varDecl: KeywordVar idList Colon type optionalInit Semicolon;
idList: ID (Comma ID)*;
optionalInit: | OpAssign constant;

funcDecl: KeywordFunction ID LParen paramList RParen (retType)? KeywordBegin stmtList KeywordEnd Semicolon;
paramList: | param (Comma param)*;

retType: Colon type;
param: ID Colon type;

stmtList: (stmt)*;
stmt: ifStmt
    | assignStmt
    | callStmt
    | whileStmt
    | forStmt
    | breakStmt
    | returnStmt
    | letStmt;

letStmt: KeywordLet declSegment KeywordIn stmtList KeywordEnd Semicolon;
returnStmt: KeywordReturn expr Semicolon;
breakStmt: KeywordBreak Semicolon;
forStmt: KeywordFor ID OpAssign expr KeywordTo expr KeywordDo stmtList KeywordEnddo Semicolon;
whileStmt: KeywordWhile expr KeywordDo stmtList KeywordEnddo Semicolon;
assignStmt: lvalue OpAssign rValue;
rValue: expr Semicolon;
callStmt: (lvalue OpAssign)? ID LParen exprList RParen Semicolon;

ifStmt: KeywordIf expr KeywordThen stmtList ifStmtTail;
ifStmtTail: KeywordEndif Semicolon
    | KeywordElse stmtList KeywordEndif Semicolon;

expr: orTerm;

orTerm: andTerm (BinOpOr andTerm)*;
andTerm: leTerm (BinOpAnd leTerm)*;
leTerm: geTerm (BinOpLeq geTerm)*;
geTerm: ltTerm (BinOpGeq ltTerm)*;
ltTerm: gtTerm (BinOpLt gtTerm)*;
gtTerm: neTerm (BinOpGt neTerm)*;
neTerm: eqTerm (BinOpNeq eqTerm)*;
eqTerm: subTerm (BinOpEq subTerm)*;
subTerm: addTerm (BinOpMinus addTerm)*;
addTerm: divTerm(BinOpPlus divTerm)*;
divTerm: mulTerm (BinOpDivide mulTerm)*;
mulTerm: parnTerm (BinOpTimes parnTerm)*;

parnTerm: (LParen expr RParen) | lvalue | constant;

//expr: constant exprTail
//    | lvalue exprTail
//    | LParen expr RParen exprTail;
//exprTail: BinOpPlus highExpr | highExpr;
//
//highExpr: BinOpPower expr | expr ;

//exprTail: | binaryOperator expr;

constant: IntLit | FloatLit;

exprList: | expr (Comma expr)*;

lvalue: ID (LBracket expr RBracket)?;

