import openai

def fine_tune_model(training_file: str, model_name: str):
    client = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
        ],
        fine_tune_prompt=f"Fine-tune for responsible use of AI using {training_file}"
    )
    return client.fine_tuned_model_checkpoint
