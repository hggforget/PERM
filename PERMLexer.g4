lexer grammar PERMLexer;

KeywordMain : 'main' ;
KeywordArray : 'array' ;
KeywordRecord : 'record' ;
KeywordBreak : 'break' ;
KeywordDo : 'do' ;
KeywordElse : 'else' ;
KeywordEnd : 'end' ;
KeywordFor : 'for' ;
KeywordFunction : 'func' ;
KeywordIf : 'if' ;
KeywordIn : 'in' ;
KeywordLet : 'let' ;
KeywordOf : 'of' ;
KeywordThen : 'then' ;
KeywordTo : 'to' ;
KeywordType : 'type' ;
KeywordVar : 'var' ;
KeywordWhile : 'while' ;
KeywordEndif : 'endif' ;
KeywordBegin : 'begin' ;
KeywordEnddo : 'enddo' ;
KeywordReturn : 'return' ;
KeywordInt : 'int';
KeywordFloat : 'float';

BinOpPlus : '+';
BinOpMinus : '-';
BinOpTimes : '*';
BinOpDivide : '/';
BinOpEq : '==';
BinOpNeq : '!=';
BinOpLt : '<';
BinOpGt : '>';
BinOpLeq : '<=';
BinOpGeq : '>=';
BinOpAnd : '&';
BinOpOr : '|';

OpAssign : ':=' ;
Equals : '=' ;

Colon : ':' ;
Semicolon : ';' ;
Comma : ',' ;
DOT: '.' ;

LParen : '(' ;
RParen : ')' ;
LBracket : '[' ;
RBracket : ']' ;

ID : [A-Za-z][A-Za-z0-9_]* ;
IntLit : '0' | [1-9][0-9]* ;
FloatLit : [0-9]+ '.' [0-9]* ;

Comment : '/*' .*? '*/' -> skip ;
Whitespace : [ \t\r\n]+ -> skip ;