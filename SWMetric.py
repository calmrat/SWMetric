# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 19:42:55 2013

@author: radim
"""

import re,os

class SWMetric:
    def __init__(self,project):
        self.__project = project
        self.Metrics = {}
        self.Metrics["SumNSCL"] = 0 # Sum number source code lines 
        self.Metrics["SumClass"] = 0 # Sum of class have project
        self.Metrics["SumMethod"] = 0 # Sum of method in project
        self.Metrics["SumFunction"] = 0 # Sum of method in project        
        self.Metrics["SumComments"] = 0 # Sum of comment in
        self.Metrics["SumImportLib"] = 0 # Sum for import libraries
        self.Metrics["SumControlFlow"] = 0 # Sum for control flow elements            
        self.Metrics["SUT"] = 0 # Sum of unit tests
        self.Metrics["SWP"] = 0 # Sum size every file
                
        self.structure_unix()
        #self.structure_windows()
        self.count_Metric()
        
    def count_Metric(self):
        for file_ in self.Metrics.keys():
            if type(self.Metrics[file_]) != int:
              if os.path.exists(self.Metrics[file_]["path"]):
                print file_
                self.Metrics["SumNSCL"] += self.Metrics[file_]["LOC"]
                self.Metrics["SumClass"] += self.Metrics[file_]["Class"]
                self.Metrics["SumMethod"] +=self.Metrics[file_]["Method"] 
                self.Metrics["SumFunction"] += self.Metrics[file_]["Function"]
                self.Metrics["SumComments"] += self.Metrics[file_]["Comments"] 
                self.Metrics["SUT"] += self.Metrics[file_]["UnitTest"]
                self.Metrics["SumImportLib"]+=self.Metrics[file_]["ImportLib"]
                self.Metrics["SumControlFlow"]+=self.Metrics[file_]["ControlFlow"]
                self.Metrics["SWP"] += os.stat(self.Metrics[file_]["path"]).st_size

      
    def structure_unix(self):
        if os.path.isdir(self.__project):
            dirpaths,dirnames,files = [],[],[]
            for dirpath, dirname, filee in os.walk(self.__project): 
                dirpaths.append(dirpath);dirnames.append(dirname);files.append(filee)
            for i in range(len(dirpaths)):
                for index in files[i]:
                    file_ = index
                    print file_
                    self.Metrics[file_] = {}
                    self.Metrics[file_]["path"] = dirpaths[i]+"/"+file_
                    self.parse(file_)               
        elif os.path.isfile(self.__project):
            if self.__project.find("/"):
                fs = self.__project.split("/")
                fname = fs[len(fs)-1]
                self.Metrics[fname] = {}
                self.Metrics[fname]["path"] = os.path.abspath(fname)
                self.parse(fname)
            else:
                fname = self.__project
                self.Metrics[fname] = {}
                self.Metrics[fname]["path"] = os.path.abspath(fname)
                self.parse(fname)                
        else:
            print "Error"
    def structure_windows(self):
        if os.path.isdir(self.__project):
            dirpaths,dirnames,files = [],[],[]
            for dirpath, dirname, filee in os.walk(self.__project): 
                dirpaths.append(dirpath);dirnames.append(dirname);files.append(filee)
            for i in range(len(dirpaths)):
                for index in files[i]:
                    file_ = index
                    print file_
                    self.Metrics[file_] = {}
                    self.Metrics[file_]["path"] = dirpaths[i]+"\\"+file_
                    self.parse(file_)               
        elif os.path.isfile(self.__project):
            if self.__project.find("\\"):
                fs = self.__project.split("\\")
                fname = fs[len(fs)-1]
                self.Metrics[fname] = {}
                self.Metrics[fname]["path"] = os.path.abspath(fname)
                self.parse(fname)
            else:
                fname = self.__project
                self.Metrics[fname] = {}
                self.Metrics[fname]["path"] = os.path.abspath(fname)
                self.parse(fname)                
        else:
            print "Error"        
            
    def parse(self,file_,lang="py"):
        print file_
        if lang == "py":
            class_pattern = re.compile("class[\s]*(.*):")
            method_pattern = re.compile("[\s]+def (.*)\(")
            function_pattern = re.compile("^\S*def[\s]*(.*)\(")
            comments_pattern = re.compile("#[^!](.*)")
            start_comments_pattern = re.compile("'''(.*)|\"\"\"(.*)")
            end_comments_pattern = re.compile("(.*)'''|(.*)\"\"\"")
            row_comment_pattern = re.compile("('''|\"\"\")(.*)('''|\"\"\")")
            unit_pattern = re.compile("assert[\s]*(.*)") 
            global_pattern = re.compile("global[\s]*(.*)");
            import_pattern = re.compile("import[\s]*(.*)")
            control_flow_pattern = re.compile("[^#]+[^\"]+if|elif|for|while")
        elif lang == "c/c++":
            class_pattern = re.compile("class[\s]*(.*){")
            method_pattern = re.compile("(short|long)?[\s]*(char|int|bool|float|double|struct) (.*)\(")
            function_pattern = re.compile("(short|long)?[\s]*(char|int|bool|float|double|struct) (.*)\(")
            comments_pattern = re.compile("/\*|//")
            unit_pattern = re.compile("assert[\s]*(.*)") 
            #global_pattern = re.compile("global[\s]*(.*)");
            import_pattern = re.compile("#include[\s]*(.*)")      
        elif lang == "java":
            class_pattern = re.compile("(synchronized|public|static|final)*[\s]*class[\s]*(.*){")
            method_pattern = re.compile("(synchronized|short|long|final|static)*[\s]*(char|int|bool|float|double|struct) (.*)(")
            function_pattern = re.compile("(synchronized|short|long)*[\s]*(char|int|bool|float|double|struct) (.*)(")
            comments_pattern = re.compile("/\*|//")
            unit_pattern = re.compile("assert[\s]*(.*)") 
           # global_pattern = re.compile("global[\s]*(.*)");
            import_pattern = re.compile("import[\s]*(.*)")
        ws_pattern = re.compile("^\s*$")
        self.Metrics[file_]["LOC"] = 0 # number of souce code lines
        self.Metrics[file_]["Class"] = 0 # counter for class
        self.Metrics[file_]["Method"] = 0 # counter for method
        self.Metrics[file_]["Function"] = 0 # counter for function
        self.Metrics[file_]["Comments"] = 0 # counter for comments
        self.Metrics[file_]["Global"] = 0 # counter for global variables
        self.Metrics[file_]["UnitTest"] = 0 # counter for unit test
        self.Metrics[file_]["ImportLib"] = 0 # counter for import libraries
        self.Metrics[file_]["ControlFlow"] = 0 # counter for control flow elements        
        start = False
        LOC = 0
        print self.Metrics[file_]["path"]
        with open(self.Metrics[file_]["path"]) as f:
            lines = 0
            line_comments = 0
            for line in f:
                reg = ws_pattern.search(line)
                lines+=1
                if reg is None:
                  LOC += 1
                reg = start_comments_pattern.search(line)
                if reg is not None:
                    start = True
                reg = end_comments_pattern.search(line)
                if reg is not None and start:
                    reg.group(1)
                    r = row_comment_pattern.search(line)
                    if r is not None:
                        print r.group()
                        self.Metrics[file_]["Comments"] += 1
                        start = False
                        continue
                    if line_comments != lines:
                        line_comments+=1
                        start = False                      
                reg = class_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["Class"] += 1
                reg = control_flow_pattern.search(line)
                if reg is not None:
                   # print reg.group()
                    self.Metrics[file_]["ControlFlow"] += 1    
                reg = function_pattern.search(line)                    
                reg = method_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["Method"] += 1    
                reg = function_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["Function"] += 1                        
                reg = comments_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["Comments"] += 1   
                reg = unit_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["UnitTest"] += 1   
                reg = global_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["Global"] += 1  
                reg = import_pattern.search(line)
                if reg is not None:
                    reg.group(1)
                    self.Metrics[file_]["ImportLib"] += 1
            self.Metrics[file_]["Comments"] += line_comments/2
            self.Metrics[file_]["LOC"] = LOC
            self.Metrics[file_]["AllLines"] = lines
        print self.Metrics[file_]
    def return_Metric(self):
        return self.Metrics
g = SWMetric("/home/radim/bakalarka/pokus-1")
print g.return_Metric()
