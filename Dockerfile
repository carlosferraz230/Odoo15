# Usa a imagem oficial do Odoo 15
FROM odoo:15.0

# Copiar os módulos customizados do seu repositório
COPY ./Odoo15 /mnt/extra-addons

# Expor a porta padrão do Odoo
EXPOSE 8069

# Comando para iniciar o Odoo com o caminho dos addons
CMD ["odoo", "--addons-path=/mnt/extra-addons"]

