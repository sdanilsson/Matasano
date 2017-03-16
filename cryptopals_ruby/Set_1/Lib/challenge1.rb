require "base64"

module HexToBase64

  # Convert hex to base64
  def self.hex_to_base64(s)
    text = s.scan(/../).map { |x| x.hex.chr }.join
    Base64.strict_encode64(text)
  end

end