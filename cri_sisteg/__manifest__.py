# -*- encoding: utf-8 -*-

{
    'name': 'CRI',
    'version': '1.0',
    'category': 'Ingresos',
    'description': """
Catalogo de Rubros de Ingresos
==================================================
Catalogos relacionados para el cobro de ingresos.
    """,
    'depends': ['base','web_tour'],
    'data': ['views/view_cri_systeg.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 10,
}
