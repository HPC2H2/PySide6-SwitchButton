from PySide6.QtWidgets import QAbstractButton
from PySide6.QtCore import (
    Qt,
    QRect,
    )
from PySide6.QtGui import QPainter
 
 
class SwitchButton(QAbstractButton):
    def __init__(self):
        super().__init__()
        self._checked = False
        
        # 字体设置
        font = self.font()
        font.setBold(True)
        self.setFont(font)
        
        # 鼠标样式
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        # PySide6 PySide6.QtGui.QBrush() 的 setColor() 只能用 GlobalColor 类中预定义的颜色
        self.color_keymap = {
            "slider": Qt.GlobalColor.white,
            "text": Qt.GlobalColor.white,
            "on bg": Qt.GlobalColor.blue,
            "off bg": Qt.GlobalColor.gray,
        }
        self.on_text = "使能"
        self.off_text = "失能"

        self.clicked.connect(self.onClicked)

        self.setStyleSheet(f"""
            SwitchButton {{
                font-family: "Microsoft YaHei";   /* 字体 */
                font-size: 20px;            /* 字体大小 */
                color: white;                      /* 文字颜色 */
                border-radius: 20px;                /* 圆角半径 */
                padding: 0 20px;                   /* 左右内边距 */
                margin: 4px;                       /* 外边距 */
                min-width: 80px;                  /* 最小宽度 */
                max-width: 80px;                  /* 最大宽度 */
                min-height: 40px;                 /* 最小高度 */
                max-height: 40px;                 /* 最大高度 */
            }}
        """)
 
    def paintEvent(self, event):
        slider_space = 2
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing,True)

        # 使能时
        if self._checked:
            # 画背景
            background_rect = QRect(0, 0, self.width(), self.height())
            painter.setPen(Qt.PenStyle.NoPen) # 不需要画出边缘
            painter.setBrush(self.color_keymap["on bg"])
            painter.drawRoundedRect(background_rect, self.height()/2, self.height()/2)
            # 画滑块
            painter.setBrush(self.color_keymap["slider"])
            slider_width = min(self.width(), self.height() - slider_space * 2)
            slider_rect = QRect(self.width() - slider_width - slider_space, slider_space, slider_width, slider_width)
            painter.drawEllipse(slider_rect)

            #画文字
            text_rect = QRect(0, 0, self.width() - slider_width, self.height())
            painter.setPen(self.color_keymap["text"])
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter,self.on_text)
            
        # 失能时
        else:
            # 画背景
            background_rect = QRect(0, 0, self.width(), self.height())
            painter.setPen(Qt.PenStyle.NoPen) # 不需要画出边缘
            painter.setBrush(self.color_keymap["off bg"])
            painter.drawRoundedRect(background_rect, self.height()/2, self.height()/2)
            
            # 画滑块
            painter.setBrush(self.color_keymap["slider"])
            slider_width = min(self.width(), self.height() - slider_space * 2)
            slider_rect = QRect(slider_space, slider_space, slider_width, slider_width)
            painter.drawEllipse(slider_rect)

            #画文字
            text_rect = QRect(slider_width + slider_space, 0, self.width() - slider_width, self.height())
            painter.setPen(self.color_keymap["text"])
            painter.setBrush(Qt.BrushStyle.NoBrush)
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter,self.off_text)

 
    # 鼠标点击，设置开关状态
    def onClicked(self):
        self._checked = not self._checked
        self.update()
    
