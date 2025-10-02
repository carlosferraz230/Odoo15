FROM odoo:15.0

USER root
RUN mkdir -p /mnt/extra-addons && chown -R odoo:odoo /mnt/extra-addons
COPY ./transport_management_system /mnt/extra-addons/transport_management_system
USER odoo

