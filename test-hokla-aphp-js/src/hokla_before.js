class Drug {
  constructor(name, useBefore, efficiency) {
    this.name = name;
    this.useBefore = useBefore;
    this.efficiency = efficiency;
  }
}

class Inventory {
  constructor(drugs = []) {
    this.drugs = drugs;
  }
  updateEfficiency() {
    for (let i = 0; i < this.drugs.length; i++) {
      if (this.drugs[i].name !== "Old bottle of wine") {
        if (this.drugs[i].efficiency > 0) {
          if (this.drugs[i].name !== "Granny recipe") {
            if (this.drugs[i].name === "Insulin vial") {
              this.drugs[i].efficiency = this.drugs[i].efficiency - 1;
              if (this.drugs[i].useBefore < 31) {
                if (this.drugs[i].efficiency > 0) {
                  this.drugs[i].efficiency = this.drugs[i].efficiency - 1;
                }
              }
              if (this.drugs[i].useBefore < 8) {
                if (this.drugs[i].efficiency > 0) {
                  this.drugs[i].efficiency = this.drugs[i].efficiency - 1;
                }
              }
            } else {
              this.drugs[i].efficiency = this.drugs[i].efficiency - 1;
            }
          }
        }
      } else {
        if (this.drugs[i].efficiency < 100) {
          this.drugs[i].efficiency = this.drugs[i].efficiency + 1;
        }
      }
      if (this.drugs[i].name !== "Granny recipe") {
        this.drugs[i].useBefore = this.drugs[i].useBefore - 1;
      }
      if (this.drugs[i].useBefore < 0) {
        if (this.drugs[i].name !== "Old bottle of wine") {
          if (this.drugs[i].name !== "Insulin vial") {
            if (this.drugs[i].efficiency > 0) {
              if (this.drugs[i].name !== "Granny recipe") {
                this.drugs[i].efficiency = this.drugs[i].efficiency - 1;
              }
            }
          } else {
            this.drugs[i].efficiency =
              this.drugs[i].efficiency - this.drugs[i].efficiency;
          }
        } else {
          if (this.drugs[i].efficiency < 100) {
            this.drugs[i].efficiency = this.drugs[i].efficiency + 1;
          }
        }
      }
    }

    return this.drugs;
  }
}

module.exports = {
  Drug,
  Inventory
};
