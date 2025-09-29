{
    'name': "Fatura Rapida",
    'version': '1.0',
    'author': 'Carlos Ferraz, Olualinet',
    'summary': 'Gerenciar Vendas',
    'description': 'Gerenciar Os Processos De Vendas.',
    'depends': ['base', 'sale_management'],
    'category': 'Serviço/Vendas',
    'data': [
        'views/menu_view.xml',
        'views/add_info_sale_view.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/fast_facture/static/src/css/style.css',
        ],
    }
}
