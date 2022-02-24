#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/hb{0,1}t{0,1}n/).join
