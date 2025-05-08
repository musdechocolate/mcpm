import unittest
from mcp_cli.cli import list_available_mcps, get_running_mcp, stop_running_mcp, pull_mcp, remove_mcp

class TestMCPCLI(unittest.TestCase):

    def test_list_available_mcps(self):
        mcps = list_available_mcps()
        self.assertIsInstance(mcps, list)

    def test_get_running_mcp(self):
        running_mcp = get_running_mcp()
        self.assertIsInstance(running_mcp, str)

    def test_stop_running_mcp(self):
        result = stop_running_mcp()
        self.assertTrue(result)

    def test_pull_mcp(self):
        result = pull_mcp('example_mcp')
        self.assertTrue(result)

    def test_remove_mcp(self):
        result = remove_mcp('example_mcp')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()