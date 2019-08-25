#!/usr/bin/env python3
# spell-checker: disable

"""
digital.py declare the basic building block
to generate a digital waveform
"""

import math
import pywave


class Nclk(pywave.Brick):
    """
    Falling edge clock with arrow
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = 0
        else:
            self.last_y = self.height / 2 if self.last_y is None else self.last_y
        dt = self.last_y * self.slewing / self.height
        # add shape
        self.paths.append(
            [
                (0, self.last_y),
                (dt, 0),
                (self.width * self.duty_cycle - self.slewing / 2, 0),
                (self.width * self.duty_cycle + self.slewing / 2, self.height),
                (self.width - self.slewing / 2, self.height),
                (self.width, self.height / 2),
            ]
        )
        if self.ignore_transition:
            self.paths[0] = self.paths[0][0] + self.paths[0][2:]
        # add arrow
        if kwargs.get("add_arrow", False):
            arrow_angle = -math.atan2(-self.height, self.slewing) * 180 / math.pi
            self.arrows.append(
                (
                    dt * (self.height / 2 - self.last_y) / self.height
                    + self.width * self.duty_cycle,
                    self.height / 2,
                    arrow_angle,
                )
            )


class Pclk(pywave.Brick):
    """
    Rising edge clock with arrow
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = self.height
        else:
            self.last_y = self.height / 2 if self.last_y is None else self.last_y
        dt = self.last_y * self.slewing / self.height
        # add shape
        self.paths.append(
            [
                (0, self.last_y),
                (dt, 0),
                (self.width * self.duty_cycle - self.slewing / 2, 0),
                (self.width * self.duty_cycle + self.slewing / 2, self.height),
                (self.width - self.slewing / 2, self.height),
                (self.width, self.height / 2),
            ]
        )
        if self.ignore_transition:
            self.paths[0] = self.paths[0][0] + self.paths[0][2:]
        # add arrow
        if kwargs.get("add_arrow", False):
            arrow_angle = math.atan2(-self.height, self.slewing) * 180 / math.pi
            self.arrows.append((dt / 2, self.height / 2, arrow_angle))


class Low(pywave.Brick):
    """
    Falling edge clock with arrow and rest at zero
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = self.height
        else:
            self.last_y = self.height if self.last_y is None else self.last_y
        dt = abs(self.height - self.last_y) * self.slewing / self.height
        # add shape
        self.paths.append([(0, self.last_y), (dt, self.height), (self.width, self.height)])
        # add arrow
        if kwargs.get("add_arrow", False) and not self.is_first:
            arrow_angle = -math.atan2(-self.height, self.slewing) * 180 / math.pi
            self.arrows.append(
                (
                    dt * (self.height / 2 - self.last_y) / self.height,
                    self.height / 2,
                    arrow_angle,
                )
            )


class High(pywave.Brick):
    """
    Rising edge clock with arrow and rest at one
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = self.height
        else:
            self.last_y = self.height if self.last_y is None else self.last_y
        dt = self.last_y * self.slewing / self.height
        # add shape
        self.paths.append([(0, self.last_y), (dt, 0), (self.width, 0)])
        # add arrow
        if kwargs.get("add_arrow", False):
            arrow_angle = math.atan2(-self.height, self.slewing) * 180 / math.pi
            self.arrows.append((dt / 2, self.height / 2, arrow_angle))


class HighZ(pywave.Brick):
    """
    High impedance mode with a reset close to VDD/2
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = self.height / 2
        else:
            self.last_y = self.height / 2 if self.last_y is None else self.last_y
        dt = abs(self.height - self.last_y) * self.slewing / self.height
        # add shape
        self.splines.append(
            [
                ("M", 0, self.last_y),
                ("C", dt, self.height / 2),
                ("", dt, self.height / 2),
                ("", min(self.width, 20), self.height / 2),
                ("L", self.width, self.height / 2),
            ]
        )


class Zero(pywave.Brick):
    """
    Zero level
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = self.height
        else:
            self.last_y = self.height if self.last_y is None else self.last_y
        dt = (self.height - self.last_y) * self.slewing / self.height
        # add shape
        self.paths.append(
            [
                (0, self.last_y),
                (3, self.last_y),
                (3 + self.slewing, self.height),
                (self.width, self.height),
            ]
        )


class One(pywave.Brick):
    """
    One level
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = 0
        else:
            self.last_y = self.height if self.last_y is None else self.last_y
        dt = (self.height - self.last_y) * self.slewing / self.height
        # add shape
        self.paths.append(
            [(0, self.last_y), (3, self.last_y), (3 + self.slewing, 0), (self.width, 0)]
        )


class Data(pywave.Brick):
    """
    Multibits value such as a Bus
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        self.last_y = self.height / 2 if self.last_y is None else self.last_y
        # add shape
        if self.is_first:
            self.paths.append(
                [
                    (0, 0),
                    (self.slewing, 0),
                    (self.width - self.slewing, 0),
                    (self.width, self.height / 2),
                ]
            )
            self.paths.append(
                [
                    (0, self.height),
                    (self.slewing, self.height),
                    (self.width - self.slewing, self.height),
                    (self.width, self.height / 2),
                ]
            )
        else:
            self.paths.append(
                [
                    (0, self.last_y),
                    (self.slewing, 0),
                    (self.width - self.slewing, 0),
                    (self.width, self.height / 2),
                ]
            )
            self.paths.append(
                [
                    (0, self.last_y),
                    (self.slewing, self.height),
                    (self.width - self.slewing, self.height),
                    (self.width, self.height / 2),
                ]
            )
        # add background
        if self.is_first:
            self.polygons.append(
                [
                    (0, 0),
                    (self.slewing, 0),
                    (self.width - self.slewing, 0),
                    (self.width, self.height / 2),
                    (self.width - self.slewing, self.height),
                    (self.slewing, self.height),
                    (0, self.height),
                ]
            )
        else:
            self.polygons.append(
                [
                    (0, self.last_y),
                    (self.slewing, 0),
                    (self.width - self.slewing, 0),
                    (self.width, self.height / 2),
                    (self.width - self.slewing, self.height),
                    (self.slewing, self.height),
                    (0, self.last_y),
                ]
            )
        # add text
        self.texts.append((self.width / 2, self.height / 2, kwargs.get("data", "")))


