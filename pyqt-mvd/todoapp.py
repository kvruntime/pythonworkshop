import typing
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from attr import dataclass

@dataclass
class Todo:
    title:str
    is_done:bool=False


class ListModel(QStringListModel):
    def __init__(self, data:typing.List[Todo]):
        super().__init__()
        self.todos=data
        pass

    def rowCount(self, parent: QModelIndex) -> int:
        return len(self.todos)

    def data(self, index: QModelIndex, role: Qt.ItemDataRole) -> typing.Any:
        todo = self.todos[index.row()]

        if role==Qt.ItemDataRole.DisplayRole:
            return todo.title

        if role==Qt.ItemDataRole.DecorationRole:
            if todo.is_done:
                return QColor(0, 200, 30)
        return
    pass

class TodoApp(QWidget):
    AppName="TodoApplication"
    AppVersion = "1.0.0"
    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 10, 10,10)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        self.listviewTodo = QListView()
        self.listviewTodo.setSelectionMode(QListView.SelectionMode.SingleSelection)
        self.listviewTodo.setFont(QFont("", 16))
        self.listviewTodo.setAlternatingRowColors(True)

        self.entryTodo = QLineEdit()
        self.entryTodo.setPlaceholderText("Todo...")
        self.buttonAdd = QPushButton("Add")
        self.buttonComplete = QPushButton("Complete")
        self.buttonDelete = QPushButton("Delete")

        labelTitle = QLabel("<h1>Todo Application</h1>")
        labelTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(labelTitle)

        layout.addWidget(self.listviewTodo)
        layout.addWidget(self.entryTodo)
        layout.addWidget(self.buttonAdd)
        layout.addWidget(self.buttonDelete)
        layout.addWidget(self.buttonComplete)

        # Data
        todos = [
            Todo(title="Call Mum", is_done=False),
            Todo(title="Call Dad", is_done=False),
            Todo(title="Call Bro", is_done=False),
            Todo(title="Call Sister", is_done=False),
        ]

        self.todo_model = ListModel(todos)
        self.listviewTodo.setModel(self.todo_model)

        # Bindings
        self.buttonAdd.clicked.connect(self.command_add_todo)
        self.buttonComplete.clicked.connect(self.command_complete_todo)
        self.buttonDelete.clicked.connect(self.command_delete_todo)
        pass

    def command_add_todo(self):
        _new_todo = self.entryTodo.text().strip()
        if _new_todo:
            self.todo_model.todos.append(Todo(title=_new_todo))
            self.todo_model.layoutChanged.emit()
            self.entryTodo.setText("")
        return None

    def command_delete_todo(self):
        _index = self.listviewTodo.selectedIndexes()
        if _index:
            del self.todo_model.todos[_index[0].row()]
            self.todo_model.layoutChanged.emit()
            self.listviewTodo.clearSelection()
            pass
        return None

    def command_complete_todo(self):
        _index = self.listviewTodo.selectedIndexes()

        if _index:
            _todo = self.todo_model.todos[ _index[0].row()]
            _todo.is_done = True
            self.todo_model.todos[_index[0].row()]=_todo
            self.todo_model.dataChanged.emit(_index[0], _index[0])

            self.listviewTodo.clearSelection()
        return None
