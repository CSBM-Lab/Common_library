from goatools import obo_parser

term = obo_parser.GODag('go.obo').query_term('GO:0003735')
print(term.parents)
print(term.level)
print(term.depth)
