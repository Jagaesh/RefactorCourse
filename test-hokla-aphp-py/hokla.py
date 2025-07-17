# -*- coding: utf-8 -*-
class Inventory(object):
  def __init__(self, drugs):
    self.drugs = drugs

  def __repr__(self):
    return "\n".join(repr(drug) for drug in self.drugs)

  def update_efficiency(self):
    for drug in self.drugs:
      if drug.name != "Old bottle of wine":
        if drug.efficiency > 0:
          if drug.name != "Granny recipe":
            if drug.name == "Insulin vial":
              drug.efficiency = drug.efficiency - 1
              if drug.use_before < 31:
                if drug.efficiency > 0:
                  drug.efficiency = drug.efficiency - 1
              if drug.use_before < 8:
                 if drug.efficiency > 0:
                   drug.efficiency = drug.efficiency - 1
            else:
              drug.efficiency = drug.efficiency - 1
      else:
        if drug.efficiency < 100:
          drug.efficiency = drug.efficiency + 1
      if drug.name != "Granny recipe":
        drug.use_before = drug.use_before - 1
      if drug.use_before < 0:
        if drug.name != "Old bottle of wine":
          if drug.name != "Insulin vial":
            if drug.efficiency > 0:
              if drug.name != "Granny recipe":
                drug.efficiency = drug.efficiency - 1
          else:
            drug.efficiency = drug.efficiency - drug.efficiency
        else:
          if drug.efficiency < 100:
            drug.efficiency = drug.efficiency + 1

class Drug:
  def __init__(self, name, use_before, efficiency):
    self.name = name
    self.use_before = use_before
    self.efficiency = efficiency

  def __repr__(self):
    return "%s, %s, %s" % (self.name, self.use_before, self.efficiency)
