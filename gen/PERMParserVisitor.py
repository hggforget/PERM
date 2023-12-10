# Generated from /Users/bytedance/PycharmProjects/PERM/PERMParser.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PERMParser import PERMParser
else:
    from PERMParser import PERMParser

# This class defines a complete generic visitor for a parse tree produced by PERMParser.

class PERMParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PERMParser#program.
    def visitProgram(self, ctx:PERMParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#suite.
    def visitSuite(self, ctx:PERMParser.SuiteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ifStmt.
    def visitIfStmt(self, ctx:PERMParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#conditionStmt.
    def visitConditionStmt(self, ctx:PERMParser.ConditionStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#condition.
    def visitCondition(self, ctx:PERMParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#assignStmt.
    def visitAssignStmt(self, ctx:PERMParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#StmtExpr.
    def visitStmtExpr(self, ctx:PERMParser.StmtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#StmtIf.
    def visitStmtIf(self, ctx:PERMParser.StmtIfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#StmtAssign.
    def visitStmtAssign(self, ctx:PERMParser.StmtAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprArithmeticBinary.
    def visitExprArithmeticBinary(self, ctx:PERMParser.ExprArithmeticBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprComparison.
    def visitExprComparison(self, ctx:PERMParser.ExprComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprBracket.
    def visitExprBracket(self, ctx:PERMParser.ExprBracketContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprIdentifier.
    def visitExprIdentifier(self, ctx:PERMParser.ExprIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprLogicalNot.
    def visitExprLogicalNot(self, ctx:PERMParser.ExprLogicalNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprFunc.
    def visitExprFunc(self, ctx:PERMParser.ExprFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprLiteral.
    def visitExprLiteral(self, ctx:PERMParser.ExprLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprLogicalBinary.
    def visitExprLogicalBinary(self, ctx:PERMParser.ExprLogicalBinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprPolicyAction.
    def visitExprPolicyAction(self, ctx:PERMParser.ExprPolicyActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ExprArithmeticUnary.
    def visitExprArithmeticUnary(self, ctx:PERMParser.ExprArithmeticUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:PERMParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#FunctionCall.
    def visitFunctionCall(self, ctx:PERMParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#StmtPrimitive.
    def visitStmtPrimitive(self, ctx:PERMParser.StmtPrimitiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#primitive_name.
    def visitPrimitive_name(self, ctx:PERMParser.Primitive_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#PrimitiveArguments.
    def visitPrimitiveArguments(self, ctx:PERMParser.PrimitiveArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#FunctionArguments.
    def visitFunctionArguments(self, ctx:PERMParser.FunctionArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#function_name.
    def visitFunction_name(self, ctx:PERMParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#compound_identifier.
    def visitCompound_identifier(self, ctx:PERMParser.Compound_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#identifier.
    def visitIdentifier(self, ctx:PERMParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#NUMBER.
    def visitNUMBER(self, ctx:PERMParser.NUMBERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#STR.
    def visitSTR(self, ctx:PERMParser.STRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#BOOL.
    def visitBOOL(self, ctx:PERMParser.BOOLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ActionAllow.
    def visitActionAllow(self, ctx:PERMParser.ActionAllowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#ActionDeny.
    def visitActionDeny(self, ctx:PERMParser.ActionDenyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#boolean.
    def visitBoolean(self, ctx:PERMParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#INT.
    def visitINT(self, ctx:PERMParser.INTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PERMParser#FLOAT.
    def visitFLOAT(self, ctx:PERMParser.FLOATContext):
        return self.visitChildren(ctx)



del PERMParser