import os

import autorag
import click
from autorag.validator import Validator
from dotenv import load_dotenv

from llama_index.embeddings.upstage import UpstageEmbedding

root_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(root_path, 'data')


@click.command()
@click.option('--config', type=click.Path(exists=True),
              default=os.path.join(root_path, 'config', 'tokenizer_benchmark.yaml'))
@click.option('--qa_data_path', type=click.Path(exists=True),
              default=os.path.join(data_path, 'qa_v4.parquet'))
@click.option('--corpus_data_path', type=click.Path(exists=True),
              default=os.path.join(data_path, 'ocr_corpus_v3.parquet'))
def main(config, qa_data_path, corpus_data_path):
    load_dotenv()
    autorag.embedding_models['upstage_embed'] = autorag.LazyInit(UpstageEmbedding)
    validator = Validator(qa_data_path, corpus_data_path)
    validator.validate(config)


if __name__ == '__main__':
    main()
