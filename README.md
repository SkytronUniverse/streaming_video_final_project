# Assignment 5: Computer Networks
## Karl Boatright and Wagner Colodette

### Installing Dependencies
##### Using Ubuntu 18 and above:
* run <code>pip3 install -r dependencies_ubuntu.txt</code>

##### Otherwise:
* run <code>pip3 install -r requirements.txt</code>

### Instructions for runnning video streaming program:
```
Note: This program has been tested in both macOS and Ubuntu 18.04.1 environments. The Ubuntu environment 
is a virtual machine, and would experience a BrokenPipeError occasionally. This is likely due to the 
limited resources of the virtual machine itself. This may occur for those  testing this program in a 
similar virtual machine environment.
```
1. This process will need to different terminal windows
2. <code>cd</code> into the root of the directory which contains the programs <code>send.py</code> and <code>receive.py</code>.
3. In one terminal run <code>python3 receive.py</code>. It is important to run <code>python3 receive.py</code> first because this program creates that socket that will listen for the data that is sent.
4. Next run <code>python3 send.py</code>. When a video is successfully streamed a window will pop up and play the video.

### Design Proposal can be found in Video_Streaming_Application_Design_Report.pdf

### Final design report can be found in Video_Streaming_Design_Report.pdf or below:

<object data="https://github.com/CSCI-UA0480-009/assignment5-2018-SkytronUniverse/blob/master/Video_Streaming_Design_Report.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/CSCI-UA0480-009/assignment5-2018-SkytronUniverse/blob/master/Video_Streaming_Design_Report.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/CSCI-UA0480-009/assignment5-2018-SkytronUniverse/blob/master/Video_Streaming_Design_Report.pdf">Download PDF</a>.</p>
    </embed>
</object>