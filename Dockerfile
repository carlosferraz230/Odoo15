FROM odoo:15.0

# Copiar módulos customizados
COPY ./my_addons /mnt/extra-addons

# Expor a porta padrão do Odoo
EXPOSE 8069

# Comando padrão do Odoo
CMD ["odoo", "--addons-path=/mnt/extra-addons"]
