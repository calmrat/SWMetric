# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:40:27 2013

@author: Radim Spigel
"""

from gittle import Gittle
import re,os,datetime
import argparse
import pprint
def dg(text,*args):
    print text
    for i in args:
        print i,

class GitStat:  
    '''
        print "        This class is for parsed git repository.\n\
        Returns parsed dictionary filled by name of users/commiters which add/modify files.\n\
        Every item has own directory which contains some counters: \
            counter for adding files\n\
            counter for deleting files\n\
            counter for files which has been modify\n\
        Next:\n    \
            all git commits in array\n\
            directory which lines in which files was modify and how many times who\n"
            '''
    def __init__(self,git_path,rskey= None,logger=dg):
        self.User = {}
        self.Commits = {}
        self.__logger = logger
        self.__tmp_repository = "/tmp/temporary_git_repository"
        if(os.path.exists(self.__tmp_repository)):
            self.__tmp_repository = self.__tmp_repository+"_"+datetime.datetime.now().isoformat()
    
        print git_path
        try:
            Gittle.clone(git_path,self.__tmp_repository)
        except:
            pass
            #self.__logger("Error could not clone repository.")
            #return
        self.__repository = Gittle(self.__tmp_repository)
        if rskey != None:
            key_file = open(rskey)
            self.__repository.auth(pkey=key_file)        
        #print self.__tmp_repository
        self.fill_User()
    def parse(self,name,commit,time):
        #print "asd",name, commit
        file_pattern = re.compile("diff --git a/(.*) b/(.*)")
        line_pattern = re.compile("@@ (.*) (.*) @@")
        regex = file_pattern.search(commit)
        file1,file2 = regex.group(1),regex.group(2)
        regex = line_pattern.search(commit)
        line1,line2 = regex.group(1),regex.group(2)
        #self.__logger("Files : ",file1,file2,line1,line2)
       # print self.User[name].has_key(file1)
        if self.User[name].has_key(file1):            
            #self.User[name][file1]['line_str'].append(line1+" "+line2)
            if self.User[name][file1].has_key(line1):
                self.User[name][file1][line1]["counter"] += 1 
                self.User[name][file1][line1]['time'].append(time)  
            else: 
                self.User[name][file1][line1] = {}
                self.User[name][file1][line1]["counter"] = 1
                self.User[name][file1][line1]['time'] = []            
                self.User[name][file1][line1]['time'].append(time)                  
            self.User[name][file1]['modify'] += 1
            self.User[name][file1]['time'].append(time)            
            if os.path.isfile(self.__tmp_repository+'/'+file1):
                self.User[name][file1]['exist'] = True            
            else:
                self.User[name][file1]['exist'] = False 
            self.Commits[name][file1]['array_commits'].append(commit)  
            self.Commits[name][file1]['time'].append(time)                 
        else:
            self.User[name][file1] = {}            
            self.User[name][file1][line1] = {}
            self.User[name][file1][line1]["counter"] = 1
            self.User[name][file1][line1]['time'] = []            
            self.User[name][file1][line1]['time'].append(time)              
            self.User[name][file1]['modify'] = 1
            self.User[name][file1]['time'] = []            
            self.User[name][file1]['time'].append(time)              
            if os.path.isfile(self.__tmp_repository+'/'+file1):
                self.User[name][file1]['exist'] = True            
            else:
                self.User[name][file1]['exist'] = False  
            self.Commits[name][file1] = {}   
            self.Commits[name][file1]['array_commits'] = []
            self.Commits[name][file1]['array_commits'].append(commit)     
            self.Commits[name][file1]['time'] = []            
            self.Commits[name][file1]['time'].append(time)                  
        return file1
    def fill_User(self):
        for commit in self.__repository.commit_info():
            sha = [commit['sha']]
            #print commit
            try:
                if not self.User.has_key(commit['committer']['name']):
                    #print commit#['committer']['name']
                    #print self.__repository.diff(*sha)[0]['diff']
                    self.User[commit['committer']['name']] = {}
                    self.Commits[commit['committer']['name']] = {}
                    self.parse(commit['committer']['name'],self.__repository.diff(*sha)[0]['diff'],commit['time'])                    
                else:
                    self.parse(commit['committer']['name'],self.__repository.diff(*sha)[0]['diff'],commit['time'])                    
                    
            except:
                pass

        #return file1                       
         
    def return_User(self):
       # print self.User
        return self.User
    def return_commits(self):
        return self.Commits
class GetParameters:
    def __init__(self):
        parser = argparse.ArgumentParser(description="Insert git repository")
        parser.add_argument("params",type=str,help="www or path to git repository")
        self.args = parser.parse_args()
        self.return_parameter()
    def return_parameter(self):
        return self.args.params

git_path = GetParameters().return_parameter()
if git_path == None:
    print "Error"
else:
    git = GitStat(git_path)    
    usr = git.return_User()
    pprint.pprint(usr)
   # pprint.pprint(git.return_commits())
   # for i in usr['Chris Ward']['gittle/gittle.py'].items():
    #    print i