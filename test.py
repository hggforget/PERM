from commonVisitor import ProgramCommonVisitor
from InterpreterVisitor import ProgramInterpreterVisitor
program_str = """program{
a = -1 * 2
c = 2
if (a == 2 or c >= 1)
{
r1 = request(sub, obj, act)
}
if (a == -2)
{
r2 = request(sub, dom , act)
}

p = policy(sub, obj, act)

e = effect(some(where (p.eft == allow)))

m1 = matcher(r1.sub == p.sub and r1.obj == p.obj and r1.act == p.act)

if (r2)
{
m2 = matcher(r2.sub == p.sub and r2.obj == p.obj and r2.act == p.act)
}

}

"""

program_tree = ProgramCommonVisitor.get_expr_tree_python_ll(program_str)
interpreter = ProgramInterpreterVisitor()
print(interpreter.visit(program_tree))
