#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([A-Za-z0-9+]+)\]|\[to:([A-Za-z0-9+]+)\]|\[flags:([0-9:-]+)\]/).flatten.compact.join(',')
