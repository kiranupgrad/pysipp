import pysipp
import tempfile
from pysipp import agent, launch, plugin
from pysipp.command import SippCmd
import re
import os
import datetime


logdir = "../logs/"
reg_script = "../scripts/register.xml"
caller_script = "../scripts/testUacAuth.xml"
uac_data = '../scripts/testUac.csv'
uac_cmd =SippCmd
remote_sock = ("phone.plivo.com", 5060)
uac_cmd.info_file = uac_data
uac_cmd.trace_error="true"
uac_cmd.trace_message="true"
uac_cmd.trace_log="true"
uac_cmd.trace_calldebug="true"
uac_cmd.trace_screen="true"
uac_cmd.local_port="6448"
uac_cmd.auth_uri="plivo.com"
uac_cmd.limit="1"
uac_cmd.call_count="1"
uac_cmd.media_port="8888"
uac_cmd.auth_username="test1281881673873471385"
uac_cmd.auth_password="plivo"
uac_cmd.default_behaviors="pingreply"



uac_caller = agent.client(destaddr=remote_sock,scen_file=caller_script)
uac_caller.enable_logging(logdir=logdir,debug="true",enable_screen_file=True)

cmdstr = uac_caller.render()
print("Sipp command for UAC call  is-------"+cmdstr)


time1 = datetime.datetime.now()
uac_caller(uac_cmd)
time2 = datetime.datetime.now()
elapsedTime = time2 - time1
l=divmod(elapsedTime.total_seconds(), 60)
print("Call Duration time is: %d minutes and %.2f seconds" % (l[0], l[1]))









def fileOutput(file_value):
     infile=file_value
     p = re.compile('\s+')
     keep_phrases =  ["CallAccept","CallDisconnect","INVITE"]
     important = []
     
     with open(infile) as f:
           f = f.readlines()
     for line in f:
          for phrase in keep_phrases:
               if phrase in line:
                  important.append(line)
                  break;
     for line in important:
         print(p.sub(" ","{}".format(line)))



uac_file= "../logs/testUacAuth_log_file"
uas_file="../logs/testUasTime_log_file"
fileOutput(uac_file)
fileOutput(uas_file)
