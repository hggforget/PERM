from antlr4.tree.Tree import TerminalNodeImpl
from commonVisitor import ProgramCommonVisitor
from gen.PERMParser import PERMParser
from entity.effect import Effect
from entity.policy import Policy
from entity.matcher import Matcher
from entity.request import Request


class ProgramInterpreterVisitor(ProgramCommonVisitor):

    primitive_mapping = {
        'request': Request,
        'policy': Policy,
        'effect': Effect,
        'matcher': Matcher
    }

    def __init__(self):
        super().__init__()
        self.requests = dict()
        self.policy = dict()
        self.effect = dict()
        self.matchers = dict()
        self.variables = dict()

    def generate_policy(self):
        requests, policy, effect, matchers = '', '', '', ''
        if self.requests:
            requests += '[request_definition]\n'
            for k, v in self.requests.items():
                requests += '{} = {}\n'.format(k, str(v))

        if self.policy:
            policy += '[policy_definition]\n'
            for k, v in self.policy.items():
                policy += '{} = {}\n'.format(k, str(v))
        if self.effect:
            effect += '[policy_effect]\n'
            for k, v in self.effect.items():
                effect += '{} = {}\n'.format(k, str(v))
        if self.matchers:
            matchers += '[matchers]\n'
            for k, v in self.matchers.items():
                matchers += '{} = {}\n'.format(k, str(v))
        policy_content = [requests, policy, effect, matchers]
        return '\n'.join(policy_content)

    def visit(self, tree):
        res = tree.accept(self)
        return res

    def visitProgram(self, ctx: PERMParser.ProgramContext):
        res = self.visitChildren(ctx)
        if res is not None:
            return self.generate_policy()

    def get_function_name(self, ctx: PERMParser.FunctionCallContext):
        function_name = ctx.function_name()
        return self.visit(function_name).lower()

    def visitAssignStmt(self, ctx: PERMParser.AssignStmtContext):
        var = ctx.getChild(0).getText()
        value = self.visit(ctx.getChild(2))
        if isinstance(value, Request):
            self.requests[var] = value
        elif isinstance(value, Effect):
            self.effect[var] = value
        elif isinstance(value, Matcher):
            self.matchers[var] = value
        elif isinstance(value, Policy):
            self.policy[var] = value
        else:
            self.variables[var] = value

    def visitNUMBER(self, ctx: PERMParser.NUMBERContext):
        return int(self.visit(ctx.getChild(0)))

    def visitBoolean(self, ctx: PERMParser.NUMBERContext):
        return bool(self.visit(ctx.getChild(0)))

    def visitExprArithmeticUnary(self, ctx: PERMParser.ExprArithmeticUnaryContext):
        op = ctx.op.text
        value = self.visit(ctx.valueExpr)
        if op == '-':
            return 0 - value
        elif op == '+':
            return value
        elif op == '~':
            return ~value

    def visitExprArithmeticBinary(self, ctx: PERMParser.ExprArithmeticBinaryContext):
        op = ctx.op.text
        left_result = self.visit(ctx.left)
        right_result = self.visit(ctx.right)
        if op == '-':
            return left_result - right_result
        elif op == '+':
            return left_result + right_result
        elif op == '*':
            return left_result * right_result
        elif op == '/':
            return left_result / right_result
        elif op == '%':
            return left_result % right_result

    def visitFunctionCall(self, ctx: PERMParser.FunctionCallContext):
        function_name = self.get_function_name(ctx)
        # function_arguments = self.visit(ctx.function_arguments())
        if function_name == 'some':
            return self.get_text(ctx)
        elif function_name == 'where':
            return self.get_text(ctx)
        else:
            raise Exception(f'Unsupported function {function_name}')

    def visitFunctionArguments(self, ctx: PERMParser.FunctionArgumentsContext):
        result = []
        n = ctx.getChildCount()
        for i in range(n):
            c = ctx.getChild(i)
            if not isinstance(c, TerminalNodeImpl):
                child_result = c.accept(self)
                result.append(child_result)

        return tuple(result)

    def visitExprLogicalBinary(self, ctx: PERMParser.ExprLogicalBinaryContext):
        op = ctx.op.text.lower()
        left_result = self.visit(ctx.left)
        right_result = self.visit(ctx.right)
        if op == 'and':
            return left_result and right_result
        elif op == 'or':
            return left_result or right_result

    def visitExprLogicalNot(self, ctx: PERMParser.ExprLogicalNotContext):
        return not self.visit(ctx.getChild(1))

    def visitExprComparison(self, ctx: PERMParser.ExprComparisonContext):
        op = self.visit(ctx.getChild(1))
        left_result = self.visit(ctx.left)
        right_result = self.visit(ctx.right)
        if op == '==':
            return left_result == right_result
        elif op == '>=':
            return left_result >= right_result
        elif op == '!=':
            return left_result != right_result
        elif op == '<':
            return left_result < right_result
        elif op == '>':
            return left_result > right_result
        elif op == '<=':
            return left_result <= right_result

    def visitExprIdentifier(self, ctx: PERMParser.ExprIdentifierContext):
        key = ctx.getText()
        for variable_set in [self.variables, self.requests, self.effect, self.policy, self.matchers]:
            if variable_set.get(key, ''):
                return variable_set[key]

    def get_primitive_name(self, ctx: PERMParser.StmtPrimitiveContext):
        function_name = ctx.primitive_name()
        return self.visit(function_name).lower()

    def visitStmtPrimitive(self, ctx: PERMParser.StmtPrimitiveContext):
        primitive_name = self.get_primitive_name(ctx)
        primitive_entity = self.primitive_mapping[primitive_name]
        if primitive_name in ['request', 'policy']:
            primitive_arguments = self.visit(ctx.primitive_arguments())
            return primitive_entity(*primitive_arguments)
        else:
            return primitive_entity(self.get_text(ctx.primitive_arguments()))

    def visitPrimitiveArguments(self, ctx: PERMParser.PrimitiveArgumentsContext):
        result = []
        n = ctx.getChildCount()
        for i in range(n):
            c = ctx.getChild(i)
            if not isinstance(c, TerminalNodeImpl):
                child_result = self.get_text(c)
                result.append(child_result)
        return tuple(result)

    def visitIfStmt(self, ctx: PERMParser.IfStmtContext):
        n = ctx.getChildCount()
        for i in range(n):
            c = ctx.getChild(i)
            if isinstance(c, PERMParser.ConditionStmtContext):
                child_result = self.visit(c)
                if isinstance(child_result, tuple):
                    return child_result[1]
        else_suite = ctx.else_
        if else_suite is not None:
            return self.visit(else_suite)
        return None

    def visitConditionStmt(self, ctx: PERMParser.ConditionStmtContext):
        condition = self.visit(ctx.condition())
        if condition:
            return condition, self.visit(ctx.suite())
        else:
            return condition

    def visitCondition(self, ctx: PERMParser.ConditionContext):
        return self.visit(ctx.expr())
    