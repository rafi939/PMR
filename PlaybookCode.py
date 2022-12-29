# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 15:03:57 2022

@author: user670
"""

#1. Playbook Code
'''
---
  - name: "Playing with Ansible and Git"
    hosts: localhost
    connection: local
    tasks:

    - name: "just execute a ls -lrt command"
      shell: "ls -lrt"
      register: "output"

    - debug: var=output.stdout_lines
'''