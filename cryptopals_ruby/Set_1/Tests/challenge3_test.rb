require "test/unit"
require_relative "../Lib/challenge3.rb"

class Challenge_3_Test < Test::Unit::TestCase
  def test_letter_frequency_ltr_exists
    assert_equal(2.782,SingleByteXORCipher.get_frequency("c"))
  end

  def test_letter_frequency_ltr_does_not_exist
    assert_equal(0,SingleByteXORCipher.get_frequency("~"))
  end

  def test_find_best_frequency
    cipher_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    ("a".."z").each { |ltr| SingleByteXORCipher.find_best_frequency(cipher_text, ltr) }
    
  end
end