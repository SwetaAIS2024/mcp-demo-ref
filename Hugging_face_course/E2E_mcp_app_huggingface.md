# From the huggingface MCP tutorial


### Link : https://huggingface.co/learn/mcp-course/en/unit2/introduction

- In this unit, you will:

    -    Create an MCP Server using Gradio’s built-in MCP support
    -    Build a sentiment analysis tool that can be used by AI models
    -    Connect to the server using different client implementations:
           1. A HuggingFace.js-based client
           2. A SmolAgents-based client for Python
    -    Deploy your MCP Server to Hugging Face Spaces
    -    Test and debug the complete system


#### Server Side

-    Uses Gradio to create a web interface and MCP server via gr.Interface
-    Implements a sentiment analysis tool using TextBlob
-    Exposes the tool through both HTTP and MCP protocols

#### Client Side

-    Implements a HuggingFace.js client
-    Or, creates a smolagents Python client
-    Demonstrates how to use the same server with different client implementations

#### Deployment

-    Deploys the server to Hugging Face Spaces
-    Configures the clients to work with the deployed serve


### Understanding the Code

- Let’s break down the key components:

    - Function Definition:
    -    The sentiment_analysis function takes a text input and returns a dictionary
    -    It uses TextBlob to analyze the sentiment
    -    The docstring is crucial as it helps Gradio generate the MCP tool schema
    -    Type hints (str and dict) help define the input/output schema

    - Gradio Interface:
    -    gr.Interface creates both the web UI and MCP server
    -    The function is exposed as an MCP tool automatically
    -    Input and output components define the tool’s schema
    -    The JSON output component ensures proper serialization

    - MCP Server:
    -    Setting mcp_server=True enables the MCP server
    -    The server will be available at http://localhost:7860/gradio_api/mcp/sse
    -    You can also enable it using the environment variable:

        - export GRADIO_MCP_SERVER=True

### Testing the Server

- You can test the server in two ways:

    - Web Interface:
    -    Open http://localhost:7860 in your browser
    -    Enter some text and click “Submit”
    -    You should see the sentiment analysis results

    - MCP Schema:
    -    Visit http://localhost:7860/gradio_api/mcp/schema
    -    This shows the MCP tool schema that clients will use
    -    You can also find this in the “View API” link in the footer of your Gradio app