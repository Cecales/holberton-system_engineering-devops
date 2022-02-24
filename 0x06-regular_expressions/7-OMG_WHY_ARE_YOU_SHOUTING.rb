#!/usr/bin/env ruby
# This is a Ruby script in which the regular expression must be only matching: capital letters

puts ARGV[0].scan(/[A-Z]/).join
