#!/usr/bin/env python3

import time
import sys

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
      """
    ]

    while True:
        for frame in frames:
            clear = "\033[H\033[J"  # ANSI escape code to clear the terminal
            sys.stdout.write(clear)
            print(frame)
            time.sleep(0.2)

if __name__ == "__main__":
    try:
        animate_clera()
    except KeyboardInterrupt:
        sys.exit(0)

