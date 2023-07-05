#!/usr/bin/env ruby
# In this script we parse one lement from the file (not opening the file)
# "text.log" and print to console the sender, receiver and flags with the format:
# [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
