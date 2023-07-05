#!/usr/bin/env ruby
# this script accepts one argument and matches strings
puts ARGV[0].scan(/hb{0,1}tn/).join
