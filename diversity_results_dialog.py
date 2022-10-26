from qgis.PyQt.QtWidgets import *
from .diversity_results_dialog_ui import Ui_dlgResults

class DlgResults(QDialog, Ui_dlgResults):
    def __init__(self):
        super(DlgResults, self).__init__()
        self.setupUi(self)
        
        self.setLayout(self.lytMain)
        self.trwresult.setColumnWidth(0, 100)
        self.trwresult.setColumnWidth(1, 80)
        self.trwresult.setColumnWidth(2, 80)
        self.trwresult.setColumnWidth(3, 80)
        self.trwresult.setColumnWidth(4, 80)
        self.trwresult.setColumnWidth(5, 80)