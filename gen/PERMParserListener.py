# Generated from /Users/bytedance/PycharmProjects/PERM/PERMParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PERMParser import PERMParser
else:
    from PERMParser import PERMParser

# This class defines a complete listener for a parse tree produced by PERMParser.
class PERMParserListener(ParseTreeListener):

    # Enter a parse tree produced by PERMParser#program.
    def enterProgram(self, ctx:PERMParser.ProgramContext):
        pass

    # Exit a parse tree produced by PERMParser#program.
    def exitProgram(self, ctx:PERMParser.ProgramContext):
        pass


    # Enter a parse tree produced by PERMParser#suite.
    def enterSuite(self, ctx:PERMParser.SuiteContext):
        pass

    # Exit a parse tree produced by PERMParser#suite.
    def exitSuite(self, ctx:PERMParser.SuiteContext):
        pass


    # Enter a parse tree produced by PERMParser#ifStmt.
    def enterIfStmt(self, ctx:PERMParser.IfStmtContext):
        pass

    # Exit a parse tree produced by PERMParser#ifStmt.
    def exitIfStmt(self, ctx:PERMParser.IfStmtContext):
        pass


    # Enter a parse tree produced by PERMParser#conditionStmt.
    def enterConditionStmt(self, ctx:PERMParser.ConditionStmtContext):
        pass

    # Exit a parse tree produced by PERMParser#conditionStmt.
    def exitConditionStmt(self, ctx:PERMParser.ConditionStmtContext):
        pass


    # Enter a parse tree produced by PERMParser#condition.
    def enterCondition(self, ctx:PERMParser.ConditionContext):
        pass

    # Exit a parse tree produced by PERMParser#condition.
    def exitCondition(self, ctx:PERMParser.ConditionContext):
        pass


    # Enter a parse tree produced by PERMParser#assignStmt.
    def enterAssignStmt(self, ctx:PERMParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by PERMParser#assignStmt.
    def exitAssignStmt(self, ctx:PERMParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by PERMParser#StmtExpr.
    def enterStmtExpr(self, ctx:PERMParser.StmtExprContext):
        pass

    # Exit a parse tree produced by PERMParser#StmtExpr.
    def exitStmtExpr(self, ctx:PERMParser.StmtExprContext):
        pass


    # Enter a parse tree produced by PERMParser#StmtIf.
    def enterStmtIf(self, ctx:PERMParser.StmtIfContext):
        pass

    # Exit a parse tree produced by PERMParser#StmtIf.
    def exitStmtIf(self, ctx:PERMParser.StmtIfContext):
        pass


    # Enter a parse tree produced by PERMParser#StmtAssign.
    def enterStmtAssign(self, ctx:PERMParser.StmtAssignContext):
        pass

    # Exit a parse tree produced by PERMParser#StmtAssign.
    def exitStmtAssign(self, ctx:PERMParser.StmtAssignContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprArithmeticBinary.
    def enterExprArithmeticBinary(self, ctx:PERMParser.ExprArithmeticBinaryContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprArithmeticBinary.
    def exitExprArithmeticBinary(self, ctx:PERMParser.ExprArithmeticBinaryContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprComparison.
    def enterExprComparison(self, ctx:PERMParser.ExprComparisonContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprComparison.
    def exitExprComparison(self, ctx:PERMParser.ExprComparisonContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprBracket.
    def enterExprBracket(self, ctx:PERMParser.ExprBracketContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprBracket.
    def exitExprBracket(self, ctx:PERMParser.ExprBracketContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprIdentifier.
    def enterExprIdentifier(self, ctx:PERMParser.ExprIdentifierContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprIdentifier.
    def exitExprIdentifier(self, ctx:PERMParser.ExprIdentifierContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprLogicalNot.
    def enterExprLogicalNot(self, ctx:PERMParser.ExprLogicalNotContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprLogicalNot.
    def exitExprLogicalNot(self, ctx:PERMParser.ExprLogicalNotContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprFunc.
    def enterExprFunc(self, ctx:PERMParser.ExprFuncContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprFunc.
    def exitExprFunc(self, ctx:PERMParser.ExprFuncContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprLiteral.
    def enterExprLiteral(self, ctx:PERMParser.ExprLiteralContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprLiteral.
    def exitExprLiteral(self, ctx:PERMParser.ExprLiteralContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprLogicalBinary.
    def enterExprLogicalBinary(self, ctx:PERMParser.ExprLogicalBinaryContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprLogicalBinary.
    def exitExprLogicalBinary(self, ctx:PERMParser.ExprLogicalBinaryContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprPolicyAction.
    def enterExprPolicyAction(self, ctx:PERMParser.ExprPolicyActionContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprPolicyAction.
    def exitExprPolicyAction(self, ctx:PERMParser.ExprPolicyActionContext):
        pass


    # Enter a parse tree produced by PERMParser#ExprArithmeticUnary.
    def enterExprArithmeticUnary(self, ctx:PERMParser.ExprArithmeticUnaryContext):
        pass

    # Exit a parse tree produced by PERMParser#ExprArithmeticUnary.
    def exitExprArithmeticUnary(self, ctx:PERMParser.ExprArithmeticUnaryContext):
        pass


    # Enter a parse tree produced by PERMParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:PERMParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by PERMParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:PERMParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by PERMParser#FunctionCall.
    def enterFunctionCall(self, ctx:PERMParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by PERMParser#FunctionCall.
    def exitFunctionCall(self, ctx:PERMParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by PERMParser#StmtPrimitive.
    def enterStmtPrimitive(self, ctx:PERMParser.StmtPrimitiveContext):
        pass

    # Exit a parse tree produced by PERMParser#StmtPrimitive.
    def exitStmtPrimitive(self, ctx:PERMParser.StmtPrimitiveContext):
        pass


    # Enter a parse tree produced by PERMParser#primitive_name.
    def enterPrimitive_name(self, ctx:PERMParser.Primitive_nameContext):
        pass

    # Exit a parse tree produced by PERMParser#primitive_name.
    def exitPrimitive_name(self, ctx:PERMParser.Primitive_nameContext):
        pass


    # Enter a parse tree produced by PERMParser#PrimitiveArguments.
    def enterPrimitiveArguments(self, ctx:PERMParser.PrimitiveArgumentsContext):
        pass

    # Exit a parse tree produced by PERMParser#PrimitiveArguments.
    def exitPrimitiveArguments(self, ctx:PERMParser.PrimitiveArgumentsContext):
        pass


    # Enter a parse tree produced by PERMParser#FunctionArguments.
    def enterFunctionArguments(self, ctx:PERMParser.FunctionArgumentsContext):
        pass

    # Exit a parse tree produced by PERMParser#FunctionArguments.
    def exitFunctionArguments(self, ctx:PERMParser.FunctionArgumentsContext):
        pass


    # Enter a parse tree produced by PERMParser#function_name.
    def enterFunction_name(self, ctx:PERMParser.Function_nameContext):
        pass

    # Exit a parse tree produced by PERMParser#function_name.
    def exitFunction_name(self, ctx:PERMParser.Function_nameContext):
        pass


    # Enter a parse tree produced by PERMParser#compound_identifier.
    def enterCompound_identifier(self, ctx:PERMParser.Compound_identifierContext):
        pass

    # Exit a parse tree produced by PERMParser#compound_identifier.
    def exitCompound_identifier(self, ctx:PERMParser.Compound_identifierContext):
        pass


    # Enter a parse tree produced by PERMParser#identifier.
    def enterIdentifier(self, ctx:PERMParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PERMParser#identifier.
    def exitIdentifier(self, ctx:PERMParser.IdentifierContext):
        pass


    # Enter a parse tree produced by PERMParser#NUMBER.
    def enterNUMBER(self, ctx:PERMParser.NUMBERContext):
        pass

    # Exit a parse tree produced by PERMParser#NUMBER.
    def exitNUMBER(self, ctx:PERMParser.NUMBERContext):
        pass


    # Enter a parse tree produced by PERMParser#STR.
    def enterSTR(self, ctx:PERMParser.STRContext):
        pass

    # Exit a parse tree produced by PERMParser#STR.
    def exitSTR(self, ctx:PERMParser.STRContext):
        pass


    # Enter a parse tree produced by PERMParser#BOOL.
    def enterBOOL(self, ctx:PERMParser.BOOLContext):
        pass

    # Exit a parse tree produced by PERMParser#BOOL.
    def exitBOOL(self, ctx:PERMParser.BOOLContext):
        pass


    # Enter a parse tree produced by PERMParser#ActionAllow.
    def enterActionAllow(self, ctx:PERMParser.ActionAllowContext):
        pass

    # Exit a parse tree produced by PERMParser#ActionAllow.
    def exitActionAllow(self, ctx:PERMParser.ActionAllowContext):
        pass


    # Enter a parse tree produced by PERMParser#ActionDeny.
    def enterActionDeny(self, ctx:PERMParser.ActionDenyContext):
        pass

    # Exit a parse tree produced by PERMParser#ActionDeny.
    def exitActionDeny(self, ctx:PERMParser.ActionDenyContext):
        pass


    # Enter a parse tree produced by PERMParser#boolean.
    def enterBoolean(self, ctx:PERMParser.BooleanContext):
        pass

    # Exit a parse tree produced by PERMParser#boolean.
    def exitBoolean(self, ctx:PERMParser.BooleanContext):
        pass


    # Enter a parse tree produced by PERMParser#INT.
    def enterINT(self, ctx:PERMParser.INTContext):
        pass

    # Exit a parse tree produced by PERMParser#INT.
    def exitINT(self, ctx:PERMParser.INTContext):
        pass


    # Enter a parse tree produced by PERMParser#FLOAT.
    def enterFLOAT(self, ctx:PERMParser.FLOATContext):
        pass

    # Exit a parse tree produced by PERMParser#FLOAT.
    def exitFLOAT(self, ctx:PERMParser.FLOATContext):
        pass



del PERMParser