#!/usr/bin/env python3

import argparse
import logging
import math

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

def run(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', dest='input', help='Input file to process.')
    parser.add_argument('--output', dest='output', help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    # We use the save_main_session option because one or more DoFn's in this
    # workflow rely on global context (e.g., a module imported at module level).
    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    with beam.Pipeline(options=pipeline_options) as p:
        def fuel(x):
            return max(0, math.floor(int(x) / 3) - 2)

        texts = (p
            | 'Read'  >> ReadFromText(known_args.input)
            | 'Fuel'  >> beam.Map(fuel)
            | 'Sum'   >> beam.CombineGlobally(sum)
            | 'Write' >> WriteToText(known_args.output)
        )

if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()
