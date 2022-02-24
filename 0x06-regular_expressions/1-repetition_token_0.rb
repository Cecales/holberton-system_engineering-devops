#!/usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression matching method

puts ARGV[0].scan(/htb{2, 5}n/).join
