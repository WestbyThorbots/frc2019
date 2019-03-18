alias pss='ps -N --pid 2 --ppid 2 --format pid,ppid,tty,user,group,wchan=-----------WCHAN-------------,%mem,%cpu,lstart,args --sort start_time --forest'
alias psz='ps -N --pid 2 --ppid 2 --format pid,ppid,tty,user,group,wchan=-----------WCHAN-------------,context,%mem,%cpu,lstart,args --sort start_time --forest'
alias psp='ps --format pid,ppid,tty,user,wchan=-----WCHAN-----,%mem,%cpu,lstart,args -ww -p '
alias psw='ps -N --pid 2 --ppid 2 --format pid,ppid,tty,user,group,wchan=-----------WCHAN-------------,%mem,%cpu,lstart,args --sort start_time --forest -ww'
alias confcat="grep -Ev '^[[:space:]]*$|^[#;]|^[[:space:]]*#|^[[:space:]]*//' "
