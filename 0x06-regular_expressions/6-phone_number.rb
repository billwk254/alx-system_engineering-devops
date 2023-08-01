#!/usr/bin/env ruby

def extract_phone_number(input)
  phone_number = input[/\b\d{10}\b/]
  phone_number.nil? ? "" : phone_number
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end

input = ARGV[0]
phone_number = extract_phone_number(input)
puts phone_number
