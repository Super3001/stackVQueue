# 增加 modify_time 和移动功能 Spec

## Why
需要追踪 item 的修改时间，并支持在栈和队列中调整 item 的顺序。

## What Changes
- 数据模型增加 `modify_time` 字段
- 修改文字时自动更新 `modify_time`
- 增加 item 上移/下移按钮（hover 时显示）
- 移动时更新数据持久化

## Impact
- Affected code: src/data_model.py, src/widgets.py

## ADDED Requirements

### Requirement: modify_time 字段
系统 SHALL 为每个 item 记录修改时间。

#### Scenario: 创建 item
- **WHEN** 用户入栈/入队创建新 item
- **THEN** modify_time 初始值等于 push_time

#### Scenario: 修改文字
- **WHEN** 用户修改 item 文字
- **THEN** modify_time 自动更新为当前时间

#### Scenario: Hover 显示
- **WHEN** 用户鼠标悬停在 item 上
- **THEN** 显示 push_time 和 modify_time

### Requirement: item 移动功能
系统 SHALL 支持在栈和队列中移动 item 顺序。

#### Scenario: 移动按钮显示
- **WHEN** 用户鼠标悬停在 item 上
- **THEN** 显示移动按钮（Stack 显示上移/下移，Queue 显示左移/右移）

#### Scenario: 移动按钮隐藏
- **WHEN** 鼠标离开 item
- **THEN** 移动按钮隐藏

#### Scenario: Stack 上移
- **WHEN** 用户点击 item 的上移按钮
- **THEN** item 向栈顶方向移动一位（交换位置）

#### Scenario: Stack 下移
- **WHEN** 用户点击 item 的下移按钮
- **THEN** item 向栈底方向移动一位（交换位置）

#### Scenario: Queue 左移
- **WHEN** 用户点击 item 的左移按钮
- **THEN** item 向队首方向移动一位（交换位置）

#### Scenario: Queue 右移
- **WHEN** 用户点击 item 的右移按钮
- **THEN** item 向队尾方向移动一位（交换位置）

#### Scenario: 移动持久化
- **WHEN** 用户移动 item
- **THEN** 新顺序保存到数据文件
