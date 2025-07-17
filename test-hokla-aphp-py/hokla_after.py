# -*- coding: utf-8 -*-
class Inventory(object):
  def __init__(self, drugs):
    self.drugs = drugs

  def update_efficiency(self):
    for drug in self.drugs:
        drug.update()

  def __repr__(self):
    return "\n".join(repr(drug) for drug in self.drugs)

class Drug:
    def __init__(self, name, use_before, efficiency):
        self.name = name
        self.use_before = use_before
        self.efficiency = efficiency

    def is_(self, name):
        return self.name == name

    def isNot(self, name):
        return self.name != name

    def isExpiringIn(self, days):
        return self.use_before < days

    def isExpired(self):
        return self.use_before < 0

    def _decrease_efficiency(self):
        if self.efficiency > 0:
            self.efficiency -= 1

    def _increase_efficiency(self):
        if self.efficiency < 100:
            self.efficiency += 1
    
    def update(self):
      if self.isNot("Old bottle of wine"):
        if self.efficiency > 0:
          if self.isNot("Granny recipe"):
            if self.is_("Insulin vial"):
              self._decrease_efficiency()
              if self.isExpiringIn(31):
                self._decrease_efficiency()
              if self.isExpiringIn(8):
                self._decrease_efficiency()
            else:
              self._decrease_efficiency()
      else:
        self._increase_efficiency()
      if self.isNot("Granny recipe"):
        self.use_before = self.use_before - 1
      if self.isExpired():
        if self.isNot("Old bottle of wine"):
          if self.isNot("Insulin vial"):
              if self.isNot("Granny recipe"):
                self._decrease_efficiency()
          else:
            self.efficiency = self.efficiency - self.efficiency
        else:
          self._increase_efficiency()

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.use_before, self.efficiency)
