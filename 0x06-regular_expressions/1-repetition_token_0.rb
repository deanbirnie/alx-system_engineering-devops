#!/usr/bin/env ruby
# this script matches patterns for variations of "hbttn" with varying number of t's
puts ARGV[0].scan(/hbt{2,5}n/).join
