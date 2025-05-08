import sqlite3
import json
import os

class MCPManager:
    def __init__(self):
        mcpm_folder = os.path.expanduser("~/.mcpm")
        if not os.path.exists(mcpm_folder):
            os.makedirs(mcpm_folder)

        # Create the SQLite database
        self.db_path = os.path.join(mcpm_folder, "mcpm.db")
        if not os.path.exists(self.db_path):
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            # Example table creation (customize as needed)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS mcps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    settings TEXT NOT NULL
                )
            """)
            conn.commit()
            conn.close()
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.running_mcp = None

    def list_mcps(self):
        self.cursor.execute("SELECT name FROM mcps")
        return [row[0] for row in self.cursor.fetchall()]

    def get_running_mcp(self):
        return self.running_mcp

    def stop_mcp(self):
        if self.running_mcp:
            self.running_mcp = None
            return True
        return False

    def pull_mcp(self, mcp_name):
        mcp_setting = {
            "mcp": {
                "inputs": [
                    {
                        "type": "promptString",
                        "id": "brave_api_key",
                        "description": "Brave Search API Key",
                        "password": True
                    }
                ],
                "servers": {
                    "brave-search": {
                        "command": "npx",
                        "args": ["-y", "@modelcontextprotocol/server-brave-search"],
                        "env": {
                            "BRAVE_API_KEY": "${input:brave_api_key}"
                        }
                    }
                }
            }
        }
        try:
            self.add_mcp(mcp_name, json.dumps(mcp_setting))
        except Exception as e:
            print(f"Error adding MCP: {e}")
        pass

    def remove_mcp(self, mcp_name):
        try:
            self.cursor.execute("DELETE FROM mcps WHERE name=?", (mcp_name,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def add_mcp(self, mcp_name, mcp_setting):
        try:
            self.cursor.execute(
                "INSERT INTO mcps (name, settings) VALUES (?, ?)", 
                (mcp_name, mcp_setting))
            self.conn.commit()
            self.mcp_list = self.load_mcps()
            return True
        except sqlite3.IntegrityError:
            print(f"MCP with name '{mcp_name}' already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False

    def run_mcp(self, mcp_name):
        try:
            self.cursor.execute("SELECT * FROM mcps WHERE name=?", (mcp_name,))
            mcp = self.cursor.fetchone()
            if mcp:
                self.running_mcp = mcp
                try:
                    mcp_data = list(mcp)
                    mcp_data[2] = json.loads(mcp_data[2]) 
                    print(tuple(mcp_data))
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    return None
            else:
                print(f"No MCP found with name '{mcp_name}'.")
                return None
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return None