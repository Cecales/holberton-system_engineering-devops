#!usr/bin/env ruby
# This is a Ruby script that accepts one argument and pass it to a regular expression matching methodi

puts ARGV[0].scan(/hbt{1,5}n/).join
