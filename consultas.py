from typing import Dict, List, Optional, Any, Union


def listar_acervo(acervo: List[Dict[str, Any]]) -> List[Dict[str, Any]]:

    return acervo

def buscar_por_codigo(acervo: List[Dict[str, Any]], codigo: Union[str, int]) -> Optional[Dict[str, Any]]:

    codigo_busca = str(codigo).strip()
    for livro in acervo:
        if str(livro.get("codigo", "")).strip() == codigo_busca:
            return livro
    return None

def buscar_por_titulo_completo(acervo: List[Dict[str, Any]], titulo: str) -> Optional[Dict[str, Any]]:

    titulo_busca = titulo.strip().lower()
    for livro in acervo:
        if str(livro.get("titulo", "")).strip().lower() == titulo_busca:
            return livro
    return None
def buscar_por_titulo_parcia():
    pass

def filtrar_por_categoria():
    pass

def filtrar_por_disponibilidade():
    pass

def consultar_acervo():
    pass


