
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "FLOAT ID INT STR\n    lista : categorias\n\n    categorias : categoria\n               | categorias categoria\n\n    categoria : nome ':' produtos\n\n    nome : ID\n\n    produtos : produto\n             | produtos produto\n\n    produto : '*' INT ';' STR ';' FLOAT ';' INT\n\n    "
    
_lr_action_items = {'ID':([0,2,3,6,8,9,11,18,],[5,5,-2,-3,-4,-6,-7,-8,]),'$end':([1,2,3,6,8,9,11,18,],[0,-1,-2,-3,-4,-6,-7,-8,]),':':([4,5,],[7,-5,]),'*':([7,8,9,11,18,],[10,10,-6,-7,-8,]),'INT':([10,17,],[12,18,]),';':([12,14,16,],[13,15,17,]),'STR':([13,],[14,]),'FLOAT':([15,],[16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'lista':([0,],[1,]),'categorias':([0,],[2,]),'categoria':([0,2,],[3,6,]),'nome':([0,2,],[4,4,]),'produtos':([7,],[8,]),'produto':([7,8,],[9,11,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> lista","S'",1,None,None,None),
  ('lista -> categorias','lista',1,'p_grammar','lista_compras_yacc.py',7),
  ('categorias -> categoria','categorias',1,'p_grammar','lista_compras_yacc.py',9),
  ('categorias -> categorias categoria','categorias',2,'p_grammar','lista_compras_yacc.py',10),
  ('categoria -> nome : produtos','categoria',3,'p_grammar','lista_compras_yacc.py',12),
  ('nome -> ID','nome',1,'p_grammar','lista_compras_yacc.py',14),
  ('produtos -> produto','produtos',1,'p_grammar','lista_compras_yacc.py',16),
  ('produtos -> produtos produto','produtos',2,'p_grammar','lista_compras_yacc.py',17),
  ('produto -> * INT ; STR ; FLOAT ; INT','produto',8,'p_grammar','lista_compras_yacc.py',19),
]