#!/usr/bin/env python3
# spell-checker: disable

"""
register.py declare the basic building block
to represent a register
"""

import pywave

class Register:
  """
  define the register as a composition of new kind of bricks
  with field informations
  """
  __slots__ = ["name", "description", "fields", "__counter"]
  def __init__(self):
    # default value
    self.name = "reg"
    self.description = ""
    self.fields = []
    # for auto increment field start position
    self.__counter = 0

  def push_field(self, field):
    """
    add a new field to the fields stack
    """
    f = None
    # add to the stack
    if isinstance(field, dict):
      f = Field.from_dict(field)
      f.start = self.__counter
      self.fields.append(f)
    elif isinstance(field, Field):
      f = field
      f.start = self.__counter
      self.fields.append(f)
    else:
      raise Exception(f"Unsupported {type(field)} of field")
    # increment counter
    if f:
      self.__counter += f.width
  
  def to_wavelane(self):
    wave = ''.join([field.wave for field in self.fields[::-1]])
    data = ''.join([field.data for field in self.fields[::-1]])
    print(wave)
    ans = {}
    ans[self.name] = {"wave": wave, "data": data}
    return ans


class FieldStart(pywave.Brick):
  """
  [
  """
  def __init__(self, **kwargs):
    pywave.Brick.__init__(self, **kwargs)
    self.paths.append([
        (self.width, self.height),
        (0, self.height),
        (0, 0),
        (self.width, 0)])
    if not self.styles.get("background", None) is None:
      self.polygons.append([
          (self.width, self.height),
          (0, self.height),
          (0, 0),
          (self.width, 0)])
    # add text
    self.text = (self.width / 2, self.height / 2, kwargs.get("data", ""))

class FieldMid(pywave.Brick):
  """
  I
  """
  def __init__(self, **kwargs):
    pywave.Brick.__init__(self, **kwargs)
    self.splines.append([
        ('M', self.width, self.height*0.75),
        ('l', 0, self.height*0.25),
        ('l', -self.width, 0),
        ('l', 0, -self.height*0.25)])
    self.splines.append([
        ('M', self.width, self.height*0.25),
        ('l', 0, -self.height*0.25),
        ('l', -self.width, 0),
        ('l', 0, self.height*0.25)])
    if not self.styles.get("background", None) is None:
      self.polygons.append([
          (self.width, self.height),
          (0, self.height),
          (0, 0),
          (self.width, 0)])
    # add text
    self.text = (self.width / 2, self.height / 2, kwargs.get("data", ""))

class FieldEnd(pywave.Brick):
  """
  I
  """
  def __init__(self, **kwargs):
    pywave.Brick.__init__(self, **kwargs)
    self.paths.append([
        (0, self.height),
        (self.width, self.height),
        (self.width, 0),
        (0, 0)])
    if not self.styles.get("background", None) is None:
      self.polygons.append([
          (self.width, self.height),
          (0, self.height),
          (0, 0),
          (self.width, 0)])
    # add text
    self.text = (self.width / 2, self.height / 2, kwargs.get("data", ""))

class FieldBit(pywave.Brick):
  """
  I
  """
  def __init__(self, **kwargs):
    pywave.Brick.__init__(self, **kwargs)
    self.paths.append([
        (0, 0),
        (0, self.height),
        (self.width, self.height),
        (self.width, 0),
        (0, 0)])
    if not self.styles.get("background", None) is None:
      self.polygons.append([
          (self.width, self.height),
          (0, self.height),
          (0, 0),
          (self.width, 0)])
    # add text
    self.text = (self.width / 2, self.height / 2, kwargs.get("data", ""))

class Field:
  """
  define what is a field inside a register
  from 1-bit to N-bits
  """
  __slots__ = ["name", "description", "start", "width", "attributes", "wave", "data"]

  def __init__(self):
    # default value
    self.name = ""
    self.description = ""
    self.start = 0
    self.width = 1
    self.attributes = []
    self.wave = ""
    self.data = ""

  @staticmethod
  def from_dict(d: dict):
    """
    Generate a field from a dict
    given after parsing
    """
    f = Field()
    f.name = str(d.get("name", ""))
    f.description = d.get("description", "")
    f.width = d.get("width", d.get("bits", 1))
    f.attributes = d.get("attributes", d.get("attr", None))
    if isinstance(d.get("name", ""), int):
      # convert number to bits
      f.data = ("{0:0"+(str(f.width))+"b}").format(d.get("name", ""))
      # split for each bits
      f.data = ' '.join([c for c in f.data])
      print(f.data)
    else:
      f.data = ' '.join([' ']*f.width)
    if f.width > 1:
      f.wave = pywave.BRICKS.field_start.value + \
            ''.join([pywave.BRICKS.field_mid.value]*(f.width-2)) + \
            pywave.BRICKS.field_end.value
    else:
      f.wave = pywave.BRICKS.field_bit.value
    return f
  
  def to_dict(self):
    """
    Allow one field per line representation
    """
    return {s: getattr(self, s, None) for s in self.__slots__}

def generate_register_symbol(symbol: str, **kwargs) -> (bool, object):
  """
  define the mapping between the symbol and the brick
  """
  # get option supported
  block = None
  if symbol == pywave.BRICKS.field_start:
    block = FieldStart(**kwargs)
  elif symbol == pywave.BRICKS.field_mid:
    block = FieldMid(**kwargs)
  elif symbol == pywave.BRICKS.field_end:
    block = FieldEnd(**kwargs)
  elif symbol == pywave.BRICKS.field_bit:
    block = FieldBit(**kwargs)
  return (not block is None, block)
