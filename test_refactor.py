import sys
sys.path.insert(0, 'src')
from data_model import DataManager, DataItem

print("=" * 60)
print("验证重构后的代码")
print("=" * 60)

dm = DataManager()
print("\n✓ DataManager 实例化成功")

print("\n方法存在性检查:")
print(f"  - move_stack_item: {hasattr(dm, 'move_stack_item')}")
print(f"  - move_queue_item: {hasattr(dm, 'move_queue_item')}")
print(f"  - _move_item (私有方法): {hasattr(dm, '_move_item')}")

print("\n" + "=" * 60)
print("测试移动功能")
print("=" * 60)

dm.stack_items = [
    DataItem(text="栈项1", push_time="2024-01-01 00:00:00", modify_time="2024-01-01 00:00:00"),
    DataItem(text="栈项2", push_time="2024-01-01 00:00:00", modify_time="2024-01-01 00:00:00"),
    DataItem(text="栈项3", push_time="2024-01-01 00:00:00", modify_time="2024-01-01 00:00:00"),
]

dm.queue_items = [
    DataItem(text="队列项1", push_time="2024-01-01 00:00:00", modify_time="2024-01-01 00:00:00"),
    DataItem(text="队列项2", push_time="2024-01-01 00:00:00", modify_time="2024-01-01 00:00:00"),
    DataItem(text="队列项3", push_time="2024-01-01 00:00:00", modify_time="2024-01-01 00:00:00"),
]

print("\n初始状态:")
print(f"  栈: {[item.text for item in dm.stack_items]}")
print(f"  队列: {[item.text for item in dm.queue_items]}")

print("\n测试栈项向下移动 (索引 0 -> 1):")
dm.move_stack_item(0, 1)
print(f"  栈: {[item.text for item in dm.stack_items]}")
assert dm.stack_items[0].text == "栈项2", "移动后索引0应为栈项2"
assert dm.stack_items[1].text == "栈项1", "移动后索引1应为栈项1"
print("  ✓ 移动成功")

print("\n测试栈项向上移动 (索引 1 -> 0):")
dm.move_stack_item(1, -1)
print(f"  栈: {[item.text for item in dm.stack_items]}")
assert dm.stack_items[0].text == "栈项1", "移动后索引0应为栈项1"
assert dm.stack_items[1].text == "栈项2", "移动后索引1应为栈项2"
print("  ✓ 移动成功")

print("\n测试队列项向右移动 (索引 0 -> 1):")
dm.move_queue_item(0, 1)
print(f"  队列: {[item.text for item in dm.queue_items]}")
assert dm.queue_items[0].text == "队列项2", "移动后索引0应为队列项2"
assert dm.queue_items[1].text == "队列项1", "移动后索引1应为队列项1"
print("  ✓ 移动成功")

print("\n测试队列项向左移动 (索引 1 -> 0):")
dm.move_queue_item(1, -1)
print(f"  队列: {[item.text for item in dm.queue_items]}")
assert dm.queue_items[0].text == "队列项1", "移动后索引0应为队列项1"
assert dm.queue_items[1].text == "队列项2", "移动后索引1应为队列项2"
print("  ✓ 移动成功")

print("\n" + "=" * 60)
print("测试边界情况")
print("=" * 60)

print("\n测试边界移动 (第一个元素向上移动):")
original_stack = [item.text for item in dm.stack_items]
dm.move_stack_item(0, -1)
current_stack = [item.text for item in dm.stack_items]
assert original_stack == current_stack, "第一个元素向上移动应无效"
print(f"  栈保持不变: {current_stack}")
print("  ✓ 边界检查正确")

print("\n测试边界移动 (最后一个元素向下移动):")
original_stack = [item.text for item in dm.stack_items]
dm.move_stack_item(2, 1)
current_stack = [item.text for item in dm.stack_items]
assert original_stack == current_stack, "最后一个元素向下移动应无效"
print(f"  栈保持不变: {current_stack}")
print("  ✓ 边界检查正确")

print("\n测试无效索引移动:")
original_stack = [item.text for item in dm.stack_items]
dm.move_stack_item(-1, 1)
dm.move_stack_item(10, 1)
current_stack = [item.text for item in dm.stack_items]
assert original_stack == current_stack, "无效索引移动应无效"
print(f"  栈保持不变: {current_stack}")
print("  ✓ 无效索引检查正确")

print("\n" + "=" * 60)
print("所有测试通过！重构成功！")
print("=" * 60)
