#!/usr/bin/env python
import sys, multiprocessing
from datetime import date, datetime, timedelta
from multiprocessing import Process

import click

import secretary
from manager import Manager
from desk import Desk


class Program:
    def __init__(self):
        self.staff = []
        self.office = [Desk(False)]
        self.log = secretary.hire( "Program", debug=True, logfile=\
                    ("run" + datetime.now().strftime('%y%m%d') + ".log") )
        
    def run(self):
        manager = Manager(debug=True, desk=self.office[0])
        m = Process(target=Manager.run, args=(manager,))
        m.daemon = True; m.start()
        self.staff.append(m)
        
        manager.inbox.put("You're Fired.")
        
        for m in self.staff:  m.join()


@click.command()
def main():
    program = Program()
    
    program.run()

if __name__ == "__main__":
    main()
