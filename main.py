import xmltodict
import os
import pandas as pd
def get_infos(name_file, valores):
    print(f'Informações do arquivo: {name_file}')
    with open(f'nfs/{name_file}', "rb") as file_xml:
        dict_file = xmltodict.parse(file_xml)
        if "NFe" in dict_file:
            info_nf = dict_file["NFe"]["infNFe"]
        else:
            info_nf = dict_file["nfeProc"]["NFe"]["infNFe"]
        numero_nota = info_nf["@Id"]
        empresa_emisora = info_nf["emit"]["xNome"]
        nome_cliente = info_nf["dest"]["xNome"]
        endereco = info_nf["dest"]["enderDest"]
        if "vol" in info_nf["transp"]:
            peso = info_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado"
        valores.append([numero_nota, empresa_emisora, nome_cliente, endereco, peso])

files = os.listdir("nfs")

colunas = ["numero_nota", "empresa_emissora", "nome_cliente", "endereço", "peso"]
valores = []

for file in files:
    get_infos(file, valores)

tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)
