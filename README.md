# Research Assistant MCP

An intelligent research assistant built with Model Context Protocol (MCP) that combines web scraping capabilities with vector database storage for comprehensive research workflows.

## Features

### 🔍 **Web Research & Scraping**
- **Firecrawl Integration**: Advanced web scraping using Firecrawl MCP server
- **Content Extraction**: Intelligent extraction of structured content from web pages
- **Multi-source Research**: Scrape and analyze multiple websites efficiently

### 🗃️ **Knowledge Management**
- **Vector Database Storage**: Powered by ChromaDB for semantic search
- **Topic Organization**: Organize research by topics with separate vector databases
- **Duplicate Detection**: Automatic content deduplication using MD5 hashing
- **Semantic Search**: Find relevant information using similarity search

### 🤖 **AI-Powered Assistant**
- **LangGraph Integration**: Sophisticated conversation flow management
- **Tool Integration**: Seamless access to research and storage tools
- **Ollama LLM**: Local language model support (Qwen3)
- **Memory Persistence**: Conversation history and context retention

## Architecture

The system consists of two main components:

### Server Component (`server.py`)
- **MCP Server**: FastMCP-based server exposing research tools
- **ChromaDB Integration**: Vector storage with Ollama embeddings
- **Research Tools**:
  - `save_research_data()`: Store content in topic-specific databases
  - `search_research_data()`: Semantic search across stored research
  - `list_research_topics()`: View all research topics
  - `delete_research_topic()`: Remove topics and data
  - `get_topic_info()`: Detailed topic information

### Client Component (`client.py`)
- **LangGraph Agent**: Orchestrates research workflows
- **Multi-Server MCP Client**: Connects to research and Firecrawl servers
- **Interactive Interface**: Command-line research assistant
- **Tool Binding**: Automatic tool discovery and integration

## Installation

### Prerequisites
- Python 3.8+
- [Ollama](https://ollama.ai/) running locally
- [Firecrawl API Key](https://firecrawl.dev/)
- Node.js (for Firecrawl MCP server)

### Setup

1. **Install Dependencies**:
```bash
uv add chromadb langchain-chroma langchain-ollama
pip install langchain langgraph langchain-mcp-adapters python-dotenv
```

2. **Configure Ollama Models**:
```bash
ollama pull qwen3
ollama pull nomic-embed-text
```

3. **Environment Configuration**:
Create a `.env` file:
```env
FIRECRAWL_API_KEY=your_firecrawl_api_key_here
```

4. **MCP Configuration**:
Update `mcp.json` paths to match your system:
```json
{
    "research_server": {
        "command": "uv",
        "args": ["--directory", "/path/to/your/project", "run", "server.py"],
        "transport": "stdio"
    },
    "firecrawl_server": {
        "command": "npx",
        "args": ["-y", "firecrawl-mcp"],
        "transport": "stdio"
    }
}
```

## Usage

### Starting the Research Assistant

```bash
python client.py
```

### Available Commands

#### Research Operations
- `"Research the latest developments in AI agents"`
- `"Scrape https://example.com and save key insights"`
- `"Search my previous research on machine learning"`

#### Knowledge Management
- `"Save this research to topic: ai_agents"`
- `"What topics have I researched?"`
- `"Show me information about topic: machine_learning"`
- `"Delete topic: outdated_research"`

### Example Workflow

1. **Web Research**: Ask the assistant to research a topic
2. **Content Scraping**: URLs are automatically scraped using Firecrawl
3. **Knowledge Storage**: Important findings are saved to topic-specific databases
4. **Information Retrieval**: Search through accumulated research using semantic queries

## Technical Details

### Vector Database Structure
- **Storage Location**: `./research_chroma_dbs/`
- **Organization**: Separate ChromaDB collection per topic
- **Embeddings**: Ollama `nomic-embed-text` model
- **Metadata**: Content hashing for deduplication

### MCP Server Tools
```python
# Research data management
save_research_data(content: List[str], topic: str = "default") -> str
search_research_data(query: str, topic: str = "default", max_results: int = 5) -> str

# Topic management
list_research_topics() -> str
get_topic_info(topic: str) -> str
delete_research_topic(topic: str) -> str
```

### LangGraph Agent Flow
1. **User Input** → Chat Node
2. **Tool Selection** → Conditional routing
3. **Tool Execution** → Research/Storage operations
4. **Response Generation** → Formatted results

## Configuration Options

### Ollama Settings
- **Base URL**: `http://localhost:11434`
- **Chat Model**: `qwen3` (configurable)
- **Embedding Model**: `nomic-embed-text`

### ChromaDB Settings
- **Persistence**: Local directory storage
- **Collection Naming**: `research_{topic}`
- **Similarity Metric**: Cosine similarity

## Troubleshooting

### Common Issues
1. **Ollama Connection**: Ensure Ollama is running on port 11434
2. **Firecrawl API**: Verify API key is set in environment
3. **Path Configuration**: Update `mcp.json` with correct project paths
4. **Dependencies**: Install all required packages with correct versions

### Error Messages
- `"No research data found for topic"`: Topic database doesn't exist
- `"Error saving research data"`: Check ChromaDB permissions
- `"Failed to start research assistant"`: Verify MCP server configuration

## Contributing

This research assistant demonstrates advanced MCP integration patterns:
- Multi-server MCP client architecture
- Vector database integration with MCP tools
- LangGraph agent orchestration
- Semantic search and knowledge management

## License

This project is part of an MCP tutorial series demonstrating research assistant capabilities with modern AI tooling.