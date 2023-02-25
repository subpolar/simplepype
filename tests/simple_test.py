from greetings import foo

def test_foo(capfd):
    foo()  # Writes "Hello World!" to stdout
    out, err = capfd.readouterr()
    assert out == "Hello World!\n"
