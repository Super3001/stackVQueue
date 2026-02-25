# Tasks

- [ ] Task 1: 数据模型增加 modify_time 字段
  - [ ] SubTask 1.1: DataItem 增加 modify_time 字段，初始等于 push_time
  - [ ] SubTask 1.2: update_item_text 方法更新 modify_time
  - [ ] SubTask 1.3: 增加 move_item 方法支持移动 item

- [ ] Task 2: 更新 widgets 显示 modify_time
  - [ ] SubTask 2.1: ItemWidget hover 显示 modify_time
  - [ ] SubTask 2.2: 修改文字后更新 modify_time 显示

- [ ] Task 3: 增加移动按钮（hover 显示）
  - [ ] SubTask 3.1: ItemWidget 增加上移/下移按钮，默认隐藏
  - [ ] SubTask 3.2: hover 时显示移动按钮，离开时隐藏
  - [ ] SubTask 3.3: StackWidget 实现上移/下移逻辑
  - [ ] SubTask 3.4: QueueWidget 实现左移/右移逻辑

# Task Dependencies
- [Task 2] depends on [Task 1]
- [Task 3] depends on [Task 1]
