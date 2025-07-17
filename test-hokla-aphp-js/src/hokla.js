class Drug {
  #name;
  #useBefore;
  #efficiency;
  
  constructor(name, useBefore, efficiency) {
    this.#name = name;
    this.#useBefore = useBefore;
    this.#efficiency = efficiency;
  }

  get name() {
    return this.#name;
  }

  get useBefore() {
    return this.#useBefore;
  }

  get efficiency() {
    return this.#efficiency;
  }

  decreaseUseBefore() {
    this.#useBefore--;
  }

  increaseEfficiency() {
    this.#efficiency = Math.min(100, this.#efficiency + 1);
  }

  decreaseEfficiency() {
    this.#efficiency = Math.max(0, this.#efficiency - 1);
  }

  resetEfficiency() {
    this.#efficiency = 0;
  }

  isExpired() {
    return this.#useBefore < 0;
  }

  isExpiringIn(days) {
    return this.#useBefore < days;
  }

  update() {
    this.decreaseEfficiency();
    if (this.isExpired()) this.decreaseEfficiency();
    this.decreaseUseBefore();
  }
}

class Wine extends Drug {
  update() {
    this.increaseEfficiency();
    if (this.isExpired()) this.increaseEfficiency();
    this.decreaseUseBefore();
  }
}

class Insulin extends Drug {
  update() {
    // comportement générique (décrément de base)
    super.update();

    // comportements spécifiques à Insulin
    if (this.isExpiringIn(31)) this.decreaseEfficiency();
    if (this.isExpiringIn(8)) this.decreaseEfficiency();
    if (this.isExpired()) this.resetEfficiency();
  }
}

class GrannyRecipe extends Drug {
  update() {
  }
}

class VaccineArn extends Drug {
  update() {
    this.decreaseEfficiency();
    this.decreaseEfficiency();
    if (this.isExpired()) {
      this.decreaseEfficiency();
      this.decreaseEfficiency();
    }
    this.decreaseUseBefore();
  }
}

class Inventory {
  constructor(drugs = []) {
    this.drugs = drugs.map(drug => {
      switch (drug.name) {
        case "Old bottle of wine":
          return new Wine(drug.name, drug.useBefore, drug.efficiency);
        case "Insulin vial":
          return new Insulin(drug.name, drug.useBefore, drug.efficiency);
        case "Granny recipe":
          return new GrannyRecipe(drug.name, drug.useBefore, drug.efficiency);
        case "ARN Vaccine":
          return new VaccineArn(drug.name, drug.useBefore, drug.efficiency);
        default:
          return new Drug(drug.name, drug.useBefore, drug.efficiency);
      }
    });
  }

  updateEfficiency() {
    this.drugs.forEach(drug => drug.update());
    return this.drugs;
  }
}


module.exports = {
  Drug,
  Inventory
};
