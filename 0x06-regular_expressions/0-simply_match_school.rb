#!/usr/bin/env ruby

def match_school(input)
  regex = /School/
  input.gsub(regex, 'School')
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <input>"
  exit 1
end

input = ARGV[0]
result = match_school(input)
puts result
