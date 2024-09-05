#!/usr/bin/env python3

import time
import sys
import os

def animate_clera():
    frames = [
        r"""
        *
             
   
   
   
   
        """,
        r"""
            
          *
            
            
        """,
        
        r"""  
        
        
         
            *
              
              
        """,

        r"""   
        
        
        
        
              *
                
                
        """,
        
                r"""   
        
        
        
        
                
                  
                 *
                
                
        """,
                r"""   
        
        
        
        
                
                
                     
                   *
                
        """,
        r"""
        
        
        
        
        
        

        
        
        
        
                   
                
                _____\\*//______
        """,
        r"""
            
            
                 
                 
                 
            
                 
                 
                         ,
                      ` 
                  *  %  '  "    :
                  '   _____   ,
                    '/_ - _\         
             _______/_||||||\_________                              
       """,
       r"""
                 CcQ0;cCQOo0.Q
              CcQ0;cCQOo0.0oCQe.e
             CcQ0;cCQOo0.0oCQe.CcQ0;
           CcQ0;cCQOo0.0oCQe.CcQ0;cCQ
          CcQ0;cCQOo0.0oCQe.cQ0;cCQOo0
       CcQ0;cCQOo0.0oCQe.cQ0;cCQOo0.0oCQe       
          CcQ0;cCQOo0.0oCQe.CcQ0;cCQ
        ____________|_|_|_|____________
       (_______________________________)
                    |||||||
                    |||||||       
                  CcQ0;cCQOo0
                 CcQ0;cCQOo0.o       
       ________CcQ0;cCQOo0.0oCQe._________
      """,
    r"""
  
      
            
      CqQ0.     ;        
      Ccqc;      \   .           CqQ0.
         \\         /         Oo0==Ccqc;
          \\                     //
                    Ccce  .;    . ;o
        ;         00Ccq;.Q
                    oOoq
         ;           ||
          .   .\     ||
     ''.''
     __________/////____\\\\\____\\\ \______
    """,
    r"""











                      *  %  '  "    :
                  '   _____   ,
                    '/_ - _\         
             _______/_||||||\_________  
   """,
   r"""










                      ',',',
                   ;,;,;,;,;,;,;
            ______/?/?////\?\?\\\______   
    """,
    r"""










                         
                         ?
                        ;;;
           ____________?????____________
     """,
     r"""











                          *
                          !
          _________________________________
    """,
    r"""












                           *
          __________________________________
     """,
     r"""












         __________________*_________________
    """,
    r"""













         ______________________________________
    """
    ]

    try:
        for frame in frames:
            clear = "\033[H\033[J"  # ANSI escape code to clear the terminal
            sys.stdout.write(clear)
            print(frame)
            time.sleep(0.3)
    except KeyboardInterrupt:
        sys.exit(0)
        
if __name__ == "__main__":
    animate_clera()
time.sleep(0.4)    
os.system('clear')