class Gap(pywave.Brick):
    """
    time compression
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        # if self.is_first:
        # raise "a gap cannot be first in a wavelane"
        self.splines.append(
            [
                ("M", 0, self.height + 2),
                ("C", 5, self.height + 2),
                ("", 5, -4),
                ("", 10, -4),
                ("L", 7, 0),
                ("C", 2, 0),
                ("", 2, self.height + 4),
                ("", -3, self.height + 4),
                ("z", "", ""),
            ]
        )
        self.splines.append(
            [
                ("M", 0, self.height + 2),
                ("C", 5, self.height + 2),
                ("", 5, -2),
                ("", 10, -2),
            ]
        )
        self.splines.append(
            [
                ("M", -3, self.height + 2),
                ("C", 2, self.height + 2),
                ("", 2, -2),
                ("", 7, -2),
            ]
        )


class Up(pywave.Brick):
    """
    RC charging to VDD
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        self.last_y = self.height if self.last_y is None else self.last_y
        self.splines.append(
            [
                ("M", 0, self.last_y),
                ("L", 3, self.last_y),
                ("C", 3 + self.slewing, self.last_y),
                ("", 3 + self.slewing, 0),
                ("", min(self.width, 20), 0),
                ("L", self.width, 0),
            ]
        )


class Down(pywave.Brick):
    """
    RC discharge to GND
    """

    def __init__(self, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        self.last_y = self.height if self.last_y is None else self.last_y
        self.splines.append(
            [
                ("M", 0, self.last_y),
                ("L", 3, self.last_y),
                ("C", 3 + self.slewing, self.last_y),
                ("", 3 + self.slewing, self.height - self.last_y),
                ("", min(self.width, 20), self.height),
                ("L", self.width, self.height),
            ]
        )


class Impulse(pywave.Brick):
    """
    pulse
    """

    def __init__(self, y, **kwargs):
        pywave.Brick.__init__(self, **kwargs)
        if self.is_first:
            self.last_y = self.height
        else:
            self.last_y = self.height if self.last_y is None else self.last_y
        # add shape
        self.paths.append(
            [
                (0, self.height - y),
                (0, y),
                (0, self.height - y),
                (self.width, self.height - y),
            ]
        )


def generate_digital_symbol(symbol: str, **kwargs) -> (bool, object):
    """
    define the mapping between the symbol and the brick
    """
    # get option supported
    height = kwargs.get("brick_height", 20)
    ignore_transition = kwargs.get("ignore_transition", False)
    block = None
    # add arrow
    if (
        symbol
        in [pywave.BRICKS.Nclk, pywave.BRICKS.Pclk, pywave.BRICKS.Low, pywave.BRICKS.High]
        and not ignore_transition
    ):
        kwargs.update({"add_arrow": True})
    # clock signals description (pPnNlLhH)
    # (N|n)clk: falling edge (with|without) arrow for repeated pattern
    if symbol in [pywave.BRICKS.nclk, pywave.BRICKS.Nclk]:
        block = Nclk(**kwargs)
    # (P|p)clk: rising edge (with|without) arrow for repeated pattern
    elif symbol in [pywave.BRICKS.pclk, pywave.BRICKS.Pclk]:
        block = Pclk(**kwargs)
    # (L|l)ow: falling edge (with|without) arrow and stuck
    elif symbol == pywave.BRICKS.low or symbol == pywave.BRICKS.Low:
        block = Low(**kwargs)
    # (H|h)igh: rising edge (with|without) arrow and stuck
    elif symbol == pywave.BRICKS.high or symbol == pywave.BRICKS.High:
        block = High(**kwargs)
    # description for data (z01=x)
    elif symbol == pywave.BRICKS.highz:
        block = HighZ(**kwargs)
    elif symbol == pywave.BRICKS.zero:
        block = Zero(**kwargs)
    elif symbol == pywave.BRICKS.one:
        block = One(**kwargs)
    elif symbol == pywave.BRICKS.data:
        block = Data(**kwargs)
    elif symbol == pywave.BRICKS.x:
        if "data" in kwargs:
            kwargs["data"] = ""
        block = Data(**kwargs)
    # time compression symbol
    elif symbol == pywave.BRICKS.gap:
        block = Gap(**kwargs)
    # capacitive charge to 1
    elif symbol == pywave.BRICKS.up:
        block = Up(**kwargs)
    # capacitive discharge to 0
    elif symbol == pywave.BRICKS.down:
        block = Down(**kwargs)
    # impulse symbol
    elif symbol == pywave.BRICKS.imp:
        block = Impulse(height, **kwargs)
    elif symbol == pywave.BRICKS.Imp:
        block = Impulse(0, **kwargs)
    else:
        block = None
    return (not block is None, block)
