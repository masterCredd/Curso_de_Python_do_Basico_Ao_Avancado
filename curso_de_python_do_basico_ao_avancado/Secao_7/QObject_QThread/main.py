import sys
import time

from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QApplication, QWidget
from worker import Ui_myWidget


class Worker_1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        """
        The run function is a simple loop that emits the progressed signal
        every second. The value of i is passed as an argument to the signal.


        :param self: Represent the instance of the class
        :return: Nothing
        :doc-author: Trelent
        """
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_myWidget):
    def __init__(self, parent=None):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the user interface and connects signals to slots.

        :param self: Represent the instance of the class
        :param parent: Pass the parent widget to the qdialog class
        :return: The object itself
        :doc-author: Trelent
        """
        super().__init__(parent)
        self.setupUi(self)

        self.button_1.clicked.connect(self.hardWork_1)
        self.button_1.clicked.connect(self.hardWork_2)

    def hardWork_1(self):
        """
        The hardWork_1 function is a function that runs the Worker_2 class in 
        a separate thread.
            The hardWork_2 function is called when the user clicks on the 
            &quot;Start&quot; button.


        :param self: Represent the instance of the class
        :return: The following:
        :doc-author: Trelent
        """
        self._worker = Worker_1()
        self._thread = QThread()

        worker_1 = self._worker
        thread = self._thread

        # mover o worker para thread
        worker_1.moveToThread(thread)

        # Run
        thread.started.connect(worker_1.run)

        worker_1.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker_1 .finished.connect(thread.deleteLater)

        worker_1.started.connect(self.worker_1Started)
        worker_1.progressed.connect(self.worker_1Progressed)
        worker_1.finished.connect(self.worker_1Finished)

        thread.start()

    def worker_1Started(self, value):
        """
        The worker_1Started function is called when the worker_thread emits a 
        signal.
        The value passed to this function is the text we want to show in the 
        label.

        :param self: Represent the instance of the class
        :param value: Display the value of the progress bar
        :return: The value of the label_2
        :doc-author: Trelent
        """
        self.button_1.setDisabled(True)
        self.label_1.setText(value)
        print('worker iniciado')

    def worker_1Progressed(self, value):
        """
        The worker_1Progressed function is called when the worker emits a 
        signal.
        The value argument is the data passed by the worker.


        :param self: Represent the instance of the object
        :param value: Pass the data from the worker thread to this function
        :return: The value of the progress bar
        :doc-author: Trelent
        """
        self.label_1.setText(value)
        print('em progresso')

    def worker_1Finished(self, value):
        """
        The worker_1Finished function is called when the worker_2 thread emits 
        a signal.
        The value argument is the value passed to the emit() function in 
        worker_2.py.

        :param self: Represent the instance of the object itself
        :param value: Update the label_2 text
        :return: The value of the worker_2finished function
        :doc-author: Trelent
        """
        self.button_1.setDisabled(False)
        self.label_1.setText(value)
        print('worker finalizado')

    def hardWork_2(self):
        """
        The hardWork_2 function is a function that creates a worker and thread,
            connects the signals to the slots, and starts the thread.


        :param self: Refer to the current instance of a class
        :return: A qthread object
        :doc-author: Trelent
        """
        self._worker_2 = Worker_1()
        self._thread_2 = QThread()

        worker_1 = self._worker_2
        thread = self._thread_2

        # mover o worker para thread
        worker_1.moveToThread(thread)

        # Run
        thread.started.connect(worker_1.run)

        worker_1.finished.connect(thread.quit)

        thread.finished.connect(thread.deleteLater)
        worker_1 .finished.connect(thread.deleteLater)

        worker_1.started.connect(self.worker_2Started)
        worker_1.progressed.connect(self.worker_2Progressed)
        worker_1.finished.connect(self.worker_2Finished)

        thread.start()

    def worker_2Started(self, value):
        """
        The worker_2Started function is called when the worker_2 emits a signal.
            The value of the signal is passed to this function and printed to 
            stdout.

        :param self: Represent the instance of the class
        :param value: Display the value of the progress bar
        :return: The value of the worker_2started function
        :doc-author: Trelent
        """
        self.button_2.setDisabled(True)
        self.label_2.setText(value)
        print('worker 2 iniciado')

    def worker_2Progressed(self, value):
        """
        The worker_2Progressed function is called when the worker_2 emits a 
        signal.
        The value argument is the value emitted by the worker_2.


        :param self: Represent the instance of the class
        :param value: Update the label_2
        :return: A string
        :doc-author: Trelent
        """
        self.label_1.setText(value)
        print('2 em progresso')

    def worker_2Finished(self, value):
        """
        The worker_2Finished function is called when the worker_2 thread emits 
        a signal.
            The value parameter is the value that was emitted by the worker_2 
            thread.

        :param self: Represent the instance of the class
        :param value: Display the result of the worker in a label
        :return: A string
        :doc-author: Trelent
        """
        self.button_2.setDisabled(False)
        self.label_2.setText(value)
        print('worker 2 finalizado')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
