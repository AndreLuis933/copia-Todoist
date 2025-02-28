import flet as ft
from flet import *


def get_margin(node, top=False, bottom=False, left=False, right=False):
    margin = get_attribute(node, "margin")

    if not margin:
        return 0

    if isinstance(margin, int):
        return sum([margin for side in [top, bottom, left, right] if side])

    sides = {"top": top, "bottom": bottom, "left": left, "right": right}

    return sum(getattr(margin, side, 0) for side, include in sides.items() if include)

def get_padding(node, top=False, bottom=False, left=False, right=False):
    padding = get_attribute(node, "padding")

    if not padding:
        return 0

    if isinstance(padding, int):
        return sum([padding for side in [top, bottom, left, right] if side])

    sides = {"top": top, "bottom": bottom, "left": left, "right": right}

    return sum(getattr(padding, side, 0) for side, include in sides.items() if include)

def get_attribute(node, attribute):
    return getattr(node, attribute, 0) or 0


def get_alignment_controls(node, horizontal=False, vertical=False):
    alignment = get_attribute(node, "alignment")

    if vertical:
        cros_alignment = get_attribute(node, "vertical_alignment")
    elif horizontal:
        cros_alignment = get_attribute(node, "horizontal_alignment")
        cros_alignment = cros_alignment or "start"
    if (
        not cros_alignment
        or cros_alignment == CrossAxisAlignment.CENTER
        or cros_alignment == "center"
    ):
        cros_alignment = 2
    if cros_alignment == CrossAxisAlignment.START or cros_alignment == "start":
        cros_alignment = 0
    if cros_alignment == CrossAxisAlignment.END or cros_alignment == "end":
        cros_alignment = 1
        
        
    if (
        
        alignment == MainAxisAlignment.CENTER
        or alignment == "center"
    ):
        alignment = 2
    elif not alignment or alignment == MainAxisAlignment.START or alignment == "start":
        alignment = 0
    elif alignment == MainAxisAlignment.END or alignment == "end":
        alignment = 1
    else:
        alignment = 1

    return cros_alignment, alignment

def get_alignment_container(node):
    aliement = get_attribute(node, "alignment")
    return aliement
    
    

def get_height(node):
    return get_attribute(node, "height")


def get_width(node):
    return get_attribute(node, "width")


def get_size(node, height):
    if height:
        return get_height(node)
    else:
        return get_width(node)


def process_container(parent, current, node, node_dim_ref):
    if isinstance(parent, Column):
        margin_element = {"top": True, "bottom": True}
        margin_transversal = {"left": True, "right": True}
        margin_node = {"right": True}
        cros_alinhamento,alinhamento = get_alignment_controls(parent, horizontal=True)
        page = node.page.window.height
        is_vertical = True
        ajuste = 40

    elif isinstance(parent, Row):
        page = node.page.window.width
        margin_element = {"left": True, "right": True}
        margin_transversal = {"top": True, "bottom": True}
        margin_node = {"top": True}
        cros_alinhamento,alinhamento = get_alignment_controls(parent, vertical=True)
        is_vertical = False
        ajuste = 16

    size_cruzado = get_size(parent, height=not is_vertical)
    offset_acumulado = -get_size(parent, height=is_vertical)
    ajuste_cruzado = 0
    spacing = getattr(parent, "spacing", 0)
    tamanho_preenchido = 0

    for elemento in parent.controls:
        if elemento == current:
            break
        offset_acumulado += spacing
        offset_acumulado += get_size(elemento, height=is_vertical) + get_margin(
            elemento, **margin_element
        )
    
    for elemento in parent.controls:    
        tamanho_preenchido += spacing
        tamanho_preenchido += get_size(elemento, height=is_vertical) + get_margin(
            elemento, **margin_element
        )

    tamanhos_transversais = [
        get_size(e, height=not is_vertical) + get_margin(e, **margin_transversal)
        for e in parent.controls
    ]
    tamanho_max_transversal = max(tamanhos_transversais) - get_margin(
        node, **margin_node
    )
    if size_cruzado:
        tamanho_max_transversal = size_cruzado
        node_dim_ref += get_margin(node, **margin_node)

    if cros_alinhamento:
        ajuste_cruzado = (tamanho_max_transversal - node_dim_ref) / cros_alinhamento

    if alinhamento:
        if page>tamanho_preenchido:
            offset_acumulado += (page-tamanho_preenchido + spacing - ajuste)/alinhamento 
            
    if tamanho_max_transversal == node_dim_ref:
        ajuste_cruzado = 0
        
    ajuste_cruzado -= size_cruzado
    return offset_acumulado, ajuste_cruzado 


