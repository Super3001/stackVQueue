# Stack & Queue 演示程序 Spec

## Why
需要一个可视化的 Stack（栈）和 Queue（队列）数据结构演示程序，帮助理解这两种数据结构的工作原理，同时具备数据持久化和桌面端组件特性。

## What Changes
- 创建 Python 项目，使用 uv 包管理
- 实现 PyQt5 图形化界面
- 实现 Stack 可视化（上下结构，入栈在上，出栈从上）
- 实现 Queue 可视化（右进左出）
- 实现格子文字编辑、自动换行功能
- 实现时间戳记录（入栈/入列时间 hover 显示，出栈/出列时间记录但不显示）
- 实现 json5 本地数据持久化
- 实现 Windows 桌面端组件特性（拖动、打开、关闭、缩放、最小化）
- 支持 exe 打包

## Impact
- 新建项目目录结构
- 创建 Python 模块文件
- 创建配置和数据持久化文件

## ADDED Requirements

### Requirement: 项目初始化
系统 SHALL 使用 uv 包管理工具初始化 Python 项目，配置虚拟环境和依赖。

#### Scenario: 项目初始化成功
- **WHEN** 用户运行项目初始化命令
- **THEN** 创建 uv 虚拟环境，安装 PyQt5、json5、pyinstaller 等依赖

### Requirement: Stack 可视化
系统 SHALL 提供 Stack（栈）的可视化展示，支持上下结构操作。

#### Scenario: 入栈操作
- **WHEN** 用户执行入栈操作并输入文字
- **THEN** 新格子添加到栈顶（上方），格子显示文字，记录入栈时间戳

#### Scenario: 出栈操作
- **WHEN** 用户执行出栈操作
- **THEN** 栈顶格子移除，记录出栈时间戳，数据保存到历史记录

#### Scenario: Hover 显示时间戳
- **WHEN** 用户将鼠标悬停在格子上
- **THEN** 显示该格子的入栈时间戳

### Requirement: Queue 可视化
系统 SHALL 提供 Queue（队列）的可视化展示，支持右进左出操作。

#### Scenario: 入队操作
- **WHEN** 用户执行入队操作并输入文字
- **THEN** 新格子添加到队列右侧，格子显示文字，记录入队时间戳

#### Scenario: 出队操作
- **WHEN** 用户执行出队操作
- **THEN** 队列左侧格子移除，记录出队时间戳，数据保存到历史记录

#### Scenario: Hover 显示时间戳
- **WHEN** 用户将鼠标悬停在格子上
- **THEN** 显示该格子的入队时间戳

### Requirement: 格子文字编辑
系统 SHALL 支持每个格子的文字编辑功能。

#### Scenario: 编辑格子文字
- **WHEN** 用户双击或选中格子进行编辑
- **THEN** 格子进入编辑模式，用户可修改文字，文字自动换行显示

#### Scenario: 文字自动换行
- **WHEN** 格子内的文字超过格子宽度
- **THEN** 文字自动换行显示，格子高度自适应

### Requirement: 数据持久化
系统 SHALL 使用 json5 格式进行本地数据持久化。

#### Scenario: 保存数据
- **WHEN** 执行入栈/入队、出栈/出队、编辑文字等操作
- **THEN** 数据自动保存到本地 json5 文件

#### Scenario: 加载数据
- **WHEN** 程序启动
- **THEN** 从本地 json5 文件加载历史数据，恢复 Stack 和 Queue 状态

### Requirement: Windows 桌面端组件
系统 SHALL 作为 Windows 桌面端组件运行，支持标准窗口操作。

#### Scenario: 窗口拖动
- **WHEN** 用户拖动窗口标题栏
- **THEN** 窗口跟随鼠标移动

#### Scenario: 窗口缩放
- **WHEN** 用户拖动窗口边框或角落
- **THEN** 窗口大小随之改变，内部组件自适应

#### Scenario: 窗口最小化/关闭
- **WHEN** 用户点击最小化或关闭按钮
- **THEN** 窗口最小化到任务栏或关闭程序

### Requirement: 字体设置
系统 SHALL 使用美观的中文字体，字号适中。

#### Scenario: 字体显示
- **WHEN** 程序运行
- **THEN** 界面文字使用微软雅黑或思源黑体等中文字体，字号 12-14pt

### Requirement: EXE 打包
系统 SHALL 支持打包为 Windows 可执行文件。

#### Scenario: 打包成功
- **WHEN** 用户运行打包命令
- **THEN** 生成独立的 exe 文件，可脱离 Python 环境运行
