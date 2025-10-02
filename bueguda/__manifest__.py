{
    'name': "Empresa Bweguda",
    'version': '1.0',
    'author': 'Carlos Ferraz, Olualinet',
    'summary': 'Gerenciar Vendas',
    'description': 'Gerenciar os processos de vendas e de relacionamento com clientes.',
    'depends': ['base', 'sale_management'],
    'category': 'Serviço/Vendas',
    'data': [
        'security/sales_security.xml',
        'security/ir.model.access.csv.csv',
        'views/client_view.xml',
        'data/client_sequence.xml',
        'views/edit_sale_page.xml',
        'views/sale_order_submenu.xml',
        'views/report_sale_order.xml',
        'views/add_buton.xml',
        'views/bueguda_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'odoo-ao-partner-training/odoo15/bueguda/static/css/style.css',
        ],
    }
}
