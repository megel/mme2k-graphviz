import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Import the Digraph class from the graphviz library
from graphviz import Digraph

# Set default values for the rendering engine and output format
default_engine = 'dot'
default_format = 'svg'

### Add flask to host my micros service
from flask import Flask, request, Response, make_response
app = Flask(__name__)

# Get the right HTTP content type by the given Graphviz output format
def get_content_type(format):
    """
    Given a Graphviz output format, return the corresponding HTTP content type.
    """
    content_types = {
        'svg': 'image/svg+xml',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'ps': 'application/postscript',
        'dot': 'text/plain',
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'tif': 'image/tiff',
        'tiff': 'image/tiff',
        'bmp': 'image/bmp',
        'ico': 'image/vnd.microsoft.icon',
        'ppm': 'image/x-portable-pixmap',
        'pgm': 'image/x-portable-graymap',
        'pbm': 'image/x-portable-bitmap',
    }
    return content_types.get(format, 'text/plain')

# Define a function to create the HTTP response
def create_response(graph, format=default_format, engine=default_engine):
    # Create a Digraph object with the given format and engine
    d = Digraph(format=format, engine=engine)
    
    # If a graph is provided, add it to the Digraph object
    if graph:
        d.body.append(graph)
    # Otherwise, add a default node with the label "GraphViz"
    else:    
        d.body.append("""node [label="GraphViz"]""")

    content_type = get_content_type(format=format)
    
    # Return the rendered graph in the specified output format
    rendered_graph = d.pipe()
    return Response(status=200, response=rendered_graph, headers={"Content-Type": f"{content_type}"})

# Define a route to provide information on how to use the API
@app.route("/info", methods=['GET'])
def info():
    return Response(status=200, response="MMe2k Render Graph with Graphviz\n\nPlease POST a graph to /render\n\nSupported formats: svg, png\n\nSupported engines: dot, neato, twopi, circo, fdp, sfdp, patchwork, osage, gvpr, acyclic, toon \n\nMore Information: https://graphviz.org/")

# Define a route to receive the graph and return the rendered graph
@app.route("/render", methods=['POST'])
def render_graph():
    try:
        logging.info(f"REQUEST: {request}")
    except:
        logging.info(f"no event")
    
    # Get the headers and query parameters from the request
    request_headers = request.headers
    queryParameters = request.args
    format = queryParameters['format'] if 'format' in queryParameters else default_format
    engine = queryParameters['engine'] if 'engine' in queryParameters else default_engine
    
    logging.info(f"Graph content: {request_headers.get('Content-Type')}")
    # If the content type is text/plain, read the graph from the request body
    if f"{request_headers.get('Content-Type')}".lower().startswith("text/plain"):
        graph = request.get_data(as_text=True)

        return create_response(graph=graph, format=format, engine=engine)
    else:
        # If the content type is not text/plain, return an error response
        return Response(status=400, response="Unsupported content type")

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(debug=True, host='0.0.0.0', port=port)