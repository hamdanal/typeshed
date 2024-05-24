from _typeshed import Incomplete
from typing import Final

from reportlab.graphics.charts.areas import PlotArea
from reportlab.graphics.widgetbase import PropHolder
from reportlab.lib.attrmap import *

__version__: Final[str]

class LineChartProperties(PropHolder): ...

class AbstractLineChart(PlotArea):
    def makeSwatchSample(self, rowNo, x, y, width, height): ...
    def getSeriesName(self, i, default: Incomplete | None = None): ...

class LineChart(AbstractLineChart): ...

class HorizontalLineChart(LineChart):
    strokeColor: Incomplete
    fillColor: Incomplete
    categoryAxis: Incomplete
    valueAxis: Incomplete
    data: Incomplete
    categoryNames: Incomplete
    lines: Incomplete
    useAbsolute: int
    groupSpacing: int
    lineLabels: Incomplete
    lineLabelFormat: Incomplete
    lineLabelArray: Incomplete
    lineLabelNudge: int
    joinedLines: int
    inFill: int
    reversePlotOrder: int
    def __init__(self) -> None: ...
    def demo(self): ...
    def calcPositions(self) -> None: ...
    def drawLabel(self, G, rowNo, colNo, x, y) -> None: ...
    def makeLines(self): ...
    def draw(self): ...

class _FakeGroup:
    def __init__(self) -> None: ...
    def add(self, what) -> None: ...
    def value(self): ...
    def sort(self) -> None: ...

class HorizontalLineChart3D(HorizontalLineChart):
    theta_x: float
    theta_y: float
    zDepth: int
    zSpace: int
    def calcPositions(self) -> None: ...
    def makeLines(self): ...

class VerticalLineChart(LineChart): ...

def sample1(): ...

class SampleHorizontalLineChart(HorizontalLineChart):
    def demo(self): ...
    def makeBackground(self): ...

def sample1a(): ...
def sample2(): ...
def sample3(): ...
def sampleCandleStick(): ...