class Service:
   def __init__(self, LT:int, AC :int, CPC:int, LCR: int, PCR: int):
      self.LT = LT
      self.AC = AC
      self.CPC = CPC
      self.LCR = LCR
      self.PCR = PCR
      #у сервиса ещё должно быть множество рессурсов
      
   def changing_characteristics(self, array):
      self.LT += array[0]
      self.AC += array[1]
      self.CPC += array[2]
      self.LCR += array[3]
      self.PCR += array[4]
      
   def get_array(self) -> list[int]:
      return [self.LT, self.AC, self.CPC, self.LCR, self.PCR]


   def __str__(self):
      return f"""
LT = {self.LT}
AC = {self.AC}
CPC = {self.CPC}
LCR = {self.LCR}
PCR = {self.PCR}
"""