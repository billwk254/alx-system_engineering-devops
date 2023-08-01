#!/usr/bin/env ruby

def extract_capital_letters(input)
  input.scan(/[A-Z]/).join
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end

input = ARGV[0]
capital_letters = extract_capital_letters(input)
puts capital_letters
