#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 wei <wei@wei-computer>
#
# Distributed under terms of the MIT license.

import vim
import os
import wavedrom
# import webbrowser

c_buffer_full_path = vim.current.buffer.name
c_buffer_name = os.path.basename(c_buffer_full_path)
output_svg_base = os.path.splitext(c_buffer_name)[0]
output_svg_name = output_svg_base + '.svg'
output_svg_path = os.path.abspath(os.getcwd())
output_svg_url = 'file://' + output_svg_path + '/' + output_svg_name

json_file = open(c_buffer_name)
json_content = json_file.read()

svg = wavedrom.render(
json_content
)
svg.saveas(output_svg_name)
