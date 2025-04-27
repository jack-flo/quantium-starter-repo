import pytest
from dash.testing.application_runners import import_app


def test_header_graph_region_picker(dash_duo):
    # Start server on dash_duo#
    app = import_app('dashApp')
    dash_duo.start_server(app)

    # Check header
    header = dash_duo.find_element('h1')
    assert header.text == 'Pink Morsel Sales By Region', 'Expected main H1 header text to match'

    # Check graph is present
    graphWrapper = dash_duo.find_element('#sales-graph .js-plotly-plot')
    assert graphWrapper is not None, 'Expected to find the Plotly graph'

    # Check radio items (region picker) are present
    regionPicker = dash_duo.find_element('#radio-options')
    assert regionPicker is not None, 'Expected to find the region picker'
