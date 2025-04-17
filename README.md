# MCP Server Demo

这是一个基于MCP (Minecraft Protocol) 官方示例的服务器演示。
This is a server demonstration based on the official MCP (Minecraft Protocol) example.

## 环境设置 (Environment Setup)

1. 创建虚拟环境 (Create virtual environment):
```bash
python -m venv venv
```

2. 激活虚拟环境 (Activate virtual environment):
```bash
# Windows
.\venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. 安装依赖 (Install dependencies):
```bash
pip install -r requirements.txt
```

## 运行服务器 (Run Server)
```bash
python main.py
```

## 功能说明 (Features)
- 基于MCP官方示例实现 (Based on official MCP example)
- 支持资源列表接口 (Supports resource listing interface)
- 使用异步IO处理 (Uses async I/O processing)
- 标准输入输出通信 (Standard I/O communication)

## 代码结构 (Code Structure)
- `app = Server("example-server")`: 创建MCP服务器实例
- `@app.list_resources()`: 定义资源列表接口
- `stdio_server()`: 处理标准输入输出流
- `asyncio.run(main())`: 异步运行主函数

## 注意事项 (Notes)
- 这是一个基础实现，可以根据需要扩展功能
- 使用异步编程模式，确保高性能
- 可以通过添加更多装饰器来扩展功能

## 连接到服务器 (Connect to Server)
1. 启动Minecraft
2. 选择多人游戏 (Multiplayer)
3. 添加服务器 (Add Server)
4. 服务器地址: localhost:25565

注意：服务器运行在离线模式，不需要正版验证。
Note: The server runs in offline mode, no premium account required. 