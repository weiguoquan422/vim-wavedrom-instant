" Name: wavedrom_instant
" Version: 0.1.1

function! Wavedrom_Instant()
    :py3file ~/.local/share/nvim/plugged/vim-wavedrom-instant/plugin/wavedrom_instant.py
    let current_buffer_fullname = expand("%:t")
    let current_buffer_name = current_buffer_fullname[:-6]
    let output_svg_name = current_buffer_name . ".svg"
    :silent exe '!firefox' output_svg_name
endfunction
