{
    "name": "Sistema de Gestão de Transporte",
    "author": "Carlos Ferraz, Olualinet",
    "version": "15.0.1.0.0",
    "category": "Service",
    "summary": "Gestão de Mercadoria",
    "description": " É um ERP de logística que usa a "
                   "tecnologia para ajudar as empresas a planejar, "
                   "executar e otimizar a movimentação de mercadorias, "
                   "garantindo conformidade, documentação e"
                   " visibilidade de toda a operação",
    "depends": ["base", "sale", "sale_management"],
    "data": [
        'security/ir.model.access.csv',
        "views/driver_view.xml",
        "views/fleet_view.xml",
        "views/route_view.xml",
        "views/trip_price_view.xml",
        "views/language_switcher_templates.xml",
        "views/main_menu_view.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "transport_management_system/static/src/js/language_switcher.js",
            'transport_management_system/static/src/css/style.css',
        ],
    },
    "installable": True,
    "application": False,
}
