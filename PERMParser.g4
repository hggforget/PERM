parser grammar PERMParser;
options {
    tokenVocab=PERMLexer;
}

program
    : PROGRAM (NEWLINE)? suite
    ;

suite
    : LR_BRACE (NEWLINE)* block((NEWLINE)* block)* (NEWLINE)* RR_BRACE
    ;


ifStmt
    : IF conditionStmt ((NEWLINE)?  ELSEIF conditionStmt)* ((NEWLINE)? ELSE (NEWLINE)? else=suite)?
    ;

conditionStmt
    : condition (NEWLINE)? suite
    ;

condition
    : LR_BRACKET expr RR_BRACKET
    ;

assignStmt
    : compound_identifier OpAssign primitive
    | compound_identifier OpAssign expr
    ;

block
    : expr                                                      # StmtExpr
    | ifStmt                                                    # StmtIf
    | assignStmt                                                # StmtAssign
//   | forStmt
    ;

expr
    : function                                                  # ExprFunc
    | LR_BRACKET expr RR_BRACKET                                # ExprBracket
    | compound_identifier                                       # ExprIdentifier
    | left=expr comparisonOperator right=expr                   # ExprComparison
    | NOT expr                                                  # ExprLogicalNot
    | left=expr op=AND right=expr                               # ExprLogicalBinary
    | left=expr op=OR  right=expr                               # ExprLogicalBinary
    | op=(ADD|SUB|TILDE) valueExpr=expr                         # ExprArithmeticUnary
    | left=expr op=(STAR|DIV|MOD) right=expr                    # ExprArithmeticBinary
    | left=expr op=(ADD|SUB) right=expr                         # ExprArithmeticBinary
    | literal                                                   # ExprLiteral
    | policyAction                                              # ExprPolicyAction
    ;


comparisonOperator
    : EQ | NEQ | LT | LTE | GT | GTE
    ;

function
    : function_name function_arguments                  #FunctionCall
    ;

primitive
    : primitive_name primitive_arguments                        #StmtPrimitive
    ;

primitive_name
    : REQUEST | POLICY | EFFECT | MATCHER
    ;

primitive_arguments
    : LR_BRACKET ( expr ( COMMA expr )* )? RR_BRACKET   #PrimitiveArguments
    ;

function_arguments
    : LR_BRACKET ( expr ( COMMA expr )* )? RR_BRACKET   #FunctionArguments
    ;

function_name
    : identifier;

compound_identifier
    : identifier DOT identifier
    | identifier
    ;

identifier
    : IDENTIFIER
    ;


literal
    : number                                    # NUMBER
    | STRING                                    # STR
    | boolean                                   # BOOL
;

policyAction
    : ALLOW                                     # ActionAllow
    | DENY                                      # ActionDeny
    ;

boolean
    :TRUE
    |FALSE;

number
	: op=SUB? INTEGER   # INT
	| op=SUB? FLOAT # FLOAT
	| op=SUB? DOT_STARTING_FLOAT # FLOAT
;
