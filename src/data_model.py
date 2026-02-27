from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional
import json5
import os


@dataclass
class DataItem:
    text: str
    push_time: str
    modify_time: str
    pop_time: Optional[str] = None

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            text=data.get('text', ''),
            push_time=data.get('push_time', ''),
            modify_time=data.get('modify_time', data.get('push_time', '')),
            pop_time=data.get('pop_time')
        )


class DataManager:
    def __init__(self, data_file: str = 'data/data.json5', history_file: str = 'data/history.jsonl'):
        self.data_file = data_file
        self.history_file = history_file
        self.stack_items: list[DataItem] = []
        self.queue_items: list[DataItem] = []
        self._ensure_data_dir()
        self.load()

    def _ensure_data_dir(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

    def load(self):
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json5.load(f)
                self.stack_items = [DataItem.from_dict(item) for item in data.get('stack', [])]
                self.queue_items = [DataItem.from_dict(item) for item in data.get('queue', [])]
        except (FileNotFoundError, ValueError, Exception):
            self.stack_items = []
            self.queue_items = []

    def _save_current_state(self):
        data = {
            'stack': [item.to_dict() for item in self.stack_items],
            'queue': [item.to_dict() for item in self.queue_items]
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json5.dump(data, f, indent=2, ensure_ascii=False)

    def _append_history(self, item: DataItem, action: str):
        with open(self.history_file, 'a', encoding='utf-8') as f:
            record = {'action': action, **item.to_dict()}
            f.write(json5.dumps(record, ensure_ascii=False) + '\n')

    def push_stack(self, text: str):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item = DataItem(text=text, push_time=now, modify_time=now)
        self.stack_items.insert(0, item)
        self._save_current_state()
        return item

    def pop_stack(self) -> Optional[DataItem]:
        if self.stack_items:
            item = self.stack_items.pop(0)
            item.pop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._append_history(item, 'stack_pop')
            self._save_current_state()
            return item
        return None

    def enqueue(self, text: str):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item = DataItem(text=text, push_time=now, modify_time=now)
        self.queue_items.append(item)
        self._save_current_state()
        return item

    def dequeue(self) -> Optional[DataItem]:
        if self.queue_items:
            item = self.queue_items.pop(0)
            item.pop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._append_history(item, 'queue_dequeue')
            self._save_current_state()
            return item
        return None

    def update_item_text(self, item: DataItem, new_text: str):
        item.text = new_text
        item.modify_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._save_current_state()

    def _move_item(self, items: list[DataItem], index: int, direction: int):
        """通用移动方法：在指定列表中交换相邻元素的位置"""
        if 0 <= index < len(items):
            new_index = index + direction
            if 0 <= new_index < len(items):
                items[index], items[new_index] = items[new_index], items[index]
                self._save_current_state()

    def move_stack_item(self, index: int, direction: int):
        """移动栈中指定位置的元素"""
        self._move_item(self.stack_items, index, direction)

    def move_queue_item(self, index: int, direction: int):
        """移动队列中指定位置的元素"""
        self._move_item(self.queue_items, index, direction)

    def delete_stack_item(self, index: int) -> Optional[DataItem]:
        """删除栈中指定位置的元素"""
        if 0 <= index < len(self.stack_items):
            item = self.stack_items.pop(index)
            item.pop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._append_history(item, 'stack_delete')
            self._save_current_state()
            return item
        return None

    def delete_queue_item(self, index: int) -> Optional[DataItem]:
        """删除队列中指定位置的元素"""
        if 0 <= index < len(self.queue_items):
            item = self.queue_items.pop(index)
            item.pop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self._append_history(item, 'queue_delete')
            self._save_current_state()
            return item
        return None

    def save(self):
        self._save_current_state()
