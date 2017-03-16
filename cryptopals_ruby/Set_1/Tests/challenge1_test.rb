require "test/unit"
require_relative "../Lib/challenge1.rb"

class Challenge_1_Test < Test::Unit::TestCase
  def test_conversion
    input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert_equal(expected,HexToBase64.hex_to_base64(input))
  end   
end