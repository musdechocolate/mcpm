import argparse
from .mcp_manager import MCPManager

def main():
    parser = argparse.ArgumentParser(description="Manage Model Context Protocols (MCPs).")
    subparsers = parser.add_subparsers(dest='command')

    # List available MCPs
    list_parser = subparsers.add_parser('ls', help='List all available MCPs.')
    
    # List running MCP
    running_parser = subparsers.add_parser('ps', help='List the currently running MCP.')
    
    # Stop running server
    run_parser = subparsers.add_parser('run', help='Run a MCP server.')
    run_parser.add_argument('mcp_name', type=str, help='Name of the MCP to stop.')

    # Stop running server
    stop_parser = subparsers.add_parser('stop', help='Stop the running MCP server.')
    stop_parser.add_argument('mcp_name', type=str, help='Name of the MCP to stop.')

    # Pull server
    pull_parser = subparsers.add_parser('pull', help='Pull a server for a specific MCP.')
    pull_parser.add_argument('mcp_name', type=str, help='Name of the MCP to pull.')

    # Remove server
    remove_parser = subparsers.add_parser('rm', help='Remove a specific MCP server.')
    remove_parser.add_argument('mcp_name', type=str, help='Name of the MCP to remove.')

    # Show server
    show_parser = subparsers.add_parser('show', help='Show a specific MCP server details.')
    show_parser.add_argument('mcp_name', type=str, help='Name of the MCP to show.')

    # Search server
    search_parser = subparsers.add_parser('search', help='Search a specific MCP server.')
    search_parser.add_argument('mcp_name', type=str, help='Search term')

    args = parser.parse_args()
    manager = MCPManager()

    if args.command == 'ls':
        mcp_list = manager.list_mcps()
        print("Available MCPs:", mcp_list)
    elif args.command == 'ps':
        running_mcp = manager.get_running_mcp()
        print("Running MCP:", running_mcp)
    elif args.command == 'run':
        manager.run_mcp(args.mcp_name)
        print(f"Stopped MCP: {args.mcp_name}")
    elif args.command == 'stop':
        manager.stop_mcp(args.mcp_name)
        print(f"Stopped MCP: {args.mcp_name}")
    elif args.command == 'pull':
        manager.pull_mcp(args.mcp_name)
        print(f"Pulled MCP: {args.mcp_name}")
    elif args.command == 'rm':
        manager.remove_mcp(args.mcp_name)
        print(f"Removed MCP: {args.mcp_name}")
    elif args.command == 'reset':
        manager.remove_mcp(args.mcp_name)
        print(f"Removed MCP: {args.mcp_name}")
    elif args.command == 'show':
        manager.remove_mcp(args.mcp_name)
        print(f"Removed MCP: {args.mcp_name}")
    elif args.command == 'search':
        manager.remove_mcp(args.mcp_name)
        print(f"Removed MCP: {args.mcp_name}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()