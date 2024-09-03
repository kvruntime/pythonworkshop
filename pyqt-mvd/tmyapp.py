import numpy as np
import typing
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import pandas as pd

# from PyQt6.QtCharts import *


class DataframeModel(QAbstractTableModel):
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self.df = df
        pass

    def rowCount(self, parent: QModelIndex) -> int:
        return self.df.shape[0]

    def columnCount(self, parent: QModelIndex) -> int:
        return self.df.shape[1]

    def data(self, index: QModelIndex, role: Qt.ItemDataRole) -> typing.Any:
        value = self.df.iloc[index.row(), index.column()]

        if role == Qt.ItemDataRole.DisplayRole:
            return str(value)

        if role == Qt.ItemDataRole.BackgroundRole:
            if index.column() == 3 and isinstance(value, (float, int)):
                if value <= 0:
                    return QColor("#0022ff")
            pass

        return ""

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ) -> typing.Any:
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return str(self.df.columns[section])
        return


class EditDelagate(QStyledItemDelegate):
    def __init__(self, df: pd.DataFrame) -> None:
        super().__init__()
        self.df = df
        pass

    def paint(
        self, painter: QPainter, option: "QStyleOptionViewItem", index: QModelIndex
    ) -> None:
        value = index.data(Qt.ItemDataRole.DisplayRole)
        if index.column() == 1:
            opts = QStyleOptionProgressBar()
            opts.rect = option.rect
            opts.minimum = (
                self.df.iloc[:, index.column()].to_numpy(dtype=np.int32).min()
            )
            opts.maximum = (
                self.df.iloc[:, index.column()].to_numpy(dtype=np.int32).max()
            )
            opts.text = "progress"
            opts.progress = int(eval(value))
            QApplication.style().drawControl(
                QStyle.ControlElement.CE_ProgressBar, opts, painter
            )

        return super().paint(painter, option, index)


class TmyApp(QWidget):
    AppName = "TmyApp"
    AppVersion = "1.0.0"

    def __init__(self):
        super().__init__()
        self.setContentsMargins(10, 10, 10, 10)

        # load tmy
        filename = "./resources/tmy.csv"
        df = pd.read_csv(filename, skiprows=16, nrows=8760)
        df.set_index(pd.date_range("2021-01-01", periods=8760, freq="H"), inplace=True)

        self.tmy_model = DataframeModel(df)
        self.edit_delegate = EditDelagate(df)

        # Initialize components
        layout = QVBoxLayout(self)
        layout_inner = QVBoxLayout(self)
        layout.setSpacing(10)
        scroll = QScrollArea()
        scroll.setLayout(layout_inner)

        self.tableview_tmy = QTableView()
        self.tableview_tmy.setAlternatingRowColors(True)
        self.tableview_tmy.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        self.tableview_tmy.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.tableview_tmy.verticalHeader().setHidden(True)
        self.tableview_tmy.horizontalHeader().setSizeAdjustPolicy(
            QTableView.SizeAdjustPolicy.AdjustToContents
        )
        self.tableview_tmy.setModel(self.tmy_model)
        self.tableview_tmy.setItemDelegate(self.edit_delegate)

        # self.chart = QChart()
        # self.chart_view = QChartView(self.chart)
        # self.chart_view.setMinimumHeight(500)

        layout.addWidget(scroll)
        layout_inner.addWidget(self.tableview_tmy)
        # layout_inner.addWidget(self.chart_view)

        pass
