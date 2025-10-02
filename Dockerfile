FROM odoo:15.0

USER root

# Copia módulos
COPY ./odoo15 /mnt/extra-addons

# Copia o ficheiro de configuração
COPY ./odoo.conf /etc/odoo/odoo.conf

RUN chown odoo:odoo /etc/odoo/odoo.conf

USER odoo

