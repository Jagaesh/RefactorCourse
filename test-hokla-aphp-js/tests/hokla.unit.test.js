
const {
  Drug,
  Wine,
  MagicPill,
  HerbalTea,
  Fervex,
  Vaccine,
  Inventory
} = require("../src/hokla");

describe("Drug", () => {
  it("should decrease useBefore and efficiency by 1", () => {
    const drug = new Drug("Normal Drug", 10, 20);
    drug.update();
    expect(drug.useBefore).toBe(9);
    expect(drug.efficiency).toBe(19);
  });

  it("should decrease efficiency twice if expired", () => {
    const drug = new Drug("Expired Drug", 0, 20);
    drug.update();
    expect(drug.efficiency).toBe(18);
  });

  it("efficiency should not go below 0", () => {
    const drug = new Drug("Low Drug", 1, 0);
    drug.update();
    expect(drug.efficiency).toBe(0);
  });
});

describe("Wine", () => {
  it("should increase efficiency by 1 before expiry", () => {
    const wine = new Wine("Wine", 5, 10);
    wine.update();
    expect(wine.efficiency).toBe(11);
  });

  it("should increase efficiency by 2 after expiry", () => {
    const wine = new Wine("Wine", 0, 10);
    wine.update();
    expect(wine.efficiency).toBe(12);
  });

  it("efficiency should not go above 100", () => {
    const wine = new Wine("Wine", 1, 100);
    wine.update();
    expect(wine.efficiency).toBe(100);
  });
});

describe("MagicPill", () => {
  it("should not change useBefore or efficiency", () => {
    const pill = new MagicPill("MagicPill", 10, 80);
    pill.update();
    expect(pill.useBefore).toBe(10);
    expect(pill.efficiency).toBe(80);
  });
});

describe("HerbalTea", () => {
  it("should increase efficiency by 1 before expiry", () => {
    const tea = new HerbalTea("HerbalTea", 5, 10);
    tea.update();
    expect(tea.efficiency).toBe(11);
  });

  it("should increase efficiency by 2 after expiry", () => {
    const tea = new HerbalTea("HerbalTea", 0, 10);
    tea.update();
    expect(tea.efficiency).toBe(12);
  });
});

describe("Fervex", () => {
  it("should increase efficiency by 1 if useBefore > 10", () => {
    const fervex = new Fervex("Fervex", 15, 10);
    fervex.update();
    expect(fervex.efficiency).toBe(11);
  });

  it("should increase efficiency by 2 if useBefore <= 10", () => {
    const fervex = new Fervex("Fervex", 10, 10);
    fervex.update();
    expect(fervex.efficiency).toBe(12);
  });

  it("should increase efficiency by 3 if useBefore <= 5", () => {
    const fervex = new Fervex("Fervex", 5, 10);
    fervex.update();
    expect(fervex.efficiency).toBe(13);
  });

  it("should drop efficiency to 0 if expired", () => {
    const fervex = new Fervex("Fervex", 0, 10);
    fervex.update();
    expect(fervex.efficiency).toBe(0);
  });
});

describe("Vaccine", () => {
  it("should decrease efficiency by 2 if useBefore <= 0", () => {
    const vaccine = new Vaccine("Vaccine", 0, 10);
    vaccine.update();
    expect(vaccine.efficiency).toBe(8);
  });

  it("should decrease efficiency by 3 if useBefore < 5", () => {
    const vaccine = new Vaccine("Vaccine", 4, 10);
    vaccine.update();
    expect(vaccine.efficiency).toBe(7);
  });

  it("should decrease efficiency by 2 if useBefore >= 5", () => {
    const vaccine = new Vaccine("Vaccine", 5, 10);
    vaccine.update();
    expect(vaccine.efficiency).toBe(8);
  });

  it("efficiency should not go below 0", () => {
    const vaccine = new Vaccine("Vaccine", 0, 1);
    vaccine.update();
    expect(vaccine.efficiency).toBe(0);
  });
});
