--[[ playback history script for mpv by pwg96 aka bodzioslaw 
  playback history will be available under your user directory eg. $HOME/mpv.log or $HOMEPATH\mpv.log 
  put this file under ~/.config/mpv/scripts or %APPDATA%\mpv\scripts ]]

function log_media()
  dirsep = package.config:sub(1,1)

  if dirsep == "/" then
    f = io.open(os.getenv("HOME")..'/mpv.log', 'a')
  elseif dirsep == "\\" then
    f = io.open(os.getenv("USERPROFILE")..'\\mpv.log', 'a')
  end

  fname = mp.get_property('filename')
  stime = os.date(os.date('%d.%m.%Y %X'))
  f:write(stime..' '..fname..'\n')
  f:close()
end
 
mp.register_event('file-loaded', log_media)
