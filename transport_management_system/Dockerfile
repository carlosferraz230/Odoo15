FROM odoo:16.0

# Cria diretório para módulos customizados
USER root
RUN mkdir -p /mnt/extra-addons && chown -R odoo:odoo /mnt/extra-addons

# Copia seus módulos customizados para dentro do container
COPY ./addons /mnt/extra-addons

USER odoo
