const { Inventory, Drug } = require("../src/hokla");

describe("Hokla", function () {
  it("should foo", function () {
    const drugs = [
      new Drug("Normal Drug", 10, 20),
      new Drug("Old bottle of wine", 2, 0),
      new Drug("Normal Drug 2", 5, 7),
      new Drug("Granny recipe", 0, 150),
      new Drug("Granny recipe", -1, 80),
      new Drug("Insulin vial", 15, 20),
      new Drug("Insulin vial", 10, 49),
      new Drug("Insulin vial", 5, 49),
      // this ARN Vaccine Drug does not work properly yet
      new Drug("ARN Vaccine", 3, 6)
    ];

    const hoklaAPHP = new Inventory(drugs);
    const updatedDrugs = hoklaAPHP.updateEfficiency();

    console.log(updatedDrugs);

    // expect(updatedDrugs[0].name).toBe("fixme");

    expect(updatedDrugs[0].name).toBe("Normal Drug");
    expect(updatedDrugs[0].useBefore).toBe(9);
    expect(updatedDrugs[0].efficiency).toBe(19);

    expect(updatedDrugs[1].name).toBe("Old bottle of wine");
    expect(updatedDrugs[1].useBefore).toBe(1);
    expect(updatedDrugs[1].efficiency).toBe(1);

    expect(updatedDrugs[2].name).toBe("Normal Drug 2");
    expect(updatedDrugs[2].useBefore).toBe(4);
    expect(updatedDrugs[2].efficiency).toBe(6);

    expect(updatedDrugs[3].name).toBe("Granny recipe");
    expect(updatedDrugs[3].useBefore).toBe(0);
    expect(updatedDrugs[3].efficiency).toBe(150);

    expect(updatedDrugs[4].name).toBe("Granny recipe");
    expect(updatedDrugs[4].useBefore).toBe(-1);
    expect(updatedDrugs[4].efficiency).toBe(80);

    expect(updatedDrugs[5].name).toBe("Insulin vial");
    expect(updatedDrugs[5].useBefore).toBe(14);
    expect(updatedDrugs[5].efficiency).toBe(18);

    expect(updatedDrugs[6].name).toBe("Insulin vial");
    expect(updatedDrugs[6].useBefore).toBe(9);
    expect(updatedDrugs[6].efficiency).toBe(47);

    expect(updatedDrugs[7].name).toBe("Insulin vial");
    expect(updatedDrugs[7].useBefore).toBe(4);
    expect(updatedDrugs[7].efficiency).toBe(46);

    expect(updatedDrugs[8].name).toBe("ARN Vaccine");
    expect(updatedDrugs[8].useBefore).toBe(2);
    // Next value is 5 when ARN case is omitted
    expect(updatedDrugs[8].efficiency).toBe(4);

  });
});
