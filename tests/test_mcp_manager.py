import unittest
from mcp_cli.mcp_manager import MCPManager

class TestMCPManager(unittest.TestCase):

    def setUp(self):
        self.manager = MCPManager()

    def test_list_mcp(self):
        mcp_list = self.manager.list_mcp()
        self.assertIsInstance(mcp_list, list)

    def test_get_running_mcp(self):
        running_mcp = self.manager.get_running_mcp()
        self.assertIsInstance(running_mcp, str)

    def test_stop_mcp(self):
        result = self.manager.stop_mcp("test_mcp")
        self.assertTrue(result)

    def test_pull_mcp(self):
        result = self.manager.pull_mcp("test_mcp")
        self.assertTrue(result)

    def test_remove_mcp(self):
        result = self.manager.remove_mcp("test_mcp")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()