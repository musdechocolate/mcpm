# MCPM

MCPM is a command-line application for managing Model Context Protocols (MCPs) on your machine. This tool allows you to easily list available MCPs, check which one is currently running, stop a running server, pull a server, and remove a server.

## Features

- List all available MCPs on the machine.
- Display the currently running MCP.
- Stop a running MCP server.
- Pull a specified MCP server.
- Remove a specified MCP server.

## Installation

You can install MCPM using pip. Run the following command:

```
pip install mcpm
```

## Usage

After installation, you can use the following commands:

- **List available MCPs:**
  ```
  mcpm list
  ```

- **Show running MCP:**
  ```
  mcpm running
  ```

- **Stop running MCP:**
  ```
  mcpm stop
  ```

- **Pull MCP:**
  ```
  mcpm pull <mcp_name>
  ```

- **Remove MCP:**
  ```
  mcpm remove <mcp_name>
  ```

## Contributing

If you would like to contribute to MCPM, please fork the repository and submit a pull request. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.