import pysipp
import tempfile
from pysipp import agent, launch, plugin
from pysipp.command import SippCmd

logdir = "../logs"
 

callee_script="../scripts/testUasTime.xml"
uas_data = '../scripts/testUas.csv'

uas_cmd =SippCmd



remote_sock = ("phone.plivo.com", 5060)
uas_cmd.info_file = uas_data
uas_cmd.trace_error="true"
uas_cmd.trace_message="true"
uas_cmd.trace_log="true"
uas_cmd.trace_calldebug="true"
uas_cmd.trace_screen="true"
uas_cmd.local_port="7452"
#uas_cmd.local_ip="10.0.2.15"
uas_cmd.auth_uri="plivo.com"
uas_cmd.limit="1"
uas_cmd.call_count="1"
uas_cmd.default_behaviors="pingreply"

uas_callee = agent.client(destaddr=remote_sock,scen_file=callee_script)




uas_callee.enable_logging(logdir=logdir,debug="true")

cmdstr = uas_callee.render()
print("Sipp command for Callee is -----"+cmdstr)

uas_callee(uas_cmd)


def fileOutput(file_value):
     infile=file_value
     p = re.compile('\s+')
     keep_phrases =  ["INVITE"]
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



uac_file= "../logs/testUasTime_log_file"
fileOutput(uac_file)
