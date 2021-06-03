import pysipp
import tempfile
from pysipp import agent, launch, plugin
from pysipp.command import SippCmd
import re



def reg_uac():
    
    logdir = "../logs/"
    reg_script = "../scripts/register.xml"
    uac_data = '../scripts/testUac.csv'
   
    reg1_cmd =SippCmd
    remote_sock = ("phone.plivo.com", 5060)
    reg1_cmd.info_file = uac_data
    reg1_cmd.trace_error="true"
    reg1_cmd.trace_message="true"
    reg1_cmd.trace_log="true"
    reg1_cmd.trace_calldebug="true"
    reg1_cmd.trace_screen="true"
    reg1_cmd.local_port="6448"
    reg1_cmd.auth_uri="plivo.com"
    reg1_cmd.limit="1"

    reg1_uac = agent.client(destaddr=remote_sock, scen_file=reg_script)
    reg1_uac.enable_logging(logdir=logdir,debug="true",enable_screen_file=True)

    cmdstr = reg1_uac.render()
    print("Sipp command for UAC registratio is-------"+cmdstr)
    reg1_uac(reg1_cmd)


if __name__ == "__main__":
    reg_uac()
       
