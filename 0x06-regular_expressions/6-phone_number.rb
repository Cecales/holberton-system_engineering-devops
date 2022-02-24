#!/usr/bin/env ruby
# This is a Ruby script in which the regular expression must match a 10 digit phone number

puts ARGV[0].scan(/^\d{10}$/).join
