#!/usr/bin/env python3

import argparse
import logging
import math

import apache_beam as beam
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

def run(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', dest='output', help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    with beam.Pipeline(options=pipeline_options) as p:
        def run_program(val):
            mem = [
                1,math.floor(val / 100),(val % 100),3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0
            ]

            pc=0
            while mem[pc] != 99:
                if mem[pc] == 1:
                    mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
                elif mem[pc] == 2:
                    mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
                else:
                    raise ValueError(f"unknown opcode {mem[pc]} at {pc}")
                pc+=4

            if mem[0] == 19690720:
                yield val

        texts = (p
            | 'Create' >> beam.Create(range(0, 10000))
            | 'Test'   >> beam.FlatMap(run_program)
            | 'Write'  >> WriteToText(known_args.output)
        )

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()
