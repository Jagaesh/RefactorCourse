import pytest
import main

def test_do_stuff():
    assert main.do_stuff(10) == 15


if __name__ == "__main__":
    pytest.main([__file__])