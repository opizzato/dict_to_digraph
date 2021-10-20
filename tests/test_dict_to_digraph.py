from dict_to_digraph.dict_to_digraph import *
import pytest


@pytest.fixture
def params():
    return {
        'edge_keys': ['tables', {'union.*': ['table']}, {'tables': ['table']}],
        'text_transforms': [lambda t: t.replace('.', '\n')],
        'node_attrs': [
            ['bx.*', {'shape': 'box'}],
            ['.*fl', {'style': 'filled'}],
        ]
    }

@pytest.mark.parametrize("test_input,expected", [
    [{'a': {'tables': 'b'}}, [['b','a']]],
    [{'a': {'union*': ({'table': 'b'})}}, [['b','a']]],
    [{'a': {'union*': ({'table': 'b'}, {'table': 'c'})}}, [['b','a'], ['c','a']]],
])
def test_edges(params, test_input, expected):

    assert dict_to_edges(test_input, params) == expected


@pytest.mark.parametrize("test_input,expected", [
    ['a.a', 'a\na'],
])
def test_labels(params, test_input, expected):

    assert text_to_label(test_input, params) == expected


@pytest.mark.parametrize("test_input,expected", [
    ['a', {}],
    ['bx', {'shape': 'box'}],
    ['bx.fl', {'shape': 'box', 'style': 'filled'}],
])
def test_nodes(params, test_input, expected):

    assert node_to_attr(test_input, params) == expected
