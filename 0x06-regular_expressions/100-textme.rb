#!/usr/bin/env ruby

def parse_log_line(log_line)
  sender = log_line[/from:([^\]]+)/, 1]
  receiver = log_line[/to:([^\]]+)/, 1]
  flags = log_line[/flags:([^\]]+)/, 1]
  "#{sender},#{receiver},#{flags}"
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

log_file_path = ARGV[0]

begin
  File.foreach(log_file_path) do |line|
    if line.include?("SMS")
      parsed_data = parse_log_line(line)
      puts parsed_data
    end
  end
rescue Errno::ENOENT
  puts "Error: Log file not found."
end
