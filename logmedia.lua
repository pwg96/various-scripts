-- media history for mpv saved to ~/mpv.log
-- by pwg aka bodzioslaw (2016)

function log_media()
         f = io.open(os.getenv("HOME")..'/mpv.log', 'a')
         fname = mp.get_property('filename')
         stime = os.date(os.date('%d.%m.%Y %X'))
         f:write(stime..' '..fname..'\n')
         f:close()
end
 
mp.register_event('file-loaded', log_media)
