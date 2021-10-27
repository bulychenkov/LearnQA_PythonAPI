class TestClass:
    def test_input_length(self):
        phrase = input("Set a phrase:")
        assert len(phrase) < 15, "Length of phrase is more then 14 symbols!"
