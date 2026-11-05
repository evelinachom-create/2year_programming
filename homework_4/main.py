import json
from wer import wer 


def main():
    with open("reference.txt", "r", encoding="utf-8") as f:
        reference = f.read()
        
    with open("hypothesis.txt", "r", encoding="utf-8") as f:
        hypothesis = f.read()

    metrics = wer(reference, hypothesis)

    output_filename = "result.json"
    with open(output_filename, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=4)
    print(f"Метрики успішно записано у файл '{output_filename}'.")

    with open(output_filename, "r", encoding="utf-8") as f:
        loaded_metrics = json.load(f)
    
    print(json.dumps(loaded_metrics, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()