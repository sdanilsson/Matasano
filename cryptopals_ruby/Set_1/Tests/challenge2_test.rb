require "test/unit"
require_relative "../Lib/challenge2.rb"

class Challenge_2_Test < Test::Unit::TestCase
  def test_conversion
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"
    assert_equal(expected,HexXOR.hex_xor(s1,s2))
  end   
end