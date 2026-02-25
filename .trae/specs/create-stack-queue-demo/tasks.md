# Tasks

- [x] Task 1: 项目初始化与依赖配置
  - [x] SubTask 1.1: 使用 uv init 初始化项目
  - [x] SubTask 1.2: 配置 pyproject.toml，添加 PyQt6、json5、pyinstaller 依赖
  - [x] SubTask 1.3: 创建项目目录结构（src、data）

- [x] Task 2: 数据模型与持久化模块
  - [x] SubTask 2.1: 创建 StackItem 和 QueueItem 数据类，包含文字、入栈/入队时间戳、出栈/出队时间戳属性
  - [x] SubTask 2.2: 实现 json5 数据持久化模块，支持保存和加载
  - [x] SubTask 2.3: 实现历史记录管理，保存已出栈/出队的数据

- [x] Task 3: 主窗口框架
  - [x] SubTask 3.1: 创建主窗口类，设置窗口标题、图标、初始大小
  - [x] SubTask 3.2: 实现窗口拖动、缩放、最小化、关闭功能
  - [x] SubTask 3.3: 设置中文字体（微软雅黑）和字号

- [x] Task 4: Stack 可视化组件
  - [x] SubTask 4.1: 创建 Stack 可视化组件，垂直布局，入栈在上
  - [x] SubTask 4.2: 实现格子组件，支持文字显示、自动换行、编辑
  - [x] SubTask 4.3: 实现入栈按钮和对话框
  - [x] SubTask 4.4: 实现出栈按钮和功能
  - [x] SubTask 4.5: 实现 hover 显示入栈时间戳

- [x] Task 5: Queue 可视化组件
  - [x] SubTask 5.1: 创建 Queue 可视化组件，水平布局，右进左出
  - [x] SubTask 5.2: 复用格子组件，支持文字显示、自动换行、编辑
  - [x] SubTask 5.3: 实现入队按钮和对话框
  - [x] SubTask 5.4: 实现出队按钮和功能
  - [x] SubTask 5.5: 实现 hover 显示入队时间戳

- [x] Task 6: 布局整合
  - [x] SubTask 6.1: 将 Stack 和 Queue 组件整合到主窗口
  - [x] SubTask 6.2: 实现响应式布局，窗口缩放时组件自适应

- [x] Task 7: 数据持久化集成
  - [x] SubTask 7.1: 在入栈/入队、出栈/出队、编辑操作时触发数据保存
  - [x] SubTask 7.2: 程序启动时加载历史数据

- [x] Task 8: EXE 打包配置
  - [x] SubTask 8.1: 创建 PyInstaller 打包脚本
  - [x] SubTask 8.2: 测试打包后的 exe 文件运行

# Task Dependencies
- [Task 2] depends on [Task 1]
- [Task 3] depends on [Task 1]
- [Task 4] depends on [Task 2, Task 3]
- [Task 5] depends on [Task 2, Task 3]
- [Task 6] depends on [Task 4, Task 5]
- [Task 7] depends on [Task 2, Task 6]
- [Task 8] depends on [Task 7]
