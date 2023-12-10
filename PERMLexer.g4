lexer grammar PERMLexer;


TRUE								: [tT][rR][uU][eE];
FALSE                               : [fF][aA][lL][sS][eE];
ALLOW                               : [Aa][Ll][Ll][Oo][Ww];
DENY                                : [Dd][Ee][Nn][Yy];

OR									:[oO][rR];									//OR函数
AND									:[aA][nN][dD];								//AND函数
NOT									:[nN][oO][tT];								//NOT函数

//keywords
PROGRAM                             : [Pp][Rr][Oo][Gg][Rr][Aa][Mm];
IF									: [iI][fF];									//IF判断函数
ELSEIF                              : [eE][lL][iI][fF];
ELSE                                : [eE][lL][sS][eE];
REQUEST                             : [Rr][Ee][Qq][Uu][Ee][Ss][Tt];
POLICY                              : [Pp][Oo][Ll][Ii][Cc][Yy];
EFFECT                              : [Ee][Ff][Ff][Ee][Cc][Tt];
MATCHER                             : [Mm][Aa][Tt][Cc][Hh][Ee][Rr];
FOR                                 : [Ff][Oo][Rr];
FROM                                : [Ff][Rr][Oo][Mm];
TO                                  : [Tt][Oo];
STEP                                : [Ss][Tt][Ee][Pp];


LR_BRACE:            '{';
RR_BRACE:            '}';
LR_BRACKET:          '(';
RR_BRACKET:          ')';
BLANK:               '';

OpAssign : '=' ;

EQ  : '==';
NEQ : '!=';
LT  : '<';
LTE : '<=';
GT  : '>';
GTE : '>=';


STAR: '*';
MUL                                 : STAR;
DIV                                 : '/';
ADD                                 : '+';
SUB                                 : '-';

MOD                                 : '%';
TILDE                               : '~';


Colon : ':' ;
Semicolon : ';' ;
COMMA: ',';
DOT: '.' ;


//数字相关匹配
INTEGER								:('0'|DIGIT+ ( E [-+]? DIGIT+ )?);									//整数，包含正整数、负整数、零

DOT_STARTING_FLOAT:
    DOT DIGIT+  ( E [-+]? DIGIT+ )?;

FLOAT                           //浮点数，包含正浮点数，负浮点数、零(0.0)
    : DIGIT+  ( E [-+]? DIGIT+ )? '.' DIGIT* ( E [-+]? DIGIT+ )?
;

DIGIT                               :[0-9];
IDENTIFIER
  : [a-zA-Z_] [a-zA-Z_0-9]*;
//BOOLEAN								:([tT][rR][uU][eE])|([fF][aA][lL][sS][eE]);		//Boolean类型，TRUE或者FALSE

CHINESE_IDENTIFIER
    : LETTER* '\u4e00'..'\u9fff' LETTER*
    ;

STRING
    : '\'' ( ~('\''|'\\') | ('\\' .) )* '\''
    |  '\\\'' ( ~('\''|'\\') | ('\\' .) )*? '\\\''
;




fragment E : [eE];
fragment LETTER : ([a-zA-Z_0-9]|'\u0100'..'\uFFFE'|[()+|.:, \-&><$]);

NEWLINE : [\n];
WS   : [ \t\r]+ -> channel(HIDDEN);