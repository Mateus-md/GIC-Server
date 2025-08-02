# (c) 2025 Mateus M. & Magnus S.
#-- SOBRE ----------------------------------------------------------------
'''

    Este script contem a função utilizada para tranformar os dados de
    requisições em um formato utilizado pelo sistema.

'''
#-- FUNÇÃO PRINCIPAL -----------------------------------------------------
def cnvFormat(payload:str, delimiter = ";") -> dict:
    ''' Converte o payload (str) em um dicionário.

    Os valores do payload devem ser separados pelo ```delimiter```
    Cada iten deve ser separado por um ":"

    Ex.: payload = "Key1:Value1;Key2:Value2"

    Args:
      payload [Obrigatório]: Uma str dos valores de um dict em texto
      delimiter [Opcional]:  Um separador dos itens. Por padrão é ";"

    Returns:
      out: Um dicionário que separa cada valor do payload devidamente

    Raises:
      TypeError: Caso o texto não seja convertido para lista.

    '''
    payload = str(payload)
    items = [item.split(":") for item in payload.split(delimiter)]

    if type(items) is not list:
      print("\33[31mUm erro ocorreu durante a formatação dos dados!\33[0m")
      raise TypeError

    return {key:value for (key,value) in items}
#-------------------------------------------------------------------------
