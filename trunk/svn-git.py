Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
#!/usr/bin/python3

############################  pre-requisite ###############################
#           os.system("yum install subversion git git-svn -y")            #
###########################################################################

import os

commit_id='r1'
repo_name = input("Enter svn repo name : ")
github_username = "PraneshNagarajan"
github_token="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"

############### Create new repo in Github ########################
#data = '"name": {},"auto_init": true, "private": true,"gitignore_template": "nanoc"'.format('"'+repo_name+'"')
data = '"name": {}, "private": true"'.format('"'+repo_name+'"')
os.system("curl -X POST -s -d ""'{"+data+"}'"+" https://"+github_username+":"+github_token+"@api.github.com/user/repos > /var/www/svn/migration_logs/"+repo_name+".log")


################ checkout svn repo from svn server  ###############
#os.system("sudo svn co https://svn.riouxsvn.com/"+svn_repo_name+"/  --username=pranesh --password=Sathya")

############### pull commits log of svn repo  ##################
os.system("sudo svn log -q https://svn.riouxsvn.com/"+repo_name+"/ --username=pranesh --password=Sathya > svn_repo_response.txt" )

############ create author list for github migration ###########
os.system("awk -F '|' '/^r/"+' {sub("^ ","", $2) ; {sub(" $","", $2)};print $2"  = "$2" <"$2">"}'+"'"+" svn_repo_response.txt > authors.txt")

################ clone svn repo from svn server  ###############
#os.system("git svn clone -"+commit_id+":HEAD --no-minimize-url --stdlayout --no-metadata --authors-file authors.txt https://pranesh:Sathya@svn.riouxsvn.com/"+repo_name)
os.system("git svn clone -"+commit_id+":1 --no-minimize-url --stdlayout --no-metadata --authors-file authors.txt https://pranesh:Sathya@svn.riouxsvn.com/"+repo_name)
################ change directory .git generated  ###############
os.chdir("/var/www/svn/"+repo_name)
os.system("pwd")
################ Add git origin and push repo to git  ###############
os.system("git remote add origin "+"https://"+github_username+":"+github_token+"@github.com/"+github_username+"/"+repo_name+".git; git branch -M main; git push -u origin main")

