# Hadoop-exercises

This repository contains source code for the assignments of Udacity's course, [Introduction to Hadoop and MapReduce](https://www.udacity.com/course/ud617), which was unveiled on 15th November, 2013.<br>
This is a short course by [Cloudera](http://www.cloudera.com) guys in association with [Udacity](https://www.udacity.com). Instructors for this course are Sarah Sproehnle and Ian Wrigley, both from Cloudera and Gundega Dekena, Course Developer is from Udacity.<br>

Course does not mandate any programming language for writing Hadoop MapReduce jobs; but they have mainly used / taught Hadoop MapReduce jobs using `Python` [i.e. with Hadoop Streaming approach for running jobs] during the course.<br>

I have developed Hadoop MapReduce code for the 2 problem statements [3 questions each] in 2 programming languages; `Python` as well as `Java`.<br>

## Instructions for Virtual Machine download and setup
Please refer [instructions document](IntroductiontoHadoopandMapreduce-VMsetup.doc) provided by Course Instructors for details on the Hadoop Virtual Machine [VM henceforth] setup required for running these examples.<br>
As mentioned in the above document, VM image with Hadoop installed and preconfigured, can be downloaded from [Udacity CDN](http://content.udacity-data.com/courses/ud617/Cloudera-Udacity-Training-VM-4.1.1.c.zip). 

Please be forewarned, the size of this compressed VM archive is 1.7 GB. Also it does not uncompress with either 7-Zip or Windows default Zip utility. You might have to use WinRAR or WinZip or even Cygwin unzip to uncompress the same, if you are on a Windows platform. On other Operating Systems, probably `unzip` command might work just fine. Uncompressed size of this VM is 4.2 GB.

Credentials to login to this Virtual Machine are: `training` / `training`. You will not need `root` access for any of the assignments of this Course. But just in case if you need, the password for `root` is `training`.

Please ensure that you configure the VM to at least 1.5 GB of RAM in [VMware Player](https://my.vmware.com/web/vmware/free#desktop_end_user_computing/vmware_player/6_0). It might run much better with 2 GB though. I have used VMware Player v5.0.2, the current latest version as of this writing [i.e. 28th November, 2013] is v6.0.1.

## Data
### Input Files

These input compressed archives can also be downloaded from Udacity servers. Please check [here](http://content.udacity-data.com/courses/ud617/purchases.txt.gz) for input file for Case 1 and [here](http://content.udacity-data.com/courses/ud617/access_log.gz) for Case 2.<br>
These links are also mentioned in the instructions document provided by Udacity Course Instructors.

## [Case 1](case1)

### Project#1
Break down all the sales by store.

#### Code
[`mapper.py`](case1/project1/mapper.py) and [`reducer.py`](case1/project1/reducer.py)

### Project#2
Instead of breaking the sales down by store, instead give us a sales breakdown by product category across all of our stores.

1. What is the value of total sales for the following categories?
	- Toys
	- Consumer Electronics

#### Code
[`mapper.py`](case1/project1/mapper.py) and [`reducer.py`](case1/project1/reducer.py)

### Project#3
Find the monetary value for the highest individual sale for each separate store.

1. What are the values for the following stores?
	- Reno
	- Toledo
	- Chandler

#### Code
[`mapper.py`](case1/project2/mapper.py) and [`reducer.py`](case1/project2/reducer.py)

### Project#4
Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.

1. Find
	- Total sales value across all the stores
	- Total number of sales

#### Code
[`mapper.py`](case1/project3/mapper.py) and [`reducer.py`](case1/project3/reducer.py)

## [Case 2](case2):

### Project#5
Write a MapReduce program which will display the number of hits for each different file on the Web site.

1. Find
	- How many hits were made to the page: /assets/js/the-associates.js?

#### Code
[`mapper.py`](case2/project5/mapper.py) and [`reducer.py`](case2/project5/reducer.py)

### Project#6
Write a MapReduce program which determines the number of hits to the site made by each different IP Address.
	
1. Find
	- How many hits were made by the IP address: 10.99.99.186?

#### Code
[`mapper.py`](case2/project6/mapper.py) and [`reducer.py`](case2/project6/reducer.py)

### Project#7
Find the most popular file on the Web site. In other words, the file which had the most hits. Your Reducer should just write out the name of the file and number of hits into HDFS.

1. Find
	- Full path to the most popular file?
	- Number of hits to that file?

#### Code
[`mapper.py`](case2/project7/mapper.py) and [`reducer.py`](case2/project7/reducer.py)
