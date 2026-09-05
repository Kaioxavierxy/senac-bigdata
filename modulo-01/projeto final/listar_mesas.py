mesas_sistema = [  
    {"numero_mesa": 1, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 2, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 3, "capacidade": 2, "status": "livre"},  
    {"numero_mesa": 4, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 5, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 6, "capacidade": 4, "status": "livre"},  
    {"numero_mesa": 7, "capacidade": 8, "status": "livre"},  
    {"numero_mesa": 8, "capacidade": 8, "status": "livre"},  
    {"numero_mesa": 9, "capacidade": 8, "status": "livre"},  
]  
  
def listar_mesas(mesas=None):  
    if mesas is None:  
        mesas = mesas_sistema  

    if not isinstance(mesas, list):  
        print("Erro! O valor passado não é uma lista.")  
        return []  
  
    if not mesas:  
        print("Nenhuma mesa cadastrada no sistema.")  
        return []  
        
    print("\n======================================")  
    print("          SISTEMA DE MESAS")  
    print("======================================")  
    print(f"Total de mesas: {len(mesas)}")  
  
    print("\n--- TODAS AS MESAS ---")  
  
    for mesa in mesas:  
        print(  
            f"Mesa {mesa['numero_mesa']} | "  
            f"Capacidade: {mesa['capacidade']} | "  
            f"Status: {mesa['status']}"  
        )  
  
    ## o alterar_status_mesa() precisa continuar conseguindo enxergar a mesa 1, mesmo ela estando indisponível.  
    return mesas 
 
mesas_no_sistema = listar_mesas()