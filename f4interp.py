__author__ = 'hyst329'

varmap = {}

defvals = {
    'INT': 0,
    'REAL': 0.0
}


def interpret(ast):
    for stat in ast:
        process(stat)


def evaluate(expr):
    op = expr[0]
    if op == 'ADD':
        return evaluate(expr[1]) + evaluate(expr[2])
    elif op == 'SUB':
        return evaluate(expr[1]) - evaluate(expr[2])
    elif op == 'MUL':
        return evaluate(expr[1]) * evaluate(expr[2])
    elif op == 'DIV':
        return evaluate(expr[1]) / evaluate(expr[2])
    elif op == 'EQL':
        return evaluate(expr[1]) == evaluate(expr[2])
    elif op == 'LEQ':
        return evaluate(expr[1]) <= evaluate(expr[2])
    elif op == 'GEQ':
        return evaluate(expr[1]) >= evaluate(expr[2])
    elif op == 'INT':
        return int(expr[1])
    elif op == 'REAL':
        return float(expr[1])
    elif op == 'ID':
        return varmap[expr[1]][1]


def process(stat):
    print stat
    instr = stat[0]
    if instr == 'BLANK':
        return
    elif instr == 'DEBUGVAR':
        for k in varmap.keys():
            print "%s  \t%s = %s" % (varmap[k][0],k, varmap[k][1])
    elif instr == 'NEW':
        typename, ident, value = stat[1], stat[2], stat[3]
        varmap[ident] = [typename, evaluate(value)]
    elif instr == 'NEWARR':
        typename, ident, size = stat[1], stat[3], evaluate(stat[2])
        varmap[ident] = [typename + '.' + str(size), [defvals[typename]] * int(size)]
    elif instr == 'IN':
        ident = stat[1]
        varmap[ident[1]][1] = input('Enter value for %s:' % ident[1])
    elif instr == 'OUT':
        expr = stat[1]
        print evaluate(expr)
    elif instr == 'MOV':
        ident, expr = stat[1], stat[2]
        varmap[ident][1] = evaluate(expr)
    elif instr == 'IF':
        cond, iftrue, iffalse = stat[1], stat[2], stat[3]
        if evaluate(cond):
            for s in iftrue:
                process(s)
        else:
            for s in iffalse:
                process(s)