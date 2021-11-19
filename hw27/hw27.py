import turtle
from lark import Lark

try:
    input = raw_input   # For Python2 compatibility
except NameError:
    pass

turtle_grammar = """
    start: instruction+
    instruction: MOVEMENT NUMBER            -> movement
               | "c" COLOR [COLOR]          -> change_color
               | "fill" code_block          -> fill
               | "repeat" NAME code_block -> repeat
               | "let" NAME NUMBER        -> let
    code_block: "{" instruction+ "}"
    MOVEMENT: "f"|"b"|"l"|"r"
    COLOR: LETTER+
    %import common.LETTER
    %import common.CNAME -> NAME

    %import common.INT -> NUMBER
    %import common.WS
    %ignore WS
"""

parser = Lark(turtle_grammar)


def run_instruction(t):
    if t.data == 'change_color':
        turtle.color(*t.children)   # We just pass the color names as-is

    elif t.data == 'movement':
        name, number = t.children
        { 'f': turtle.fd,
          'b': turtle.bk,
          'l': turtle.lt,
          'r': turtle.rt, }[name](int(number))
        
    elif t.data == 'let':
        globals()[t.children[0]] = int(t.children[1])
        """print(f"{t.children[0]=}")"""
       

    elif t.data == 'repeat':
        count = globals()[t.children[0]]
        block = t.children[1]
        for i in range(int(count)):
            run_instruction(block)

    elif t.data == 'fill':
        turtle.begin_fill()
        run_instruction(t.children[0])
        turtle.end_fill()

    elif t.data == 'code_block':
        for cmd in t.children:
            run_instruction(cmd)
    else:
        raise SyntaxError('Unknown instruction: %s' % t.data)


def run_turtle(program):
    parse_tree = parser.parse(program)
    for inst in parse_tree.children:
        run_instruction(inst)

def main():
    while True:
        code = input('> ')
        try:
            run_turtle(code)
        except Exception as e:
            print(e)

def test():
    text = """
        c green blue
        let n 36
        fill { repeat n {
      f200 l170
        }}
    """
    run_turtle(text)

if __name__ == '__main__':
    test()
    #main()

