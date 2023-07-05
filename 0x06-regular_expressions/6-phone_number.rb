#!/usr/bin/env ruby
# this script accepts one argument and matches strings
puts ARGV[0].scan(/^[0-9]{10}$/).join
