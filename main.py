from fastmcp import FastMCP
import socket
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 创建 FastMCP 实例
mcp = FastMCP("python-mcp-tools")

@mcp.tool("get_weather", description="获取天气信息")
def get_weather(string: str) -> str:
    """获取天气信息"""
    return "今天天气是晴天"

@mcp.tool("get_bbw_info", description="获取布布威相关信息")
def get_bbw_info(string: str) -> str:
    """获取布布威相关信息"""
    return "布布威会吃巴比馒头" + string

if __name__ == "__main__":
    # 打印所有注册的工具
    logging.info("已注册的工具列表:")
    # 使用 dir() 来查看所有可用的工具
    tools = [attr for attr in dir(mcp) if not attr.startswith('_')]
    logging.info(f"可用工具: {tools}")
    
    print("启动 MCP 服务器...")
    mcp.run(transport="sse")