def get_element_position(node):
    """Soma valores no caminho da raiz até um nó específico"""
    node_height = get_height(node) + get_margin(node, bottom=True)
    height = -node_height
    node_width = get_width(node) + get_margin(node, right=True)
    width = -node_width
    current = node
    com_alinhamento =[]
    while True:
        parent = current.parent
        if not parent:
            break
        if isinstance(parent, Column):

            incremento = process_container(parent, current, node, node_width)
            height += incremento[0]
            width += incremento[1]

        elif isinstance(parent, Row):
            incremento = process_container(parent, current, node, node_height)
            height += incremento[1] 
            width += incremento[0]
        elif isinstance(parent, Container):
            height -= get_height(parent) + get_margin(parent, top=True, bottom=True)-get_padding(parent, top=True)
            width -= get_width(parent) + get_margin(parent, left=True, right=True)-get_padding(parent, left=True)
            alignmene= get_alignment_container(parent)
            if alignmene:
                
                com_alinhamento.append([get_width(parent), get_height(parent),alignmene,get_margin(parent, left=True, right=True)])
                #print((1+ alignmene.x))
                #print((1+ alignmene.y))
                #width+=(get_width(parent)/2) * (1+ alignmene.x)
                #height+=(get_height(parent)/2) * (1+ alignmene.y)
                
            
        elif isinstance(current, Stack):
            current = parent
            continue

        height += get_height(current) + get_margin(current, top=True, bottom=True)
        width += get_width(current) + get_margin(current, left=True, right=True)
        current = parent
        #print(height)

    #print(com_alinhamento)
    def calcular_posicao_top_left(containers):
        inverso_containers =list(reversed(containers))
        interno_x = 0
        interno_y = 0
        if len(inverso_containers) == 1:
            largura, altura, alin = inverso_containers[0]
            interno_x = (largura / 2) * (1 + alin.x)
            interno_y = (altura / 2) * (1 + alin.y)
        for atual, proximo in zip(inverso_containers, inverso_containers[1:]):
            largura, altura, alin = atual
            centro_x = (largura / 2) * (1 + alin.x)
            centro_y = (altura / 2) * (1 + alin.y)
            
            if not proximo is None:
                interno_00x = (centro_x - (proximo[0] / 2)) if (centro_x - (proximo[0] / 2)) > 0 else 0
                interno_00y= (centro_y - (proximo[1] / 2)) if (centro_y - (proximo[1] / 2)) > 0 else 0
                if largura - centro_x < proximo[0]:
                    interno_00x = centro_x - proximo[0]
                if altura - centro_y < proximo[1]:
                    centro_y -= proximo[1]
                    interno_00y = centro_y
                    
                interno_x += interno_00x + ((proximo[0] / 2) * (1+proximo[2].x))
                interno_y +=  interno_00y + ((proximo[1] / 2) * (1+proximo[2].y))
                if interno_x < 0:
                    interno_x = 0
                elif interno_x > largura:
                    interno_x = largura
                if interno_y <0:
                    interno_y = 0
                elif interno_y > altura:
                    interno_y = altura
            
        return interno_x,interno_y
    
    incremento = calcular_posicao_top_left(com_alinhamento)
    width += incremento[0]
    height += incremento[1]
    
    return height , width
