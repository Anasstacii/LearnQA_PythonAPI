class Test:
    def test_check_lenght(self):
        phrase = input("Type any phrase less than 15 characters: ")
        assert len(phrase) < 15, f"Typed phrase more than 15 characters. You typed {len(phrase)} characters"