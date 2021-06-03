import time
from multiprocessing import Process
from  pysippReg_caller import reg_uac
from  pysippReg_callee import reg_uas
from  pysippUAS_final import  Uas_Callee
from pysippUAC_final import Uac_Caller
from pysippUAC_final import fileOutput



if __name__=='__main__':
     p1 = Process(target = reg_uac)
     p1.start()
     time.sleep(3)
     
     p2 = Process(target = reg_uas)
     p2.start()
     
     time.sleep(3)
     p3 = Process(target= Uas_Callee)
     p3.start()
     
     time.sleep(1)
     p4= Process(target= Uac_Caller)
     p4.start()

     p1.join()
     p2.join()
     p3.join()
     p4.join()

     if p4.is_alive() == False:
        uac_file= "../logs/testUacAuth_log_file"
        uas_file="../logs/testUasTime_log_file"
        fileOutput(uac_file)
        fileOutput(uas_file)


     
