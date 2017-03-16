require "base64"

module HexXOR

  # Convert hex to base64
  def self.hex_xor(s1,s2)
    unless s1.length == s2.length then 
      raise "Buffer length error: not equal size."
    else
      puts "s1 = #{s1.length} s2 = #{s2.length}"
    end
  end
end