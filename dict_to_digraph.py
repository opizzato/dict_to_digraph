import re
from collections.abc import Iterable
import graphviz


def dict_to_digraph(input_dict, params):

    edges = dict_to_edges(input_dict, params)

    dot = graphviz.Digraph(
        format=params.get('format', 'svg'),
        graph_attr=params.get('graph_attr', {}),
    )
    for s,d in edges:
        labels = [text_to_label(t, params) for t in [s,d]]
        dot.edge(*labels)

    nodes = list(set([n for n,_ in edges] + [n for _,n in edges]))
    for n in nodes:
        attr = node_to_attr(n, params)
        label = text_to_label(n, params)
        dot.node(label, **attr)

    return dot


def text_to_label(text, params):

    for t in params.get('text_transforms', []):
        text = t(text)

    return text

def node_to_attr(node, params):

    attr = {}
    for regexp, a in params.get('node_attrs', []):
        if re.match(regexp, node):
            attr.update(a)

    return attr


def key_value_to_sources(k, v, params):

    sources = []

    for fk in params.get('edge_keys', []):

        if isinstance(fk, str):
            if re.match(fk, k):
                if isinstance(v, str):
                    sources.append(v)

        if isinstance(fk, dict):
            for dfk, fks in fk.items():
                if re.match(dfk, k):
                    if isinstance(v, dict):
                        for fk in fks:
                            for sk,sv in v.items():
                                if re.match(fk, sk):
                                    if isinstance(sv, str):
                                        sources.append(sv)
                    if isinstance(v, Iterable):
                        for vv in v:
                            if isinstance(vv, dict):
                                for fk in fks:
                                    for sk,sv in vv.items():
                                        if re.match(fk, sk):
                                            if isinstance(sv, str):
                                                sources.append(sv)
    return sources


def dict_to_edges(d, params):

    edges = []
    if isinstance(d, dict):
        for k,v in d.items():
            if isinstance(v, dict):
                for vk, vv in v.items():
                    sources = key_value_to_sources(vk, vv, params)
                    for s in sources:
                        edges.append([s,k])

    return edges
