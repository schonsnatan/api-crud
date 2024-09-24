from typing import Union, Dict


GenericSchema = Dict[str, Union[str, float, int]]


CompraSchema: GenericSchema = {
    "ean" : int,
    "price" : float,
    "store" : int,
    "dateTime" : str
}

'''
- GenericSchema define um dicionário onde as chaves são strings, e os valores podem ser str, float ou int.
- CompraSchema é um exemplo específico de um dicionário que segue a estrutura do GenericSchema, mapeando chaves como "ean", "price", "store" e "dateTime" para tipos específicos (int, float, int, str respectivamente).
- Este tipo de estrutura é útil para garantir consistência nos tipos de dados em um código Python, especialmente em projetos que utilizam APIs ou outras formas de validação de dados estruturados.
'''