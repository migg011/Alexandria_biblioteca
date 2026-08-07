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
def buscar_por_titulo_parcial(acervo: List[Dict[str, Any]], termo: str) -> List[Dict[str, Any]]:

    termo_busca = termo.strip().lower()
    if not termo_busca:
        return []
    return [
        livro for livro in acervo
        if termo_busca in str(livro.get("titulo", "")).lower()
    ]

def filtrar_por_categoria(acervo: List[Dict[str, Any]], categoria: str) -> List[Dict[str, Any]]:

    categoria_busca = categoria.strip().lower()
    return [
        livro for livro in acervo
        if str(livro.get("categoria", "")).strip().lower() == categoria_busca
    ]

def filtrar_por_disponibilidade(acervo: List[Dict[str, Any]], apenas_disponiveis: bool = True) -> List[Dict[str, Any]]:

    return [
        livro for livro in acervo
        if (livro.get("disponivel", False) and livro.get("quantidade", 0) > 0) == apenas_disponiveis
    ]

def consultar_acervo(
    acervo: List[Dict[str, Any]],
    termo_titulo: Optional[str] = None,
    autor: Optional[str] = None,
    categoria: Optional[str] = None,
    disponivel: Optional[bool] = None
) -> List[Dict[str, Any]]:
    resultados = acervo.copy()

    if termo_titulo:
        termo = termo_titulo.strip().lower()
        resultados = [l for l in resultados if termo in str(l.get("titulo", "")).lower()]

    if autor:
        termo_autor = autor.strip().lower()
        resultados = [l for l in resultados if termo_autor in str(l.get("autor", "")).lower()]

    if categoria:
        cat = categoria.strip().lower()
        resultados = [l for l in resultados if str(l.get("categoria", "")).strip().lower() == cat]

    if disponivel is not None:
        resultados = [
            l for l in resultados
            if (l.get("disponivel", False) and l.get("quantidade", 0) > 0) == disponivel
        ]

    return resultados


