#!/usr/bin/env ruby

def match_string(input)
  matches = input.scan(/hbt*n/)
  matches.empty? ? "" : matches.join
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end

input = ARGV[0]
result = match_string(input)
puts result
