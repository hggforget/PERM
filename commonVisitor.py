from io import StringIO

from gen.PERMParserVisitor import PERMParserVisitor
from gen.PERMLexer import PERMLexer
from gen.PERMParser import PERMParser
from antlr4 import *


class ProgramCommonVisitor(PERMParserVisitor):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_expr_tree_python_ll(expr_ll):
        """
        Python LL算法为兜底算法，防止SLL算法解析出错导致失败
        Args:
            expr_ll:

        Returns:

        """
        lexer = PERMLexer(InputStream(expr_ll))
        stream = CommonTokenStream(lexer)

        # parsing
        parser = PERMParser(stream)
        return parser.program()

    def get_text(self, node):
        """获取文本内容（递归）
        """
        if node.getChildCount() == 0:
            return node.getText()
        if isinstance(node, PERMParser.Compound_identifierContext):
            return node.getText()

        with StringIO() as builder:
            for child in node.getChildren():
                child_text = self.get_text(child)
                if not child_text.endswith(' '):
                    child_text += ' '
                builder.write(child_text)
            return builder.getvalue()

    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            if not self.shouldVisitNextChild(node, result):
                return result
            c = node.getChild(i)
            child_result = c.accept(self)
            result = self.aggregateResult(result, child_result)

        return result

    def visitTerminal(self, node):
        return node.getText()

    def visitErrorNode(self, node):
        return self.defaultResult()

    def defaultResult(self):
        return ''
