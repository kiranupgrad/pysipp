import pysipp
import tempfile
from pysipp import agent, launch, plugin
from pysipp.command import SippCmd
import re



logdir = "../logs/"
reg_script = "../scripts/register.xml"
uas_data = '../scripts/testUas.csv'




reg2_cmd =SippCmd
remote_sock = ("phone.plivo.com", 5060)



reg2_cmd.info_file = uas_data
reg2_cmd.trace_error="true"
reg2_cmd.trace_message="true"
reg2_cmd.trace_log="true"
reg2_cmd.trace_calldebug="true"
reg2_cmd.trace_screen="true"
reg2_cmd.local_port="7452"
reg2_cmd.auth_uri="plivo.com"
#reg_cmd.limit="1"
#reg_cmd.call_count="1"



reg2_uas = agent.client(destaddr=remote_sock, scen_file=reg_script)


reg2_uas.enable_logging(logdir=logdir,debug="true",enable_screen_file=True)



cmdstr = reg2_uas.render()
print("Sipp command for UAS registration  is-------"+cmdstr)
reg2_uas(reg2_cmd)

       
