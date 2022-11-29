class Test:
    def test_check_lenght(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, f"Typed phrase more than 15 characters. You typed {len(phrase)} characters"