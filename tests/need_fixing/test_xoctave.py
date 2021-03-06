import pweave

def test_xoctave():
    """Test Octave code"""
    pweave.weave("tests/octave/octave_test.mdw", doctype = "leanpub", shell = "octave")
    assertSameContent("tests/octave/octave_test.txt", "tests/octave/octave_test_ref.md")

def assertSameContent(REF, outfile):
    out = open(outfile)
    ref = open(REF)
    assert (out.read() == ref.read())
