from subprocess import call 

name =input ('Enter the name of video:')
search=["ytsearch:"+name]
path=input("save path like /home/user/foldr name")
command=['youtube-dl', '-o',path+'%(title)s.%(ext)s+']
command.extend(search)

call(command)
