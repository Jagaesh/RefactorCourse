# -*- coding: utf-8 -*-

from hokla import Drug, Inventory

class InventoryTest:
    def test_foo(self):
        items = [
            Drug("Normal Drug", 10, 20),
            Drug("Old bottle of wine", 2, 0),
            Drug("Normal Drug 2", 5, 7),
            Drug("Granny recipe", 0, 150),
            Drug("Granny recipe", -1, 80),
            Drug("Insulin vial", 15, 20),
            Drug("Insulin vial", 10, 49),
            Drug("Insulin vial", 5, 49),
            # this ARN Vaccine drug does not work properly yet
            Drug("ARN Vaccine", 3, 6)
        ]

        expected_output = """Normal Drug, 9, 19
Old bottle of wine, 1, 1
Normal Drug 2, 4, 6
Granny recipe, 0, 150
Granny recipe, -1, 80
Insulin vial, 14, 18
Insulin vial, 9, 47
Insulin vial, 4, 46
ARN Vaccine, 2, 5"""

        inventory = Inventory(items)
        inventory.update_efficiency()

        assert repr(inventory) == expected_output, "❌ Inventory output does not match expected result"

        print("✅ All tests passed.")
        print(repr(inventory))


if __name__ == '__main__':
    test = InventoryTest()
    test.test_foo()
