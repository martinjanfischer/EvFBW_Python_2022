#!/usr/bin/env python

import sys
import math

from PyQt5.QtCore import QPointF, QRect, QRectF, Qt, QTimer
from PyQt5.QtGui import (QBrush, QColor, QFont, QFontMetrics, QLinearGradient, QPainter,
        QPen, QSurfaceFormat)
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QOpenGLWidget,
        QWidget)


class Helper(object):
    def __init__(self):
        gradient = QLinearGradient(QPointF(50, -20), QPointF(80, 20))
        gradient.setColorAt(0.0, Qt.white)
        gradient.setColorAt(1.0, QColor(0xa6, 0xce, 0x39))

        self.background = QBrush(QColor(64, 32, 64))
        self.circleBrush = QBrush(gradient)
        self.circlePen = QPen(Qt.black)
        self.circlePen.setWidth(1)
        self.textPen = QPen(Qt.white)
        self.textFont = QFont()
        self.textFont.setPixelSize(50)
        
        self.text = "Hallo Welt,\nmein Name ist\n ..."
        self.step = 0;

    def paint(self, painter, event, elapsed):
        painter.fillRect(event.rect(), self.background)
        painter.translate(200, 200)

        painter.save()
        painter.setBrush(self.circleBrush)
        painter.setPen(self.circlePen)
        painter.rotate(elapsed * 0.030)

        r = elapsed / 1000.0
        n = 30
        for i in range(n):
            painter.rotate(30)
            radius = 0 + 120.0*((i+r)/n)
            circleRadius = 1 + ((i+r)/n)*20
            painter.drawEllipse(QRectF(radius, -circleRadius,
                    circleRadius*2, circleRadius*2))

        painter.restore()

        sineTable = (0, 38, 71, 92, 100, 92, 71, 38, 0, -38, -71, -92, -100, -92, -71, -38)
        
        metrics = QFontMetrics(self.textFont)
        x = int(-metrics.width(self.text) / 4)
        y = int(-(metrics.ascent() - metrics.descent()))
        color = QColor()

        painter.setFont(self.textFont)

        for i, ch in enumerate(self.text):
            if ch == "\n":
                x = int(-(metrics.width(self.text)) / 4)
                y += int(metrics.height())
                continue
            index = (self.step + i) % 16
            color.setHsv((15 - index) * 16, 255, 191)
            painter.setPen(color)
            dy = int((sineTable[index] * int(metrics.height())) / 400)
            painter.drawText(x, y - dy, ch)
            x += int(metrics.width(ch))


class GLWidget(QOpenGLWidget):
    def __init__(self, helper, parent):
        super(GLWidget, self).__init__(parent)

        self.helper = helper
        self.elapsed = 0
        self.setFixedSize(400, 400)
        self.setAutoFillBackground(False)

    def animate(self):
        self.elapsed = (self.elapsed + self.sender().interval()) % 1000
        self.helper.step += 1
        self.update()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        self.helper.paint(painter, event, self.elapsed)
        painter.end()


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Willkommen")

        helper = Helper()
        openGLLabel = QLabel("Wie heisst Du?")
        openGLLabel.setAlignment(Qt.AlignHCenter)
        openGL = GLWidget(helper, self)

        layout = QGridLayout()
        layout.addWidget(openGLLabel, 0, 1)
        layout.addWidget(openGL, 1, 1)
        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(openGL.animate)
        timer.start(50)


if __name__ == '__main__':

    app = QApplication(sys.argv)

    fmt = QSurfaceFormat()
    fmt.setSamples(4)
    QSurfaceFormat.setDefaultFormat(fmt)

    window = Window()
    window.show()
    sys.exit(app.exec_())
