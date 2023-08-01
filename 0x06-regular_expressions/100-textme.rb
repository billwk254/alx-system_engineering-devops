#!/usr/bin/env ruby

def extract_data(log_line)
  sender = log_line[/from:(.*?)\]/, 1]
  receiver = log_line[/to:(.*?)\]/, 1]
  flags = log_line[/flags:(.*?)\]/, 1]
  [sender, receiver, flags].join(',')
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_line>"
  exit 1
end

log_line = ARGV[0]
parsed_data = extract_data(log_line)
puts parsed_data
