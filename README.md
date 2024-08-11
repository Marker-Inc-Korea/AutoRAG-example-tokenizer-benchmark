# AutoRAG-example-tokenizer-benchmark

This is a benchmark of Korean tokenizers at BM25 retriever.
With [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG), you can make this kind of benchmark easy and fast.

# Result

## top-k 1

| Module Name   | F1 Score   | Recall     | Precision  | mAP        | NDCG       |
|---------------|------------|------------|------------|------------|------------|
| ko_kkma       | 0.7544     | 0.7544     | 0.7544     | 0.7544     | 0.7544     |
| ko_kiwi       | 0.7281     | 0.7281     | 0.7281     | 0.7281     | 0.7281     |
| space         | 0.6667     | 0.6667     | 0.6667     | 0.6667     | 0.6667     |
| **ko_okt**    | **0.7982** | **0.7982** | **0.7982** | **0.7982** | **0.7982** |
| upstage_embed | 0.6667     | 0.6667     | 0.6667     | 0.6667     | 0.6667     |

## top-k 3

| Module Name   | F1 Score   | Recall     | Precision  | mAP        | NDCG       |
|---------------|------------|------------|------------|------------|------------|
| ko_kkma       | 0.4649     | 0.9298     | 0.3099     | 0.8319     | 0.8570     |
| ko_kiwi       | 0.4430     | 0.8860     | 0.2953     | 0.7968     | 0.8197     |
| space         | 0.4167     | 0.8333     | 0.2778     | 0.7383     | 0.7626     |
| **ko_okt**    | **0.4781** | **0.9561** | **0.3187** | **0.8684** | **0.8910** |
| upstage_embed | 0.4298     | 0.8596     | 0.2865     | 0.3582     | 0.4842     |

## top-k 5

| Module Name   | F1 Score   | Recall     | Precision  | mAP        | NDCG       |
|---------------|------------|------------|------------|------------|------------|
| ko_kkma       | 0.3216     | 0.9649     | 0.1930     | 0.8402     | 0.8718     |
| ko_kiwi       | 0.3158     | 0.9474     | 0.1895     | 0.8108     | 0.8449     |
| space         | 0.2836     | 0.8509     | 0.1702     | 0.7418     | 0.7694     |
| **ko_okt**    | **0.3216** | **0.9649** | **0.1930** | **0.8706** | **0.8948** |
| upstage_embed | 0.3041     | 0.9123     | 0.1825     | 0.2232     | 0.3862     |

## top-k 10

| Module Name   | F1 Score   | Recall     | Precision  | mAP        | NDCG       |
|---------------|------------|------------|------------|------------|------------|
| ko_kkma       | 0.1770     | 0.9737     | 0.0974     | 0.8417     | 0.8749     |
| ko_kiwi       | 0.1754     | 0.9649     | 0.0965     | 0.8129     | 0.8504     |
| space         | 0.1659     | 0.9123     | 0.0912     | 0.7509     | 0.7901     |
| **ko_okt**    | **0.1786** | **0.9825** | **0.0982** | **0.8731** | **0.9005** |
| upstage_embed | 0.1738     | 0.9561     | 0.0956     | 0.1094     | 0.2898     |

## top-k 50

| Module Name   | F1 Score   | Recall     | Precision  | mAP        | NDCG       |
|---------------|------------|------------|------------|------------|------------|
| ko_kkma       | **0.0392** | **1.0000** | **0.0200** | 0.8427     | 0.8804     |
| ko_kiwi       | 0.0389     | 0.9912     | 0.0198     | 0.8144     | 0.8566     |
| space         | 0.0372     | 0.9474     | 0.0189     | 0.7532     | 0.7988     |
| **ko_okt**    | **0.0392** | **1.0000** | **0.0200** | **0.8743** | **0.9050** |
| upstage_embed | **0.0392** | **1.0000** | **0.0200** | 0.0206     | 0.1776     |


# Installation

```bash
pip install -r requirements.txt
```

# Running the project

1. Download dataset to data folder.
2. Make `.env` file using `.env.template` file. (You have to specify Upstage API key)
3. Run evaluator with the following command.

```bash
python3 main.py
```

3. Check the result in the benchmark folder.

You can check the config file at config folder. (`tokenizer_benchmark.yaml`)

And you can specify project dir if you want.
