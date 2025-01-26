import re

# Exemplo de padrão de CNPJ para validação
cnpj = "12.345.678/0001-95"
if re.match(r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}", cnpj):
    print("CNPJ válido!")
